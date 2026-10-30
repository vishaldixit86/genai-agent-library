#!/usr/bin/env python3
"""Sync Microsoft HVE Core components into this repository from a checked-out upstream source."""
import json
import shutil
import sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit("Usage: python scripts/import_hve_core.py <upstream-hve-root> <destination-repo-root>")

source = Path(sys.argv[1]).resolve()
target = Path(sys.argv[2]).resolve()
manifest = json.loads((source / "plugin.json").read_text(encoding="utf-8"))
counts = {}

def safe_source(relative):
    p = (source / relative).resolve()
    if not p.is_relative_to(source) or not p.exists():
        raise ValueError(f"Unsafe or missing source: {relative}")
    return p

def copy_component(relative, destination):
    src = safe_source(relative)
    dst = (target / destination).resolve()
    if not dst.is_relative_to(target):
        raise ValueError(f"Unsafe destination: {destination}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)

for kind, prefix, mapped in [
    ("agents", ".github/agents/", "hve-core/agents/"),
    ("skills", ".github/skills/", "skills/"),
    ("rules", ".github/instructions/", "hve-core/instructions/"),
    ("commands", ".github/prompts/", "hve-core/prompts/"),
]:
    entries = manifest.get(kind, [])
    counts[kind] = len(entries)
    for item in entries:
        if not item.startswith(prefix):
            raise ValueError(f"Unexpected manifest entry: {item}")
        suffix = item[len(prefix):]
        copy_component(item, mapped + suffix)
        # Project-native paths allow VS Code Copilot to discover imported items.
        copy_component(item, prefix + suffix)

# Do not modify the user's reserved own-agents directory.
(target / "own-agents").mkdir(exist_ok=True)
(target / "own-agents" / ".gitkeep").touch(exist_ok=True)
(target / "hve-core" / "SOURCE.json").write_text(
    json.dumps({"source": "https://github.com/microsoft/hve-core", "version": manifest.get("version"), "counts": counts},
               indent=2) + "\n", encoding="utf-8")
print("Imported HVE Core:", counts)
