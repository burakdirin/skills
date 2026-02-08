# Task Card Format (agent-friendly)

Each task should be small enough to finish in 30–90 minutes and should have explicit done signals.

Required fields:
- ID: P1-T01 style
- Title
- Objective (1 sentence)
- Scope (IN/OUT)
- Likely files/areas (paths)
- Dependencies (IDs)
- Acceptance criteria (checkboxes)
- Verification:
  - commands to run (if available)
  - manual checks (if not)

Good acceptance criteria examples:
- [ ] Screen renders with loading/empty/error states
- [ ] Route is reachable from the correct entry point
- [ ] Analytics event fires with correct name
- [ ] Errors show retry CTA and succeeds on retry
