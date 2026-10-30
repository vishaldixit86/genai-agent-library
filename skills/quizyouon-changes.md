# Quiz You on Changes — Clarify, Challenge, and Confirm

## Purpose
Before making consequential code edits, the AI agent should **quiz the requester on important design choices** and ensure the proposed change matches intent. After making changes, the agent should **quiz/verify understanding of what changed**, including behavior, impact, and rollback.

## Before editing: ask only questions that matter
First inspect the request and relevant repository code. Do **not** repeatedly ask for facts the user already supplied. Present your understanding, proposed scope, assumptions, and impacts. Ask focused questions **only when** a missing answer materially changes implementation, safety, or acceptance criteria. Group related high-stakes decisions; offer a recommended default when possible.

### Pre-change prompts (adapt to the task)
1. What exact user-visible behavior should change, and what must stay the same?
2. Which files, routes, APIs, consumers, or data contracts are in scope?
3. Should the change preserve backward compatibility?
4. What are the edge cases and failure conditions?
5. Does it affect auth, data access, secrets, privacy, cost, or performance?
6. Which test cases prove success, and what is the rollback strategy?

**Approval gate:** For destructive database migrations, permission changes, secret handling, production deployments, or irreversible operations, stop and request explicit human authorization. For ordinary low-risk edits, proceed using clear assumptions and document them rather than blocking unnecessarily.

## Before implementation: change proposal
```markdown
### Proposed change
- Goal:
- Current behavior (verified):
- Expected behavior:
- Files/functions affected:
- Proposed approach and rationale:
- Risks and compatibility:
- Questions requiring user decision (if any):
- Acceptance criteria:
- Tests to run:
```

## After implementation: explain and test knowledge
Summarize:
- Exactly what changed (files and functions).
- What calls what now; update `docs/code-flow.md` using `skills/flow.md`.
- Why this approach was chosen; log meaningful decisions using `skills/decision.md`.
- Tests executed and outcomes; state **not run** where relevant.
- Remaining risks, follow-ups, and rollback.

Then, when useful, ask 2–5 short review questions such as:
- Should feature X remain enabled for existing clients?
- Is this changed API response consistent with the expected consumers?
- Is the new error handling acceptable for timeout scenario Y?
- Would you like an explicit regression test for edge case Z?
- Can we approve the documented compatibility trade-off?

Do not quiz the user for trivial formatting changes or artificially delay requested work. Do not invent tests or imply the user approved changes unless they did.
