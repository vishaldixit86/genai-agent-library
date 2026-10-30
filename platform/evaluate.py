#!/usr/bin/env python3
"""Evaluate routing and approval behavior against local JSON test cases."""
import argparse
import json
from pathlib import Path
from task_router import route

def evaluate(cases):
    results = []
    for case in cases:
        actual = route(case["task"])
        passed = actual["workflow"] == case["workflow"] and actual["approval_required"] == case["approval_required"]
        results.append({"task": case["task"], "passed": passed,
                        "expected": {"workflow": case["workflow"], "approval_required": case["approval_required"]},
                        "actual": {"workflow": actual["workflow"], "approval_required": actual["approval_required"]}})
    return results

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--cases", type=Path, default=Path(__file__).resolve().parents[1]/"evaluations"/"routing-cases.json")
    args=p.parse_args()
    results=evaluate(json.loads(args.cases.read_text(encoding="utf-8")))
    print(json.dumps({"passed":sum(r["passed"] for r in results), "total":len(results),"cases":results},indent=2))
    raise SystemExit(0 if all(r["passed"] for r in results) else 1)
