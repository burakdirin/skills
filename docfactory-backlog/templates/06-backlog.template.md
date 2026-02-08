# 06-backlog.md

## Decision Summary
- ...

## Open Questions
- ...

## Assumptions
- [ASSUMPTION-A1] ...

## Risks & Mitigations
- [RISK] ...

## 1) Backlog Overview
- Goal: ship MVP in 2–4 weeks (solo dev)
- Source of truth files used:
  - 00-project-brief.md
  - 00-decisions.md
  - 00-glossary.md
  - 02-prd.md
  - 03-ui-ux-spec.md
  - 04-tech-architecture.md

## 2) Phases
### Phase 1 — MVP (ship)
- Deliverable: end-to-end core loop + paywall + basic analytics + release-ready build

### Phase 2 — Post-MVP (polish & retention)
- Deliverable: improvements driven by early feedback

### Phase 3 — Growth (optional)
- Deliverable: ASO iterations + experiments

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
List the minimum chain required to ship (task IDs):
- P1-T01 → P1-T02 → ...

## 5) Task Cards (Phase 1 — MVP)
> Each task is 30–90 minutes. Use stable IDs: P1-T01, P1-T02, ...

### P1-T01 — <Title>
- Objective:
- Scope:
  - IN:
  - OUT:
- Likely files/areas:
  - ...
- Dependencies:
  - (none)
- Acceptance criteria:
  - [ ] ...
  - [ ] ...
- Verification:
  - `...` (commands) + manual checks

(Repeat; at least 20 tasks)

## 6) Task Cards (Phase 2 — Post-MVP)
> At least 5 tasks.

### P2-T01 — <Title>
- ...

## 7) Definition of Done
Use `references/dod-checklist.md` and tailor it to this project:
- MVP DoD:
  - [ ] ...
- Release candidate DoD:
  - [ ] ...

## 8) Notes for IDE Agents
- Preferred execution order: critical path first
- Always preserve naming from glossary
- Do not add dependencies without justification
