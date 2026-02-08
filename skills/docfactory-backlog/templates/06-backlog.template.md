# 06-backlog.md

## Decision Summary

<!-- One sentence summary of the build plan and sequencing strategy. -->

- ...

## Open Questions

<!-- List any execution-level questions that remain (e.g., exact CI provider). -->

- ...

## Assumptions

<!-- Tag as [ASSUMPTION-A1], [ASSUMPTION-A2], etc. -->

- [ASSUMPTION-A1] ...

## Risks & Mitigations

<!-- Tag as [RISK] (e.g., [RISK] Third-party SDK integration takes longer than expected). -->

- [RISK] ...

## 1) Backlog Overview

- Goal: ship MVP in 2–4 weeks (solo dev)
- Source of truth files used:
  - 00-project-brief.md
  - 00-decisions.md
  - 00-glossary.md
  - 02-prd.md
  - 03-ui-ux-spec.md
  - 04-tech-architecture.md (Expo Stack)

## 2) Phases

### Phase 1 — MVP (ship)

- Deliverable: end-to-end core loop + paywall + release-ready build.

### Phase 2 — Post-MVP (polish)

- Deliverable: improvements driven by early feedback.

## 3) Epics (Phase 1)

- Epic A: Project scaffold & conventions
- Epic B: Navigation & route skeletons
- Epic C: Auth & onboarding
- Epic D: Core loop vertical slice
- Epic E: History
- Epic F: Paywall & subscription
- Epic G: Analytics & instrumentation
- Epic H: Release pipeline (EAS/CI)

## 4) Critical Path

<!-- List the minimum chain required to ship (task IDs). -->

- P1-T01 → P1-T02 → ...

## 5) Task Cards (Phase 1 — MVP)

<!-- Each task is 30–90 minutes. Use stable IDs: P1-T01, P1-T02, ... -->
<!-- At least 20 tasks required for Phase 1. -->

### P1-T01 — <Title>

- Objective: <!-- 1 sentence. -->
- Scope:
  - IN:
  - OUT:
- Likely files/areas:
- Dependencies:
- Acceptance criteria:
  - [ ] ...
- Verification:
  - `...` (commands) or manual checks.

## 6) Task Cards (Phase 2 — Post-MVP)

<!-- At least 5 tasks. -->

## 7) Definition of Done

<!-- Tailor to this project. -->

- MVP DoD:
  - [ ] ...

## 8) Notes for IDE Agents

- Preferred execution order: critical path first.
- Always preserve naming from glossary.
- Do not add dependencies without justification.
