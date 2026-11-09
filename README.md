# MSST 模型备份

这里备份了 10 个用于 [Music Source Separation Training（MSST）](https://github.com/ZFTurbo/Music-Source-Separation-Training) 的 Roformer 模型及对应 YAML 配置。模型文件保存在 **GitHub Releases 的 Assets** 中，点击下面的链接即可直接下载，无需从仓库源码中查找。

## 常用模型（置顶）

按使用用途排列，备用模型紧随主模型。这里的“备选”是使用上的分类，不代表性能排名。

| 用途 | 模型文件（.ckpt） | 模型 | YAML 配置 | 原始来源 |
| --- | --- | --- | --- | --- |
| **人声** | `bs_leap_xe_voc.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/bs_leap_xe_voc.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/leap_xe_config_voc.yaml)（`leap_xe_config_voc.yaml`） | [来源](https://huggingface.co/pcunwa/BS-Roformer-Leap) |
| **人声备选** | `model_bs_roformer_ep_368_sdr_12.9628.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.yaml)（`model_bs_roformer_ep_368_sdr_12.9628.yaml`） | [来源](https://huggingface.co/Eddycrack864/Music-Source-Separation-Training) |
| **和声伴奏** | `karaoke_bs_roformer_anvuew.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/karaoke_bs_roformer_anvuew.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/karaoke_bs_roformer_anvuew.yaml)（`karaoke_bs_roformer_anvuew.yaml`） | [来源](https://huggingface.co/anvuew/karaoke_bs_roformer) |
| **和声伴奏备选** | `bs_roformer_karaoke_frazer_becruily.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/bs_roformer_karaoke_frazer_becruily.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_karaoke_frazer_becruily.yaml)（`config_karaoke_frazer_becruily.yaml`） | [来源](https://huggingface.co/becruily/bs-roformer-karaoke) |
| **无和声伴奏** | `BS-Roformer-Resurrection-Inst.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Inst.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Inst-Config.yaml)（`BS-Roformer-Resurrection-Inst-Config.yaml`） | [来源](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| **无和声伴奏备选** | `melband_roformer_inst_v2.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/melband_roformer_inst_v2.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_melbandroformer_inst_v2.yaml)（`config_melbandroformer_inst_v2.yaml`） | [来源](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |

## 其他模型

| 用途 | 模型文件（.ckpt） | 模型 | YAML 配置 | 原始来源 |
| --- | --- | --- | --- | --- |
| — | `inst_v1e.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/inst_v1e.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_melbandroformer_inst.yaml)（`config_melbandroformer_inst.yaml`） | [来源](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |
| — | `BS-Roformer-Resurrection-Vocal.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Vocal.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Config.yaml)（`BS-Roformer-Resurrection-Config.yaml`） | [来源](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| — | `mel_band_roformer_instrumental_becruily.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/mel_band_roformer_instrumental_becruily.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_instrumental_becruily.yaml)（`config_instrumental_becruily.yaml`） | [来源](https://huggingface.co/becruily/mel-band-roformer-instrumental) |
| **六轨分离** | `BS-Rofo-SW-Fixed.ckpt` | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/BS-Rofo-SW-Fixed.ckpt) | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/BS-Rofo-SW-Fixed.yaml)（`BS-Rofo-SW-Fixed.yaml`） | [来源](https://huggingface.co/enerjazzer/BS-ROFO-SW-Fixed) |

## Release 与校验文件

- [九模型合集：models-2026-11-10](https://github.com/iqonli/MSSTmodelBackup/releases/tag/models-2026-11-10)：9 组权重和 YAML，并附有 `SHA256SUMS.txt` 与 `SOURCE_MANIFEST.json`。
- [BS-RoFormer SW Fixed：bs-roformer-sw-fixed-2026-11-10](https://github.com/iqonli/MSSTmodelBackup/releases/tag/bs-roformer-sw-fixed-2026-11-10)：独立发布的六轨模型，含权重、YAML、`SHA256SUMS.txt` 与 `DOWNLOAD_SPEED.json`。

每个模型建议同时保存其权重和对应的 YAML；不同 Roformer 变体的配置不可随意互换。下载后可利用各 Release 中的 `SHA256SUMS.txt` 检查文件完整性。

**文件名说明：** `BS-Roformer-Resurrection-Vocal.ckpt` 在原始仓库中的文件名为 `BS-Roformer-Resurrection.ckpt`，备份时为了区分人声与伴奏版本进行了重命名，其 YAML 仍是 `BS-Roformer-Resurrection-Config.yaml`。

## 自动备份

模型权重不提交至 Git 历史。本仓库通过 GitHub Actions 从原始发布源获取权重，再上传至 Releases：

- [九模型发布工作流](.github/workflows/publish-models.yml) · [模型来源清单](models.json)
- [BS-RoFormer SW Fixed 发布工作流](.github/workflows/publish-bs-roformer-sw-fixed.yml)：在 Actions 日志中输出实时和平均下载速度，测速记录也保存在对应 Release 中。

## 来源与许可

本仓库仅作模型文件备份与下载索引。模型权重、配置文件的作者和使用许可以各自原始发布页为准；仓库的 MIT 许可证只适用于本仓库的代码，不代表第三方模型权重采用 MIT 许可。BS-RoFormer SW Fixed 的备份来源是 `enerjazzer/BS-ROFO-SW-Fixed` 镜像，其原作者仓库当前不可用，权重授权情况未确认。
