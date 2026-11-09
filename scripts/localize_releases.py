#!/usr/bin/env python3
"""同步四个已发布 Release 的中文标题和说明。只修改 name、body，不改标签、附件或 Latest。"""
import json
import os
from pathlib import Path
import subprocess


RELEASES = [
    ("models-2026-11-10", "九款 Roformer 模型｜权重与 YAML 配置"),
    ("bs-roformer-sw-fixed-2026-11-10", "BS-RoFormer SW Fixed｜六轨分离模型"),
    ("uvr-all-public-models-2026-11-10", "UVR 公共模型全集｜按架构分类备份"),
    ("yaml-config-bundles-2026-11-10", "YAML 配置合集｜MSST 与 UVR 双 ZIP"),
]


def gh(method, endpoint, payload=None):
    cmd = ["gh", "api"]
    if method != "GET":
        cmd += ["--method", method]
    cmd.append(endpoint)
    if payload is not None:
        cmd += ["--input", "-"]
    done = subprocess.run(
        cmd, input=json.dumps(payload, ensure_ascii=False) if payload else None,
        capture_output=True, text=True,
    )
    if done.returncode:
        raise RuntimeError(f"{method} {endpoint} 失败：{done.stderr}")
    return json.loads(done.stdout)


def main():
    repo = os.environ["GH_REPO"]
    latest_before = gh("GET", f"repos/{repo}/releases/latest")["tag_name"]
    print(f"LATEST_BEFORE {latest_before}", flush=True)

    for tag, title in RELEASES:
        notes = Path("release-notes") / f"{tag}.md"
        if not notes.is_file():
            raise FileNotFoundError(notes)
        body = notes.read_text(encoding="utf-8")
        current = gh("GET", f"repos/{repo}/releases/tags/{tag}")
        if current["draft"]:
            raise RuntimeError(f"Release 仍为草稿：{tag}")

        original_assets = {
            a["name"]: (a["id"], a["size"]) for a in current["assets"]
        }
        if current["name"] != title or current["body"] != body:
            gh("PATCH", f"repos/{repo}/releases/{current['id']}", {
                "name": title, "body": body
            })
        after = gh("GET", f"repos/{repo}/releases/{current['id']}")
        new_assets = {
            a["name"]: (a["id"], a["size"]) for a in after["assets"]
        }
        if after["name"] != title or after["body"] != body:
            raise RuntimeError(f"Release 文本校验失败：{tag}")
        if after["tag_name"] != tag or new_assets != original_assets:
            raise RuntimeError(f"Release 标签或附件被意外修改：{tag}")
        print(f"UPDATED {tag}: {title} ({len(new_assets)} 个附件)", flush=True)

    latest_after = gh("GET", f"repos/{repo}/releases/latest")["tag_name"]
    print(f"LATEST_AFTER {latest_after}", flush=True)
    if latest_after != latest_before:
        raise RuntimeError(f"Latest 意外变化：{latest_before} -> {latest_after}")


if __name__ == "__main__":
    main()
