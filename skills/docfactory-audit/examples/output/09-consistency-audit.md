# 09-consistency-audit.md

## Decision Summary

- Example stub only. Replace with a real audit derived from the docs.
- Primary outcome: list concrete conflicts + patches.

## Open Questions

- None

## Assumptions

- [ASSUMPTION-A1] Tokens in 00-decisions.md are placeholders and must be finalized.

## Risks & Mitigations

- [RISK] Scope creep between PRD and UI spec. Mitigation: enforce MVP screen list and remove extras.

## 3) Findings Table

| ID    | Severity | Summary                                           | Impacted docs                      | Why it matters              | Recommended fix                                                      |
| ----- | -------- | ------------------------------------------------- | ---------------------------------- | --------------------------- | -------------------------------------------------------------------- |
| A-001 | HIGH     | PRD lists a “Results” screen but UI spec does not | 02-prd.md, 03-ui-ux-spec.md        | Missing screen causes drift | Add Results screen spec and route                                    |
| A-002 | BLOCKER  | RevenueCat entitlement name not defined           | 02-prd.md, 04-tech-architecture.md | Implementation blocked      | Define entitlement `pro` in 00-decisions.md and reference everywhere |

## 6) Proposed Patches (grouped by file)

### Patch: 00-decisions.md

- Add explicit entitlement name: `pro`

### Patch: 03-ui-ux-spec.md

- Add “Results” screen with states + analytics events.

## 7) Next Actions (ordered)

1. Fix blockers: entitlement name, route map completeness
2. Align PRD screens with UI spec
