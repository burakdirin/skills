#!/usr/bin/env python3
"""Generate stub DocFactory Init files from an idea capsule YAML.

NOTE: This generates *templates with placeholders*.
It's meant as a helper for humans or agents that want a starting scaffold.
The actual content quality should come from the AI skill execution.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    print("PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: generate_docfactory_init.py <idea.yaml>")
        sys.exit(1)

    idea_path = Path(sys.argv[1])
    idea = yaml.safe_load(idea_path.read_text(encoding="utf-8"))

    name = idea.get("name", "...")
    target_user = idea.get("target_user", "...")
    core_loop = idea.get("core_loop", "...")
    monetization = idea.get("monetization", "...")
    differentiator = idea.get("differentiator", "...")

    brief = f"""# 00-project-brief.md

## Decision Summary
- (auto-generated stub)

## Open Questions
- (fill in)

## Assumptions
- [ASSUMPTION-A1] ...

## Risks & Mitigations
- [RISK] ...

## Product snapshot
- **Product name:** {name}
- **Target user:** {target_user}
- **Core loop (1 sentence):** {core_loop}
- **Monetization:** {monetization}
- **Differentiator:** {differentiator}

## MVP scope
### IN (Must-have)
- ...

### OUT (Explicit non-goals)
- ...
"""

    decisions = """# 00-decisions.md (Source of Truth)

## Decision Summary
- (auto-generated stub)

## Open Questions
- (fill in)

## Assumptions
- [ASSUMPTION-A1] ...

## Risks & Mitigations
- [RISK] ...

## Stack (locked for MVP)
- Expo SDK: 54+
- TypeScript: yes
- Routing: Expo Router
- Styling: NativeWind v4
- Backend: Supabase (Auth + Postgres + RLS)
- Subscriptions: RevenueCat

## Verification commands (must pass)
- Install: ...
- Lint: ...
- Typecheck: ...
- Tests: ...
- Build: ...
"""

    glossary = """# 00-glossary.md

## Decision Summary
- (auto-generated stub)

## Open Questions
- (fill in)

## Assumptions
- [ASSUMPTION-A1] ...

## Risks & Mitigations
- [RISK] ...

## Domain terms
- **EntityName:** definition
"""

    Path("00-project-brief.md").write_text(brief, encoding="utf-8")
    Path("00-decisions.md").write_text(decisions, encoding="utf-8")
    Path("00-glossary.md").write_text(glossary, encoding="utf-8")
    print("Generated: 00-project-brief.md, 00-decisions.md, 00-glossary.md")


if __name__ == "__main__":
    main()
