# MSST model backup

A single GitHub Release containing nine Roformer checkpoints and the matching configuration YAMLs whenever they exist upstream.

**Release:** [models-2026-11-10](https://github.com/iqonli/MSSTmodelBackup/releases/tag/models-2026-11-10)

| Checkpoint asset | YAML asset | Original model repository |
| --- | --- | --- |
| `inst_v1e.ckpt` | `config_melbandroformer_inst.yaml` | [pcunwa/Mel-Band-Roformer-Inst](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |
| `bs_leap_xe_voc.ckpt` | `leap_xe_config_voc.yaml` | [pcunwa/BS-Roformer-Leap](https://huggingface.co/pcunwa/BS-Roformer-Leap) |
| `model_bs_roformer_ep_368_sdr_12.9628.ckpt` | `model_bs_roformer_ep_368_sdr_12.9628.yaml` | [Eddycrack864/Music-Source-Separation-Training](https://huggingface.co/Eddycrack864/Music-Source-Separation-Training) |
| `karaoke_bs_roformer_anvuew.ckpt` | `karaoke_bs_roformer_anvuew.yaml` | [anvuew/karaoke_bs_roformer](https://huggingface.co/anvuew/karaoke_bs_roformer) |
| `bs_roformer_karaoke_frazer_becruily.ckpt` | `config_karaoke_frazer_becruily.yaml` | [becruily/bs-roformer-karaoke](https://huggingface.co/becruily/bs-roformer-karaoke) |
| `BS-Roformer-Resurrection-Inst.ckpt` | `BS-Roformer-Resurrection-Inst-Config.yaml` | [pcunwa/BS-Roformer-Resurrection](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| `BS-Roformer-Resurrection-Vocal.ckpt` | `BS-Roformer-Resurrection-Config.yaml` | [pcunwa/BS-Roformer-Resurrection](https://huggingface.co/pcunwa/BS-Roformer-Resurrection) |
| `mel_band_roformer_instrumental_becruily.ckpt` | `config_instrumental_becruily.yaml` | [becruily/mel-band-roformer-instrumental](https://huggingface.co/becruily/mel-band-roformer-instrumental) |
| `melband_roformer_inst_v2.ckpt` | `config_melbandroformer_inst_v2.yaml` | [pcunwa/Mel-Band-Roformer-Inst](https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst) |

The source file for `BS-Roformer-Resurrection-Vocal.ckpt` is named `BS-Roformer-Resurrection.ckpt` upstream. It is renamed only in the backup Release. The paired YAML is `BS-Roformer-Resurrection-Config.yaml`.

This repository stores the publishing workflow and a [machine-readable source list](models.json), not the large checkpoints. [GitHub Actions](.github/workflows/publish-models.yml) downloads each checkpoint, uploads it directly to the same draft Release, and adds the YAML if found. A missing checkpoint or failed transfer stops the process; a missing upstream YAML is skipped. The Release is published only after all nine weights succeed. Workflow runs can be started manually and reuse the same Release tag.

The Release includes `SHA256SUMS.txt` and `SOURCE_MANIFEST.json` for verifying downloads and recording the exact upstream revision. The workflow requires the GitHub Actions token to have **Contents: write** permission.

## Credits and licensing

Models and YAML configurations belong to their respective authors and may carry different licenses. Follow each linked upstream model repository for attribution, licenses, and usage restrictions. The MIT license in this GitHub repository covers the automation code only; it **does not** relicense third-party weights or configurations.
