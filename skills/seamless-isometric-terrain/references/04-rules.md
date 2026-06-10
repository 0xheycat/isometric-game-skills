# 04 — Rules & Avoid-List (Professional Handler)

## ✅ DO

1. **Lock ONE fixed seed** for the entire tile set. This is non-negotiable — it is
   what makes tiles share the same diamond shape.
2. **Keep prompts short.** Surface phrase = a few words max.
3. **Change only the surface phrase** between tiles; keep the rest of the prompt identical.
4. **Use a thick solid soil base** under every tile so thickness matches.
5. **Keep the background flat and plain** so background removal is clean.
6. **Generate the grass tile first** as your reference, then match all others to it.
7. **Always export to transparent PNG** (rembg / SAM) before importing to the engine.
8. **Verify each tile against the grass tile**: same angle, same thickness, same fill.

## ❌ AVOID (these break seamlessness)

1. **`thin grassy rim` / `green grass along the edges`** — #1 cause of stray rims and
   irregular shapes. Never include it.
2. **`Hay Day mobile farm game art style, cute hand-painted cartoon`** — adds random
   props and mixes colors. Describe the style with `soft painterly shading` instead.
3. **Long, wordy surface descriptions** — cause mixed/irregular colors. Keep it short.
4. **Letting the seed float / randomize** — every tile becomes a different shape.
5. **Asking for `tilemap grid` / `multiple tiles` / `seamless repeating pattern`** —
   you want ONE tile per generation, not a sheet.
6. **`props`, `house`, `building`, `character`, `flowers`** on a ground tile — clutter
   that ruins repetition. (Add these only as separate object sprites, not on tiles.)
7. **Mixing checkpoints/LoRA strengths mid-set** — changes the look; keep them constant.
8. **Upscaling some tiles but not others** — inconsistent edges. Treat the whole set the same.

## Visual reference: wrong vs right

![Wrong vs right](../assets/04-wrong-vs-right.png)

- **❌ Left:** tiles with different angles/sizes → gaps and visible edges when placed.
- **✅ Right:** identical angle and size → they connect into one smooth surface.

## Mental model

> If a tile looks great alone but bad in a map, it's a **shape/consistency** problem,
> not a texture problem. Go back to the **fixed seed** and matching shape — not the prompt wording.

Next: `05-troubleshooting.md`.
