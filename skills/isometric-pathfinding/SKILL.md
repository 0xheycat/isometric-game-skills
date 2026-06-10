---
name: isometric-pathfinding
description: Use when units must navigate an isometric grid around obstacles using A* on the walkable layer with correct iso neighbor rules.
license: MIT
---

# Isometric Pathfinding

## Overview

Pathfinding runs on grid coordinates, not screen pixels. This skill implements A* over the walkable layer with proper diagonal handling so units take natural paths and never cut through blocked corners.

## When to Use

- Units or NPCs need to move to a target around obstacles.
- Characters walk through walls or take ugly paths.
- You have a walkable layer and need movement on it.

## Process

1. Run A* on grid coords using the tilemap walkable layer.
2. Define neighbors: 4-way or 8-way; for 8-way, forbid cutting blocked corners.
3. Use an admissible heuristic (octile distance for 8-way).
4. Return a path of grid tiles, then convert to screen with `isometric-grid-math`.
5. Smooth the path (string-pulling) to avoid zig-zag.
6. Recompute or repath when the map or target changes.
7. Cap search cost (node budget) for large maps.

```text
heuristic (octile): dx=|x1-x2|, dy=|y1-y2|; h = (dx+dy) + (1.414-2)*min(dx,dy)
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "Straight-line movement is fine" | Units will walk into walls. Use A* on the walkable layer. |
| "Corner cutting looks fine" | Units clip through diagonal walls. Forbid blocked-corner cuts. |

## Red Flags - STOP if you catch yourself:

- Pathfinding on screen coords instead of grid coords.
- Allowing diagonal moves through blocked corners.
- No node budget so large maps freeze.

## Verification

You are NOT done until every box is checked:

- [ ] A* finds paths around obstacles on the walkable layer.
- [ ] Diagonal moves never cut blocked corners.
- [ ] Path converts correctly back to screen positions.
