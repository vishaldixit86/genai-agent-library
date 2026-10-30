# AI Engineer Platform — runnable foundation

This is a **local deterministic** orchestration/control layer, not an autonomous multi-agent runtime.

## Commands
```powershell
python platform/task_router.py "Implement case-level access control"
python platform/evaluate.py
python platform/code_graph.py --project C:\Projects\fincrime --output C:\Projects\fincrime\docs\code-graph.json
python platform/policy_gate.py --evidence C:\Projects\fincrime\docs\change-evidence.json
```

- `task_router.py` recommends workflow, candidate agents and approval needs; does not execute agents.
- `code_graph.py` builds a **static Python AST graph** locally. Edges contain expressions, not resolved dynamic calls; not a semantic knowledge graph.
- `policy_gate.py` verifies that required fields exist; does not verify evidence truth, security, tests, or approvals.
- `evaluate.py` runs fixture-based deterministic routing tests.
- `ai-engineer-ci.yml` tests this repository's orchestration scripts, not client applications.

For production: integrate a permission-controlled agent runtime, explicit delegated execution and approval queue, private graph storage, CI scan enforcement, signed pinned releases, and evaluation with real repo fixtures. Never store client files in this public repo.
