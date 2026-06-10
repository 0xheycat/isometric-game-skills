---
name: using-isometric-skills
description: Use when starting ANY isometric game task to route the request to the correct specialized skill before writing code or generating art.
license: MIT
---

# Using Isometric Skills (Router)

## Overview

This is the meta-skill. Isometric games fail when you jump straight into code or art without picking the right workflow. This skill maps an incoming request to the exact specialized skill that should handle it, in the correct order: art direction -> asset generation -> asset processing -> engine -> gameplay -> polish.

## When to Use

- The user asks for anything isometric and you are not sure which skill applies.
- You are tempted to free-style a renderer, tile, or sprite without a workflow.
- A task spans multiple stages (art + engine) and needs sequencing.

## Process

1. Classify the request into one phase: Art Foundations, Asset Generation, Asset Processing, Engine & Rendering, Gameplay, or Polish.
2. Open the matching skill from the table below and follow it exactly. Do not improvise.
3. If the task spans phases, run skills in pipeline order (art -> assets -> processing -> engine -> gameplay -> polish).
4. Lock art direction FIRST. Every asset skill depends on a single agreed style sheet.
5. Return to this router whenever the user changes scope.

### Routing table

| If the task is about... | Use skill |
|---|---|
| Low-VRAM ComfyUI / model setup | `comfyui-lowvram-setup` |
| Choosing a consistent art style | `isometric-art-direction` |
| Ground tiles that tile seamlessly | `seamless-isometric-terrain` |
| Trees, rocks, props | `isometric-object-sprites` |
| Houses, barns, shops | `isometric-building-sprites` |
| Characters, 8-direction | `isometric-character-sprites` |
| Animated water, fire, windmills | `animated-sprite-generation` |
| Removing backgrounds / edges | `transparent-cutout-cleanup` |
| Packing sprites into an atlas | `spritesheet-atlas-packing` |
| Auto edge transitions | `autotiling-transitions` |
| Grid <-> screen math | `isometric-grid-math` |
| Drawing the world on canvas | `canvas2d-isometric-renderer` |
| Things drawn in wrong order | `depth-sorting-occlusion` |
| Map file format | `tilemap-data-format` |
| Moving units around obstacles | `isometric-pathfinding` |
| Pan / zoom camera | `camera-pan-zoom-controls` |
| Click-to-select a tile | `tile-picking-interaction` |
| Frame drops, lag | `canvas-performance-optimization` |
| Automating the asset pipeline | `asset-pipeline-automation` |

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "This task is simple, I do not need a skill" | Simple tasks are where silent inconsistencies enter. Route it anyway. |
| "I will pick the skill later" | Order matters. Wrong order means re-generating assets twice. |

## Red Flags - STOP if you catch yourself:

- Writing renderer code before art direction is locked.
- Generating assets in 3 different styles because no style sheet exists.
- Skipping straight to gameplay before the world renders correctly.

## Verification

You are NOT done until every box is checked:

- [ ] The request is mapped to exactly one starting skill.
- [ ] Multi-phase tasks have an explicit skill order written down.
- [ ] Art direction is locked before any asset is generated.
