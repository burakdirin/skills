# DocFactory PRD — Agent Skill (docfactory-prd)

Drafts `02-prd.md` (vision, personas, JTBD, MVP scope, user stories, monetization, metrics, ASO) using the project's Source-of-Truth files and market memo.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-prd/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`
- `docfactory-market` → `01-market-research.md`

## Output

- `02-prd.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/02-prd.template.md` — PRD template
- `references/` — checklists and story formats
- `scripts/validate_docfactory_prd.py` — validator (optional)
- `examples/` — example idea + example PRD stub

## Notes

- Does **not** generate code or technical architecture.
- Focuses on scope discipline for a solo indie dev (2–4 weeks MVP).
