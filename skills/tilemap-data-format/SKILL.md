---
name: tilemap-data-format
description: Use when designing the map data format (layers, tiles, objects, metadata) so maps are editable, versionable, and engine-agnostic.
license: MIT
---

# Tilemap Data Format

## Overview

A good map format separates data from rendering. This skill defines a JSON tilemap with layers (ground, transitions, objects) and per-tile metadata (walkable, type) so designers and the engine share one source of truth.

## When to Use

- You are deciding how maps are stored.
- Maps are hard-coded in source instead of data files.
- You need walkability/metadata alongside visuals.

## Process

1. Separate layers: ground, transitions, objects, and a collision/walkable layer.
2. Store the grid as width/height + arrays of tile indices per layer.
3. Reference tiles by atlas name or index, never by raw pixel coords.
4. Attach per-tile metadata (type, walkable, cost) for gameplay systems.
5. Keep it pure JSON so it diffs cleanly in git and loads anywhere.
6. Version the format with a `version` field for migrations.
7. Validate maps on load (dimensions, indices in range).

```json
{ "version": 1, "w": 32, "h": 32,
  "layers": { "ground": [/*...*/], "objects": [/*...*/] },
  "meta": { "walkable": [/*...*/] } }
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will hard-code the map in code" | Then designers cannot touch it and diffs are unreadable. Use data files. |
| "One flat array is enough" | Gameplay needs a separate walkable layer. Separate concerns. |

## Red Flags - STOP if you catch yourself:

- Maps embedded in source instead of data files.
- No walkable/collision layer.
- Tiles referenced by pixel coordinates.

## Verification

You are NOT done until every box is checked:

- [ ] Map is pure JSON with separated layers.
- [ ] Per-tile gameplay metadata exists (walkable, type).
- [ ] Loader validates dimensions and tile indices.
