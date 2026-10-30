# Code Flow Map — Files, Functions, and Call Order

## Purpose
Explain **how code executes** from an entry point to its downstream files, classes, functions, services, and return values. This is an instruction template; store each project's actual code-specific flow in `docs/code-flow.md`.

## When to update
Update when an agent adds, removes, renames, or changes a call path, route, event handler, background job, queue consumer, dependency injection binding, orchestration step, database operation, or external integration.

## How to trace a flow
1. Identify entry points (HTTP route, CLI command, job scheduler, event consumer, UI action, test).
2. Read source code rather than infer call graphs from function names.
3. Follow the exact call order, including branches, callbacks, awaits, retries, and exception paths.
4. For every hop, give the repository-relative file, symbol, input/output, and why the call happens.
5. Distinguish direct calls from **indirect**, dependency-injected, event-driven, dynamically dispatched, and external calls.
6. Identify where state/data changes, authorization checks occur, and requests cross service boundaries.
7. Flag uncertain paths as **unverified**; add a reproducible trace/test when possible.
8. After code changes, update only affected flows and verify against tests or runtime traces where feasible.

## Flow entry template
```markdown
## Flow: <feature / request>
- Last verified:
- Trigger / entry point: `path/to/file.py::route_handler`
- Inputs:
- Output / side effects:
- Authentication / permissions:

### Execution order
1. `api/routes.py::handler()` — receives request; calls `service.execute()`.
2. `services/service.py::execute()` — validates data; calls `repo.load()`.
3. `data/repo.py::load()` — reads data; returns records.
4. `services/service.py::execute()` — transforms records; returns result.
5. `api/routes.py::handler()` — builds response.

### Call graph
```text
HTTP request
  -> api/routes.py::handler()
     -> services/service.py::execute()
        -> data/repo.py::load()
     <- result
  <- HTTP response
```

### Branches / failures / async steps
- Condition:
- Exception/retry handling:
- Background work:
- External services / data stores:

### Evidence
- Source references:
- Tests / traces:
- Unverified assumptions:
```

## Rules
Do not assert that code runs in a given order without inspecting implementation. When execution is concurrent or event-driven, show scheduling/await boundaries rather than inventing a deterministic sequence. Include cyclic calls and recursive relationships if present.
