# 05 — Troubleshooting (Symptom → Cause → Fix)

Use this table when a tile or map looks wrong. Most issues trace back to **seed** or
**prompt length**, not the model.

| Symptom | Likely cause | Fix |
|---|---|---|
| **Visible seams / edges between tiles** | Seed not fixed → shapes differ | Lock ONE fixed seed for the whole set; regenerate all tiles |
| **Gaps between tiles** | Tile shape not a clean 2:1 diamond | Raise `isometric_tilemap_xl` to ~0.8; remove any `irregular`/`pond shape` wording |
| **Stray grass on edges of non-grass tiles** | `grassy rim` / leftover grass terms | Add `grass, grassy edges, plants` to that tile's negative; remove rim phrasing |
| **Mixed / irregular / blotchy colors** | Prompt too long, or `cute cartoon` style term | Shorten surface phrase; remove `Hay Day ... cute hand-painted cartoon` |
| **Random props / houses / plants on tiles** | Style term pulling in farm clutter | Add `props, house, building, plants` to negative; drop game-name style terms |
| **Halo / white fringe after background removal** | Background not flat enough | Keep `white_background_sdxl` @ 0.7; ensure `plain flat background` in prompt |
| **Tile thickness varies across set** | `thick solid [COLOR] soil base` omitted on some | Keep the base phrase identical on every tile |
| **Water looks like a pond, not a tile** | `pond shape` / `irregular edges` leaking in | Use `calm flat blue water surface on top`; negative `pond shape, irregular edges` |
| **Result looks like a gemstone/crystal** | Model latching onto "diamond" | Keep `diamond gemstone, crystal, jewel, gem` in negative (already in base) |
| **Tiles look 3D-rendered / photographic** | Missing style guard | Keep `realistic photo, 3d render` in negative; rely on `soft painterly shading` |
| **Top-down flat instead of isometric** | iso LoRA too weak / `flat top-down texture` | Raise iso LoRA strength; keep `flat top-down texture` in negative |
| **Tiles inconsistent across a batch** | batch > 1 with varied latents | Use batch 1, fixed seed, generate one tile at a time |

## Decision flow

```
Tile bad?
 |- Bad ONLY when placed in map (alone it's fine)
 |     -> shape/consistency issue -> FIX SEED, match grass tile shape
 |- Bad even alone
       |- wrong colors / clutter   -> SHORTEN prompt, clean negative
       |- wrong geometry           -> adjust isometric_tilemap_xl strength
       |- bad cutout / fringe      -> check white_background LoRA + rembg
```

## Golden recovery step

If in doubt, **regenerate the whole set from the known-good grass tile**: same seed,
same settings, swap only the surface phrase. Consistency beats per-tile tweaking.

Next: `06-tileset-spec.md`.
