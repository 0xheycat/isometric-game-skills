# 01 — Overview & Core Concepts

## The goal

We want ground tiles that, when placed on an isometric grid, form one continuous map
with **no visible seams, no gaps, and consistent color** — the look of Hay Day / mobile
farm games.

![Target seamless map](../assets/01-goal-map.png)
*This is the target: grass, water, road and field tiles that read as one map.*

> ⚠️ **This image is a GOAL reference (a single AI render of a whole map).**
> In a real game you do **not** generate one big picture. You generate **individual
> tiles** and the engine assembles them on a grid. Use this only as "what the final
> result should feel like."

## What "seamless" actually means

Seamless is **not** about painting a perfect repeating texture. For isometric tiles it means:

1. **Identical diamond shape** — every tile is the same 2:1 isometric rhombus.
2. **Identical thickness** — the soil base under each tile is the same height.
3. **Surface fills the whole tile** — no stray rim, no empty corners.
4. **Flat, neutral background** — so it can be cut to a transparent PNG cleanly.

![Single target tile](../assets/02-single-grass-tile.png)
*The unit we actually produce: one clean tile.*

## The golden rule

> **Shape first, texture second.** Lock a **FIXED seed** for the whole set so every tile
> is the same diamond. Only change the short *surface phrase* (grass / dirt / water…)
> between tiles. If you let the seed float, every tile becomes a slightly different
> shape and they will never tile cleanly.

## How a tile set fits together

![Tile set](../assets/03-tile-set.png)
*Five tiles from one family — grass, water, dirt, road, field. Same angle, same thickness.*

When all tiles belong to the same "family" (same shape/lighting/thickness), the engine
can place them next to each other and they read as one surface. The art only has to be
consistent — the engine handles the snapping.

## Hardware context (RTX 3060 12GB / 32GB RAM)

- SDXL @ 1024² with 2 LoRAs fits comfortably in 12GB VRAM.
- Batch 1 is recommended for tiles (you want deterministic, fixed-seed output).
- Typical generation: ~15–30s per tile at 30 steps. Plenty fast for a tile set.

## Pipeline summary

```
ComfyUI (Resep D, fixed seed)  ->  raw 1024² tile on flat background
        ->  rembg / SAM  ->  transparent PNG
        ->  import into engine tilemap  ->  seamless map
```

Next: `02-production-guide.md` for the exact ComfyUI setup.
