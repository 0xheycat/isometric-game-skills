# 🎯 Goal & Success Criteria

This repo is **not a pile of tips**. It is a complete skill set with one provable goal:

> **When an AI agent loads these skills and runs them end-to-end, it produces a
> real, playable isometric game scene — art + engine — not a description of one.**

If the criteria below are met, the goal is **achieved**. That is the proof.

---

## Definition of Done (the proof bar)

A run is successful when **all** of these are true:

### Art (generation pipeline)
- [ ] **Seamless ground tiles** for at least 3 terrain types (e.g. grass, dirt, water) that tile in a grid with **no visible seams, edges, or color mismatch**.
- [ ] At least **4 object/building sprites** with **clean transparent alpha** (no halo/fringe).
- [ ] All assets share **one locked art style** (angle, light, palette, scale) — they look like one game, not a random dump.
- [ ] Sprites packed into **one atlas + JSON map**.

### Engine (runtime)
- [ ] A tilemap renders in correct **2:1 isometric** projection from a data file.
- [ ] Sprites and tiles are **depth-sorted** — nothing draws in the wrong order.
- [ ] **Mouse picking** returns the correct tile under the cursor.
- [ ] Camera **pans and zooms** and stays within bounds.
- [ ] The scene holds **~60 fps** on a normal laptop.

### Proof artifacts (must exist, must run)
- [ ] `demo/index.html` opens and draws a live, interactive isometric map. ✅ *(shipped)*
- [ ] `python3 scripts/validate_skills.py` exits **0** (all skills well-formed). ✅ *(shipped)*
- [ ] `docs/build-a-game.md` walkthrough can be followed start-to-finish with no missing step.

---

## How each phase is verified

Every skill ends with its own **Verification** checklist. The capstone
[`docs/build-a-game.md`](docs/build-a-game.md) chains those checks into one
acceptance test, phase by phase. Green at every phase → **goal achieved**.

| Layer | Proof you can run today |
|---|---|
| Skills are valid | `scripts/validate_skills.py` (CI-enforced, green badge) |
| Engine works | `demo/index.html` (live renderer, 6 skills in action) |
| Whole pipeline | `docs/build-a-game.md` (end-to-end recipe + acceptance test) |
| Art consistency | `STYLE.md` (locked style sheet, referenced by every asset) |
