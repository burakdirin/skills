---
name: docfactory-backlog
description: Creates 06-backlog.md as a solo-friendly build plan (30–90 min tasks) derived from 00-* docs + PRD + UI/UX + Architecture. Includes phases, epics, dependencies, acceptance criteria, and verification commands. Use after docfactory-arch or when the user asks for a backlog, task breakdown, or build plan. Do not generate code.
---

# DocFactory Backlog (06-backlog.md)

This skill produces a **buildable backlog** for a solo indie dev: small tasks that can be executed by an IDE agent with clear done signals.

## Prerequisites (required context)

This skill expects these files already exist:

- `00-project-brief.md`
- `00-decisions.md` (Source of Truth; tokens, navigation conventions, verification commands)
- `00-glossary.md` (screen names, domain terms, event naming)
- `02-prd.md` (stories, flows, monetization, MVP scope)
- `03-ui-ux-spec.md` (routes, screens, states, component inventory)
- `04-tech-architecture.md` (folder tree, data layer plan, integrations, deployment)

Optional but recommended:

- `01-market-research.md` (wedge, competitor gaps)

If any required file is missing, STOP and tell the user which file is missing and which skill to run first.

## Output (exact file)

Produce exactly one file:

- `06-backlog.md`

### Required top sections (in this order)

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag as `[RISK]`)

## Hard rules

- Language: English.
- Do NOT add features beyond PRD MVP scope.
- Tasks must be **30–90 minutes** of focused work for a solo dev.
- Every task must have:
  - Objective
  - Scope (what is IN / OUT)
  - Files/areas likely touched (paths)
  - Acceptance criteria as checkboxes
  - Verification steps (commands or manual checks)
  - Dependencies (task IDs)
- Use stable IDs: `P1-T01`, `P1-T02`, ... by phase.
- Keep implementation details minimal; backlog should guide execution, not contain code.

## What to include in 06-backlog.md

Use `templates/06-backlog.template.md`.

### Minimum requirements

1. **Phases**
   - Phase 1: MVP (ship vertical slice)
   - Phase 2: Post-MVP (polish/retention)
   - Phase 3: Growth/ASO/experiments (optional)

2. **Epics aligned to PRD flows**
   - Auth & onboarding
   - Core loop (create → results → export)
   - History
   - Paywall / subscription
   - Settings + legal
   - Analytics & instrumentation
   - Infra/CI/Release

3. **Dependency graph**
   - A short section listing critical path tasks (the minimum chain to ship)

4. **Task cards**
   - At least 20 tasks for Phase 1 (MVP)
   - At least 5 tasks for Phase 2 (optional)
   - Each task uses the Task Card format (see `references/task-card-format.md`)

5. **Definition of Done**
   - MVP DoD: lint/typecheck/tests/build and UX states implemented
   - Release checklist: EAS build profile, env vars set, basic smoke steps

## Procedure

1. Read `02-prd.md` and list MVP epics/stories; map each story to screens/routes from `03-ui-ux-spec.md`.
2. Use `04-tech-architecture.md` to identify infra tasks (folder tree, data layer, integrations, CI/CD).
3. Break work into 30–90 min tasks:
   - Prefer “vertical slice” sequencing: scaffold → auth → one end-to-end flow → paywall → polish.
4. For each task:
   - Keep scope narrow (single deliverable)
   - Add explicit acceptance criteria and verification
   - Attach dependencies and mark critical path tasks
5. Ensure naming consistency with `00-glossary.md` (screens, events, domain terms).
6. Output `06-backlog.md` as a single markdown file.

## Stop & ask conditions

Stop and ask the user if:

- Phase 1 MVP scope is unclear or conflicts across docs.
- The number of MVP screens/routes cannot be derived from UI/UX spec.
- Integration choices are ambiguous (analytics provider, AI provider, etc.).

## Additional Resources

- For the backlog template, see [templates/06-backlog.template.md](templates/06-backlog.template.md)
- For definition of done checklist, see [references/dod-checklist.md](references/dod-checklist.md)
- For estimation rubric, see [references/estimation-rubric.md](references/estimation-rubric.md)
- For task card format, see [references/task-card-format.md](references/task-card-format.md)
- For a complete example, see [examples/idea.example.yaml](examples/idea.example.yaml)
- For example output, see [examples/output/06-backlog.md](examples/output/06-backlog.md)
- For validation script, see [scripts/validate_docfactory_backlog.py](scripts/validate_docfactory_backlog.py)
