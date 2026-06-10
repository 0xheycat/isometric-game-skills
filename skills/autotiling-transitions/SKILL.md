---
name: autotiling-transitions
description: Use when making different terrain types (grass, water, sand) blend with automatic edge and corner transition tiles instead of hard seams.
license: MIT
---

# Autotiling & Edge Transitions

![Autotiling & Edge Transitions demo](assets/demo.png)

## Overview

Hard edges between grass and water look like a checkerboard. Autotiling picks the correct edge/corner transition tile based on a bitmask of neighbors. This skill defines the transition set and the bitmask rule.

## When to Use

- Two terrain types meet and the seam looks harsh.
- You want maps to look hand-blended without hand-placing every edge.
- You need a repeatable rule for which transition tile to use.

## Process

1. Define the base terrains and their priority order (e.g. water < sand < grass).
2. Author the 16-tile (or 47-tile) transition set for each terrain pair.
3. For each cell, compute a neighbor bitmask (N, E, S, W and corners).
4. Map the bitmask to the correct transition tile index.
5. Render the transition tile on top of the lower-priority base.
6. Verify all 16 bitmask cases visually with a test map.
7. Cache the bitmask->tile lookup for performance.

```text
bitmask = N*1 + E*2 + S*4 + W*8  ->  transitionTile[bitmask]
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I will hand-place edge tiles" | Hundreds of edges by hand is unmaintainable. Use a bitmask rule. |
| "One generic edge tile is enough" | Corners need their own tiles or you get gaps. Author the full set. |

## Red Flags - STOP if you catch yourself:

- Hard checkerboard seams between terrains.
- Missing corner transition tiles.
- Bitmask computed but never cached (slow).

## Verification

You are NOT done until every box is checked:

- [ ] A complete transition set exists per terrain pair.
- [ ] All bitmask cases render correctly on a test map.
- [ ] The bitmask->tile lookup is cached.
