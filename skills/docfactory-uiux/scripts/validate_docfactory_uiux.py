#!/usr/bin/env python3
"""Validate docfactory-uiux output structure.

Checks:
- 03-ui-ux-spec.md exists
- Required top sections exist
- Contains route map section
- Contains component inventory section
- Contains screen specifications section
- Contains state matrix and accessibility section
"""

import sys
from pathlib import Path

REQUIRED_FILE = Path("03-ui-ux-spec.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]


MUST_CONTAIN = [
    "## 3) Expo Router Route Map",
    "## 5) Component Inventory",
    "## 6) Screen Specifications",
    "## 7) State Matrix",
    "## 9) Accessibility",
    "## 10) UI Consistency Rules",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 03-ui-ux-spec.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    missing = [s for s in MUST_CONTAIN if s not in text]
    if missing:
        fail(f"Missing required sections: {missing}")

    # Ensure at least one screen section exists
    if "### Screen:" not in text and "### Screen: <Name>" not in text:
        print(
            "WARNING: No explicit screen sections found. Ensure each MVP screen is specified."
        )

    print("PASS: 03-ui-ux-spec.md looks structurally valid.")


if __name__ == "__main__":
    main()
