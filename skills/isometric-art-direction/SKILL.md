---
name: isometric-art-direction
description: Use when starting an isometric project to lock ONE consistent art style (angle, light, palette, scale) before generating any asset.
license: MIT
---

# Isometric Art Direction

## Overview

The difference between a hobby project and a polished game is consistency. This skill produces a one-page style sheet that every other asset skill must obey, so 200 generated assets look like one game instead of a random asset dump.

## When to Use

- Before generating the first tile, sprite, or building.
- Assets already look mismatched and need a unifying standard.
- Multiple people or sessions will generate art.

## Process

1. Fix the projection: true 2:1 isometric (dimetric). Write it down.
2. Fix the light direction (e.g. top-left) and keep it identical on every asset.
3. Define a tight color palette (8-12 swatches) and forbid off-palette colors.
4. Define the tile base size in pixels (e.g. 128x64) and the anchor point.
5. Pick ONE shading style (soft painterly / cel / pixel) and one reference image.
6. Write all of this into a single STYLE.md and link it from every asset prompt.
7. Generate 3 test assets and confirm they look like the same game before scaling up.

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will keep the style consistent in my head" | Your head is not version-controlled. Write the style sheet. |
| "I can fix the style later" | Restyling 150 assets later costs 10x more than agreeing now. |

## Red Flags - STOP if you catch yourself:

- No written style sheet exists.
- Light direction changes between assets.
- Color palette grows uncontrolled with every generation.

## Verification

You are NOT done until every box is checked:

- [ ] A STYLE.md exists with projection, light, palette, scale, anchor, shading.
- [ ] 3 test assets visibly belong to the same game.
- [ ] Every asset prompt references the style sheet.
