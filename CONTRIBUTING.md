# Contributing

Thanks for helping build the best open collection of isometric game agent skills!

## Ways to contribute

- **New skill** — fill a gap in the pipeline (open a [new-skill issue](.github/ISSUE_TEMPLATE/new-skill.md) first).
- **Improve a skill** — sharper steps, better red flags, more honest rationalizations.
- **Add visuals** — a demo image makes a skill 10x more convincing.
- **Fix docs** — typos, broken links, setup gotchas.

## Skill requirements (non-negotiable)

Every skill MUST:

1. Live at `skills/<kebab-case-name>/SKILL.md`.
2. Start with YAML frontmatter: `name`, `description` (must begin with "Use when…"), `license`.
3. Follow the anatomy: Overview -> When to Use -> Process -> Rationalizations -> Red Flags -> Verification.
4. Use **process, not prose** — numbered, actionable steps.
5. Include a **Verification** checklist. A skill with no way to verify it is incomplete.
6. Be tool-agnostic where possible (works in Claude Code, Cursor, Codex).

See [`docs/skill-anatomy.md`](docs/skill-anatomy.md) for the template.

## PR checklist

- [ ] Skill follows the anatomy and naming convention.
- [ ] `description` begins with "Use when…".
- [ ] Steps are concrete and ordered.
- [ ] Verification checklist is present.
- [ ] Any images are optimized (< 600KB each) and placed in the skill's `assets/`.
- [ ] Links are relative and resolve.

## Style

- Keep it short. An agent has a limited context budget — every line must earn its place.
- No marketing fluff inside skills. Save the hype for the README.
- Prefer concrete numbers (steps, CFG, pixels) over vague advice.
