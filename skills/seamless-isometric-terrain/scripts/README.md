# Scripts

Helper files to build the proven "Resep D" ComfyUI workflow that produces seamless
isometric tiles with transparent backgrounds.

## Files

- `build_workflow.py` — Python builder that emits the ComfyUI graph JSON for Resep D
  (checkpoint + 2 LoRAs + KSampler + VAE decode + rembg + save).
- `MEOWART_iso_tile_transparent_resepD_v3.json` — ready-to-load ComfyUI workflow
  (drag-and-drop into the ComfyUI canvas, or load via the API).

## How to use

### Option A — load the JSON directly
1. Open ComfyUI.
2. Menu → **Load** → pick `MEOWART_iso_tile_transparent_resepD_v3.json`.
3. Paste your positive/negative prompts (see `../references/03-prompts.md`).
4. Set the **seed to a fixed number** and queue.

### Option B — regenerate the JSON
```bash
python3 build_workflow.py   # writes the workflow JSON next to this script
```

## Node plan (Resep D v3, with rembg)

```
CheckpointLoaderSimple (juggernautXL_ragnarokBy)
 -> LoraLoader (isometric_tilemap_xl, 0.75)
 -> LoraLoader (white_background_sdxl, 0.7)
 -> CLIPTextEncode (positive) / CLIPTextEncode (negative)
EmptyLatentImage (1024x1024, batch 1)
KSampler (seed FIXED, 30 steps, CFG 6.5, dpmpp_2m, karras, denoise 1.0)
VAELoader (sdxl_vae) -> VAEDecode
 -> InspyrenetRembg (pack: ComfyUI-Inspyrenet-Rembg, mode "default")
 -> SaveImage   (transparent PNG)
```

> Requires the custom node pack **ComfyUI-Inspyrenet-Rembg** for the transparent
> output. Without it, remove the rembg node and use SAM (`sam_vit_b_01ec64`) or
> export the raw tile and cut it externally.
