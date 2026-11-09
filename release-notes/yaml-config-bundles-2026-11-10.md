将三个模型 Release 的 YAML 配置整理为两份 ZIP，每份包含 `README.txt`、`relation.txt` 和 `yaml/` 目录。

## 下载

| 压缩包 | 配置数量 | 下载 |
| :--- | ---: | :--- |
| `MSST-YAML-Configs.zip` | 10 | [下载 ZIP](https://github.com/iqonli/MSSTmodelBackup/releases/download/yaml-config-bundles-2026-11-10/MSST-YAML-Configs.zip) |
| `UVR-YAML-Configs.zip` | 14 | [下载 ZIP](https://github.com/iqonli/MSSTmodelBackup/releases/download/yaml-config-bundles-2026-11-10/UVR-YAML-Configs.zip) |

`relation.txt` 列出每个 YAML 对应的权重文件名、可用的下载地址、字节数和 SHA256。UVR 的 Demucs 配置可能引用本仓库未收录的权重，相关记录中会标记缺失字段。

制作时优先从上游下载 YAML，校验 SHA256 后打包；上游不可用时使用本仓库的 Release 附件。两个 ZIP 均不包含权重。

[返回 README 下载入口](https://github.com/iqonli/MSSTmodelBackup#快速下载)
