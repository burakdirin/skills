#!/usr/bin/env python3
"""Validate docfactory-arch output structure.

Checks:
- 04-tech-architecture.md exists
- Required top sections exist
- Contains: dependency plan table, data model section, deployment section, folder tree section
"""

import sys
from pathlib import Path

REQUIRED_FILE = Path("04-tech-architecture.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]


MUST_CONTAIN = [
    "## 3) Dependency Plan",
    "## 6) Data Model",
    "## 12) Deployment & CI/CD",
    "## 14) Appendix",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 04-tech-architecture.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    missing = [s for s in MUST_CONTAIN if s not in text]
    if missing:
        fail(f"Missing required sections: {missing}")

    # Simple heuristic: ensure a table exists
    if "| Package (npm) |" not in text:
        print(
            "WARNING: Dependency table header not found. Ensure the dependency plan is tabular."
        )

    if "RLS" not in text and "Row Level" not in text:
        print("WARNING: RLS not mentioned. Ensure Supabase RLS approach is documented.")

    if "eas" not in text.lower():
        print("WARNING: EAS not mentioned. Ensure EAS Build/Submit is covered.")

    print("PASS: 04-tech-architecture.md looks structurally valid.")


if __name__ == "__main__":
    main()
