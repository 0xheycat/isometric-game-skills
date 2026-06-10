# Skill Anatomy

Every skill in this repo follows the same structure. This consistency is what lets an AI agent pick the right skill and execute it without improvising.

## File location & naming

```
skills/<kebab-case-name>/SKILL.md
skills/<kebab-case-name>/assets/      # optional images
skills/<kebab-case-name>/scripts/     # optional helper scripts
skills/<kebab-case-name>/references/  # optional deep-dive docs
```

## Template

```markdown
---
name: my-skill-name
description: Use when <trigger condition> to <outcome>.
license: MIT
---

# My Skill Name

## Overview
One short paragraph: what this is and why naive attempts fail.

## When to Use
- Concrete trigger 1
- Concrete trigger 2

## Process
1. Numbered, non-negotiable step.
2. Another concrete step.

## Rationalizations (Stop Lying to Yourself)
| Excuse | Reality |
|---|---|
| "The excuse an agent makes" | Why it is wrong. |

## Red Flags - STOP if you catch yourself:
- A condition that means you are about to ship something broken.

## Verification
You are NOT done until every box is checked:
- [ ] Concrete, checkable outcome.
```

## The five design principles

1. **Process, not prose.** Agents follow numbered steps far better than paragraphs.
2. **Anti-rationalization.** Name the excuse, then kill it. This is what stops corner-cutting.
3. **Verification is mandatory.** A skill with no checklist cannot be "done".
4. **Progressive disclosure.** Keep `SKILL.md` tight; push depth into `references/`.
5. **Trigger-first descriptions.** Start `description` with "Use when…" so agents auto-select.
