# MSST 模型备份

MSST、Roformer 和 UVR 音源分离模型的集中下载索引。权重与配置保存在 GitHub Releases，表格中的链接可直接下载附件。

## 快速下载

| 内容 | 下载 | 包含 |
| :--- | :--- | :--- |
| **MSST 配置合集** | [下载 ZIP](https://github.com/iqonli/MSSTmodelBackup/releases/download/yaml-config-bundles-2026-11-10/MSST-YAML-Configs.zip) | 10 个 YAML、`README.txt`、`relation.txt` |
| **UVR 配置合集** | [下载 ZIP](https://github.com/iqonli/MSSTmodelBackup/releases/download/yaml-config-bundles-2026-11-10/UVR-YAML-Configs.zip) | 14 个 YAML、`README.txt`、`relation.txt` |
| **九款 Roformer 模型** | [查看 Release](https://github.com/iqonli/MSSTmodelBackup/releases/tag/models-2026-11-10) | 9 组权重与配置 |
| **BS-RoFormer SW Fixed** | [查看 Release](https://github.com/iqonli/MSSTmodelBackup/releases/tag/bs-roformer-sw-fixed-2026-11-10) | 六轨分离权重与配置 |
| **UVR 模型全集** | [查看 Release](https://github.com/iqonli/MSSTmodelBackup/releases/tag/uvr-all-public-models-2026-11-10) | 86 个模型及配置附件 |

> 配置 ZIP 不含模型权重。`relation.txt` 记录配置与权重的对应关系、下载地址、大小及 SHA256。

## 常用模型

按预设用途排列；每个模型都有独立的权重和 YAML 下载链接。

| 用途 | 模型文件 | 权重 | YAML 配置 | 来源 |
| :--- | :--- | :---: | :--- | :--- |
| 人声 | `bs_leap_xe_voc.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/bs_leap_xe_voc.ckpt) | `leap_xe_config_voc.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/leap_xe_config_voc.yaml) | [来源](https://huggingface.co/pcunwa/BS-Roformer-Leap) |
| 人声备选 | `model_bs_roformer_ep_368_sdr_12.9628.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.ckpt) | `model_bs_roformer_ep_368_sdr_12.9628.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.yaml) | [来源](https://huggingface.co/Eddycrack864/Music-Source-Separation-Training) |
| 和声伴奏 | `karaoke_bs_roformer_anvuew.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/karaoke_bs_roformer_anvuew.ckpt) | `karaoke_bs_roformer_anvuew.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/karaoke_bs_roformer_anvuew.yaml) | [来源](https://huggingface.co/anvuew/karaoke_bs_roformer) |
| 和声伴奏备选 | `bs_roformer_karaoke_frazer_becruily.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/bs_roformer_karaoke_frazer_becruily.ckpt) | `config_karaoke_frazer_becruily.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_karaoke_frazer_becruily.yaml) | [来源](https://huggingface.co/becruily/bs-roformer-karaoke) |
| 无和声伴奏 | `BS-Roformer-Resurrection-Inst.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Inst.ckpt) | `BS-Roformer-Resurrection-Inst-Config.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Inst-Config.yaml) | [来源](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| 无和声伴奏备选 | `melband_roformer_inst_v2.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/melband_roformer_inst_v2.ckpt) | `config_melbandroformer_inst_v2.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_melbandroformer_inst_v2.yaml) | [来源](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |

### 其他 Roformer 模型

| 用途 | 模型文件 | 权重 | YAML 配置 | 来源 |
| :--- | :--- | :---: | :--- | :--- |
| — | `inst_v1e.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/inst_v1e.ckpt) | `config_melbandroformer_inst.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_melbandroformer_inst.yaml) | [来源](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |
| — | `BS-Roformer-Resurrection-Vocal.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Vocal.ckpt) | `BS-Roformer-Resurrection-Config.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/BS-Roformer-Resurrection-Config.yaml) | [来源](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| — | `mel_band_roformer_instrumental_becruily.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/mel_band_roformer_instrumental_becruily.ckpt) | `config_instrumental_becruily.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/config_instrumental_becruily.yaml) | [来源](https://huggingface.co/becruily/mel-band-roformer-instrumental) |
| 六轨分离 | `BS-Rofo-SW-Fixed.ckpt` | [下载权重](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/BS-Rofo-SW-Fixed.ckpt) | `BS-Rofo-SW-Fixed.yaml` · [下载配置](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/BS-Rofo-SW-Fixed.yaml) | [来源](https://huggingface.co/enerjazzer/BS-ROFO-SW-Fixed) |

> `BS-Roformer-Resurrection-Vocal.ckpt` 的原始文件名为 `BS-Roformer-Resurrection.ckpt`，备份时为区分版本进行了重命名。

## UVR 模型全集

来源：[TRvlvr / all_public_uvr_models](https://github.com/TRvlvr/model_repo/releases/tag/all_public_uvr_models) · 86 个上游文件 · 约 16.08 GB。

按架构分类，点击分类名称展开文件列表。全部链接均直达本仓库的 Release 附件。

<details>
<summary><strong>VR 模型（PTH）</strong> · 27 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `1_HP-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/1_HP-UVR.pth) |
| `2_HP-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/2_HP-UVR.pth) |
| `3_HP-Vocal-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/3_HP-Vocal-UVR.pth) |
| `4_HP-Vocal-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/4_HP-Vocal-UVR.pth) |
| `5_HP-Karaoke-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/5_HP-Karaoke-UVR.pth) |
| `6_HP-Karaoke-UVR.pth` | 120.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/6_HP-Karaoke-UVR.pth) |
| `7_HP2-UVR.pth` | 524.6 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/7_HP2-UVR.pth) |
| `8_HP2-UVR.pth` | 524.6 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/8_HP2-UVR.pth) |
| `9_HP2-UVR.pth` | 524.6 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/9_HP2-UVR.pth) |
| `10_SP-UVR-2B-32000-1.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/10_SP-UVR-2B-32000-1.pth) |
| `11_SP-UVR-2B-32000-2.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/11_SP-UVR-2B-32000-2.pth) |
| `12_SP-UVR-3B-44100.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/12_SP-UVR-3B-44100.pth) |
| `13_SP-UVR-4B-44100-1.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/13_SP-UVR-4B-44100-1.pth) |
| `14_SP-UVR-4B-44100-2.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/14_SP-UVR-4B-44100-2.pth) |
| `15_SP-UVR-MID-44100-1.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/15_SP-UVR-MID-44100-1.pth) |
| `16_SP-UVR-MID-44100-2.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/16_SP-UVR-MID-44100-2.pth) |
| `17_HP-Wind_Inst-UVR.pth` | 213.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/17_HP-Wind_Inst-UVR.pth) |
| `MGM_HIGHEND_v4.pth` | 30.4 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_HIGHEND_v4.pth) |
| `MGM_LOWEND_A_v4.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_LOWEND_A_v4.pth) |
| `MGM_LOWEND_B_v4.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_LOWEND_B_v4.pth) |
| `MGM_MAIN_v4.pth` | 30.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MGM_MAIN_v4.pth) |
| `UVR-BVE-4B_SN-44100-1.pth` | 213.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-BVE-4B_SN-44100-1.pth) |
| `UVR-De-Echo-Aggressive.pth` | 121.2 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-De-Echo-Aggressive.pth) |
| `UVR-De-Echo-Normal.pth` | 121.2 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-De-Echo-Normal.pth) |
| `UVR-DeEcho-DeReverb.pth` | 213.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeEcho-DeReverb.pth) |
| `UVR-DeNoise-Lite.pth` | 17.1 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeNoise-Lite.pth) |
| `UVR-DeNoise.pth` | 121.2 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-DeNoise.pth) |

</details>

<details>
<summary><strong>MDX-Net（ONNX）</strong> · 30 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `Kim_Inst.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Inst.onnx) |
| `Kim_Vocal_1.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Vocal_1.onnx) |
| `Kim_Vocal_2.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Kim_Vocal_2.onnx) |
| `kuielab_a_bass.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_bass.onnx) |
| `kuielab_a_drums.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_drums.onnx) |
| `kuielab_a_other.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_other.onnx) |
| `kuielab_a_vocals.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_a_vocals.onnx) |
| `kuielab_b_bass.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_bass.onnx) |
| `kuielab_b_drums.onnx` | 20.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_drums.onnx) |
| `kuielab_b_other.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_other.onnx) |
| `kuielab_b_vocals.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/kuielab_b_vocals.onnx) |
| `Reverb_HQ_By_FoxJoy.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/Reverb_HQ_By_FoxJoy.onnx) |
| `UVR_MDXNET_1_9703.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_1_9703.onnx) |
| `UVR_MDXNET_2_9682.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_2_9682.onnx) |
| `UVR_MDXNET_3_9662.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_3_9662.onnx) |
| `UVR_MDXNET_9482.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_9482.onnx) |
| `UVR_MDXNET_KARA_2.onnx` | 50.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_KARA_2.onnx) |
| `UVR_MDXNET_KARA.onnx` | 28.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_KARA.onnx) |
| `UVR_MDXNET_Main.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_MDXNET_Main.onnx) |
| `UVR-MDX-NET_Crowd_HQ_1.onnx` | 56.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET_Crowd_HQ_1.onnx) |
| `UVR-MDX-NET-Inst_1.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_1.onnx) |
| `UVR-MDX-NET-Inst_2.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_2.onnx) |
| `UVR-MDX-NET-Inst_3.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_3.onnx) |
| `UVR-MDX-NET-Inst_HQ_1.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_1.onnx) |
| `UVR-MDX-NET-Inst_HQ_2.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_2.onnx) |
| `UVR-MDX-NET-Inst_HQ_3.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_3.onnx) |
| `UVR-MDX-NET-Inst_HQ_4.onnx` | 56.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_4.onnx) |
| `UVR-MDX-NET-Inst_HQ_5.onnx` | 56.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_HQ_5.onnx) |
| `UVR-MDX-NET-Inst_Main.onnx` | 50.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Inst_Main.onnx) |
| `UVR-MDX-NET-Voc_FT.onnx` | 63.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR-MDX-NET-Voc_FT.onnx) |

</details>

<details>
<summary><strong>Roformer（CKPT）</strong> · 9 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt` | 870.8 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt) |
| `melband_roformer_inst_v1.ckpt` | 870.8 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_inst_v1.ckpt) |
| `melband_roformer_inst_v2.ckpt` | 1501.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_inst_v2.ckpt) |
| `melband_roformer_instvoc_duality_v1.ckpt` | 1639.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_instvoc_duality_v1.ckpt) |
| `melband_roformer_instvox_duality_v2.ckpt` | 1639.5 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/melband_roformer_instvox_duality_v2.ckpt) |
| `model_bs_roformer_ep_317_sdr_12.9755.ckpt` | 609.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_317_sdr_12.9755.ckpt) |
| `model_bs_roformer_ep_368_sdr_12.9628.ckpt` | 609.7 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_368_sdr_12.9628.ckpt) |
| `model_bs_roformer_ep_937_sdr_10.5309.ckpt` | 374.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bs_roformer_ep_937_sdr_10.5309.ckpt) |
| `model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt` | 961.1 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt) |

</details>

<details>
<summary><strong>MDX23C（CKPT）</strong> · 2 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `MDX23C_D1581.ckpt` | 174.9 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MDX23C_D1581.ckpt) |
| `MDX23C-8KFFT-InstVoc_HQ.ckpt` | 427.3 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/MDX23C-8KFFT-InstVoc_HQ.ckpt) |

</details>

<details>
<summary><strong>其他模型（CKPT）</strong> · 2 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `checkpoint-multi_fixed.ckpt` | 142.2 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/checkpoint-multi_fixed.ckpt) |
| `model_bandit_plus_dnr_sdr_11.47.ckpt` | 142.0 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/model_bandit_plus_dnr_sdr_11.47.ckpt) |

</details>

<details>
<summary><strong>Demucs 权重（TH）</strong> · 2 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `ebf34a2d.th` | 159.6 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/ebf34a2d.th) |
| `ebf34a2db.th` | 159.6 MiB | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/ebf34a2db.th) |

</details>

<details>
<summary><strong>Demucs 配置（YAML）</strong> · 14 个文件</summary>

| 文件 | 大小 | 下载 |
| :--- | ---: | :---: |
| `hdemucs_mmi.yaml` | 33 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/hdemucs_mmi.yaml) |
| `htdemucs_6s.yaml` | 21 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs_6s.yaml) |
| `htdemucs_ft.yaml` | 149 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs_ft.yaml) |
| `htdemucs.yaml` | 21 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/htdemucs.yaml) |
| `mdx_extra_q.yaml` | 69 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_extra_q.yaml) |
| `mdx_extra.yaml` | 68 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_extra.yaml) |
| `mdx_q.yaml` | 162 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx_q.yaml) |
| `mdx.yaml` | 162 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/mdx.yaml) |
| `repro_mdx_a_hybrid_only.yaml` | 69 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a_hybrid_only.yaml) |
| `repro_mdx_a_time_only.yaml` | 69 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a_time_only.yaml) |
| `repro_mdx_a.yaml` | 69 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/repro_mdx_a.yaml) |
| `UVR_Demucs_Model_1.yaml` | 33 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_1.yaml) |
| `UVR_Demucs_Model_2.yaml` | 32 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_2.yaml) |
| `UVR_Demucs_Model_Bag.yaml` | 45 B | [点击下载](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/UVR_Demucs_Model_Bag.yaml) |

</details>


## 下载校验

| Release | SHA256 校验表 | 来源与记录 |
| :--- | :--- | :--- |
| 九款 Roformer | [SHA256SUMS.txt](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/SHA256SUMS.txt) | [SOURCE_MANIFEST.json](https://github.com/iqonli/MSSTmodelBackup/releases/download/models-2026-11-10/SOURCE_MANIFEST.json) |
| SW Fixed | [SHA256SUMS.txt](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/SHA256SUMS.txt) | [下载测速记录](https://github.com/iqonli/MSSTmodelBackup/releases/download/bs-roformer-sw-fixed-2026-11-10/DOWNLOAD_SPEED.json) |
| UVR 全集 | [SHA256SUMS.txt](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/SHA256SUMS.txt) | [SOURCE_MANIFEST.json](https://github.com/iqonli/MSSTmodelBackup/releases/download/uvr-all-public-models-2026-11-10/SOURCE_MANIFEST.json) |

Windows PowerShell 可用 `Get-FileHash -Algorithm SHA256 文件名` 核对下载文件。

## 自动备份

- [九款 Roformer 发布流程](.github/workflows/publish-models.yml) · [原始来源清单](models.json)
- [SW Fixed 发布与测速](.github/workflows/publish-bs-roformer-sw-fixed.yml)
- [UVR 模型镜像](.github/workflows/publish-uvr-models.yml) · [UVR 附件清单](uvr_source_assets.json)
- [YAML 配置打包](.github/workflows/publish-yaml-bundles.yml) · [Demucs 配置对应关系](uvr_yaml_weights.json)

权重原文件、配置及其著作权归各自发布者；本仓库的 MIT 许可证适用于仓库代码。
