# DocFactory Init — Agent Skill (docfactory-init)

Creates the three Source-of-Truth docs (`00-project-brief.md`, `00-decisions.md`, `00-glossary.md`) for a brand-new mobile app idea from a short Idea Capsule.

## Install

This skill follows the [Agent Skills](https://agentskills.io) format.
Copy the `docfactory-init/` directory into your agent's configured skills directory.

## Output

- `00-project-brief.md`
- `00-decisions.md`
- `00-glossary.md`

## Included Files

- `SKILL.md` — skill instructions
- `templates/` — output templates for each doc
- `references/idea-capsule.template.yaml` — input format reference
- `scripts/validate_docfactory_init.py` — structure validator (optional)
- `scripts/generate_docfactory_init.py` — local stub generator (requires PyYAML)
- `examples/` — example idea + example outputs

## Notes

- This is the first skill in the DocFactory pipeline — no prerequisites.
- Does **not** do market sizing, competitor research, or coding.
- Avoids invented numbers; uses `[NO_DATA]` where data isn't available.
