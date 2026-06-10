---
name: depth-sorting-occlusion
description: Use when sprites draw in the wrong order so characters appear in front of objects they should be behind in an isometric scene.
license: MIT
---

# Depth Sorting & Occlusion

## Overview

In isometric, draw order IS depth. A character is behind a tree if its anchor tile sorts earlier. This skill gives the correct sort key and handles tall/multi-tile objects that break naive sorting.

## When to Use

- Characters render in front of trees/walls they should be behind.
- Tall or multi-tile objects sort incorrectly.
- You added objects and the layering looks wrong.

## Process

1. Give every drawable a depth key based on its anchor tile: depth = row + col.
2. Sort all objects by depth ascending before drawing.
3. For ties, break by a secondary key (e.g. y, then creation order).
4. For multi-tile objects, sort by the FRONT-most occupied tile.
5. For very tall objects, consider splitting into stackable slices.
6. Re-sort only when objects move, not every frame if static.
7. Test the classic case: walk a character around all four sides of a tree.

```js
objects.sort((a, b) => (a.row + a.col) - (b.row + b.col));
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "Painter order by y is good enough" | Pure y fails for multi-tile and tall sprites. Use anchor row+col. |
| "I will sort once at load" | Moving objects must re-sort. Sort on movement. |

## Red Flags - STOP if you catch yourself:

- Sorting by raw y instead of anchor tile.
- Multi-tile objects using their center instead of front tile.
- Characters clipping through tall buildings.

## Verification

You are NOT done until every box is checked:

- [ ] Walking around all sides of an object always sorts correctly.
- [ ] Multi-tile and tall objects occlude properly.
- [ ] Sorting updates when objects move.
