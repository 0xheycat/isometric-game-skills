# 02 — Production Guide (ComfyUI · Resep D)

This is the **proven, winning recipe**. Follow it exactly before experimenting.

## Required models (inventory)

| Type | File | Note |
|---|---|---|
| Checkpoint | `juggernautXL_ragnarokBy` | SDXL base |
| LoRA 1 | `isometric_tilemap_xl` | strength **0.75** — gives the iso diamond shape |
| LoRA 2 | `white_background_sdxl` | strength **0.7** — clean cuttable background |
| VAE | `sdxl_vae` | standard SDXL VAE |
| (Export) | `ComfyUI-Inspyrenet-Rembg` **or** SAM `sam_vit_b_01ec64` | background removal |

## Sampler settings (do not improvise first)

| Setting | Value |
|---|---|
| Sampler | `dpmpp_2m` |
| Scheduler | `karras` |
| Steps | 30 |
| CFG | 6.5 |
| Denoise | 1.0 |
| Seed | **FIXED** (e.g. `123456789`) — same for every tile |
| Latent | `EmptyLatentImage` 1024×1024, batch 1 |

## Node graph (Resep D)

```
CheckpointLoaderSimple (juggernautXL_ragnarokBy)
   -> LoraLoader (isometric_tilemap_xl, 0.75)
      -> LoraLoader (white_background_sdxl, 0.7)
         -> CLIPTextEncode (positive)
         -> CLIPTextEncode (negative)
EmptyLatentImage (1024x1024, batch 1)
KSampler (seed FIXED, 30 steps, CFG 6.5, dpmpp_2m, karras, denoise 1.0)
VAELoader (sdxl_vae) -> VAEDecode
   -> SaveImage                      (raw tile)
   -> InspyrenetRembg -> SaveImage   (transparent PNG)
```

A ready-to-load builder + JSON is in `scripts/` (`build_workflow.py`,
`MEOWART_iso_tile_transparent_resepD_v3.json`).

## Step-by-step

1. Load the checkpoint and both LoRAs at the strengths above.
2. Paste the **positive** and **negative** prompts from `03-prompts.md`.
3. Set the **seed to a fixed number** and KSampler settings as in the table.
4. Generate the **first tile (grass)**. Confirm: clean diamond, thick base, flat background.
5. **Keep the seed locked.** Change **only the surface phrase** for the next tile.
6. Repeat for every material. The shape stays identical because the seed is fixed.
7. Run each output through **rembg / SAM** to get a transparent PNG.
8. Import into your engine's tilemap.

## Why two LoRAs

- `isometric_tilemap_xl` forces the **2:1 diamond geometry** (the part the engine needs).
- `white_background_sdxl` keeps the background **flat and uniform**, so background
  removal is clean with no halo/edge fringe.

## Post-processing (transparent PNG)

Use the `InspyrenetRembg` node (pack: `ComfyUI-Inspyrenet-Rembg`, mode `default`) right
after `VAEDecode`, then `SaveImage`. If you prefer SAM, use `sam_vit_b_01ec64`. Either
way you get a PNG with alpha, ready for the tilemap.

Next: `03-prompts.md` for the exact prompts.
