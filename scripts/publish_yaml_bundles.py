#!/usr/bin/env python3
"""Build 2 YAML-only ZIPs from 3 existing GitHub Releases.

Attempt original upstream YAML URLs first. Verify downloaded size and SHA256
against the mirrored Release asset; use that Release as fallback if needed.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from urllib.parse import quote
import zipfile

import requests

TAG = "yaml-config-bundles-2026-11-10"
MSST_TAG = "models-2026-11-10"
SW_TAG = "bs-roformer-sw-fixed-2026-11-10"
UVR_TAG = "uvr-all-public-models-2026-11-10"
EXPECTED = {"MSST-YAML-Configs.zip": 10, "UVR-YAML-Configs.zip": 14}


def cmd(*args, check=True):
    result = subprocess.run(args, text=True, capture_output=True)
    if check and result.returncode:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {args}\n"
            f"{result.stdout}\n{result.stderr}"
        )
    return result


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def get_release(tag):
    repo = os.environ["GH_REPO"]
    data = json.loads(cmd("gh", "api", f"repos/{repo}/releases/tags/{tag}").stdout)
    if data.get("draft"):
        raise RuntimeError(f"Source Release is draft: {tag}")
    return {asset["name"]: asset for asset in data["assets"]}


def asset_details(asset, label):
    value = asset.get("digest")
    if not value or not value.startswith("sha256:"):
        raise RuntimeError(f"Missing GitHub SHA256 for {label}")
    return {
        "name": asset["name"],
        "size_bytes": asset["size"],
        "sha256": value.removeprefix("sha256:"),
        "url": asset["browser_download_url"],
    }


def upstream_hf(repo, filename):
    path = "/".join(quote(part, safe="") for part in filename.split("/"))
    return f"https://huggingface.co/{repo}/resolve/main/{path}?download=true"


def yaml_record(name, upstream, yaml_asset, refs, basis, source_tag):
    return {
        "yaml": name,
        "yaml_asset": asset_details(yaml_asset, name),
        "sources": [("upstream", upstream), ("backup_release", yaml_asset["browser_download_url"])],
        "weight_refs": refs,
        "pairing_basis": basis,
        "source_tag": source_tag,
    }


def known_weight(name, source_asset, upstream=None):
    if source_asset is None:
        return {"file": name, "present": False, "size_bytes": None,
                "sha256": None, "download_url": None, "original_url": None}
    asset = asset_details(source_asset, name)
    return {
        "file": name, "present": True, "size_bytes": asset["size_bytes"],
        "sha256": asset["sha256"], "download_url": asset["url"],
        "original_url": upstream,
    }


def build_index():
    msst_release, sw_release, uvr_release = (
        get_release(MSST_TAG), get_release(SW_TAG), get_release(UVR_TAG)
    )
    models = json.loads(Path("models.json").read_text(encoding="utf-8"))["models"]
    uvr_manifest = json.loads(Path("uvr_source_assets.json").read_text(encoding="utf-8"))
    pair_map = json.loads(Path("uvr_yaml_weights.json").read_text(encoding="utf-8"))["pairs"]
    original_files = {a["name"]: a for a in uvr_manifest["assets"]}
    result_msst = []

    for model in models:
        yaml_name = Path(model["yaml"]).name
        yaml_asset = msst_release[yaml_name]
        weight_asset = msst_release[model["asset"]]
        result_msst.append(yaml_record(
            yaml_name, upstream_hf(model["repo"], model["yaml"]),
            yaml_asset,
            [known_weight(model["asset"], weight_asset,
                          upstream_hf(model["repo"], model["file"]))],
            "models.json (specific checkpoint and YAML)", MSST_TAG,
        ))

    yaml_name = "BS-Rofo-SW-Fixed.yaml"
    result_msst.append(yaml_record(
        yaml_name, upstream_hf("enerjazzer/BS-ROFO-SW-Fixed", yaml_name),
        sw_release[yaml_name],
        [known_weight("BS-Rofo-SW-Fixed.ckpt",
                      sw_release["BS-Rofo-SW-Fixed.ckpt"],
                      upstream_hf("enerjazzer/BS-ROFO-SW-Fixed", "BS-Rofo-SW-Fixed.ckpt"))],
        "separate BS-RoFormer SW Fixed Release", SW_TAG,
    ))

    result_uvr = []
    for item in uvr_manifest["assets"]:
        name = item["name"]
        if not name.endswith(".yaml"):
            continue
        if name not in pair_map:
            raise RuntimeError(f"Missing Demucs relationship for {name}")
        mapping = pair_map[name]
        refs = []
        for model_name in mapping["model_files"]:
            asset = uvr_release.get(model_name)
            upstream = original_files.get(model_name, {}).get("source_url")
            refs.append(known_weight(model_name, asset, upstream))
        result_uvr.append(yaml_record(
            name, item["source_url"], uvr_release[name], refs,
            mapping["label"] + " (UVR file index / YAML definition)", UVR_TAG,
        ))
    result_uvr.sort(key=lambda x: x["yaml"].casefold())
    if len(result_msst) != 10 or len(result_uvr) != 14:
        raise RuntimeError("Unexpected number of YAML configurations")
    if len({x["yaml"] for x in result_msst}) != len(result_msst):
        raise RuntimeError("Duplicate MSST YAML names")
    if len({x["yaml"] for x in result_uvr}) != len(result_uvr):
        raise RuntimeError("Duplicate UVR YAML names")
    return result_msst, result_uvr


def read_url(url, expected_size, expected_hash):
    with requests.get(url, timeout=(20, 40), stream=True,
                      headers={"Accept-Encoding": "identity"}) as response:
        response.raise_for_status()
        chunks = []
        received = 0
        for part in response.iter_content(chunk_size=64 * 1024):
            if not part:
                continue
            received += len(part)
            if received > 2 * 1024 * 1024:
                raise RuntimeError("Refusing oversized YAML response")
            chunks.append(part)
        content = b"".join(chunks)
    if len(content) != expected_size:
        raise RuntimeError(f"Size differs: {len(content)} != {expected_size}")
    checksum = digest(content)
    if checksum != expected_hash:
        raise RuntimeError(f"SHA256 differs: {checksum} != {expected_hash}")
    return content


def download_yaml(entry, directory):
    expected = entry["yaml_asset"]
    for method, url in entry["sources"]:
        try:
            content = read_url(url, expected["size_bytes"], expected["sha256"])
            print(f"YAML_OK {entry['yaml']} [{method}], {len(content)} B, sha256={digest(content)}",
                  flush=True)
            return content, method, url
        except (requests.RequestException, RuntimeError, OSError) as error:
            print(f"YAML_SOURCE_FAILED {entry['yaml']} [{method}]: {error}", flush=True)
    # Alternate transport for the backup: GitHub CLI instead of direct HTTP.
    filename = entry["yaml"]
    output = directory / filename
    output.unlink(missing_ok=True)
    repo = os.environ["GH_REPO"]
    res = cmd("gh", "release", "download", entry["source_tag"],
              "-R", repo, "--pattern", filename, "--dir", str(directory), check=False)
    if res.returncode:
        raise RuntimeError(f"No verified copy available for {filename}: {res.stderr}")
    content = output.read_bytes()
    output.unlink(missing_ok=True)
    if len(content) != expected["size_bytes"] or digest(content) != expected["sha256"]:
        raise RuntimeError(f"Checksum/size mismatch in CLI fallback: {filename}")
    print(f"YAML_OK {filename} [backup_release_cli], sha256={digest(content)}", flush=True)
    return content, "backup_release_cli", entry["sources"][-1][1]


def readme_text(archive_name, count):
    if archive_name.startswith("UVR"):
        details = (
            "本包来自 UVR 公共模型全集 Release 的 14 个 Demucs YAML。\n"
            "这些 YAML 可能对应多份 .th 权重；部分权重未收录在三个既有 Release 中。\n"
            "对于未收录的权重，relation.txt 仍记录已有证据支持的文件名，但大小、SHA256、下载地址标注为未找到。\n"
            "其他架构（VR/MDX/部分 CKPT）没有因文件同处一个 Release 就被强行分配给这些 YAML。\n"
        )
    else:
        details = (
            "本包收录九模型合集的 9 份 YAML，以及 BS-RoFormer SW Fixed 的 1 份 YAML。\n"
            "每份 YAML 都对应一个已有备份权重，relation.txt 中包含对应文件名、大小和 SHA256。\n"
        )
    return (
        f"{archive_name}\n\n"
        f"包含 YAML 配置文件：{count} 个\n"
        "ZIP 内文件：README.txt、relation.txt、yaml/ 文件夹。\n"
        "YAML 下载策略：先尝试原始发布源，校验其大小和 SHA256；失败时改用备份 Release。\n"
        "模型权重文件不包含在 ZIP 内；请按 relation.txt 的链接单独下载。\n"
        "README.txt 与 relation.txt 使用 UTF-8 编码（带 BOM），适合 Windows 记事本。\n\n"
        + details + "\n"
        "SHA256 与文件大小依据现有 GitHub Release 的已发布附件元数据。\n"
        "模型/配置的版权和使用许可归原作者所有；本仓库 MIT 许可不适用于第三方权重。\n"
    )


def relation_text(records):
    result = [
        "YAML <-> checkpoint relationship / 配置与权重对应关系",
        "SHA256 and size from mirrored GitHub Release metadata.",
        "未收录模型的大小、校验和与下载地址留空；仅已核实的地址会填写。",
        "",
    ]
    for idx, r in enumerate(records, 1):
        y = r["yaml_asset"]
        result.extend([
            f"[{idx:02d}] {r['yaml']}",
            f"YAML 文件名：{r['yaml']}",
            f"YAML 大小（字节）：{y['size_bytes']}",
            f"YAML SHA256：{y['sha256']}",
            f"YAML 上游下载：{r['sources'][0][1]}",
            f"YAML 备份下载：{r['sources'][1][1]}",
            f"本次获取方式：{r['fetched_from']}",
            f"本次实际下载地址：{r['fetched_url']}",
            f"匹配依据：{r['pairing_basis']}",
            f"引用权重数量：{len(r['weight_refs'])}",
        ])
        for k, weight in enumerate(r["weight_refs"], 1):
            result.extend([
                f"  模型 {k} 文件名：{weight['file']}",
                f"  模型 {k} 是否已收录：{'是' if weight['present'] else '否'}",
                f"  模型 {k} 大小（字节）：{weight['size_bytes'] if weight['present'] else '未找到'}",
                f"  模型 {k} SHA256：{weight['sha256'] if weight['present'] else '未找到'}",
                f"  模型 {k} 备份下载：{weight['download_url'] or '未找到'}",
                f"  模型 {k} 原始下载：{weight['original_url'] or '未找到'}",
            ])
        result.extend(["", "-" * 68, ""])
    return "\n".join(result) + "\n"


def make_archive(name, records, directory):
    archive = directory / name
    with tempfile.TemporaryDirectory(prefix="yaml-cfg-") as temp:
        tmp = Path(temp)
        for r in records:
            raw, method, url = download_yaml(r, tmp)
            r["fetched_from"], r["fetched_url"] = method, url
            p = tmp / "yaml" / r["yaml"]
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
        readme = tmp / "README.txt"
        relation = tmp / "relation.txt"
        readme.write_text(readme_text(name, len(records)), encoding="utf-8-sig")
        relation.write_text(relation_text(records), encoding="utf-8-sig")
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as target:
            target.write(readme, arcname="README.txt")
            target.write(relation, arcname="relation.txt")
            for r in records:
                target.write(tmp / "yaml" / r["yaml"], arcname="yaml/" + r["yaml"])
    with zipfile.ZipFile(archive) as verify:
        names = verify.namelist()
        expected_names = {"README.txt", "relation.txt"} | {"yaml/" + r["yaml"] for r in records}
        if set(names) != expected_names or verify.testzip() is not None:
            raise RuntimeError(f"ZIP integrity/member check failed: {name}")
    print(f"ZIP_OK {name}: {len(records)} YAMLs, {archive.stat().st_size:,} B, "
          f"SHA256 {hashlib.sha256(archive.read_bytes()).hexdigest()}", flush=True)
    return archive


def upload(tag, archive):
    for attempt in range(3):
        res = cmd("gh", "release", "upload", tag, str(archive), "--clobber", check=False)
        if res.returncode == 0:
            print(f"UPLOAD_OK {archive.name}", flush=True)
            return
        print(f"UPLOAD_RETRY {archive.name}: {res.stderr}", flush=True)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"Could not upload {archive.name}")


def publish(archives, directory):
    notes = directory / "RELEASE_NOTES.md"
    notes.write_text(
        "# YAML configuration bundles\n\n"
        "Two ZIP packages, each containing only YAML configs, README.txt, relation.txt.\n\n"
        "- MSST-YAML-Configs.zip: 10 YAML files from nine-model and SW Fixed Releases.\n"
        "- UVR-YAML-Configs.zip: 14 Demucs YAML files from UVR public models Release.\n\n"
        "Original source URLs are attempted first and verified against backup SHA256 "
        "and sizes; fallback to backup Release if necessary.\n"
        "relation.txt lists all known checkpoint filenames, backup/source download links, "
        "sizes and SHA256. Demucs references absent from these Releases are labeled missing.\n"
        "No model checkpoint weights are included in the ZIPs.\n",
        encoding="utf-8"
    )
    current = cmd("gh", "release", "view", TAG, "--json", "isDraft", check=False)
    if current.returncode == 0:
        if not json.loads(current.stdout)["isDraft"]:
            raise RuntimeError(f"Already published {TAG}; refusing to clobber existing Release")
        print("REUSE_DRAFT", flush=True)
    else:
        cmd("gh", "release", "create", TAG, "--draft", "--latest=false",
            "--target", os.environ.get("GITHUB_SHA", "main"),
            "--title", "YAML configuration bundles (MSST + UVR)", "--notes-file", str(notes))
        print("CREATE_DRAFT", flush=True)

    for archive in archives:
        upload(TAG, archive)
    info = json.loads(cmd("gh", "release", "view", TAG, "--json", "assets").stdout)
    expected = {a.name: a.stat().st_size for a in archives}
    found = {a["name"]: a["size"] for a in info["assets"]}
    if expected != found or set(found) != set(EXPECTED):
        raise RuntimeError(f"Release asset verification failed: {found} vs {expected}")
    cmd("gh", "release", "edit", TAG, "--draft=false", "--latest=false")
    print(f"RELEASE_PUBLISHED https://github.com/{os.environ['GH_REPO']}/releases/tag/{TAG}",
          flush=True)


def main():
    msst, uvr = build_index()
    dest = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "yaml-bundles"
    dest.mkdir(parents=True, exist_ok=True)
    result = [
        make_archive("MSST-YAML-Configs.zip", msst, dest),
        make_archive("UVR-YAML-Configs.zip", uvr, dest),
    ]
    publish(result, dest)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("## YAML configuration packages\n\n")
            f.write("Published **10 MSST YAMLs + 14 UVR YAMLs** in 2 ZIP files.\n\n")
            f.write(f"https://github.com/{os.environ['GH_REPO']}/releases/tag/{TAG}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FATAL: {exc}", file=sys.stderr, flush=True)
        sys.exit(1)
