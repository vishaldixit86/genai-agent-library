# AI Engineer /release

## Goal
Evaluate release readiness.

## Runbook
Inspect CI, security, migrations, rollback, observability and approvals. Return PASS, CONDITIONAL or BLOCK with explicit evidence and remaining risks; do not deploy without permission.

## Required outputs
- Verified repository evidence with file and symbol references
- Risks, open questions and explicit assumptions
- Relevant tests and actual results (or NOT RUN)
- Project-local documentation updates where applicable

## Guardrails
Use project-approved tools only. Require explicit approval for destructive, privileged or production operations. Never transfer client information into the public shared library. Reference `skills/decision.md`, `skills/flow.md` and `skills/quizyouon-changes.md` for meaningful code changes.
