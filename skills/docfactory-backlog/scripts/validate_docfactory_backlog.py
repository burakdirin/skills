#!/usr/bin/env python3
"""Validate docfactory-backlog output structure.

Checks:
- 06-backlog.md exists
- Required top sections exist
- Contains phases, epics, critical path, and at least N Phase-1 tasks
"""
from pathlib import Path
import re
import sys

REQUIRED_FILE = Path("06-backlog.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]

PHASE_1_TASK_RE = re.compile(r"^###\s+P1-T\d{2,3}\s+—\s+.+$", re.M)

MIN_P1_TASKS = 20

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 06-backlog.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    if "## 2) Phases" not in text:
        fail("Missing Phases section")

    if "## 3) Epics" not in text:
        fail("Missing Epics section")

    if "## 4) Critical Path" not in text:
        fail("Missing Critical Path section")

    tasks = PHASE_1_TASK_RE.findall(text)
    if len(tasks) < MIN_P1_TASKS:
        print(f"WARNING: Found {len(tasks)} Phase-1 tasks, expected >= {MIN_P1_TASKS}. Consider splitting big tasks into 30–90 min chunks.")
    else:
        print(f"PASS: Found {len(tasks)} Phase-1 task cards.")

if __name__ == "__main__":
    main()
