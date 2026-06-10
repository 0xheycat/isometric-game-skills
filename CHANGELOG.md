# Changelog

All notable changes to this project are documented here. This project adheres to
[Semantic Versioning](https://semver.org/) and the
[Keep a Changelog](https://keepachangelog.com/) format.

## [1.0.0] — 2026-06-11

First public release. 🎉 A complete, agent-ready toolkit for building isometric games.

### Added
- **20 SKILL.md skills** across the full pipeline: low-VRAM ComfyUI setup, art
  direction, seamless terrain, object/building/character/animated sprite
  generation, cutout cleanup, atlas packing, autotiling, grid math, Canvas2D
  renderer, depth sorting, tilemap format, pathfinding, camera controls, tile
  picking, performance optimization, and asset-pipeline automation — plus the
  `using-isometric-skills` router meta-skill.
- **Live demo** (`demo/`) — a single-file, dependency-free Canvas2D isometric
  renderer with procedural terrain, depth-sorted objects, tile picking, pan/zoom
  camera, and a toggleable **sprite mode** with embedded painterly sprites.
- **Tested engine** (`engine/`) — `iso.js` grid math (`gridToScreen`,
  `screenToGrid`, `tileAt`, `depth`, `depthSort`) with a passing Node test suite.
- **Headless example** (`examples/`) — `sample-map.json` + `render-map.mjs` that
  renders the map to SVG/PNG using the tested engine.
- **Terrain tile set** — water, sand, grass, road (path), field, and **bare
  ground (Dirt / Tanah)**, with the brown path vs. bare-ground distinction made
  explicit in the docs and palette.
- **Style guide** (`STYLE.md`) — locked painterly palette + the "Obsidian & Gold"
  product-UI brand layer.
- **Proof layer** — `GOAL.md`, `docs/build-a-game.md`, `skills.json` catalog, a
  `validate_skills.py` validator, and CI (`.github/workflows/validate.yml`) that
  validates every skill and runs the engine tests on each push.
- **Repo polish** — README with badges, gallery, hero banner, animated demo,
  social preview, FUNDING config, issue/PR templates, code of conduct,
  contributing guide, and MIT license.

[1.0.0]: https://github.com/0xheycat/isometric-game-skills/releases/tag/v1.0.0
