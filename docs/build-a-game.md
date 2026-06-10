# 🏗️ Capstone: Build a Playable Isometric Scene (all 20 skills)

This is the **end-to-end proof**. Follow it and an agent goes from an empty folder
to a live, interactive isometric scene — using every skill in the repo, in order.

Each phase lists the skills it uses and an **✅ Acceptance test** you must pass
before moving on. Pass all of them and the [goal](../GOAL.md) is **achieved**.

> New here? Start with the router skill
> [`using-isometric-skills`](../skills/using-isometric-skills/SKILL.md), which points
> any request to the right skill. This capstone is the “run everything” path.

---

## Phase 0 · Setup & art direction

**Skills:** `comfyui-lowvram-setup`, `isometric-art-direction`

1. Configure ComfyUI for a 12GB GPU so SDXL runs without OOM.
2. Lock ONE art style into [`STYLE.md`](../STYLE.md): projection, light, palette, scale.

**✅ Acceptance:** ComfyUI generates a 1024² test image without crashing, and
`STYLE.md` is filled in. Every later prompt references it.

---

## Phase 1 · Generate the art

**Skills:** `seamless-isometric-terrain`, `isometric-object-sprites`,
`isometric-building-sprites`, `isometric-character-sprites`, `animated-sprite-generation`

1. Generate seamless ground tiles (grass, dirt, water, …).
2. Generate props, buildings, and an 8-direction character.
3. Generate at least one looping animated sprite (water/flag/fire).

**✅ Acceptance:** Tiles repeat with **no visible seam**; every sprite matches the
`STYLE.md` look; the animated strip loops cleanly.

---

## Phase 2 · Process the art into engine-ready assets

**Skills:** `transparent-cutout-cleanup`, `spritesheet-atlas-packing`, `autotiling-transitions`

1. Cut backgrounds to clean alpha (no halo/fringe).
2. Pack sprites into one atlas + JSON frame map.
3. Build edge/corner transition tiles so terrains blend.

**✅ Acceptance:** One atlas image + JSON exists; cutouts have clean edges;
grass→sand→water transitions have no hard seams.

---

## Phase 3 · Build the engine

**Skills:** `isometric-grid-math`, `canvas2d-isometric-renderer`,
`depth-sorting-occlusion`, `tilemap-data-format`

1. Implement `gridToScreen` / `screenToGrid` (2:1).
2. Load a tilemap data file and render it back-to-front.
3. Depth-sort sprites by `row + col` so occlusion is correct.

**✅ Acceptance:** A map from a data file renders in correct isometric order;
a character walking behind a tree is drawn behind it.
See the working reference in [`demo/`](../demo/).

---

## Phase 4 · Make it interactive

**Skills:** `tile-picking-interaction`, `camera-pan-zoom-controls`, `isometric-pathfinding`

1. Convert mouse → tile for hover/selection/placement.
2. Add pan + zoom + clamping.
3. Move a unit along an A* path on the walkable layer.

**✅ Acceptance:** Hover highlights the right tile; camera pans/zooms within bounds;
a unit routes around obstacles to a clicked tile.

---

## Phase 5 · Optimize & automate

**Skills:** `canvas-performance-optimization`, `asset-pipeline-automation`

1. Cut draw calls/allocations to hold 60fps.
2. Wire a script: regenerate art → cutout → atlas → map, in one command.

**✅ Acceptance:** Scene holds ~60fps; re-running the pipeline rebuilds the atlas
without manual steps.

---

## 🏁 Goal achieved

You now have a live isometric scene built **entirely** from these skills.
Confirm against the [Definition of Done](../GOAL.md#definition-of-done-the-proof-bar).
When every box is checked, you have **proof, not theory.**

| Phase | Skills used | Proven by |
|---|---|---|
| 0 Setup | 2 | `STYLE.md` filled, ComfyUI runs |
| 1 Art | 5 | seamless tiles + on-style sprites |
| 2 Process | 3 | atlas + JSON, clean alpha |
| 3 Engine | 4 | `demo/` renders correctly |
| 4 Interaction | 3 | picking + camera + pathfinding |
| 5 Ship | 2 | 60fps + one-command pipeline |
| Router | 1 | `using-isometric-skills` |
| **Total** | **20** | **playable scene** |
