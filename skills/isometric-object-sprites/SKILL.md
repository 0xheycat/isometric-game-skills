---
name: isometric-object-sprites
description: Use when generating isolated isometric props (trees, rocks, bushes, stumps) that drop cleanly onto tiles with correct scale and a transparent background.
license: MIT
---

# Isometric Object Sprites

![Isometric Object Sprites demo](assets/demo.png)

## Overview

Objects are sprites that sit ON tiles, not tiles themselves. They must be isolated on a plain background, share one scale, and have a defined ground-anchor so depth sorting works later. This skill produces clean, consistent props.

## When to Use

- You need trees, rocks, bushes, fences, or other decorative props.
- Props look different sizes or styles when placed together.
- You need transparent, drop-in-ready object sprites.

## Process

1. Confirm art direction is locked (see `isometric-art-direction`).
2. Prompt ONE object per image, isolated on a plain flat background, with a soft contact shadow.
3. Keep the surface/style phrase SHORT - long prompts add unwanted props and edges.
4. Use a FIXED seed and identical settings across the whole object set for scale consistency.
5. Generate, then send to `transparent-cutout-cleanup` for clean alpha edges.
6. Define the ground-anchor (bottom-center of the footprint) for each sprite.
7. Place 3 objects on a test tile to confirm scale and anchor before scaling up.

Prompt template:

```text
single isometric [object], 2:1 isometric view, soft painterly shading,
simple clean composition, isolated on plain flat background, soft contact shadow,
game asset, high quality
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I can generate several objects in one image to save time" | Then you cannot place them individually and scales drift. One object per image. |
| "Scale looks close enough" | Close enough reads as broken in-game. Fix the seed and settings. |

## Red Flags - STOP if you catch yourself:

- Multiple objects crammed into one generation.
- Inconsistent scale across the prop set.
- Leftover background fringe because cleanup was skipped.

## Verification

You are NOT done until every box is checked:

- [ ] Each prop is a single isolated sprite with transparent background.
- [ ] All props share one scale and style.
- [ ] Each sprite has a defined ground-anchor and passes a placement test.
