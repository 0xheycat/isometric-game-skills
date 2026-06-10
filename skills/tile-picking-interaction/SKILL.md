---
name: tile-picking-interaction
description: Use when converting a mouse/touch position into the correct isometric tile for selection, highlighting, and placement.
license: MIT
---

# Tile Picking & Interaction

## Overview

Picking is screen->grid with the camera inverse applied first. This skill turns a pointer position into the exact tile under it, with a highlight and hit-test that respects camera pan/zoom.

## When to Use

- Clicking selects the wrong tile.
- You need hover highlight or click-to-place.
- Picking ignores camera pan/zoom.

## Process

1. Take the pointer position in screen space.
2. Apply the inverse camera transform (see `camera-pan-zoom-controls`).
3. Apply screen->grid from `isometric-grid-math` and round to a tile.
4. Clamp the result to map bounds and check walkable if needed.
5. Draw a highlight on the picked tile for feedback.
6. On click, dispatch the tile coord to the gameplay handler.
7. Test picking at multiple zoom levels and pan offsets.

```js
const world = screenToWorld(pointer, cam);
const tile = worldToGrid(world, W, H); // then round
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will skip the camera inverse" | Then picking breaks the moment you pan/zoom. Always invert. |
| "No need to highlight" | Players need feedback on what they will click. Highlight. |

## Red Flags - STOP if you catch yourself:

- Picking that ignores camera pan/zoom.
- No rounding so edge tiles mis-select.
- No visual highlight feedback.

## Verification

You are NOT done until every box is checked:

- [ ] Picked tile is correct at any pan and zoom.
- [ ] Hover highlight matches the actual selected tile.
- [ ] Clicks dispatch the right grid coordinate.
