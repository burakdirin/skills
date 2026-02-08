#!/usr/bin/env python3
"""Validate DocFactory Init outputs.

Checks:
- Required files exist
- Each file includes required top sections
- Assumptions are tagged [ASSUMPTION-A#]
- No invented market numbers (basic heuristic)
"""

import re
import sys
from pathlib import Path

REQUIRED_FILES = ["00-project-brief.md", "00-decisions.md", "00-glossary.md"]
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]

NUMBERY_PAT = re.compile(
    r"\b(TAM|SAM|SOM|downloads?|installs?|MAU|DAU|ARR|MRR)\b", re.IGNORECASE
)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    base = Path(".")
    missing = [f for f in REQUIRED_FILES if not (base / f).exists()]
    if missing:
        fail(f"Missing files: {missing}")

    for f in REQUIRED_FILES:
        p = base / f
        text = p.read_text(encoding="utf-8")

        for h in REQUIRED_HEADINGS:
            if h not in text:
                fail(f"{f} missing heading: {h}")

        # Assumption tags check (if assumptions section not empty)
        # Allow empty assumptions, but if there is content, tags should be present.
        m = re.search(r"## Assumptions\s*(.*?)(?:\n## |\Z)", text, re.S)
        if m:
            body = m.group(1).strip()
            if body and "[ASSUMPTION-" not in body:
                fail(
                    f"{f} assumptions content exists but no [ASSUMPTION-A#] tags found"
                )

        # Heuristic: forbid market sizing terms in init outputs
        if NUMBERY_PAT.search(text):
            print(
                f"WARNING: {f} includes market/metric terms. Ensure you did not invent numbers."
            )

    print("PASS: DocFactory init outputs look structurally valid.")


if __name__ == "__main__":
    main()
