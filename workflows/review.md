# AI Engineer /review

## Goal
Review code changes before merge.

## Runbook
Inspect diff and contracts; rank concrete correctness, security, performance and test findings by severity; attach evidence, recommend fixes and use the PR template.

## Required outputs
- Verified repository evidence with file and symbol references
- Risks, open questions and explicit assumptions
- Relevant tests and actual results (or NOT RUN)
- Project-local documentation updates where applicable

## Guardrails
Use project-approved tools only. Require explicit approval for destructive, privileged or production operations. Never transfer client information into the public shared library. Reference `skills/decision.md`, `skills/flow.md` and `skills/quizyouon-changes.md` for meaningful code changes.
