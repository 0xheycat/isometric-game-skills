---
name: godot4-isometric-tilemap
description: Use when setting up correct 2:1 isometric rendering in Godot 4 with TileMapLayer + Y-sort, mapping this repo's engine-agnostic grid math and depth rules onto Godot's native APIs.
license: MIT
---

# Godot 4 Isometric TileMap

## Overview

Godot 4 supports isometric natively, but the defaults fight you: wrong tile shape, broken draw order, and magic pixel offsets that look fine until something moves. This skill maps the repo's tested concepts (grid math, depth sorting) onto Godot's `TileMapLayer` + Y-sort so it is correct the first time.

## When to Use

- Starting an isometric scene in Godot 4 (4.3+, `TileMapLayer`).
- Characters draw in front of / behind tiles they should not.
- Tiles overlap, or mouse picking selects the wrong cell.

## Process

1. TileSet: set Tile Shape = **Isometric**, Tile Layout = **Diamond Down**, and Tile Size to your 2:1 footprint (e.g. 64x32).
2. Put ground on a `TileMapLayer`. For anything that must sort against characters, enable **Y Sort Enabled** on the layer and its parent node.
3. Set each movable sprite's `y_sort_origin` to the tile's feet/anchor (not its top). This is Godot's version of the `depth = col + row` rule (see depth-sorting-occlusion).
4. Convert coordinates with the built-ins `local_to_map()` / `map_to_local()` instead of hand-rolled offsets (mirrors isometric-grid-math).
5. Mouse picking: `local_to_map(get_local_mouse_position())` to get the cell, then `map_to_local()` to snap a highlight (see tile-picking-interaction).
6. Keep ONE tile size and anchor convention across every layer and scene.

```gdscript
# grid <-> world: let Godot do the iso math
var cell: Vector2i = ground.local_to_map(ground.get_local_mouse_position())
var world: Vector2 = ground.map_to_local(cell)  # center of that tile
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I'll nudge sprite offsets until it lines up" | Manual offsets break under Y-sort and zoom. Set `y_sort_origin` to the anchor. |
| "I'll write the iso math myself" | `local_to_map` / `map_to_local` are exact and tested. Use them. |

## Red Flags - STOP if you catch yourself:

- Y Sort disabled, or `y_sort_origin` left at the default (0,0).
- Hand-written screen<->grid math instead of the `TileMapLayer` API.
- Mixed tile sizes or anchors across layers.

## Verification

You are NOT done until every box is checked:

- [ ] TileSet shape = Isometric, layout = Diamond Down, 2:1 tile size.
- [ ] Y Sort on; a character sorts correctly walking around a tall object.
- [ ] Picking via `local_to_map` selects the cell under the cursor.
- [ ] Round-trip `local_to_map(map_to_local(cell))` returns the same cell.
