---
name: isometric-building-sprites
description: Use when generating isometric buildings (houses, barns, shops) that sit on a defined tile footprint and depth-sort correctly with characters.
license: MIT
---

# Isometric Building Sprites

![Isometric Building Sprites demo](assets/demo.png)

## Overview

Buildings are large multi-tile sprites. They need a clear footprint (how many tiles they occupy), a consistent height-to-base ratio, and a known anchor so characters can walk in front of and behind them.

## When to Use

- You need houses, barns, shops, towers, or other structures.
- Buildings overlap tiles incorrectly or float.
- Characters draw in front of buildings they should be behind.

## Process

1. Lock art direction and the tile base size first.
2. Decide each building footprint in tiles (e.g. 2x2) BEFORE generating.
3. Prompt one building, isolated on a plain background, sitting on a visible diamond footprint with a soft contact shadow.
4. Keep settings + seed fixed so all buildings share one style and light.
5. Clean alpha with `transparent-cutout-cleanup`.
6. Set the anchor at the front-bottom tile of the footprint for depth sorting.
7. Place a character next to and behind the building to verify occlusion (see `depth-sorting-occlusion`).

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "Footprint does not matter, I will eyeball placement" | Eyeballed footprints break collision and sorting. Decide tiles first. |
| "Buildings can be a slightly different style" | The biggest objects on screen must match hardest. Fix style + seed. |

## Red Flags - STOP if you catch yourself:

- No defined tile footprint per building.
- Building height/scale varies wildly across the set.
- Characters render in front of tall buildings.

## Verification

You are NOT done until every box is checked:

- [ ] Each building has a documented tile footprint and anchor.
- [ ] All buildings share one style, light, and scale.
- [ ] Character occlusion in front of and behind each building is correct.
