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
