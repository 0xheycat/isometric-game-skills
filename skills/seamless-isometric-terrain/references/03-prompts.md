# 03 — Prompts

> Rule of thumb: **short prompts win.** Long surface descriptions cause mixed,
> irregular colors. Keep the surface phrase to a few words.

## Positive prompt (template)

Replace `[SURFACE]` and `[COLOR]` per tile. Everything else stays the same so the
shape stays the same.

```
single isometric full [SURFACE] block tile, 2:1 isometric view,
thick solid [COLOR] soil base underneath, soft painterly shading,
simple clean composition, isolated on plain flat background,
game asset, high quality
```

## Negative prompt (base — use for every tile)

```
diamond gemstone, crystal, jewel, gem, shiny stone, cracked dry soil,
desert ground, flat top-down texture, seamless repeating pattern,
multiple tiles, tilemap grid, scenery, landscape, realistic photo,
3d render, blurry, low quality, watermark, text, signature,
harsh shadows, busy background, house, props, building, character
```

## Per-tile surface phrases (the only thing you change)

| Tile | `[SURFACE]` + `[COLOR]` | Add to negative |
|---|---|---|
| 🌱 Grass (Rumput) | `full grass land` · `green` soil base | `bare dirt top` |
| 🟫 Dirt (Tanah) | `full dirt ground` · `brown` soil base | `grass, grassy edges, plants, flowers, water, cracks, mixed colors, props` |
| 💧 Water (Air) | `full water, calm flat blue water surface on top` · `blue` base | `grass, grassy rim, plants, land, pond shape, irregular edges, mixed colors, props` |
| 🛤️ Road (Jalan) | `full dirt path, light tan packed dirt path surface on top` · `brown` base | `grass, grassy edges, plants, curved path, irregular shape, mixed colors, props` |
| 🌾 Field (Ladang) | `full plowed farm field, even rows of tilled soil furrows on top` · `brown` base | `grass, grassy edges, plants, crops, irregular furrows, mixed colors, props` |

## Example (grass tile, filled in)

**Positive:**
```
single isometric full grass land block tile, 2:1 isometric view,
thick solid green soil base underneath, soft painterly shading,
simple clean composition, isolated on plain flat background,
game asset, high quality
```
**Negative:** base negative + `bare dirt top`

## Seasonal variants (grass) — keep seed fixed, swap the surface phrase

| Season | Surface phrase |
|---|---|
| Spring | `lush green grass with tiny flowers` |
| Summer | `dense vivid green grass` |
| Autumn | `grass with orange and red fallen leaves` |
| Winter | `snow-covered ground with icy patches` |

Next: `04-rules.md`.
