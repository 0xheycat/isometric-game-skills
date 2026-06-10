---
name: isometric-character-sprites
description: Use when generating isometric characters in consistent 8 directions with a fixed feet-anchor for movement and depth sorting.
license: MIT
---

# Isometric Character Sprites

![Isometric Character Sprites demo](assets/demo.png)

## Overview

Characters move, so they need consistent proportions across 8 facing directions and a fixed feet-anchor (where the character touches the ground). Without this, characters appear to slide, jitter, or sort incorrectly when walking.

## When to Use

- You need a player or NPC that faces multiple directions.
- Characters change size or proportion between directions.
- Movement looks like the sprite is sliding or floating.

## Process

1. Lock art direction and character height in pixels.
2. Generate the same character in 8 directions (S, SW, W, NW, N, NE, E, SE) on a plain background.
3. Keep proportions identical - same height line and feet baseline across all 8.
4. Fix seed/settings; regenerate any direction that drifts in size or style.
5. Clean alpha with `transparent-cutout-cleanup`.
6. Define the feet-anchor (bottom-center) identically for every direction.
7. Test by cycling directions in place - the feet must not jump between frames.

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "4 directions is enough" | Diagonal movement looks broken with 4 directions in iso. Do 8. |
| "Slight height differences are fine" | A 3px height drift reads as bobbing. Align the baseline. |

## Red Flags - STOP if you catch yourself:

- Inconsistent character height across directions.
- Feet-anchor differs per direction so the sprite slides.
- Only front-facing direction exists.

## Verification

You are NOT done until every box is checked:

- [ ] 8 consistent directions exist for the character.
- [ ] Feet-anchor is identical across all directions.
- [ ] Cycling directions in place shows no jump or slide.
