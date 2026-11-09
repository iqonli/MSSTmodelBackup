#!/usr/bin/env python3
"""Copy an exact, pinned snapshot of public UVR Release assets to a non-latest draft."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import requests


def command(*args, check=True):
    run = subprocess.run(list(args), text=True, capture_output=True)
    if check and run.returncode:
        raise RuntimeError(f"Command failed: {args}\n{run.stdout}\n{run.stderr}")
    return run


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for buf in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            h.update(buf)
    return h.hexdigest()


def verify_source(manifest):
    release_id = manifest["source_release_id"]
    result = command("gh", "api",
        f"repos/{manifest['source_repository']}/releases/{release_id}/assets?per_page=100")
    live = json.loads(result.stdout)
    expected = {a["name"]: (a["id"], a["size"]) for a in manifest["assets"]}
    actual = {a["name"]: (a["id"], a["size"]) for a in live}
    if len(live) != manifest["expected_assets"] or expected != actual:
        raise RuntimeError(
            f"Upstream assets differ from pinned snapshot "
            f"(expected={len(expected)}, live={len(live)}). "
            "Update the manifest intentionally before starting a new mirror."
        )
    total = sum(a["size"] for a in manifest["assets"])
    if total != manifest["source_total_bytes"]:
        raise RuntimeError(f"Manifest total byte count changed: {total}")
    print(f"UPSTREAM_VERIFIED {len(live)} assets, {total:,} bytes", flush=True)


def retrieve_requests(asset, output):
    """Try full GET once, then resume partial bytes with Range when supported."""
    partial = output.with_suffix(output.suffix + ".part")
    for attempt in range(2):
        offset = partial.stat().st_size if partial.exists() else 0
        if offset > asset["size"]:
            partial.unlink()
            offset = 0
        headers = {
            "User-Agent": "MSSTmodelBackup-UVR-mirror/1.0",
            "Accept-Encoding": "identity",
        }
        if offset:
            headers["Range"] = f"bytes={offset}-"
        try:
            with requests.get(
                asset["source_url"], headers=headers,
                timeout=(35, 120), stream=True, allow_redirects=True
            ) as response:
                response.raise_for_status()
                if offset and response.status_code == 206:
                    content_range = response.headers.get("Content-Range", "")
                    if not content_range.startswith(f"bytes {offset}-"):
                        raise RuntimeError(f"Bad Content-Range: {content_range}")
                elif offset:
                    # Some CDNs do not honor Range: restart using the returned full body.
                    offset = 0
                mode = "ab" if offset else "wb"
                last = time.monotonic()
                got = offset
                with partial.open(mode) as handle:
                    for chunk in response.iter_content(chunk_size=2 * 1024 * 1024):
                        if not chunk:
                            continue
                        handle.write(chunk)
                        got += len(chunk)
                        now = time.monotonic()
                        if now - last >= 10:
                            print(f"DOWNLOAD_PROGRESS {asset['name']}: "
                                  f"{got:,}/{asset['size']:,} bytes "
                                  f"({got * 100 / asset['size']:.1f}%)", flush=True)
                            last = now
            if partial.stat().st_size != asset["size"]:
                raise RuntimeError(
                    f"Incorrect size {partial.stat().st_size:,} vs {asset['size']:,}"
                )
            partial.replace(output)
            return "requests"
        except (requests.RequestException, OSError, RuntimeError) as exc:
            print(f"DOWNLOAD_ATTEMPT_FAILED {asset['name']} "
                  f"(attempt {attempt + 1}/2): {exc}", flush=True)
    return None


def download(asset, directory, source_repo, source_tag):
    name = asset["name"]
    output = directory / name
    if output.exists():
        output.unlink()
    start = time.monotonic()
    route = retrieve_requests(asset, output)
    if route is None:
        # Different client and GitHub API path; start afresh rather than trusting a partial.
        part = output.with_suffix(output.suffix + ".part")
        part.unlink(missing_ok=True)
        print(f"DOWNLOAD_FALLBACK_GH {name}", flush=True)
        command("gh", "release", "download", source_tag,
                "-R", source_repo, "--pattern", name, "--dir", str(directory))
        route = "gh-release-download"
    if output.stat().st_size != asset["size"]:
        raise RuntimeError(
            f"Size mismatch for {name}: {output.stat().st_size:,} "
            f"versus {asset['size']:,}"
        )
    digest = sha256(output)
    elapsed = time.monotonic() - start
    speed = asset["size"] / max(elapsed, 1e-6) / 1048576
    print(f"DOWNLOAD_OK {name}: {asset['size']:,} bytes, "
          f"{elapsed:.2f}s, {speed:.2f} MiB/s, "
          f"SHA256={digest} (source provided no digest; verified length)", flush=True)
    return {
        "name": name, "size": asset["size"], "source_asset_id": asset["id"],
        "source_url": asset["source_url"], "category": asset["category"],
        "sha256": digest, "elapsed_seconds": round(elapsed, 3),
        "average_mib_s": round(speed, 3), "transport": route,
    }


def upload(tag, path):
    first = command("gh", "release", "upload", tag, str(path), check=False)
    if first.returncode != 0:
        print(f"UPLOAD_RETRY {path.name}: {first.stderr.strip()}", flush=True)
        # On retry switch to clobber, handling a timed-out upload that actually finished.
        command("gh", "release", "upload", tag, str(path), "--clobber")
    print(f"UPLOAD_OK {path.name} ({path.stat().st_size:,} bytes)", flush=True)


def main(path):
    m = json.loads(Path(path).read_text(encoding="utf-8"))
    assert len(m["assets"]) == m["expected_assets"]
    assert len({a["name"] for a in m["assets"]}) == m["expected_assets"]
    verify_source(m)

    work = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "uvr-backup"
    work.mkdir(parents=True, exist_ok=True)
    tag = m["backup_tag"]
    notes = work / "RELEASE_NOTES.md"
    notes.write_text(
        "# UVR public model backup\n\n"
        f"Exact backup of {m['expected_assets']} original assets from "
        f"https://github.com/{m['source_repository']}/releases/tag/{m['source_tag']}.\n\n"
        "As of 2026-11-10, the upstream Release contains 86 (not 88) files. "
        "All source filenames are retained. Release is intentionally not Latest.\n\n"
        "SHA256SUMS.txt and SOURCE_MANIFEST.json were added as audit metadata. "
        "The hashes were calculated after download; the upstream listing did "
        "not provide SHA256 digests for the original files.\n\n"
        "The original authors retain all rights; this repository's MIT license "
        "does not relicense these third-party models.\n",
        encoding="utf-8",
    )
    existing = command("gh", "release", "view", tag, "--json", "isDraft", check=False)
    if existing.returncode:
        command("gh", "release", "create", tag, "--draft", "--latest=false",
                "--target", os.environ.get("GITHUB_SHA", "main"),
                "--title", "UVR public models (86 upstream assets)",
                "--notes-file", str(notes))
        print(f"DRAFT_CREATED {tag}, latest=false", flush=True)
    elif not json.loads(existing.stdout)["isDraft"]:
        raise RuntimeError(f"Release {tag} already published; refusing to overwrite it")
    else:
        print(f"DRAFT_REUSED {tag}", flush=True)

    copied = []
    for idx, asset in enumerate(m["assets"], 1):
        print(f"\n--- ASSET {idx}/{m['expected_assets']}: {asset['name']} ---", flush=True)
        record = download(asset, work, m["source_repository"], m["source_tag"])
        upload(tag, work / asset["name"])
        copied.append(record)
        (work / asset["name"]).unlink()
        (work / (asset["name"] + ".part")).unlink(missing_ok=True)

    if len(copied) != m["expected_assets"]:
        raise RuntimeError(f"Incomplete backup: {len(copied)} files")
    checksums = work / "SHA256SUMS.txt"
    checksums.write_text(
        "".join(f"{a['sha256']}  {a['name']}\n" for a in copied),
        encoding="utf-8",
    )
    upload(tag, checksums)
    manifest = work / "SOURCE_MANIFEST.json"
    manifest.write_text(
        json.dumps(
            {"source_repository": m["source_repository"],
             "source_tag": m["source_tag"],
             "source_release_id": m["source_release_id"],
             "original_asset_count": len(copied),
             "original_total_bytes": m["source_total_bytes"], "assets": copied},
            ensure_ascii=False, indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    upload(tag, manifest)

    # The two metadata files mean 88 assets in the destination, 86 from upstream.
    view = json.loads(command(
        "gh", "release", "view", tag, "--json", "assets,isDraft"
    ).stdout)
    actual = {a["name"]: a["size"] for a in view["assets"]}
    expected = {a["name"]: a["size"] for a in m["assets"]}
    expected["SHA256SUMS.txt"] = checksums.stat().st_size
    expected["SOURCE_MANIFEST.json"] = manifest.stat().st_size
    if actual != expected:
        raise RuntimeError("Release asset list/size mismatch; keeping draft. "
                           f"expected {len(expected)}, got {len(actual)}")

    command("gh", "release", "edit", tag, "--draft=false", "--latest=false")
    print(f"RELEASE_PUBLISHED {tag}: 86 source assets + 2 audit files; latest=false", flush=True)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(f"## UVR backup\n\n"
                         f"Copied **86 / 86** upstream files (16,077,696,038 bytes), "
                         f"plus 2 metadata assets. Explicitly **not Latest**.\n\n"
                         f"https://github.com/{os.environ['GH_REPO']}/releases/tag/{tag}\n")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise RuntimeError("Usage: mirror_uvr_release.py uvr_source_assets.json")
        main(sys.argv[1])
    except Exception as exc:
        print(f"FATAL: {exc}", file=sys.stderr, flush=True)
        raise
