# 06-backlog.md

## Decision Summary
- Example stub only. Replace with a real backlog derived from the docs.
- Keep tasks small and verifiable.

## Open Questions
- Which analytics provider is IN for MVP?

## Assumptions
- [ASSUMPTION-A1] MVP uses email auth only.

## Risks & Mitigations
- [RISK] Over-scoped MVP. Mitigation: keep Phase 1 limited to the core loop + paywall.

## 2) Phases
### Phase 1 — MVP (ship)
- Deliverable: end-to-end flow + paywall

## 3) Epics (Phase 1)
- Epic A: Scaffold
- Epic B: Navigation
- Epic C: Core loop

## 4) Critical Path
- P1-T01 → P1-T02 → P1-T03

## 5) Task Cards (Phase 1 — MVP)
### P1-T01 — Repository scaffold and conventions
- Objective: Create folders and baseline conventions as per architecture doc.
- Scope:
  - IN: create folder tree; add placeholder README; ensure routing directory is clean
  - OUT: no features
- Likely files/areas:
  - app/, src/, docs/
- Dependencies: (none)
- Acceptance criteria:
  - [ ] Folder tree matches architecture
  - [ ] No non-route code inside app/ (except layouts/pages)
- Verification:
  - Manual: open tree and confirm structure

### P1-T02 — Add route skeletons for MVP screens
- ...

(continue splitting until >=20 tasks)

## 7) Definition of Done
- [ ] Lint/typecheck/build green
