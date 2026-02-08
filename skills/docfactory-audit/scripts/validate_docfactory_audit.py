#!/usr/bin/env python3
"""Validate docfactory-audit output structure.

Checks:
- 09-consistency-audit.md exists
- Required top sections exist
- Contains Findings Table and Proposed Patches sections
"""

import sys
from pathlib import Path

REQUIRED_FILE = Path("09-consistency-audit.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]


MUST_CONTAIN = [
    "## 3) Findings Table",
    "## 6) Proposed Patches",
    "## 7) Next Actions",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 09-consistency-audit.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    missing = [s for s in MUST_CONTAIN if s not in text]
    if missing:
        fail(f"Missing required sections: {missing}")

    if "| ID | Severity |" not in text:
        print(
            "WARNING: Findings table header not found. Ensure findings are tabulated for scanning."
        )

    print("PASS: 09-consistency-audit.md looks structurally valid.")


if __name__ == "__main__":
    main()
