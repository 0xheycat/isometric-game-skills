---
name: camera-pan-zoom-controls
description: Use when adding pan, zoom, and clamping to an isometric camera so the world stays crisp and within bounds across screen sizes.
license: MIT
---

# Camera Pan & Zoom Controls

## Overview

A camera is a single transform applied before drawing. This skill implements pan (drag), zoom (toward cursor), and clamping to map bounds, keeping tiles pixel-aligned to avoid shimmer.

## When to Use

- The world is bigger than the screen.
- You need drag-to-pan and scroll-to-zoom.
- Tiles shimmer or the camera leaves the map.

## Process

1. Represent the camera as offset (x, y) and scale (zoom).
2. Apply it once per frame before drawing (translate then scale).
3. Pan by adding drag delta to the offset.
4. Zoom toward the cursor: adjust offset so the point under the cursor stays put.
5. Clamp offset and zoom so the view never leaves the map bounds.
6. Snap the final transform to whole pixels to avoid tile shimmer.
7. Feed the inverse transform into `tile-picking-interaction`.

```js
ctx.setTransform(zoom,0,0,zoom, -cam.x*zoom, -cam.y*zoom);
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "Zoom toward center is fine" | Users expect zoom toward the cursor. Anchor the zoom point. |
| "Clamping is optional" | Without clamps the player pans into the void. Clamp to bounds. |

## Red Flags - STOP if you catch yourself:

- Zoom anchored to screen center, not cursor.
- No bounds clamping.
- Sub-pixel camera offsets causing shimmer.

## Verification

You are NOT done until every box is checked:

- [ ] Drag pans and scroll zooms toward the cursor.
- [ ] Camera is clamped within map bounds at all zooms.
- [ ] Transform snaps to whole pixels (no shimmer).
