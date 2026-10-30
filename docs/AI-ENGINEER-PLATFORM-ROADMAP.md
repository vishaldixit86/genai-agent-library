# AI Engineer Platform — implementation roadmap

## Available now (verify in Actions)
- Five Copilot-discoverable AI Engineer agent definitions.
- Eight workflow guides and three decision/flow/change-question guides.
- Local installer with conflict detection.
- Deterministic task router, basic evidence gate, static Python AST call-expression graph and routing evaluation fixtures.
- CI job that compiles the platform and runs deterministic fixtures.

## Next integration milestones
1. **Delegated agents (not implemented):** map routing output to supported Copilot or other agent runtime APIs, scoped tools, timeouts, budget limits and audit logs; obtain consent for delegated actions.
2. **Policy enforcement (partial):** protect main with required status checks; publish project-specific evidence gate and combine with dependency scanning, secret scanning, static analysis, test suites and reviewer approvals. Do not treat presence of JSON fields as genuine approval.
3. **Private project knowledge graph (partial):** expand AST indexing to imports/symbol resolution, incremental updates, graph storage with branch/commit provenance, and authorized retrieval. Never centralize client code or client metadata in this public repository.
4. **Evaluation harness (partial):** add representative synthetic and private per-project tests, tool traces, security red-team cases, regressions, false-positive monitoring and review gates.
5. **Distribution:** pin approved tags, produce signed releases, validate licenses, distribute updates through PRs, support rollback and deprecation.
6. **Operational safety:** separate read-only and write tools, human approval for sensitive access or deployments, per-project audit trails, monitoring and a kill switch.

## Rollout
- Pilot on one synthetic FinCrime repository before any client project.
- Validate task routing, import collisions, actual code graph accuracy, PR check behavior and developer feedback.
- Expand to 5–10 AI Engineers; do not promise performance improvements before measuring.
- Only then publish controlled templates for 100+ engineers.

## Security boundary
The central repository is public. Client data, private architecture, source code, prompts containing confidential information, secrets, graphs and telemetry remain inside each approved private project/environment.
