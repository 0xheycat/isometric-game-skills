---
name: canvas2d-isometric-renderer
description: Use when building a Canvas 2D renderer that draws an isometric tilemap and sprites efficiently with correct ordering.
license: MIT
---

# Canvas2D Isometric Renderer

## Overview

This skill builds the core render loop: draw ground tiles back-to-front, then depth-sorted objects, using the grid math transform and the atlas. It is the backbone every gameplay skill plugs into.

## When to Use

- You need to actually draw the isometric world.
- Tiles or sprites render in the wrong order.
- You are wiring grid math + atlas into a render loop.

## Process

1. Use `isometric-grid-math` for all coordinate conversions.
2. Draw ground tiles in back-to-front order (by row+col).
3. Draw objects/characters AFTER tiles, sorted by depth (see `depth-sorting-occlusion`).
4. Source every image from the atlas (see `spritesheet-atlas-packing`).
5. Apply the camera transform once per frame (see `camera-pan-zoom-controls`).
6. Only draw tiles within the visible viewport (culling).
7. Keep the draw loop pure - no allocations per frame.

```js
for (const tile of tilesInView) drawTile(tile);
for (const obj of sortByDepth(objectsInView)) drawSprite(obj);
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will draw everything every frame" | Drawing off-screen tiles wastes the frame budget. Cull. |
| "Order does not matter much" | Wrong order = objects behind walls. Sort every frame. |

## Red Flags - STOP if you catch yourself:

- Drawing the entire map instead of the viewport.
- Allocating arrays/objects inside the draw loop.
- No separation between tile pass and object pass.

## Verification

You are NOT done until every box is checked:

- [ ] Ground tiles draw back-to-front correctly.
- [ ] Objects draw after tiles in depth order.
- [ ] Only visible tiles are drawn (culling works).
