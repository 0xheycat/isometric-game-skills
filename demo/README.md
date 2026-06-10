# 🎮 Live Demo — Isometric Renderer

A single-file, dependency-free Canvas2D isometric renderer. It is **proof the skills are real**, not theory — every technique in this demo maps to a skill in this repo.

## Run it

No build step. Either:

```bash
# option 1: just open the file
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows

# option 2: serve it (recommended)
python3 -m http.server 8080
# then visit http://localhost:8080/demo/
```

## Controls

| Action | Input |
|---|---|
| Pan | drag with mouse |
| Zoom | mouse wheel |
| Pick a tile | hover — the tile highlights and its `(col, row)` shows in the HUD |
| 🔄 Regenerate | new procedural map (re-seeds the noise) |
| ▦ Grid / # Coords | toggle tile outlines and `(col,row)` labels |
| 🖼️ Sprites | swap the vector blocks for **real embedded PNG sprites** (tiles + tree/rock/house) |
| ⌖ Reset view | recenter the camera |

## What it demonstrates

| In the demo | Skill |
|---|---|
| `gridToScreen()` / `screenToGrid()` | [isometric-grid-math](../skills/isometric-grid-math/SKILL.md) |
| Back-to-front diagonal draw of tiles + objects | [canvas2d-isometric-renderer](../skills/canvas2d-isometric-renderer/SKILL.md) |
| Objects drawn after their tile, by `row+col` | [depth-sorting-occlusion](../skills/depth-sorting-occlusion/SKILL.md) |
| Procedural terrain (water / sand / grass / road / field / bare ground) | [tilemap-data-format](../skills/tilemap-data-format/SKILL.md) |
| Hover highlight via inverse transform | [tile-picking-interaction](../skills/tile-picking-interaction/SKILL.md) |
| Drag-pan + wheel-zoom camera | [camera-pan-zoom-controls](../skills/camera-pan-zoom-controls/SKILL.md) |

## Sprite mode

Hit **🖼️ Sprites** to switch from the vector blocks to **real PNG sprites** (base64-embedded so it works offline). This is the bridge to the asset-generation skills: replace the embedded sprites with your own output from
[seamless-isometric-terrain](../skills/seamless-isometric-terrain/SKILL.md) and
[isometric-object-sprites](../skills/isometric-object-sprites/SKILL.md), packed with
[spritesheet-atlas-packing](../skills/spritesheet-atlas-packing/SKILL.md), and you have the start of a real game.
