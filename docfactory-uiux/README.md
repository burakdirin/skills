# DocFactory UI/UX — Agent Skill (docfactory-uiux)

Drafts `03-ui-ux-spec.md` (IA, route map, screen list, design tokens, component inventory, accessibility) from the Source-of-Truth docs and PRD.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-uiux/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`
- `docfactory-prd` → `02-prd.md`

Optional:

- `docfactory-market` → `01-market-research.md`

## Output

- `03-ui-ux-spec.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/` — UI/UX spec templates
- `references/` — checklists (accessibility, IA/routing, screen spec, component inventory)
- `scripts/validate_docfactory_uiux.py` — validator (optional)
- `examples/` — example idea + example outputs

## Notes

- Does **not** generate code. This is a design/spec artifact.
- Aligns with iOS platform conventions and content-first design principles.
