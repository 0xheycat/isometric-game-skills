#!/usr/bin/env python3
"""Validate every skill in skills/ and (re)generate skills.json.

Run locally or in CI:  python3 scripts/validate_skills.py
Exits non-zero if any skill is malformed, so CI fails loudly.
"""
import os, re, json, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

errors = []
manifest = []

for slug in sorted(os.listdir(SKILLS)):
    sdir = os.path.join(SKILLS, slug)
    if not os.path.isdir(sdir):
        continue
    path = os.path.join(sdir, "SKILL.md")
    rel = f"skills/{slug}/SKILL.md"
    if not os.path.exists(path):
        errors.append(f"{slug}: missing SKILL.md")
        continue
    text = open(path, encoding="utf-8").read()

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{slug}: missing YAML frontmatter")
        continue
    fm = m.group(1)

    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.*)$", fm, re.M)
    lic = re.search(r"^license:\s*(.+)$", fm, re.M)

    if not name:
        errors.append(f"{slug}: frontmatter missing 'name'")
    elif name.group(1).strip() != slug:
        errors.append(f"{slug}: name '{name.group(1).strip()}' != folder name")
    if not lic:
        errors.append(f"{slug}: frontmatter missing 'license'")

    # description may be a single line or a YAML block scalar ('>' / '|')
    dtext = desc.group(1).strip() if desc else ""
    if dtext in (">", "|", ">-", "|-", ""):
        cont = []
        tail = fm[desc.end():] if desc else ""
        for line in tail.splitlines():
            if line.startswith((" ", "\t")):
                cont.append(line.strip())
            elif line.strip() == "":
                continue
            else:
                break
        dtext = " ".join(cont).strip()
    if not dtext:
        errors.append(f"{slug}: frontmatter missing 'description'")

    if not re.search(r"^# ", text, re.M):
        errors.append(f"{slug}: no H1 title in body")
    if "Verification" not in text and "verify" not in text.lower():
        errors.append(f"{slug}: no Verification / verify section (skills must be checkable)")

    manifest.append({"name": slug, "path": rel, "description": dtext})

# (re)write machine-readable manifest
manifest_path = os.path.join(ROOT, "skills.json")
json.dump({"count": len(manifest), "skills": manifest},
          open(manifest_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(manifest_path, "a").write("\n")

print(f"Checked {len(manifest)} skills · {len(errors)} error(s)")
for e in errors:
    print("  ❌", e)
if not errors:
    print("✅ All skills valid. Wrote skills.json")
sys.exit(1 if errors else 0)
