---
name: asset-pipeline-automation
description: Use when automating the path from generated sprites to a shipped atlas + map so re-generating art does not mean hours of manual rework.
license: MIT
---

# Asset Pipeline Automation

## Overview

Manual asset handling does not scale past a few sprites. This skill builds a one-command pipeline: clean -> pack atlas -> emit JSON -> validate, so artists regenerate and the game just updates.

## When to Use

- You regenerate assets often and redo packing by hand.
- Atlas/JSON drifts out of sync with the sprites.
- You want a reproducible build step for art.

## Process

1. Define input (raw generated sprites) and output (atlas + JSON + map) folders.
2. Script step 1: background cleanup (see `transparent-cutout-cleanup`).
3. Script step 2: atlas packing + JSON (see `spritesheet-atlas-packing`).
4. Script step 3: validate every referenced sprite exists in the atlas.
5. Make it one command (`npm run assets`) and idempotent.
6. Fail loudly if a sprite is missing or an anchor is undefined.
7. Run it in CI so broken assets never ship.

```bash
npm run assets   # clean -> pack -> emit json -> validate
```

## Rationalizations (Stop Lying to Yourself)

| Excuse | Reality |
|---|---|
| "Packing by hand is fine for now" | It will not be fine at 100 sprites. Automate early. |
| "I will validate manually" | Manual validation misses one sprite and ships a hole. Automate the check. |

## Red Flags - STOP if you catch yourself:

- Manual atlas packing on every art change.
- Atlas and JSON drifting out of sync.
- No validation that referenced sprites exist.

## Verification

You are NOT done until every box is checked:

- [ ] One command rebuilds atlas + JSON from raw sprites.
- [ ] Pipeline validates all references and fails loudly.
- [ ] Build is idempotent and runs in CI.
