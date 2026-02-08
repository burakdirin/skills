---
name: docfactory-audit
description: Creates 09-consistency-audit.md by checking consistency across DocFactory outputs (00-*, 01, 02, 03, 04, 06). Report conflicts, missing details, and propose patches to source docs. Use after docfactory-backlog. No coding.
---

# DocFactory Consistency Audit (09-consistency-audit.md)

This skill audits the DocFactory documents for internal consistency and build readiness.
It outputs a single audit report with **actionable fixes** (patch proposals) to reduce drift before implementation.

## Prerequisites (required context)

Required files (must exist):

- `00-project-brief.md`
- `00-decisions.md`
- `00-glossary.md`
- `02-prd.md`
- `03-ui-ux-spec.md`
- `04-tech-architecture.md`
- `06-backlog.md`

Optional inputs (use if present):

- `01-market-research.md`

If any required file is missing, STOP and tell the user which file is missing and which skill to run first.

## Output (exact file)

Produce exactly one file:

- `09-consistency-audit.md`

### Required top sections (in this order)

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag as `[RISK]`)

## Hard rules

- Language: English.
- Do NOT generate code. This is a review artifact.
- Do NOT invent market numbers. If the docs contain invented numbers, flag them as a finding.
- Prefer objective checks: name matches, screen lists match, route map matches, entitlement names match, etc.
- Source of truth precedence:
  1. `00-decisions.md` (tokens, navigation conventions, stack constraints)
  2. `00-project-brief.md` (MVP IN/OUT and product snapshot)
  3. `00-glossary.md` (screen names, domain terms, analytics naming)
  4. `02-prd.md` (requirements and scope)
  5. `03-ui-ux-spec.md` (UI details consistent with PRD)
  6. `04-tech-architecture.md` (technical decisions consistent with above)
  7. `06-backlog.md` (execution plan derived from above)

## Severity rubric

Use these labels:

- **BLOCKER**: prevents MVP build or causes major rework
- **HIGH**: likely to cause drift or major bugs
- **MEDIUM**: causes friction, inconsistent UX, or rework later
- **LOW**: polish / clarity

## Audit checklist (minimum)

Use the checklist in `references/consistency-checklist.md`. At minimum check:

1. Identity & positioning

- Product name, target user, core loop, monetization, differentiator match across docs.

2. MVP scope consistency

- Brief IN/OUT vs PRD MUST/SHOULD/NICE vs Backlog Phase 1 tasks.
- No extra features introduced in UI/UX or Arch.

3. Screen & route consistency

- Glossary screen names vs PRD flows vs UI/UX screen list.
- UI/UX Expo Router route map matches Arch folder tree (app/ routes).
- Paywall access points consistent with PRD monetization triggers.

4. Design tokens & UI primitives

- Tokens are concrete (hex, scale) and consistent.
- Component inventory covers screens; avoid one-off components.
- State matrix covers every MVP screen (loading/empty/error).

5. Data model & security alignment

- Arch conceptual entities match PRD stories and UI screens.
- RLS intent is specified for user-owned tables.
- Auth/route protection aligns with UI/UX route groups.

6. Integrations alignment

- RevenueCat entitlement names and paywall behavior consistent across PRD/UI/UX/Arch.
- Analytics event naming consistent with glossary; events appear in PRD/UI spec.
- Push notifications only if PRD includes it; otherwise explicitly OUT.

7. Backlog executability

- Tasks are 30–90 minutes, have acceptance criteria and verification.
- Critical path exists and maps to a shippable vertical slice.

## Output requirements (what 09-consistency-audit.md must contain)

Use `templates/09-consistency-audit.template.md`. Include:

- A table of findings (ID, severity, summary, impacted docs)
- A “Proposed Patches” section grouped by file, with concise edits (bullets or small diff-like blocks)
- A “Next Actions” section that orders fixes from highest leverage to lowest

## Optional: structure validator

After producing the file, optionally run:

- `python scripts/validate_docfactory_audit.py`

## Stop & ask conditions

Stop and ask the user if:

- The docs disagree on MVP scope and there’s no clear precedence
- Screen list or route map is missing so you can’t audit navigation consistency
- The user expects you to also fix the source docs in-place (tooling-dependent)
