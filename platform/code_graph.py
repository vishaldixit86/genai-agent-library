#!/usr/bin/env python3
"""Generate a local static Python call graph; does not upload project source."""
import argparse
import ast
import json
from pathlib import Path

def scan(root: Path):
    nodes, edges, parse_errors = [], [], []
    for file in sorted(root.rglob("*.py")):
        if any(p in {".git", ".venv", "venv", "node_modules", "__pycache__"} for p in file.parts):
            continue
        rel = file.relative_to(root).as_posix()
        try:
            tree = ast.parse(file.read_text(encoding="utf-8"), filename=rel)
        except (SyntaxError, UnicodeError, OSError) as exc:
            parse_errors.append({"file": rel, "error": type(exc).__name__})
            continue
        class Walk(ast.NodeVisitor):
            def __init__(self):
                self.stack = []
            def enter(self, node):
                qual = ".".join([*self.stack, node.name])
                node_id = f"{rel}::{qual}"
                nodes.append({"id": node_id, "file": rel, "line": node.lineno})
                self.stack.append(node.name)
                for stmt in node.body:
                    self.visit(stmt)
                self.stack.pop()
            def visit_FunctionDef(self, node): self.enter(node)
            def visit_AsyncFunctionDef(self, node): self.enter(node)
            def visit_ClassDef(self, node):
                self.stack.append(node.name)
                for stmt in node.body: self.visit(stmt)
                self.stack.pop()
            def visit_Call(self, node):
                if self.stack:
                    target = ast.unparse(node.func)
                    edges.append({"from": f"{rel}::" + ".".join(self.stack),
                                  "calls_expression": target, "line": node.lineno,
                                  "resolution": "unverified-static-expression"})
                self.generic_visit(node)
        Walk().visit(tree)
    return {"nodes": nodes, "call_expressions": edges, "parse_errors": parse_errors,
            "limitations": "AST-only: dynamic dispatch, imports, polymorphism, ordering and runtime behavior are not resolved."}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--project", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    root = args.project.resolve()
    if not root.is_dir(): p.error("Project directory missing")
    result = scan(root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Mapped {len(result['nodes'])} functions and {len(result['call_expressions'])} call expressions")
