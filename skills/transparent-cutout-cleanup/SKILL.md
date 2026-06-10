---
name: transparent-cutout-cleanup
description: Use when removing backgrounds from generated sprites to get clean alpha edges with no halo, fringe, or leftover background pixels.
license: MIT
---

# Transparent Cutout Cleanup

## Overview

AI-generated sprites come on a background. Naive removal leaves a colored halo or jagged edge that screams amateur when tiles are placed together. This skill produces clean, premultiplied-safe alpha cutouts.

## When to Use

- Any generated sprite needs a transparent background.
- Placed sprites show a white/gray halo or fringe.
- Edges look jagged or have leftover background color.

## Process

1. Generate on a PLAIN flat background (easier to key out than a busy one).
2. Use a background-removal model (e.g. InSPyReNet / rembg) rather than a hard color key.
3. Inspect edges at 400% zoom for halo or fringe pixels.
4. Defringe / decontaminate edge color so no background tint remains.
5. Erode the alpha by 1px if a faint halo persists.
6. Save as PNG with straight alpha; verify on both light and dark backgrounds.
7. Batch the cleaned sprites for the atlas packer.

Pair this with the ComfyUI rembg node in `seamless-isometric-terrain/scripts`.

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "A white halo is barely visible" | On a dark tile it is glaring. Defringe every sprite. |
| "Hard color-key is faster" | It eats anti-aliased edges and looks jagged. Use a proper matting model. |

## Red Flags - STOP if you catch yourself:

- Visible halo/fringe when placed on a contrasting background.
- Jagged, aliased cutout edges.
- Background color contaminating semi-transparent pixels.

## Verification

You are NOT done until every box is checked:

- [ ] Edges are clean at 400% zoom on light AND dark backgrounds.
- [ ] No background-color contamination on semi-transparent pixels.
- [ ] All sprites exported as straight-alpha PNG.
