# Getting Started

## 1. Clone the repo

```bash
git clone https://github.com/0xheycat/isometric-game-skills.git
cd isometric-game-skills
```

## 2. Start with the router

Open [`skills/using-isometric-skills/SKILL.md`](../skills/using-isometric-skills/SKILL.md). It maps any task to the right skill in the right order.

## 3. Follow the pipeline order

For a new game, run skills in this order:

1. `isometric-art-direction` — lock the style.
2. `comfyui-lowvram-setup` — set up reproducible generation.
3. `seamless-isometric-terrain` -> object/building/character sprites — make assets.
4. `transparent-cutout-cleanup` -> `spritesheet-atlas-packing` — process them.
5. `isometric-grid-math` -> `canvas2d-isometric-renderer` -> `depth-sorting-occlusion` — render.
6. `tilemap-data-format` -> pathfinding / camera / picking — gameplay.
7. `canvas-performance-optimization` + `asset-pipeline-automation` — ship.

## 4. Install into your agent

See the table in the [README](../README.md#-quick-start) and [`cursor-setup.md`](cursor-setup.md).

## 5. Verify as you go

Every skill ends with a Verification checklist. Do not move to the next skill until the current one's boxes are checked.
