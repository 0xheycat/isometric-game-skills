// Headless renderer: reads sample-map.json and draws it to an SVG using the
// *tested* engine math (../engine/iso.js). No browser, no dependencies.
//
//   node examples/render-map.mjs
//
// -> writes examples/sample-map.svg  (proof the data format + engine render a real map)
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { gridToScreen, depth, depthSort } from "../engine/iso.js";

const here = dirname(fileURLToPath(import.meta.url));
const map = JSON.parse(readFileSync(join(here, "sample-map.json"), "utf8"));

const W = map.tileSize.w;
const H = map.tileSize.h;
const SIDE = 10; // faux-thickness on the south edge

const TOP = {
	water: "#4f86c6",
	sand: "#dcc38a",
	grass: "#5aa54a",
	path: "#b9925a",
	field: "#c9a94a",
	"bare-ground": "#a9763f",
};
const SIDECOL = {
	water: "#3a679b",
	sand: "#b39e6a",
	grass: "#3f7d36",
	path: "#8f6f42",
	field: "#9c7d38",
	"bare-ground": "#6f4a28",
};

const ground = map.layers.find((l) => l.name === "ground").data;
const objects = map.layers.find((l) => l.name === "objects").items;

// --- collect drawables ---
const tiles = [];
for (let r = 0; r < map.size.rows; r++) {
	for (let c = 0; c < map.size.cols; c++) {
		tiles.push({ c, r, type: map.tileset[String(ground[r][c])] });
	}
}
tiles.sort((a, b) => depth(a.c, a.r) - depth(b.c, b.r));

// --- bounds ---
let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
for (const t of tiles) {
	const s = gridToScreen(t.c, t.r, W, H);
	minX = Math.min(minX, s.x - W / 2);
	maxX = Math.max(maxX, s.x + W / 2);
	minY = Math.min(minY, s.y);
	maxY = Math.max(maxY, s.y + H + SIDE);
}
const pad = 24;
const ox = -minX + pad;
const oy = -minY + pad;
const vw = Math.round(maxX - minX + pad * 2);
const vh = Math.round(maxY - minY + pad * 2);

const esc = (n) => Math.round(n * 100) / 100;
function diamond(s) {
	const top = `${esc(s.x)},${esc(s.y)}`;
	const right = `${esc(s.x + W / 2)},${esc(s.y + H / 2)}`;
	const bottom = `${esc(s.x)},${esc(s.y + H)}`;
	const left = `${esc(s.x - W / 2)},${esc(s.y + H / 2)}`;
	return { top, right, bottom, left };
}

const parts = [];
parts.push(
	`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${vw} ${vh}" width="${vw}" height="${vh}" font-family="sans-serif">`,
);
parts.push(`<rect width="${vw}" height="${vh}" fill="#0A0A0F"/>`);
parts.push(`<g transform="translate(${esc(ox)},${esc(oy)})">`);

for (const t of tiles) {
	const s = gridToScreen(t.c, t.r, W, H);
	const d = diamond(s);
	const side = SIDECOL[t.type] || "#333";
	const top = TOP[t.type] || "#888";
	// south-east + south-west faces for thickness
	parts.push(
		`<polygon points="${d.left} ${d.bottom} ${esc(s.x)},${esc(s.y + H + SIDE)} ${esc(s.x - W / 2)},${esc(s.y + H / 2 + SIDE)}" fill="${side}"/>`,
	);
	parts.push(
		`<polygon points="${d.bottom} ${d.right} ${esc(s.x + W / 2)},${esc(s.y + H / 2 + SIDE)} ${esc(s.x)},${esc(s.y + H + SIDE)}" fill="${side}" opacity="0.82"/>`,
	);
	// top face
	parts.push(
		`<polygon points="${d.top} ${d.right} ${d.bottom} ${d.left}" fill="${top}" stroke="rgba(0,0,0,0.18)" stroke-width="1"/>`,
	);
}

// objects on top, back-to-front
const markers = { tree: "\uD83C\uDF33", house: "\uD83C\uDFE0", rock: "\uD83E\uDEA8" };
for (const o of depthSort(objects)) {
	const s = gridToScreen(o.col, o.row, W, H);
	const cx = esc(s.x);
	const cy = esc(s.y + H / 2);
	parts.push(
		`<text x="${cx}" y="${cy + 4}" font-size="22" text-anchor="middle">${markers[o.sprite] || "?"}</text>`,
	);
}

parts.push(`</g>`);
parts.push(
	`<text x="${vw / 2}" y="${vh - 8}" font-size="11" fill="#6E6B66" text-anchor="middle">rendered from sample-map.json via engine/iso.js</text>`,
);
parts.push(`</svg>`);

const out = join(here, "sample-map.svg");
writeFileSync(out, parts.join("\n"));
console.log(`wrote ${out} (${vw}x${vh})`);
