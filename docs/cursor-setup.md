# Cursor Setup

Cursor does not have a native `skills/` folder like Claude Code, but you can still use these skills.

## Option A: Project rules (recommended)

1. Create `.cursor/rules/` in your project.
2. For each skill you want active, copy the body of its `SKILL.md` into a `.mdc` rule file.
3. Set the rule to **Auto Attach** using a glob (e.g. `**/*.ts` for engine skills) or **Agent Requested** with the skill's description.

## Option B: Paste on demand

When you start a relevant task, paste the skill's `SKILL.md` into the chat. The "Use when…" description tells the agent when it applies.

## Tips

- Keep only the skills relevant to your current phase attached — context budget matters.
- The router skill (`using-isometric-skills`) is a great always-on rule.
- Pair engine skills (grid math, renderer, depth sorting) since they reference each other.
