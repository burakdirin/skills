#!/usr/bin/env python3
"""Validate docfactory-market output structure.

Checks:
- 01-market-research.md exists
- Required top sections exist
- Contains competitor table header
- Contains a Sources section with at least N URLs (warn only if not)
"""

import re
import sys
from pathlib import Path

REQUIRED_FILE = Path("01-market-research.md")
REQUIRED_HEADINGS = [
    "## Decision Summary",
    "## Open Questions",
    "## Assumptions",
    "## Risks & Mitigations",
]
MIN_URLS = 8

URL_RE = re.compile(r"https?://\S+")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    if not REQUIRED_FILE.exists():
        fail("Missing 01-market-research.md")

    text = REQUIRED_FILE.read_text(encoding="utf-8")

    for h in REQUIRED_HEADINGS:
        if h not in text:
            fail(f"Missing heading: {h}")

    if ("## 2) Competitor landscape" not in text) and ("| Competitor |" not in text):
        fail("Missing competitor landscape section/table")

    if ("## 8) Sources" not in text) and ("## Sources" not in text):
        fail("Missing Sources section")

    urls = URL_RE.findall(text)
    if len(urls) < MIN_URLS:
        print(
            f"WARNING: Only {len(urls)} URLs found, expected >= {MIN_URLS}. If browsing was unavailable, ensure [NO_DATA] is used."
        )
    else:
        print(f"PASS: Found {len(urls)} URLs in the doc.")


if __name__ == "__main__":
    main()
