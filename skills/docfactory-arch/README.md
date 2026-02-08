# DocFactory Arch — Agent Skill (docfactory-arch)

Drafts `04-tech-architecture.md` (stack decisions, data layer, integrations, folder tree, deployment, security) from the Source-of-Truth docs, PRD, and UI/UX spec.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-arch/` directory into your agent's configured skills directory.

## Prerequisites

Run these skills first:

- `docfactory-init` → `00-project-brief.md`, `00-decisions.md`, `00-glossary.md`
- `docfactory-prd` → `02-prd.md`
- `docfactory-uiux` → `03-ui-ux-spec.md`

Optional:

- `docfactory-market` → `01-market-research.md`

## Output

- `04-tech-architecture.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/04-tech-architecture.template.md` — architecture template
- `references/` — checklists (dependency pinning, deployment, Supabase RLS, RevenueCat, NativeWind, Expo Router)
- `scripts/validate_docfactory_arch.py` — validator (optional)
- `examples/` — example idea + example outputs

## Notes

- Does **not** generate code or migrations. This is a design/spec artifact.
- Prefers choices that reduce maintenance for a solo dev.
