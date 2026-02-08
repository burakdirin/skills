# DocFactory Backlog — Agent Skill (docfactory-backlog)

Produces `06-backlog.md`: a solo-friendly, agent-executable backlog broken into 30–90 minute tasks with acceptance criteria and verification commands.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-backlog/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`
- `docfactory-prd` → `02-prd.md`
- `docfactory-uiux` → `03-ui-ux-spec.md`
- `docfactory-arch-expo` → `04-tech-architecture.md`

Optional:

- `docfactory-market` → `01-market-research.md`

## Output

- `06-backlog.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/06-backlog.template.md` — backlog template
- `references/task-card-format.md` — task card format
- `references/estimation-rubric.md` — estimation rubric
- `references/dod-checklist.md` — definition of done checklist
- `scripts/validate_docfactory_backlog.py` — validator (optional)

## Notes

- Does **not** generate code. This is an execution plan artifact.
- Tasks are scoped for a solo indie dev (30–90 min each).
