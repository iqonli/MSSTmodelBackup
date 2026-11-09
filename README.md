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

## UVR 公共模型全集备份

来源：[TRvlvr/model_repo · all_public_uvr_models](https://github.com/TRvlvr/model_repo/releases/tag/all_public_uvr_models)。2026-11-10 核对时，上游实际列出 **86 个附件**（27 个 PTH、30 个 ONNX、13 个 CKPT、2 个 TH、14 个 YAML），共 **16,077,696,038 字节**。历史介绍中的“88 个”与当前上游清单不符，因此下面只列出实际存在的 86 个原始文件。

**[打开本仓库的 UVR 独立 Release](https://github.com/iqonli/MSSTmodelBackup/releases/tag/uvr-all-public-models-2026-11-10)**（明确不设为 Latest）。文件名保持上游原样；各“点击下载”直接指向 Release Assets，不使用 Raw Content。

### VR Architecture（.pth）（27）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `1_HP-UVR.pth` | 120.92 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/1_HP-UVR.pth) |
| `2_HP-UVR.pth` | 120.91 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/2_HP-UVR.pth) |
| `3_HP-Vocal-UVR.pth` | 120.92 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/3_HP-Vocal-UVR.pth) |
| `4_HP-Vocal-UVR.pth` | 120.92 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/4_HP-Vocal-UVR.pth) |
| `5_HP-Karaoke-UVR.pth` | 120.91 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/5_HP-Karaoke-UVR.pth) |
| `6_HP-Karaoke-UVR.pth` | 120.91 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/6_HP-Karaoke-UVR.pth) |
| `7_HP2-UVR.pth` | 524.64 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/7_HP2-UVR.pth) |
| `8_HP2-UVR.pth` | 524.65 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/8_HP2-UVR.pth) |
| `9_HP2-UVR.pth` | 524.65 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/9_HP2-UVR.pth) |
| `10_SP-UVR-2B-32000-1.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/10_SP-UVR-2B-32000-1.pth) |
| `11_SP-UVR-2B-32000-2.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/11_SP-UVR-2B-32000-2.pth) |
| `12_SP-UVR-3B-44100.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/12_SP-UVR-3B-44100.pth) |
| `13_SP-UVR-4B-44100-1.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/13_SP-UVR-4B-44100-1.pth) |
| `14_SP-UVR-4B-44100-2.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/14_SP-UVR-4B-44100-2.pth) |
| `15_SP-UVR-MID-44100-1.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/15_SP-UVR-MID-44100-1.pth) |
| `16_SP-UVR-MID-44100-2.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/16_SP-UVR-MID-44100-2.pth) |
| `17_HP-Wind_Inst-UVR.pth` | 213.30 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/17_HP-Wind_Inst-UVR.pth) |
| `MGM_HIGHEND_v4.pth` | 30.39 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_HIGHEND_v4.pth) |
| `MGM_LOWEND_A_v4.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_LOWEND_A_v4.pth) |
| `MGM_LOWEND_B_v4.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_LOWEND_B_v4.pth) |
| `MGM_MAIN_v4.pth` | 30.46 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_MAIN_v4.pth) |
| `UVR-BVE-4B_SN-44100-1.pth` | 213.29 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-BVE-4B_SN-44100-1.pth) |
| `UVR-De-Echo-Aggressive.pth` | 121.25 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-De-Echo-Aggressive.pth) |
| `UVR-De-Echo-Normal.pth` | 121.25 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-De-Echo-Normal.pth) |
| `UVR-DeEcho-DeReverb.pth` | 213.29 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeEcho-DeReverb.pth) |
| `UVR-DeNoise-Lite.pth` | 17.09 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeNoise-Lite.pth) |
| `UVR-DeNoise.pth` | 121.25 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeNoise.pth) |

### MDX-Net / ONNX（.onnx）（30）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `Kim_Inst.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Inst.onnx) |
| `Kim_Vocal_1.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Vocal_1.onnx) |
| `Kim_Vocal_2.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Vocal_2.onnx) |
| `kuielab_a_bass.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_bass.onnx) |
| `kuielab_a_drums.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_drums.onnx) |
| `kuielab_a_other.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_other.onnx) |
| `kuielab_a_vocals.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_vocals.onnx) |
| `kuielab_b_bass.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_bass.onnx) |
| `kuielab_b_drums.onnx` | 20.91 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_drums.onnx) |
| `kuielab_b_other.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_other.onnx) |
| `kuielab_b_vocals.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_vocals.onnx) |
| `Reverb_HQ_By_FoxJoy.onnx` | 63.69 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Reverb_HQ_By_FoxJoy.onnx) |
| `UVR_MDXNET_1_9703.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_1_9703.onnx) |
| `UVR_MDXNET_2_9682.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_2_9682.onnx) |
| `UVR_MDXNET_3_9662.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_3_9662.onnx) |
| `UVR_MDXNET_9482.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_9482.onnx) |
| `UVR_MDXNET_KARA_2.onnx` | 50.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_KARA_2.onnx) |
| `UVR_MDXNET_KARA.onnx` | 28.33 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_KARA.onnx) |
| `UVR_MDXNET_Main.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_Main.onnx) |
| `UVR-MDX-NET_Crowd_HQ_1.onnx` | 56.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET_Crowd_HQ_1.onnx) |
| `UVR-MDX-NET-Inst_1.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_1.onnx) |
| `UVR-MDX-NET-Inst_2.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_2.onnx) |
| `UVR-MDX-NET-Inst_3.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_3.onnx) |
| `UVR-MDX-NET-Inst_HQ_1.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_1.onnx) |
| `UVR-MDX-NET-Inst_HQ_2.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_2.onnx) |
| `UVR-MDX-NET-Inst_HQ_3.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_3.onnx) |
| `UVR-MDX-NET-Inst_HQ_4.onnx` | 56.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_4.onnx) |
| `UVR-MDX-NET-Inst_HQ_5.onnx` | 56.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_5.onnx) |
| `UVR-MDX-NET-Inst_Main.onnx` | 50.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_Main.onnx) |
| `UVR-MDX-NET-Voc_FT.onnx` | 63.67 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Voc_FT.onnx) |

### Roformer（.ckpt）（9）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt` | 870.80 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt) |
| `melband_roformer_inst_v1.ckpt` | 870.80 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_inst_v1.ckpt) |
| `melband_roformer_inst_v2.ckpt` | 1501.54 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_inst_v2.ckpt) |
| `melband_roformer_instvoc_duality_v1.ckpt` | 1639.48 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_instvoc_duality_v1.ckpt) |
| `melband_roformer_instvox_duality_v2.ckpt` | 1639.48 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_instvox_duality_v2.ckpt) |
| `model_bs_roformer_ep_317_sdr_12.9755.ckpt` | 609.71 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_317_sdr_12.9755.ckpt) |
| `model_bs_roformer_ep_368_sdr_12.9628.ckpt` | 609.70 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.ckpt) |
| `model_bs_roformer_ep_937_sdr_10.5309.ckpt` | 374.86 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_937_sdr_10.5309.ckpt) |
| `model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt` | 961.13 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt) |

### MDX23C（.ckpt）（2）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `MDX23C_D1581.ckpt` | 174.88 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MDX23C_D1581.ckpt) |
| `MDX23C-8KFFT-InstVoc_HQ.ckpt` | 427.34 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MDX23C-8KFFT-InstVoc_HQ.ckpt) |

### 其他 CKPT 模型（2）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `checkpoint-multi_fixed.ckpt` | 142.22 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/checkpoint-multi_fixed.ckpt) |
| `model_bandit_plus_dnr_sdr_11.47.ckpt` | 141.99 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bandit_plus_dnr_sdr_11.47.ckpt) |

### Demucs 权重（.th）（2）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `ebf34a2d.th` | 159.64 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/ebf34a2d.th) |
| `ebf34a2db.th` | 159.64 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/ebf34a2db.th) |

### Demucs 配置（.yaml）（14）

| 文件名 | 大小（MiB） | 下载 |
| --- | ---: | --- |
| `hdemucs_mmi.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/hdemucs_mmi.yaml) |
| `htdemucs_6s.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs_6s.yaml) |
| `htdemucs_ft.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs_ft.yaml) |
| `htdemucs.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs.yaml) |
| `mdx_extra_q.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_extra_q.yaml) |
| `mdx_extra.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_extra.yaml) |
| `mdx_q.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_q.yaml) |
| `mdx.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx.yaml) |
| `repro_mdx_a_hybrid_only.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a_hybrid_only.yaml) |
| `repro_mdx_a_time_only.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a_time_only.yaml) |
| `repro_mdx_a.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a.yaml) |
| `UVR_Demucs_Model_1.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_1.yaml) |
| `UVR_Demucs_Model_2.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_2.yaml) |
| `UVR_Demucs_Model_Bag.yaml` | 0.00 | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_Bag.yaml) |

### 完整性校验与自动备份

- [SHA256SUMS.txt](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/SHA256SUMS.txt)：完成下载后计算的 86 个原始文件 SHA256，可用于校验备份完整性。
- [SOURCE_MANIFEST.json](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/SOURCE_MANIFEST.json)：上游文件名、文件大小、来源 Asset ID 与下载后哈希记录。

独立 [GitHub Actions 工作流](.github/workflows/publish-uvr-models.yml) 按顺序下载、校验大小、上传并清理临时文件。全部文件上传成功后才发布 Release；失败时保留草稿，以免误报完整。上游 14 个 YAML 是 Demucs 配置清单，不保证与所有其他架构模型一一配对。模型版权和授权以原项目及权重作者为准，本仓库 MIT 许可证不覆盖第三方模型。
