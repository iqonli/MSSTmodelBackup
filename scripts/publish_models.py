#!/usr/bin/env python3
"""Mirror selected public Hugging Face model weights and available YAMLs to a draft GitHub Release."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

from huggingface_hub import HfApi, hf_hub_download


def gh(*args, check=True):
    command = ["gh", *args]
    result = subprocess.run(command, text=True, capture_output=True)
    if check and result.returncode:
        raise RuntimeError(
            f"GitHub command failed ({result.returncode}): {command}\n"
            f"{result.stdout}\n{result.stderr}"
        )
    return result


def upload(tag, path):
    for attempt in range(3):
        result = gh("release", "upload", tag, str(path), "--clobber", check=False)
        if result.returncode == 0:
            return
        print(f"Upload attempt {attempt + 1} failed for {path.name}: {result.stderr}", flush=True)
        if attempt < 2:
            time.sleep((attempt + 1) * 10)
    raise RuntimeError(f"Could not upload {path.name}; the Release remains a draft.")


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def source_url(repo_id, revision, filename):
    return f"https://huggingface.co/{repo_id}/resolve/{revision}/{quote(filename, safe='/')}"


def download(repo_id, revision, filename, directory):
    try:
        return Path(
            hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                revision=revision,
                local_dir=directory,
            )
        )
    except Exception as first_error:
        # A different transport path for failures in the HF Hub/Xet client.
        print(f"Hub client failed for {filename}: {first_error}; using curl.", flush=True)
        output = directory / filename
        output.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [
                "curl", "--fail", "--location", "--silent", "--show-error",
                "--connect-timeout", "30", "--max-time", "3600",
                "--output", str(output),
                source_url(repo_id, revision, filename) + "?download=true",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise RuntimeError(
                f"Both Hub client and curl failed for {repo_id}/{filename}: "
                f"{result.stderr}"
            ) from first_error
        return output


def main(manifest_path):
    config = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    tag = config["tag"]
    title = config["title"]
    models = config["models"]
    staging = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "msst-model-backup"
    staging.mkdir(parents=True, exist_ok=True)

    lines = [
        "Backup of nine Roformer model checkpoints and their available YAML configurations.",
        "",
        "Each weight retains a link to its original Hugging Face repository. "
        "The original authors retain their rights; the repository's MIT license "
        "does not relicense third-party model weights.",
        "",
        "### Original sources",
        "",
    ]
    for model in models:
        lines.append(
            f"- \`{model['asset']}\`: "
            f"[{model['repo']}](https://huggingface.co/{model['repo']}) "
            f"(source: \`{model['file']}\`; YAML: \`{model.get('yaml') or 'none'}\`)."
        )
    lines.extend([
        "",
        "\`SHA256SUMS.txt\` contains hashes of the uploaded files. "
        "\`SOURCE_MANIFEST.json\` records upstream revisions and hashes.",
        "",
    ])
    notes = staging / "RELEASE_NOTES.md"
    notes.write_text("\n".join(lines), encoding="utf-8")

    existing = gh("release", "view", tag, "--json", "isDraft", check=False)
    if existing.returncode != 0:
        gh(
            "release", "create", tag, "--draft",
            "--title", title, "--notes-file", str(notes),
            "--target", os.environ.get("GITHUB_SHA", "main"),
        )
        print(f"Created draft Release {tag}.", flush=True)
    else:
        state = json.loads(existing.stdout)
        print(f"Reusing existing Release {tag} (draft={state['isDraft']}).", flush=True)

    api = HfApi()
    repositories = {}
    assets = []
    checksums = []
    for idx, model in enumerate(models, 1):
        repo = model["repo"]
        if repo not in repositories:
            info = api.model_info(repo_id=repo, files_metadata=True)
            repositories[repo] = (
                info.sha,
                {s.rfilename: s for s in (info.siblings or [])},
            )
        revision, siblings = repositories[repo]
        weight = model["file"]
        if weight not in siblings:
            raise FileNotFoundError(f"Required checkpoint missing upstream: {repo}/{weight}")

        for is_yaml, original, asset in (
            (False, weight, model["asset"]),
            (True, model.get("yaml"), Path(model["yaml"]).name if model.get("yaml") else None),
        ):
            if not original:
                continue
            if original not in siblings:
                if is_yaml:
                    print(f"Skipping missing YAML {repo}/{original}", flush=True)
                    continue
                raise FileNotFoundError(f"Required checkpoint missing: {repo}/{original}")

            workdir = staging / f"{idx:02d}_{'yaml' if is_yaml else 'weight'}"
            workdir.mkdir(parents=True, exist_ok=True)
            original_path = download(repo, revision, original, workdir)
            upload_path = workdir / "asset" / asset
            upload_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(original_path), str(upload_path))

            actual_size = upload_path.stat().st_size
            metadata = siblings[original]
            expected_size = getattr(metadata, "size", None)
            lfs = getattr(metadata, "lfs", None) or {}
            if isinstance(lfs, dict):
                expected_size = expected_size or lfs.get("size")
                expected_hash = lfs.get("sha256")
            else:
                expected_hash = None
            if not is_yaml and actual_size < 1024 * 1024:
                raise RuntimeError(f"Checkpoint is suspiciously small: {asset} ({actual_size} bytes)")
            if expected_size is not None and int(expected_size) != actual_size:
                raise RuntimeError(
                    f"Size mismatch for {asset}: expected {expected_size}, got {actual_size}"
                )
            digest = sha256_file(upload_path)
            if expected_hash and digest.lower() != expected_hash.lower():
                raise RuntimeError(f"Upstream SHA256 mismatch for {asset}")

            print(f"Uploading {asset} ({actual_size} bytes, SHA256 {digest})", flush=True)
            upload(tag, upload_path)
            checksums.append(f"{digest}  {asset}")
            assets.append({
                "asset": asset,
                "source_repo": repo,
                "source_revision": revision,
                "source_file": original,
                "source_url": source_url(repo, revision, original),
                "size": actual_size,
                "sha256": digest,
                "yaml": is_yaml,
            })
            shutil.rmtree(workdir, ignore_errors=True)
            xet_cache = os.environ.get("HF_XET_CACHE")
            if xet_cache:
                shutil.rmtree(xet_cache, ignore_errors=True)

    published_weights = sum(not asset["yaml"] for asset in assets)
    if published_weights != len(models):
        raise RuntimeError(f"Expected {len(models)} weights, uploaded {published_weights}")

    sums_file = staging / "SHA256SUMS.txt"
    sums_file.write_text("\n".join(checksums) + "\n", encoding="utf-8")
    upload(tag, sums_file)
    metadata_file = staging / "SOURCE_MANIFEST.json"
    metadata_file.write_text(
        json.dumps({"tag": tag, "assets": assets}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    upload(tag, metadata_file)

    gh("release", "edit", tag, "--draft=false")
    release_url = f"https://github.com/{os.environ.get('GH_REPO', 'iqonli/MSSTmodelBackup')}/releases/tag/{tag}"
    summary = (
        f"Published {published_weights} weights and "
        f"{len(assets) - published_weights} YAML files.\n\n{release_url}\n"
    )
    print(summary, flush=True)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
            stream.write(f"## Model backup Release\n\n{summary}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python publish_models.py models.json")
    main(sys.argv[1])
