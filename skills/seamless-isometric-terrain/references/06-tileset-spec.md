# 06 — Tile Set Spec & Extending

## Core set (ship these first)

![Tile set](../assets/03-tile-set.png)

| # | Tile | Surface phrase | Base color |
|---|---|---|---|
| 1 | Grass (Rumput) | `full grass land` | green |
| 2 | Water (Air) | `full water, calm flat blue water surface on top` | blue |
| 3 | Dirt (Tanah) | `full dirt ground` | brown |
| 4 | Road (Jalan) | `full dirt path, light tan packed dirt path surface on top` | brown |
| 5 | Field (Ladang) | `full plowed farm field, even rows of tilled soil furrows on top` | brown |

All five use the **same fixed seed** and the same base prompt — only the surface
phrase and the per-tile negative change (see `03-prompts.md`).

> **Don't confuse the two brown tiles.** **Dirt (Tanah)** is *solid bare ground* — a
> plain earth surface you tile across a whole area. **Road (Jalan)** is a *path* you
> draw as a line across other terrain. Same brown family, different job.

## Bonus materials (same method)

| Tile | Surface phrase | Base color | Extra negative |
|---|---|---|---|
| Sand (Pasir) | `full sand ground` | tan | `grass, plants, water, mixed colors` |
| Stone (Batu) | `full stone ground, flat rocky surface on top` | gray | `grass, plants, cracks, mixed colors` |
| Snow (Salju) | `full snow ground, smooth white snow surface on top` | white | `grass, plants, dirt, mixed colors` |
| Forest floor (Hutan) | `full mossy forest floor` | dark green | `trees, props, mixed colors` |

> Trees, mountains, rocks and houses are **objects, not tiles.** Generate them as
> separate sprites with transparent backgrounds and let the engine depth-sort them on
> top of the ground tiles. Do not bake them into terrain tiles.

## Naming convention (suggested)

```
tile_grass_01.png
tile_water_01.png
tile_dirt_01.png
tile_road_01.png
tile_field_01.png
tile_grass_spring_01.png   # seasonal variant
```

Keep one folder per material if you have multiple variants.

## QA checklist before shipping a set

- [ ] All tiles generated with the **same fixed seed**.
- [ ] Same diamond angle and base thickness across the set (compare to grass tile).
- [ ] No stray rims, props, or mixed colors.
- [ ] All exported as **transparent PNG** (no white fringe).
- [ ] Placed a quick test grid — no seams, no gaps.
- [ ] Consistent file naming.

Done. Back to `../SKILL.md` for the quick reference card.
