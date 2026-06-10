# STYLE.md — Project Art Direction (Example)

> This is a real example of the one-page style sheet produced by the
> [`isometric-art-direction`](skills/isometric-art-direction/SKILL.md) skill.
> Copy it into your own project and every asset prompt must reference it.
> A locked style sheet is why 200 generated assets look like **one game**
> instead of a random asset dump.

## 1. Projection

- **Type:** True 2:1 isometric (dimetric).
- **Tile base:** `128 x 64` px (W = 2 x H).
- **Block thickness:** 16 px for raised terrain.
- **Anchor:** bottom-center of the tile footprint for every sprite.

## 2. Light

- **Direction:** top-left, fixed on EVERY asset.
- **Key/fill:** warm key from upper-left, soft cool fill, gentle ambient occlusion at contact.
- **Shadows:** soft elliptical contact shadow under objects; never a hard drop shadow.

## 3. Shading style

- Soft **hand-painted / painterly** (Hay Day-like). No harsh cel outlines, no pixel art.
- Medium contrast, rounded forms, readable silhouette at small size.

## 4. Palette

| Role | Swatch |
|---|---|
| Grass | `#7cc36b` / shade `#4f9a4a` |
| Path / road (Jalan) | `#c8a877` / shade `#9c8050` |
| Bare ground / dirt (Tanah) | `#a9763f` / shade `#6f4a28` |
| Sand | `#e6d2a0` / shade `#bda674` |
| Water | `#4f9ad6` / hi `#9fd0f0` |
| Field (tilled) | `#caa24a` / shade `#9a7a2f` |
| Wood | `#a4632f` |
| Stone | `#8d9299` |

- **Off-palette colors are forbidden.** New colors must be added here first.

## 5. Scale rules

- A 1-storey house ≈ 1.5 tiles tall. A tree ≈ 1 tile tall. A character ≈ 0.75 tile tall.
- All props in a set share ONE scale — generate with a fixed seed + identical settings.

## 6. Prompt boilerplate

Every asset prompt MUST end with this suffix so style stays consistent:

```text
..., 2:1 isometric view, soft painterly hand-painted shading, top-left light,
isolated on plain flat background, soft contact shadow, game asset, high quality
```

Negative (for SDXL): `harsh outline, pixel art, photo, multiple objects, busy background, drop shadow, off-palette colors`

## 7. Reference image

Keep ONE pinned reference (see `assets/hero-banner.png` in the repo root) and visually
check every new asset against it before accepting.

---

## 8. UI / Brand — “Obsidian & Gold” (MeowArt)

> The in-game art uses the warm painterly palette above. The **product UI**
> (launcher, store, website, HUD chrome) uses this darker brand layer so the
> shell feels premium while the world stays bright.

**Surfaces**

| Token | Value |
|---|---|
| `--bg-base` | `#0A0A0F` |
| `--bg-raised` | `#111118` |
| `--bg-overlay` | `#16161F` |
| `--glass` | `rgba(255,255,255,.04)` |
| `--border` | `rgba(255,255,255,.08)` |

**Gold accent**

| Token | Value |
|---|---|
| `--gold-400` | `#F5B45A` |
| gradient | `linear-gradient(135deg,#FFD9A0,#F5B45A,#E8852C)` |

**Text**

| Role | Value |
|---|---|
| primary | `#F5F3EF` |
| secondary | `#B5B2AC` |
| muted | `#6E6B66` |

**Type & shape**

- Display: **Clash Display**. Body: **Satoshi / Inter**. Mono: **Geist Mono**.
- Corner radius scale: `10 / 16 / 22 / 28`.
- Suggested stack: Tailwind + Radix/shadcn + Framer Motion + GSAP + Lenis (+ R3F/drei for 3D moments).
- The live demo in [`demo/`](demo/) already uses these exact UI tokens for its panels — a working reference.

---

**Verification (from the art-direction skill):**

- [x] Projection, light, palette, scale, anchor, shading all defined.
- [x] 3 test assets visibly belong to the same game.
- [x] Every asset prompt references this sheet.
