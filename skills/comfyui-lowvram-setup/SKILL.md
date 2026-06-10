---
name: comfyui-lowvram-setup
description: Use when configuring ComfyUI to generate SDXL isometric assets on a 12GB GPU (RTX 3060) without out-of-memory crashes.
license: MIT
---

# ComfyUI Low-VRAM Setup (12GB)

## Overview

Most isometric asset failures on consumer GPUs are setup failures, not prompt failures. This skill gives a deterministic, low-VRAM-safe SDXL configuration so generations are reproducible and never OOM on a 12GB card.

## When to Use

- Setting up ComfyUI on an RTX 3060 / 12GB or similar.
- Generations randomly crash, stall, or produce inconsistent output.
- You need reproducible results across a whole tile set.

## Process

1. Launch ComfyUI with low-VRAM flags: `--lowvram` (or `--medvram-sdxl`) and `--use-split-cross-attention`.
2. Use one SDXL checkpoint for the whole project (e.g. juggernautXL). Never mix checkpoints mid-set.
3. Set the sampler to DPM++ 2M Karras, 30 steps, CFG 6.5. Keep these FIXED for every asset.
4. Load the matching SDXL VAE explicitly (sdxl_vae) - do not rely on baked VAE.
5. FIX the seed for a tile set. A changing seed is the #1 cause of mismatched assets.
6. Generate at 1024x1024, then downscale - do not generate above VRAM budget.
7. Save the workflow JSON so the exact graph is reproducible and shareable.

```bash
python main.py --lowvram --use-split-cross-attention
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I have enough VRAM, I will skip the flags" | One LoRA stack later you OOM mid-batch and lose the seed. Set flags up front. |
| "Changing the seed makes assets more varied" | Varied = inconsistent. A tile set needs the SAME seed and settings. |

## Red Flags - STOP if you catch yourself:

- Mixing checkpoints between assets in the same set.
- Letting the seed randomize across a tile set.
- Generating at 1536+ then wondering why it crashes.

## Verification

You are NOT done until every box is checked:

- [ ] ComfyUI launches with low-VRAM flags and does not OOM on a full batch.
- [ ] Sampler, steps, CFG, VAE and seed are documented and fixed.
- [ ] The workflow JSON is saved and re-loads identically.
