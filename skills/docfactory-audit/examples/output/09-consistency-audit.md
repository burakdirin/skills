# 09-consistency-audit.md

## Decision Summary

- Audit complete for "Headshot Studio".
- Identified 2 BLOCKER findings regarding missing route protection and undefined entitlement names.
- Readiness Score: **🔴 BLOCKED** until patches are applied.

## Open Questions

- None.

## Assumptions

- [ASSUMPTION-A1] The Source of Truth for all naming is 00-glossary.md.

## Risks & Mitigations

- [RISK] High risk of unauthorized API access if RLS policies are not explicitly verified in the backlog. Mitigation: Added a new task P1-T21 for RLS verification.

## 1) Inputs & Document Inventory

- Found: All 7 required docs + 01-market-research.md.

## 2) Executive Summary

- **Readiness Score**: 🔴 BLOCKED.
- Ship blockers (count): 2.
- Highest-leverage fixes: Define entitlement name and add auth guard logic to the backlog.
- Overall score: The documentation is 90% complete, but the final 10% contains critical implementation gaps.

## 3) Findings Table

| ID    | Severity | Summary                                         | Impacted docs                      | Why it matters         | Recommended fix                                                      |
| ----- | -------- | ----------------------------------------------- | ---------------------------------- | ---------------------- | -------------------------------------------------------------------- |
| A-001 | BLOCKER  | RevenueCat entitlement name not defined         | 02-prd.md, 04-tech-architecture.md | Implementation blocked | Define entitlement `pro` in 00-decisions.md and reference everywhere |
| A-002 | BLOCKER  | Missing auth guard task in backlog              | 06-backlog.md                      | Security vulnerability | Add task P1-T05 for Auth Guard implementation                        |
| A-003 | HIGH     | PRD lists "Results" screen but UI spec does not | 02-prd.md, 03-ui-ux-spec.md        | Navigation drift       | Add Results screen spec to 03-ui-ux-spec.md                          |
| A-004 | MEDIUM   | Inconsistent spacing token (12px vs 16px)       | 00-decisions.md, 03-ui-ux-spec.md  | Visual inconsistency   | Align on 16px as the standard base spacing                           |
| A-005 | LOW      | Missing "Restore Purchases" in SelfieGuide      | 03-ui-ux-spec.md                   | UX friction            | Add restore button to SelfieGuide footer                             |

## 6) Proposed Patches (grouped by file)

### Patch: 00-decisions.md

- **Add to Stack section**: `Entitlement Name: pro`
- **Update Spacing scale**: Change `12 / 16 / 24` to `16 / 24 / 32` for consistency.

### Patch: 03-ui-ux-spec.md

- **Add Screen Spec**:

  ```markdown
  ### Screen: Results

  - Purpose: Show the 4 generated headshots.
  - Primary actions: "Save to Camera Roll".
  - States: Loading (blurred), Error (Alert).
  ```

### Patch: 06-backlog.md

- **Add Task**:

  ```markdown
  ### P1-T05 — Auth Guard and Route Protection

  - Objective: Protect (tabs) group from unauthenticated access.
  - Acceptance criteria: [ ] Redirects to /login if no session.
  ```

## 7) Next Actions (ordered)

1. Apply Patch A-001 (Entitlement Name) to 00-decisions.md.
2. Apply Patch A-002 (Auth Guard Task) to 06-backlog.md.
3. Align UI Spec screens with PRD (A-003).
