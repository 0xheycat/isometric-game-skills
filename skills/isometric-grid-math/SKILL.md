---
name: isometric-grid-math
description: Use when converting between grid coordinates and screen pixels in a 2:1 isometric projection, including screen-to-grid for mouse picking.
license: MIT
---

# Isometric Grid Math

## Overview

Every isometric bug eventually traces back to the coordinate transform. This skill gives the exact, tested grid<->screen formulas for a 2:1 projection so placement and picking are pixel-correct.

## When to Use

- Tiles render in the wrong place or overlap.
- Mouse clicks select the wrong tile.
- You are starting a renderer and need the core transform.

## Process

1. Fix tile width W and height H (2:1 means W = 2*H).
2. grid->screen: screenX = (col - row) * (W/2); screenY = (col + row) * (H/2).
3. Add the world origin offset so (0,0) is where you want it on screen.
4. screen->grid (for picking): invert the transform using W and H.
5. Round screen->grid results to integer tile coords.
6. Validate round-trip: grid -> screen -> grid returns the original tile.
7. Document the anchor (tile top vs tile center) and stay consistent.

```js
const screenX = (col - row) * (W / 2);
const screenY = (col + row) * (H / 2);
// inverse
const col = ((screenX / (W/2)) + (screenY / (H/2))) / 2;
const row = ((screenY / (H/2)) - (screenX / (W/2))) / 2;
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will tweak offsets until it looks right" | Magic offsets break on resize/zoom. Derive the transform. |
| "Rounding does not matter" | Unrounded screen->grid selects the wrong tile near edges. Round it. |

## Red Flags - STOP if you catch yourself:

- Hard-coded pixel offsets instead of a derived transform.
- No screen->grid inverse for picking.
- Round-trip grid->screen->grid does not return the same tile.

## Verification

You are NOT done until every box is checked:

- [ ] grid->screen and screen->grid are both implemented.
- [ ] Round-trip conversion is exact for integer tiles.
- [ ] Anchor convention is documented and consistent.
