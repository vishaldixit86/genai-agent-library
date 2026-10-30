#!/usr/bin/env python3
"""Deterministic, inspectable AI Engineer task router. No model/API calls."""
import argparse
import json
import re
from pathlib import Path

ROUTES = {
    "understand": (r"understand|onboard|explain|explore|map repository", ["project-brain", "code-investigator"]),
    "design": (r"design|architecture|ontology|schema|plan", ["project-brain", "orchestrator"]),
    "fix": (r"fix|bug|error|traceback|incident|debug", ["code-investigator", "orchestrator"]),
    "review": (r"review|pull request|\bpr\b|audit", ["smart-pr-reviewer", "code-investigator"]),
    "test": (r"test|evaluate|regression|coverage", ["orchestrator", "smart-pr-reviewer"]),
    "release": (r"release|deploy|migration|production", ["release-advisor", "smart-pr-reviewer"]),
    "handover": (r"handover|transfer|documentation|runbook", ["project-brain", "orchestrator"]),
    "build": (r"build|implement|feature|create|add", ["orchestrator", "smart-pr-reviewer"]),
}
SENSITIVE = re.compile(r"production|deploy|delete|drop table|migrat|access control|permission|secret|credential|pii|customer data", re.I)

def route(text: str) -> dict:
    matches = [key for key, (pattern, _) in ROUTES.items() if re.search(pattern, text, re.I)]
    selected = matches[0] if matches else "understand"
    return {
        "task": text, "workflow": selected, "candidate_agents": ROUTES[selected][1],
        "approval_required": bool(SENSITIVE.search(text)),
        "stages": ["inspect", "plan", "human-approval" if SENSITIVE.search(text) else "implement", "verify", "document"],
        "note": "Suggested routing only. No agents or tools were executed."
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("task")
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    result = json.dumps(route(args.task), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result + "\n", encoding="utf-8")
    print(result)
