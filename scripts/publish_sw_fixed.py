#!/usr/bin/env python3
"""Mirror two files, report live download speeds and publish a separate Release."""
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

TAG = "bs-roformer-sw-fixed-2026-11-10"
UPSTREAM = "https://huggingface.co/enerjazzer/BS-ROFO-SW-Fixed/resolve/main/"
FILES = {
    "BS-Rofo-SW-Fixed.ckpt": (699412152, "24e7d35ee9c64415673d3fd33e06a67cac2c103c5df6267ba1576459c775916e"),
    "BS-Rofo-SW-Fixed.yaml": (4613, "f9fada9f94e5ba2d2e4600196299459294bc5f532b314c209cc156ac63e4329b"),
}
FALLBACK = "https://huggingface.co/FractalSurfer/BS-RoFormer-SW-6stem/resolve/main/"

def gh(*args, check=True):
    p = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"gh {' '.join(args)} failed: {p.stderr}")
    return p

def download(name, size, digest, out):
    sources = [UPSTREAM, FALLBACK]
    started = time.monotonic()
    transferred = 0
    previous_tick = started
    previous_bytes = 0
    for base in sources:
        for attempt in range(2):
            # Restart on each changed source to keep per-transfer measurement honest.
            out.unlink(missing_ok=True)
            print(f"DOWNLOAD_SOURCE {name}: {base} attempt {attempt + 1}", flush=True)
            try:
                req = urllib.request.Request(base + name + "?download=true",
                    headers={"User-Agent": "MSSTmodelBackup-Actions/1.0"})
                with urllib.request.urlopen(req, timeout=120) as remote, out.open("wb") as dest:
                    file_start = time.monotonic()
                    previous_tick = file_start
                    previous_bytes = 0
                    count = 0
                    h = hashlib.sha256()
                    while True:
                        chunk = remote.read(1024 * 1024)
                        if not chunk:
                            break
                        dest.write(chunk)
                        h.update(chunk)
                        count += len(chunk)
                        transferred += len(chunk)
                        now = time.monotonic()
                        if now - previous_tick >= 2:
                            instant = (count - previous_bytes) / (now - previous_tick) / 1048576
                            average = count / (now - file_start) / 1048576
                            print(f"DOWNLOAD_PROGRESS {name}: {count:,}/{size:,} B "
                                  f"({100 * count / size:.1f}%), current={instant:.2f} MiB/s, "
                                  f"average={average:.2f} MiB/s, elapsed={now - file_start:.1f}s", flush=True)
                            previous_tick, previous_bytes = now, count
                if count != size:
                    raise ValueError(f"size mismatch: expected {size}, got {count}")
                if h.hexdigest() != digest:
                    raise ValueError(f"SHA256 mismatch: expected {digest}, got {h.hexdigest()}")
                elapsed = time.monotonic() - file_start
                avg = count / elapsed / 1048576
                print(f"DOWNLOAD_COMPLETE {name}: size={count:,} B; "
                      f"duration={elapsed:.2f}s; average={avg:.2f} MiB/s; "
                      f"average={count * 8 / elapsed / 1e6:.2f} Mbps; SHA256 OK", flush=True)
                return {"file": name, "bytes": size, "sha256": digest, "elapsed_s": round(elapsed, 3),
                        "avg_MiB_s": round(avg, 3), "avg_Mbps": round(count * 8 / elapsed / 1e6, 3),
                        "source": base + name}
            except Exception as e:
                print(f"DOWNLOAD_ERROR {name}: {type(e).__name__}: {e}", flush=True)
                time.sleep(3)
    raise RuntimeError(f"Unable to obtain validated file: {name}")

def upload(path):
    for attempt in range(3):
        p = gh("release", "upload", TAG, str(path), "--clobber", check=False)
        if p.returncode == 0:
            print(f"UPLOAD_SUCCESS {path.name} ({path.stat().st_size:,} bytes)", flush=True)
            return
        print(f"UPLOAD_ERROR attempt={attempt + 1} file={path.name} {p.stderr}", flush=True)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"Cannot upload {path.name}; Release remains draft")

def main():
    dest = pathlib.Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "swfixed"
    dest.mkdir(parents=True, exist_ok=True)
    notes = dest / "NOTES.md"
    notes.write_text(
        "BS-RoFormer SW Fixed (6 stems) with its original YAML configuration.\n\n"
        "Source: https://huggingface.co/enerjazzer/BS-ROFO-SW-Fixed\n\n"
        "Checkpoint and YAML SHA256 verified. GitHub Actions logs contain live "
        "download speed; DOWNLOAD_SPEED.json records average speeds on the runner. "
        "This benchmark is not the download speed of end users.\n\n"
        "Third-party weights have unknown licensing; no additional rights are granted.\n",
        encoding="utf-8")
    if gh("release", "view", TAG, check=False).returncode:
        gh("release", "create", TAG, "--draft", "--title", "BS-RoFormer SW Fixed",
           "--notes-file", str(notes), "--target", os.environ.get("GITHUB_SHA", "main"))
        print("DRAFT_RELEASE_CREATED", flush=True)
    else:
        print("RELEASE_EXISTS; will update matching assets", flush=True)

    results = []
    for name, (size, sha256) in FILES.items():
        path = dest / name
        result = download(name, size, sha256, path)
        upload(path)
        results.append(result)
        path.unlink()
    sums = dest / "SHA256SUMS.txt"
    sums.write_text("".join(f"{r['sha256']}  {r['file']}\n" for r in results))
    upload(sums)
    speeds = dest / "DOWNLOAD_SPEED.json"
    speeds.write_text(json.dumps({"location": "GitHub Actions ubuntu-24.04", "files": results}, indent=2) + "\n")
    upload(speeds)
    gh("release", "edit", TAG, "--draft=false")
    print(f"RELEASE_PUBLISHED https://github.com/{os.environ['GH_REPO']}/releases/tag/{TAG}", flush=True)
    summary = "## BS-RoFormer SW Fixed — download speed\n\n| File | Time | Average MiB/s | Average Mbps | SHA256 |\n|---|---:|---:|---:|---|\n"
    for r in results:
        summary += f"| {r['file']} | {r['elapsed_s']} s | {r['avg_MiB_s']} | {r['avg_Mbps']} | OK |\n"
    print(summary, flush=True)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
            f.write(summary)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"FATAL: {error}", file=sys.stderr, flush=True)
        sys.exit(1)
