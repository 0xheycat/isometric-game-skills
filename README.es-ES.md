<div align="center">

# 🏔️ Isometric Game Agent Skills (Habilidades para Agentes de Juegos Isométricos)

**Habilidades de IA de grado de producción para crear juegos isométricos — desde el arte generado por IA hasta el motor de renderizado.**

El conjunto de herramientas faltante que enseña a los agentes de codificación de IA cómo los artistas de juegos senior y los programadores de motores construyen realmente mundos isométricos: tiles fluidos, sprites ordenados por profundidad, matemáticas de rejilla y todo el pipeline de assets.

![Skills](https://img.shields.io/badge/skills-21-8957e5) ![Format](https://img.shields.io/badge/format-SKILL.md-F5B45A) ![License](https://img.shields.io/badge/license-MIT-22c55e) ![PRs](https://img.shields.io/badge/PRs-welcome-3b82f6) ![GitHub stars](https://img.shields.io/github/stars/0xheycat/isometric-game-skills?style=flat&logo=github&color=f5b45a) ![Validate](https://img.shields.io/github/actions/workflow/status/0xheycat/isometric-game-skills/validate.yml?label=skills%20valid&logo=github) ![Agents](https://img.shields.io/badge/Claude%20·%20Cursor%20·%20Codex-ready-111118) [![Live Demo](https://img.shields.io/badge/▶_demo-live-22c55e?logo=github&logoColor=white)](https://0xheycat.github.io/isometric-game-skills/demo/) [![Project](https://img.shields.io/badge/project-0xheycat.xyz-f5b45a)](https://0xheycat.xyz/work/isometric-game-skills)

[Inicio Rápido](#-quick-start) · [Demo en Vivo](#-live-demo) · [Las Habilidades](#-the-skill-collection) · [Galería](#-gallery) · [Cómo Funcionan las Habilidades](#-how-skills-work) · [Contribución](#-contributing) · [Hoja de Ruta](#-roadmap)

![Hero banner](assets/hero-banner.png)

</div>

---

## Por qué existe esto

Los agentes de codificación de IA son geniales con React y terribles con los juegos isométricos. Generan tiles que no encajan, sprites en 5 estilos diferentes, personajes que se renderizan detrás de las paredes y renderizadores que caen a 12fps. No porque los modelos sean débiles, sino porque nadie escribió **cómo trabaja realmente un desarrollador isométrico experimentado**.

Este repositorio es ese conocimiento, codificado como archivos **SKILL.md** que un agente puede cargar bajo demanda. Dirige Claude Code, Cursor o Codex hacia él y tu agente, de repente, construirá mundos isométricos como si ya hubiera lanzado tres de ellos.

> ¿Eres nuevo aquí? Comienza con la meta-habilidad **[using-isometric-skills](skills/using-isometric-skills/SKILL.md)** — esta redirige cualquier tarea entrante al flujo de trabajo correcto.

## 🚀 Inicio Rápido

```bash
git clone https://github.com/0xheycat/isometric-game-skills.git
```

Luego conéctalo a tu agente (elige tu herramienta):

| Herramienta | Cómo instalar |
|---|---|
| **Claude Code** | Copia cualquier carpeta `skills/<name>/` en `.claude/skills/` en tu proyecto. |
| **Cursor** | Consulta [`docs/cursor-setup.md`](docs/cursor-setup.md) — añade el cuerpo de la habilidad a las reglas del proyecto. |
| **Codex / otros** | Pega el `SKILL.md` relevante en el contexto de tu agente o en la carpeta de habilidades. |

Guía completa: [`docs/getting-started.md`](docs/getting-started.md).

## 🎮 Demo en Vivo

**▶️ [Juégalo en vivo en tu navegador](https://0xheycat.github.io/isometric-game-skills/demo/)** — alojado en GitHub Pages, sin instalación. Arrastra para desplazar, scroll para hacer zoom, alterna 🖼️ Sprites.

Un renderizador isométrico Canvas2D de un solo archivo y sin dependencias reside en [`demo/`](demo/) — **prueba de que estas habilidades son reales, no teoría**. Terreno procedimental, objetos ordenados por profundidad, selección de tiles y una cámara de pan/zoom, todo en un archivo HTML.

```bash
python3 -m http.server 8080   # luego abre http://localhost:8080/demo/
```

Ejercita directamente seis habilidades: `isometric-grid-math`, `canvas2d-isometric-renderer`, `depth-sorting-occlusion`, `tilemap-data-format`, `tile-picking-interaction`, y `camera-pan-zoom-controls`. Consulta [`demo/README.md`](demo/README.md).

> ¿Quieres el mismo mundo con sprites pictóricos en lugar de bloques planos? Intercambia los assets por los de las habilidades de generación + [`spritesheet-atlas-packing`](skills/spritesheet-atlas-packing/SKILL.md).

<!-- Maintainer note: set the GitHub social card under Settings → Social preview using assets/social-preview.png (1280×640). -->

## 🗺️ Cómo encaja todo

Estos no son 20 consejos sueltos — se encadenan en un pipeline que lleva a un agente desde una carpeta vacía hasta una **escena isométrica jugable**. Pruebas, no teoría.

![Pipeline: all 20 skills from setup to playable scene](assets/pipeline.svg)

- 🎯 **[GOAL.md](GOAL.md)** — la Definición de Hecho (Definition of Done) medible. Cuando cada casilla está marcada, el objetivo se ha *logrado*.
- 🏗️ **[docs/build-a-game.md](docs/build-a-game.md)** — la guía final que ejecuta las **20 habilidades** en orden, con una prueba de aceptación por fase.
- ✅ **[`scripts/validate_skills.py`](scripts/validate_skills.py)** — verificación forzada por CI de que cada `SKILL.md` esté bien formado (la insignia `skills valid` de arriba). Índice legible por máquina: [`skills.json`](skills.json).
- 🧮 **[`engine/iso.js`](engine/iso.js)** — las matemáticas iso canónicas 2:1 (grid↔pantalla, selección, orden de profundidad) con **pruebas unitarias aprobadas** ([`engine/iso.test.mjs`](engine/iso.test.mjs), ejecutadas en CI). Las matemáticas están *probadas*, no afirmadas.
- 🗂️ **[`examples/sample-map.json`](examples/sample-map.json)** — un mapa creado a mano en el formato `tilemap-data-format`. Renderízalo sin interfaz con [`examples/render-map.mjs`](examples/render-map.mjs) → [`sample-map.svg`](examples/sample-map.svg) (dibujado por el motor probado, sin navegador).

## 🧩 La Colección de Habilidades

**21 habilidades** que cubren todo el pipeline de un juego isométrico, agrupadas por fase. Ejecútalas en orden o carga solo la que necesites.

### 🧭 Meta
| Habilidad | Qué hace |
|---|---|
| [using-isometric-skills](skills/using-isometric-skills/SKILL.md) | Enrutador — mapea cualquier tarea a la habilidad correcta, en el orden correcto. |

### 🎨 Fundamentos Artísticos
| Habilidad | Qué hace |
|---|---|
| [comfyui-lowvram-setup](skills/comfyui-lowvram-setup/SKILL.md) | Configuración reproducible de SDXL que nunca agota la memoria (OOM) en una GPU de 12GB. |
| [isometric-art-direction](skills/isometric-art-direction/SKILL.md) | Bloquea UNA hoja de estilo para que 200 assets parezcan de un mismo juego. |

### 🖼️ Generación de Assets (IA)
| Habilidad | Qué hace |
|---|---|
| [seamless-isometric-terrain](skills/seamless-isometric-terrain/SKILL.md) ⭐ | Buque insignia — tiles de suelo que se repiten sin costuras visibles en los bordes. |
| [isometric-object-sprites](skills/isometric-object-sprites/SKILL.md) | Árboles, rocas, accesorios — aislados, consistentes y listos para usar. |
| [isometric-building-sprites](skills/isometric-building-sprites/SKILL.md) | Casas y graneros con huella y oclusión correctas. |
| [isometric-character-sprites](skills/isometric-character-sprites/SKILL.md) | Personajes en 8 direcciones con un anclaje de pies fijo. |
| [animated-sprite-generation](skills/animated-sprite-generation/SKILL.md) | Agua, fuego y molinos con bucles fluidos como tiras de fotogramas. |

### 🧰 Procesamiento de Assets
| Habilidad | Qué hace |
|---|---|
| [transparent-cutout-cleanup](skills/transparent-cutout-cleanup/SKILL.md) | Bordes alfa limpios, sin halos ni franjas. |
| [spritesheet-atlas-packing](skills/spritesheet-atlas-packing/SKILL.md) | Empaca sprites en un solo atlas + mapa JSON. |
| [autotiling-transitions](skills/autotiling-transitions/SKILL.md) | Mezcla de bordes/esquinas mediante bitmask entre terrenos. |

### ⚙️ Motor y Renderizado
| Habilidad | Qué hace |
|---|---|
| [isometric-grid-math](skills/isometric-grid-math/SKILL.md) | Transformaciones exactas rejilla <-> pantalla (y la inversa). |
| [canvas2d-isometric-renderer](skills/canvas2d-isometric-renderer/SKILL.md) | El bucle de renderizado central: primero tiles, luego objetos ordenados. |
| [depth-sorting-occlusion](skills/depth-sorting-occlusion/SKILL.md) | Orden de dibujo correcto para objetos altos y de múltiples tiles. |
| [tilemap-data-format](skills/tilemap-data-format/SKILL.md) | Formato de mapa JSON versionable y por capas. |
| [godot4-isometric-tilemap](skills/godot4-isometric-tilemap/SKILL.md) | Iso nativo de Godot 4: `TileMapLayer` + Y-sort hecho correctamente. |

### 🕹️ Sistemas de Jugabilidad
| Habilidad | Qué hace |
|---|---|
| [isometric-pathfinding](skills/isometric-pathfinding/SKILL.md) | A* en la capa caminable con vecinos isométricos adecuados. |
| [camera-pan-zoom-controls](skills/camera-pan-zoom-controls/SKILL.md) | Desplazamiento, zoom al cursor y limitación de bordes. |
| [tile-picking-interaction](skills/tile-picking-interaction/SKILL.md) | Convierte una posición del ratón en el tile correcto. |

### 🚀 Pulido y Lanzamiento
| Habilidad | Qué hace |
|---|---|
| [canvas-performance-optimization](skills/canvas-performance-optimization/SKILL.md) | Perfilado, culling, batching — mantiene unos 60fps constantes. |
| [asset-pipeline-automation](skills/asset-pipeline-automation/SKILL.md) | Un solo comando: limpiar -> empacar -> validar. |

## 🖼️ Galería

Resultado real siguiendo estas habilidades (estilo pictórico isométrico tipo Hay Day):

| Terreno fluido | Sprites de objetos | Sprites de edificios |
|---|---|---|
| ![terrain](skills/seamless-isometric-terrain/assets/01-goal-map.png) | ![objects](skills/isometric-object-sprites/assets/demo.png) | ![buildings](skills/isometric-building-sprites/assets/demo.png) |

| Personaje 8-direcciones | Transiciones de autotiling | Fotogramas animados |
|---|---|---|
| ![character](skills/isometric-character-sprites/assets/demo.png) | ![autotiling](skills/autotiling-transitions/assets/demo.png) | ![animation](skills/animated-sprite-generation/assets/demo.png) |

## 📐 Cómo Funcionan las Habilidades

Cada habilidad es un único `SKILL.md` con frontmatter YAML y una anatomía fija diseñada para **evitar que un agente tome atajos**:

- **Frontmatter** — `name` + una `description` que comienza con "Usa cuando..." para que los agentes lo seleccionen automáticamente.
- **Process (Proceso)** — pasos numerados y no negociables (procesos, no prosa).
- **Rationalizations (Racionalizaciones)** — las excusas que un agente suele dar, emparejadas con la realidad, para que no pueda convencerse de no hacer el trabajo.
- **Red Flags (Banderas Rojas)** — condiciones de parada que indican que estás a punto de entregar algo roto.
- **Verification (Verificación)** — una lista de verificación; no has terminado hasta que cada casilla esté marcada.

Lee la especificación completa en [`docs/skill-anatomy.md`](docs/skill-anatomy.md).

## 🤝 Contribución

Las PRs son bienvenidas — nuevas habilidades, correcciones y capturas de pantalla ayudan mucho. Lee [`CONTRIBUTING.md`](CONTRIBUTING.md) y usa la [plantilla de issue para nuevas habilidades](.github/ISSUE_TEMPLATE/new-skill.md) para proponer una. Cada habilidad debe seguir la anatomía e incluir una lista de verificación.

## 🗺️ Hoja de Ruta

- [x] 20 habilidades principales (arte -> motor -> jugabilidad -> lanzamiento)
- [x] Pack de referencia para motor Godot 4 ([godot4-isometric-tilemap](skills/godot4-isometric-tilemap/SKILL.md)) — Phaser / Unity a continuación
- [ ] Set de tiles inicial descargable (CC0)
- [ ] Playground web para previsualizar sets de tiles
- [ ] Tutoriales en vídeo por habilidad

## ⭐ Dale una estrella a este repo

Si esto te ahorró un fin de semana peleando con tu agente, **dale una estrella** — ayuda a otros desarrolladores de juegos a encontrarlo.

## 📈 Historial de Estrellas

<a href="https://star-history.com/#0xheycat/isometric-game-skills&Date">
  <img src="https://api.star-history.com/svg?repos=0xheycat/isometric-game-skills&type=Date" alt="Star History Chart" width="600">
</a>

## 📄 Licencia

MIT — consulta [`LICENSE`](LICENSE). Úsalo en juegos comerciales, hazle un fork, remezclalo.

---

## Palabras Clave

<sub>`isometric-game-skills` · `isometric` · `game-development` · `gamedev` · `ai-agents` · `agent-skills` · `claude-code` · `cursor` · `comfyui` · `sdxl` · `sprite-generation` · `tilemap` · `autotiling` · `canvas2d` · `pathfinding` · `depth-sorting` · `godot` · `game-art` · `asset-pipeline` · `procedural-generation` · `2d-games`</sub>
