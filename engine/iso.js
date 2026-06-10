// Canonical 2:1 isometric math — pure, dependency-free, unit-tested.
// Same formulas the live demo (../demo/index.html) uses. Import this in your
// own engine so the math is proven, not copy-pasted.
//
// Default tile footprint: W=64, H=32 (a 2:1 diamond). Pass your own W/H to override.

export const TILE_W = 64;
export const TILE_H = 32;

/** Grid (col,row) -> screen pixel anchor (no camera applied). */
export function gridToScreen(col, row, W = TILE_W, H = TILE_H) {
	return { x: (col - row) * (W / 2), y: (col + row) * (H / 2) };
}

/** Screen pixel -> fractional grid coords (inverse of gridToScreen). */
export function screenToGrid(x, y, W = TILE_W, H = TILE_H) {
	return {
		col: (x / (W / 2) + y / (H / 2)) / 2,
		row: (y / (H / 2) - x / (W / 2)) / 2,
	};
}

/** Screen pixel -> the integer tile under that point (for mouse picking). */
export function tileAt(x, y, W = TILE_W, H = TILE_H) {
	const g = screenToGrid(x, y, W, H);
	return { col: Math.floor(g.col), row: Math.floor(g.row) };
}

/** Painter's-order depth key for an isometric scene. Higher = nearer the camera. */
export function depth(col, row) {
	return col + row;
}

/** Return a new array sorted back-to-front so occlusion is correct. */
export function depthSort(items) {
	return [...items].sort((a, b) => depth(a.col, a.row) - depth(b.col, b.row));
}
