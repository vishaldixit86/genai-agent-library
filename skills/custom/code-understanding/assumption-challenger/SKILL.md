---
name: assumption-challenger
description: Use for assumption challenger in software engineering tasks; ground all conclusions in source evidence.
---
# assumption challenger
## Trigger
Use when tasks involve assumption challenger.
## Method
1. Read the requested outcome, acceptance criteria, and relevant repository files before making assumptions.
2. Map affected files, functions, interfaces, dependencies, trust boundaries and downstream callers.
3. Identify competing approaches, compatibility risks, security impact and evidence gaps.
4. Recommend a minimal implementable plan, with file paths and symbols that can be verified.
5. If editing is authorized, make focused changes, run relevant tests, and record exact results; require approval for destructive or production work.
6. Document meaningful decisions in docs/ai-decisions.md, function flow in docs/code-flow.md, and ask targeted change-review questions following skills/decision.md, skills/flow.md and skills/quizyouon-changes.md.
## Output
Findings, evidence with file/function references, recommended changes, risk level, validation cases and status (PASS/FAIL/NOT RUN), alternatives and rollback.
## Safety
Never fabricate code facts, tests, approvals or metrics; safeguard secrets and private data; do not make unrelated edits.
