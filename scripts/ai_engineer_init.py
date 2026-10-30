#!/usr/bin/env python3
"""Install AI Engineer assets from this cloned library into a local project safely.

Run: python scripts/ai_engineer_init.py --project C:/path/to/project --pack genai-graphrag
This script never sends project files to the library or to a remote service.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

LIBRARY = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--project", type=Path, required=True)
parser.add_argument("--pack", choices=["python-fastapi","react","aws","azure","terraform","data-engineering","genai-graphrag"])
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
target = args.project.expanduser().resolve()
if not target.is_dir():
    parser.error("Project directory does not exist")
if target == LIBRARY:
    parser.error("Choose a separate project repository, not the central library")

mapping = {}
for source in (LIBRARY / "own-agents").glob("*.agent.md"):
    mapping[source] = target / ".github" / "agents" / source.name
for source in (LIBRARY / "skills" / "custom").glob("**/SKILL.md"):
    skill = source.parent
    for file in skill.rglob("*"):
        if file.is_file():
            mapping[file] = target / ".github" / "skills" / skill.name / file.relative_to(skill)
for name in ("decision.md","flow.md","quizyouon-changes.md"):
    source = LIBRARY / "skills" / name
    if source.exists():
        mapping[source] = target / "docs" / "ai-engineer-guides" / name
for source in (LIBRARY / "workflows").glob("*.md"):
    mapping[source] = target / "docs" / "ai-engineer-workflows" / source.name
for source in (LIBRARY / "templates").glob("*.md"):
    mapping[source] = target / "docs" / "ai-engineer-templates" / source.name

problems = []
writes = []
for src, dst in mapping.items():
    if not dst.resolve().is_relative_to(target):
        problems.append(f"Unsafe destination: {dst}")
    elif dst.exists() and hashlib.sha256(src.read_bytes()).digest() != hashlib.sha256(dst.read_bytes()).digest():
        problems.append(f"Existing customized file: {dst.relative_to(target)}")
    elif not dst.exists():
        writes.append((src,dst))
if problems:
    print("ABORT: conflict(s) detected, no files changed")
    print("\n".join(problems))
    raise SystemExit(2)

for src,dst in writes:
    print(f"{'WOULD ADD' if args.dry_run else 'ADD'} {dst.relative_to(target)}")
    if not args.dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src,dst)
if args.pack:
    catalog = json.loads((LIBRARY/"packs"/"catalog.json").read_text(encoding="utf-8"))
    pack = next(p for p in catalog["packs"] if p["id"] == args.pack)
    path = target/"docs"/"ai-engineer-pack.json"
    if path.exists():
        print("SKIP existing pack selection",path)
    elif not args.dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(pack,indent=2)+"\n",encoding="utf-8")
print(f"{'Dry run' if args.dry_run else 'Install'} completed; {len(writes)} new files. No existing files overwritten.")
