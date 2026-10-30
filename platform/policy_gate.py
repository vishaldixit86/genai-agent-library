#!/usr/bin/env python3
"""PR evidence gate: fails closed for missing evidence on relevant changes."""
import argparse
import json
from pathlib import Path

REQUIRED = ("change_summary", "risk_assessment", "test_evidence", "decision_record", "flow_reviewed", "security_reviewed", "rollback_plan")

def evaluate(data):
    missing = [field for field in REQUIRED if not data.get(field)]
    denied = data.get("sensitive_operation") and data.get("human_approval") is not True
    return {"status": "BLOCK" if missing or denied else "PASS", "missing": missing,
            "approval_missing": bool(denied), "note": "Evidence presence only; not independent security validation."}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--evidence", required=True, type=Path)
    args = p.parse_args()
    result = evaluate(json.loads(args.evidence.read_text(encoding="utf-8")))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
