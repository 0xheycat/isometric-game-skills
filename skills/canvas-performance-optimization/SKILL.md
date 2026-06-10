---
name: canvas-performance-optimization
description: Use when an isometric Canvas game drops frames, to cut draw calls and allocations and hold a steady 60fps.
license: MIT
---

# Canvas Performance Optimization

## Overview

Isometric games die by a thousand draw calls. This skill profiles the frame, culls off-screen tiles, batches from the atlas, and removes per-frame allocations to hit a stable 60fps.

## When to Use

- Frame rate drops or stutters.
- Large maps lag when panning.
- You suspect GC pauses or overdraw.

## Process

1. Profile first - measure where the frame time actually goes.
2. Cull: only draw tiles/objects inside the viewport.
3. Batch draws from one atlas to minimize texture binds.
4. Cache static layers (ground) to an offscreen canvas; redraw only when it changes.
5. Eliminate per-frame allocations (reuse arrays/objects).
6. Avoid sub-pixel blits; snap to integer pixels.
7. Re-profile to confirm the fix, do not assume.

```text
Profile -> Cull -> Batch -> Cache static layer -> Kill allocations -> Re-profile
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "I know what is slow without profiling" | Guessing wastes hours on the wrong thing. Profile first. |
| "Redrawing the ground every frame is fine" | Static ground should be cached. Redraw only on change. |

## Red Flags - STOP if you catch yourself:

- Optimizing before profiling.
- Redrawing static layers every frame.
- Allocating inside the render loop.

## Verification

You are NOT done until every box is checked:

- [ ] Frame time was profiled before and after.
- [ ] Off-screen content is culled and static layers cached.
- [ ] No allocations occur inside the render loop; 60fps holds.
