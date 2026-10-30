# GenAI Agent Library

Personal public library of Microsoft's HVE Core and custom GenAI agents.

## Repository folders

- `hve-core/agents/` — Microsoft HVE Core agents (populated from Microsoft's official manifest).
- `skills/` — Microsoft HVE Core skills, including scripts and supporting resources.
- `own-agents/` — reserved for your own custom agents; initially empty.
- `.github/agents/` — Copilot-discoverable copies of HVE agents (maintained by import workflow).
- `.github/skills/` — Copilot-discoverable copies of HVE skills.
- `.github/instructions/` — HVE Core instructions.

## Importing HVE Core

The workflow `Import Microsoft HVE Core` runs when initially added and can be rerun manually from GitHub Actions. It checks out `microsoft/hve-core`, reads its `plugin.json`, copies listed components into the folders above, and commits changes.

**Review any upstream agent and skill instructions before allowing access to sensitive repositories or secrets.**
The repository is **public**. Never commit credentials, private company source, or proprietary instructions.

Source: https://github.com/microsoft/hve-core

Copyright and license notices remain with the imported files. Check Microsoft HVE Core's own license and third-party notices before redistribution.

## AI Engineer Accelerator

This public library now includes five custom AI Engineer agents in `own-agents/`, eight human-readable workflows in `workflows/`, project-local knowledge and quality templates in `templates/`, optional technology-pack definitions in `packs/`, and a safe local installer in `scripts/ai_engineer_init.py`.

### Install into another project

Clone this library separately, then run from its root:

```powershell
python scripts/ai_engineer_init.py --project C:\Projects\my-app --pack python-fastapi --dry-run
python scripts/ai_engineer_init.py --project C:\Projects\my-app --pack python-fastapi
```

The installer copies custom agents to the consuming project's `.github/agents/`, custom SKILL.md directories to `.github/skills/`, and reference workflows/templates to `docs/`. It **never overwrites modified files**; rerun with a fresh project or resolve conflicts deliberately. It does not install every Microsoft HVE Core agent, and it does not activate a CLI command named `ai-engineer`.

**Client confidentiality:** Keep client-specific project memory, flows, docs and secrets inside each authorized project, never in this public library. Always review agent instructions and external code before using them in client environments. The custom skill catalog is being built incrementally; do not assume all 100 proposed skills have been published.
