---
name: docfactory-init
description: Creates the Source-of-Truth docs for a new mobile app idea (00-project-brief.md, 00-decisions.md, 00-glossary.md) from a short Idea Capsule. Use at the start of every new idea, before PRD/UX/architecture. Do not do market research, TAM/SAM/SOM, or generate code.
---

# DocFactory Init (Source-of-Truth Pack)

This skill produces a **consistent starting point** for a new product so downstream agents (PRD, UX, Tech, Backlog, Prompt Packs) do not drift.

## When to use

Use this skill when the user says something like:

- "I have an app idea, create the initial docs / brief / decisions"
- "Start a new idea and produce the 00-\* files"
- "Initialize the project context pack"

Do **not** use this skill when:

- The user asks for market research, competitor analysis, or TAM/SAM/SOM
- The user asks to code the app / generate repo files (that is BuildFactory)

## Inputs (Idea Capsule)

Ask for missing required fields if they are not provided.

Required fields:

- `name`
- `target_user`
- `core_loop` (one sentence)
- `monetization`
- `differentiator`

Optional fields:

- `must_include`, `must_not_include`
- `target_markets`, `platforms`
- `stack_overrides`

Reference: `references/idea-capsule.template.yaml`

## Outputs (exact files)

Produce **exactly** these files:

1. `00-project-brief.md` (≤ 1 page)
2. `00-decisions.md` (Source of Truth)
3. `00-glossary.md`

Each output file MUST start with these sections in this order:

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag assumptions as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag risks as `[RISK]`)

Templates:

- `templates/00-project-brief.template.md`
- `templates/00-decisions.template.md`
- `templates/00-glossary.template.md`

Examples:

- `examples/idea.example.yaml`
- `examples/output/*`

## Hard rules

- Language: English.
- Never invent market numbers (TAM/SAM/SOM, downloads, revenue, MAU/DAU, etc.). If unknown: write `[NO_DATA]`.
- Keep MVP scope tiny: solo dev, 2–4 weeks to a shippable vertical slice.
- Decisions must be **concrete and executable** (no “modern UI” without tokens or rules).
- Maintain internal consistency across the three files (same naming, same screens, same terminology).

## Procedure

1. Parse the Idea Capsule. If required fields are missing, ask only for what is required.
2. Draft `00-decisions.md` first to lock:
   - UI tokens (colors/typography/spacing)
   - Navigation model (Expo Router)
   - Data & auth approach (Supabase)
   - Verification commands (lint/typecheck/test/build placeholders)
   - Definition of Done
3. Draft `00-project-brief.md` as the one-page snapshot:
   - Problem, target user, core loop, monetization
   - MVP IN/OUT lists
   - Success criteria
4. Draft `00-glossary.md`:
   - Domain terms
   - Screen names (MVP)
   - Analytics event naming convention
5. If file-write tools are available: write the files to disk with the exact names.
   Otherwise: output all three files in the chat using clear delimiters:
   - `---FILE: 00-project-brief.md---`
   - `---FILE: 00-decisions.md---`
   - `---FILE: 00-glossary.md---`
6. Optional validation: run `scripts/validate_docfactory_init.py` and fix issues.

## Stop & ask conditions

Stop and ask the user if:

- The Idea Capsule is missing required fields
- The user requests market sizing / competitor stats (out of scope for init)
- The user wants coding output (out of scope for init)
