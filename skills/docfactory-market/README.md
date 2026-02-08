# DocFactory Market — Agent Skill (docfactory-market)

Drafts `01-market-research.md` using credible sources and citations, without inventing metrics.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-market/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`

## Output

- `01-market-research.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/01-market-research.template.md` — report template
- `references/` — checklists and query templates
- `scripts/validate_docfactory_market.py` — validator (optional)
- `examples/` — example idea + example outputs

## Notes

- Does **not** invent TAM/SAM/SOM or download estimates.
- Uses `[NO_DATA]` placeholders where verified data is unavailable.
