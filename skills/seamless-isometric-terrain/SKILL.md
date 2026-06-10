---
name: seamless-isometric-terrain
description: >
  Generate seamless, tileable isometric terrain tiles (Hay Day / farm-game style)
  with ComfyUI on consumer GPUs (RTX 3060 12GB). Use this skill whenever the user
  wants to create ground tiles (grass, dirt, water, road, plowed field, sand, stone,
  snow), build a tilemap that connects without seams or gaps, fix tiles that have
  visible edges/mismatched shapes/mixed colors, or set up the proven "Resep D"
  isometric tile workflow, prompts, and post-processing (transparent PNG via rembg/SAM).
license: MIT
---

# Seamless Isometric Terrain (Hay Day-style) — Skill

## What this skill does

This skill produces **isometric ground tiles** that snap together into a clean map
with **no seams, no gaps, and no color chaos** — the look of mobile farm games like
Hay Day. It targets **ComfyUI on an RTX 3060 12GB / 32GB RAM** but the recipe works
on any SDXL-capable GPU.

The single most important idea: **a map looks seamless when every tile shares the
exact same diamond shape and thickness.** Get the shape consistent first (fixed seed),
then vary only the surface texture. Everything in this skill enforces that rule.

![Target seamless map](assets/01-goal-map.png)
*Goal: tiles that connect into a continuous map. This is a reference render — production tiles are generated one-by-one in ComfyUI and assembled by the game engine.*

## When to use this skill

- The user wants to make terrain / ground tiles for an isometric game or map.
- Tiles don't line up: visible **edges, seams, gaps**, or **mismatched sizes/angles**.
- Tiles have **mixed/irregular colors**, stray grass rims, or random props.
- The user needs the **ComfyUI workflow, prompts, settings, or transparent-PNG export** for tiles.
- The user asks to extend a tile set (seasons, new materials like sand/stone/snow).

## How to use this skill (workflow at a glance)

1. **Read the overview** → `references/01-overview.md` (concepts + the golden rule).
2. **Set up ComfyUI** with the proven recipe → `references/02-production-guide.md`.
3. **Copy the prompts** (positive/negative + per-tile table) → `references/03-prompts.md`.
4. **Follow the rules + the avoid-list** → `references/04-rules.md`.
5. **If a tile is wrong**, diagnose it → `references/05-troubleshooting.md`.
6. **Build the full set / extend it** → `references/06-tileset-spec.md`.

When running the workflow programmatically, see `scripts/` for the ComfyUI graph
builder and the rembg (transparent background) node plan.

## The golden rule (never break this)

> **Fix the seed. Keep the prompt short. Same shape for every tile.**
>
> Seam problems are almost never a texture problem — they are a **shape consistency**
> problem. Use one **FIXED seed** for the whole set so every tile is the same diamond,
> then only swap the short surface phrase per material.

![Single target tile](assets/02-single-grass-tile.png)
*One tile, done right: 2:1 diamond, full surface, thick solid soil base, clean background.*

## Quick reference card

| Setting | Value |
|---|---|
| Checkpoint | `juggernautXL_ragnarokBy` |
| LoRA 1 | `isometric_tilemap_xl` @ 0.75 |
| LoRA 2 | `white_background_sdxl` @ 0.7 |
| Sampler / Scheduler | DPM++ 2M / Karras |
| Steps / CFG | 30 / 6.5 |
| Seed | **FIXED** (identical for every tile in the set) |
| Resolution | 1024 × 1024, batch 1 |
| VAE | `sdxl_vae` |
| Export | rembg / SAM → transparent PNG |

**Positive template:**
```
single isometric full [SURFACE] block tile, 2:1 isometric view,
thick solid [COLOR] soil base underneath, soft painterly shading,
simple clean composition, isolated on plain flat background,
game asset, high quality
```

**Never put these in the prompt** (top 3 causes of failure):
1. `thin grassy rim` / `green grass along the edges`
2. `Hay Day mobile farm game art style, cute hand-painted cartoon`
3. Long, wordy surface descriptions

See `references/04-rules.md` for the full avoid-list and `references/05-troubleshooting.md` for fixes.

## Verification

The tile set is done only when **every** box is checked:

- [ ] Each tile fills its full 2:1 isometric footprint — no thin grassy rim or stray edge.
- [ ] Placed in a grid, tiles connect with **no visible seam, gap, or color mismatch**.
- [ ] The seed was **fixed** across the whole set, so colors/lighting match.
- [ ] No stray props, buildings, or extra objects baked into a ground tile.
- [ ] Background removed to clean transparent alpha (no halo/fringe).
- [ ] The prompt did **not** contain any of the 3 banned phrases above.
- [ ] 3+ terrain types generated and verified together in one test map.
