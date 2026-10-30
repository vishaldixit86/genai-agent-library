# AI Engineer /fix

## Goal
Reproduce and fix a defect.

## Runbook
Gather actual error evidence; isolate failure, trace call chain, test competing hypotheses, implement focused fix, run regression tests and document cause.

## Required outputs
- Verified repository evidence with file and symbol references
- Risks, open questions and explicit assumptions
- Relevant tests and actual results (or NOT RUN)
- Project-local documentation updates where applicable

## Guardrails
Use project-approved tools only. Require explicit approval for destructive, privileged or production operations. Never transfer client information into the public shared library. Reference `skills/decision.md`, `skills/flow.md` and `skills/quizyouon-changes.md` for meaningful code changes.
