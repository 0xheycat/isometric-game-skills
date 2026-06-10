---
name: spritesheet-atlas-packing
description: Use when packing many isometric sprites into a texture atlas with a JSON map so the engine draws from one image with correct frame coordinates.
license: MIT
---

# Spritesheet & Atlas Packing

## Overview

Drawing 200 separate images means 200 texture binds and slow load. An atlas packs sprites into one image plus a JSON of frame rects. This skill produces an atlas the renderer can index by name.

## When to Use

- You have many individual sprite PNGs to ship.
- Load times or draw calls are high because of separate images.
- The renderer needs named frame lookups.

## Process

1. Collect all cleaned, transparent sprites into one folder.
2. Pad each frame by 1-2px to prevent texture bleeding between neighbors.
3. Pack into a power-of-two atlas (e.g. 2048x2048) using a bin-packer.
4. Emit a JSON map: name -> {x, y, w, h, anchorX, anchorY}.
5. Keep anchors from the source sprites so placement stays correct.
6. Verify every sprite is found by name and renders at the right anchor.
7. Regenerate the atlas automatically in the build (see `asset-pipeline-automation`).

```json
{ "tree_oak": { "x": 0, "y": 0, "w": 128, "h": 160, "anchorX": 64, "anchorY": 150 } }
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will just load images individually" | Hundreds of texture binds kill performance. Pack an atlas. |
| "Padding is unnecessary" | Without padding, neighbors bleed at non-integer zoom. Always pad. |

## Red Flags - STOP if you catch yourself:

- No padding between packed frames (texture bleeding).
- Atlas not power-of-two.
- Anchors lost during packing so placement breaks.

## Verification

You are NOT done until every box is checked:

- [ ] All sprites packed into a power-of-two atlas with padding.
- [ ] JSON map resolves every sprite by name with correct anchor.
- [ ] No texture bleeding at fractional zoom.
