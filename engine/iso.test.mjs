// Run: node --test engine/   (also runs in CI on every push/PR)
import { test } from "node:test";
import assert from "node:assert/strict";
import {
	gridToScreen,
	screenToGrid,
	tileAt,
	depth,
	depthSort,
} from "./iso.js";

test("origin maps to (0,0)", () => {
	assert.deepEqual(gridToScreen(0, 0), { x: 0, y: 0 });
});

test("grid <-> screen round-trips exactly", () => {
	for (let c = -8; c <= 8; c++) {
		for (let r = -8; r <= 8; r++) {
			const s = gridToScreen(c, r);
			const g = screenToGrid(s.x, s.y);
			assert.ok(Math.abs(g.col - c) < 1e-9, `col ${c},${r}`);
			assert.ok(Math.abs(g.row - r) < 1e-9, `row ${c},${r}`);
		}
	}
});

test("tileAt floors onto the correct tile", () => {
	const s = gridToScreen(3, 2);
	assert.deepEqual(tileAt(s.x, s.y), { col: 3, row: 2 });
});

test("custom tile size still round-trips", () => {
	const s = gridToScreen(4, 1, 128, 64);
	const g = screenToGrid(s.x, s.y, 128, 64);
	assert.ok(Math.abs(g.col - 4) < 1e-9 && Math.abs(g.row - 1) < 1e-9);
});

test("depthSort orders back-to-front", () => {
	const out = depthSort([
		{ col: 2, row: 2 }, // depth 4 (front)
		{ col: 0, row: 0 }, // depth 0 (back)
		{ col: 1, row: 0 }, // depth 1
	]);
	assert.deepEqual(
		out.map((o) => depth(o.col, o.row)),
		[0, 1, 4],
	);
});
