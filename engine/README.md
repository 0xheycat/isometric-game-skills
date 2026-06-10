# 🧮 Reference engine — `iso.js`

The **canonical 2:1 isometric math** used across the skills and the [live demo](../demo/). Pure functions, zero dependencies, and **unit-tested in CI** — so the core math is proven, not asserted.

```js
import { gridToScreen, screenToGrid, tileAt, depthSort } from "./iso.js";

gridToScreen(3, 2);        // -> { x, y } pixel anchor for a tile
tileAt(mouseX, mouseY);    // -> { col, row } under the cursor (picking)
depthSort(sprites);        // -> back-to-front draw order (occlusion)
```

## Run the tests

```bash
node --test engine/
```

Backed by the [`isometric-grid-math`](../skills/isometric-grid-math/SKILL.md) and [`depth-sorting-occlusion`](../skills/depth-sorting-occlusion/SKILL.md) skills.
