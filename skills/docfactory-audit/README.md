# DocFactory Audit — Agent Skill (docfactory-audit)

Produces `09-consistency-audit.md` by cross-checking all DocFactory outputs for internal consistency and proposing fixes to reduce drift before coding.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-audit/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`
- `docfactory-prd` → `02-prd.md`
- `docfactory-uiux` → `03-ui-ux-spec.md`
- `docfactory-arch` → `04-tech-architecture.md`
- `docfactory-backlog` → `06-backlog.md`

Optional:

- `docfactory-market` → `01-market-research.md`

## Output

- `09-consistency-audit.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/09-consistency-audit.template.md` — audit report template
- `references/consistency-checklist.md` — cross-doc check areas
- `references/severity-rubric.md` — BLOCKER/HIGH/MEDIUM/LOW definitions
- `references/patch-style-guide.md` — patch proposal format
- `scripts/validate_docfactory_audit.py` — validator (optional)

## Notes

- Does **not** generate code. This is a review artifact.
- This is the final skill in the DocFactory pipeline.
