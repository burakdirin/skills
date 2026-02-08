#!/usr/bin/env python3
"""Validate docfactory-prd output structure.

Checks:
- 02-prd.md exists
- Required top headings exist
- Contains MVP scope section and at least one user story checkbox
- Contains monetization table and metrics section
"""

import sys
from pathlib import Path

REQUIRED_FILE = Path("02-prd.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 02-prd.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    if "## 4) MVP scope" not in text and "MVP scope" not in text:
        fail("Missing MVP scope section")

    if "- [ ]" not in text:
        fail("No acceptance criteria checkboxes found (- [ ])")

    if "## 7) Monetization design" not in text and "Free vs Premium" not in text:
        fail("Missing monetization design section/table")

    if "## 8) Metrics" not in text and "North Star" not in text:
        fail("Missing metrics section")

    if "## 9) ASO" not in text:
        print(
            "WARNING: ASO section not found. Consider adding it for app store readiness."
        )

    print("PASS: 02-prd.md looks structurally valid.")


if __name__ == "__main__":
    main()
