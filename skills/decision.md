# Decision Log — AI-Assisted Code Changes

## Purpose
Record **meaningful decisions** an AI coding agent proposes or makes when changing code, configuration, dependencies, interfaces, tests, infrastructure, or architecture. Explain **why** the change is needed and what alternatives were considered. This file is the protocol; put actual entries in the project's `docs/ai-decisions.md` (create if absent).

## When to log
Log any change that affects: behavior, API contracts, schema, authorization, privacy, performance, error handling, dependencies, architecture, deployments, data migration, cost, compatibility, or testing strategy. Log a rejected approach when it materially influenced the choice. Do not flood the log with trivial formatting changes.

## Agent rules
1. Inspect relevant code and available requirements **before** recommending a change.
2. Before making a nontrivial edit, state the intent, evidence, expected impact, and alternative(s). For high-impact/irreversible changes, request human approval.
3. After edits, append a decision entry with actual file paths, functions, tests, results, and follow-ups. Never fabricate validation, approvals, measurements, or citations.
4. Distinguish **proposed**, **approved**, **implemented**, **verified**, and **reverted** states; never label a change verified merely because it was written.
5. Link the relevant commit/PR/issue when available; otherwise use `not yet available`.
6. Redact secrets, credentials, PII, and internal information not suitable for the repository. Avoid logging sensitive code excerpts.
7. On revisions, append a superseding entry or clearly mark the prior entry superseded; preserve the decision history.

## Entry template
```markdown
### DEC-YYYYMMDD-NNN — <short decision title>
- Timestamp (UTC):
- Status: proposed | approved | implemented | verified | reverted | superseded
- Request / issue:
- Context and observed behavior:
- Decision:
- Why (evidence and reasoning):
- Alternatives considered and why rejected:
- Files / functions / interfaces affected:
- Expected behavior and risks:
- Security / privacy / compatibility implications:
- Validation planned:
- Validation performed and results (or not run):
- Human approval (if required; otherwise N/A):
- Commit / PR:
- Rollback plan:
- Owner and follow-up:
```

## Definition of done
No meaningful AI-authored change is complete until its rationale and actual impact are recorded, and unverified assumptions or missing tests are explicit.
