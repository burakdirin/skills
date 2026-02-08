# 04-tech-architecture.md

## Decision Summary

- Example stub only. Replace with a real architecture derived from 00-\* + PRD + UI/UX spec.
- Keep choices minimal for solo dev.

## Open Questions

- Which analytics provider will we use in MVP (or is it OUT)?

## Assumptions

- [ASSUMPTION-A1] Use Supabase email auth for MVP.

## Risks & Mitigations

- [RISK] Dependency version drift. Mitigation: enforce `npx expo install --check` in CI.

## 3) Dependency Plan (packages)

| Package (npm) | Why     | Risk | Alternatives | Version       |
| ------------- | ------- | ---- | ------------ | ------------- |
| expo          | core    | low  | -            | [PENDING_PIN] |
| expo-router   | routing | low  | manual nav   | [PENDING_PIN] |

## 6) Data Model (Supabase) — Conceptual

- generations (user-owned)
  - RLS: user can read/write only their own rows

## 12) Deployment & CI/CD

- EAS Build: preview + production profiles
- EAS Submit for store uploads

## 14) Appendix — File/Folder Tree (complete)

- app/
- src/
