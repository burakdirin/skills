# 04-tech-architecture.md

## Decision Summary

- ...

## Open Questions

- ...

## Assumptions

- [ASSUMPTION-A1] ...

## Risks & Mitigations

- [RISK] ...

## 1) System Overview

- High-level diagram (text):
  - UI (screens) → Data layer → Integrations
- Core principles:
  - ...

## 2) Stack Decisions (with reasons)

- Expo SDK: [PENDING_PIN] (pin after scaffold)
- Routing: Expo Router (file-based)
- Styling: NativeWind v4
- Backend: Supabase (Auth + Postgres + RLS)
- Subscriptions: RevenueCat
- Analytics: ...
- Push notifications: IN/OUT (per PRD)
- AI providers: ...

## 3) Dependency Plan (packages)

> Do not invent versions. Use [PENDING_PIN] and list the command to obtain exact versions.

| Package (npm)                       | Why     | Risk                  | Alternatives            | Version       |
| ----------------------------------- | ------- | --------------------- | ----------------------- | ------------- |
| expo                                | core    | low                   | -                       | [PENDING_PIN] |
| expo-router                         | routing | low                   | react-navigation manual | [PENDING_PIN] |
| nativewind                          | styling | medium (config drift) | styled-components       | [PENDING_PIN] |
| @supabase/supabase-js               | backend | low                   | firebase                | [PENDING_PIN] |
| react-native-purchases (RevenueCat) | IAP     | medium                | StoreKit direct         | [PENDING_PIN] |
| ...                                 | ...     | ...                   | ...                     | ...           |

## 4) App Architecture (layers)

- `app/` (navigation only)
- `src/ui/` (components)
- `src/features/` (feature modules)
- `src/lib/` (infra: supabase client, revenuecat wrapper, analytics)
- `src/state/` (query/cache or state)
- `src/types/` (shared types)

## 5) Navigation & Route Protection

- Route groups: `(auth)`, `(tabs)` per UI/UX spec
- Auth guard strategy:
- Modal screens (paywall, etc.):

## 6) Data Model (Supabase) — Conceptual

> No SQL here (SQL/migrations live in the DB skill).

### Entities & relationships

- Entity A:
- Entity B:

### RLS policy intent (per table)

For each table specify:

- SELECT:
- INSERT:
- UPDATE:
- DELETE:
- Notes: use `auth.uid()` where relevant.

### Indexing notes

- ...

## 7) Auth (Supabase)

- Session storage:
- Refresh strategy:
- Error states:
- Security notes:

## 8) Integrations

### RevenueCat

- Entitlement name(s):
- Paywall triggers (from PRD):
- Restore purchases behavior:
- Offline behavior:

### Analytics

- Event naming: from glossary
- Privacy considerations:
- Minimal event set (MVP):

### Push notifications (if applicable)

- Provider:
- Permission UX:
- Use-cases:

### AI provider boundary (if applicable)

- Provider:
- Request/response contracts:
- Rate limiting:
- Error handling:
- Cost controls:

## 9) State, Caching, Offline

- Strategy:
- Cache keys:
- Retry/backoff:
- Offline stance:

## 10) Error Handling & Observability

- Error normalization:
- User-facing errors:
- Logging strategy:
- Crash reporting: IN/OUT for MVP

## 11) Performance Plan

- Budgets:
- Images:
- Network:
- Rendering:

## 12) Deployment & CI/CD

- EAS Build profiles:
  - preview:
  - production:
- EAS Submit:
- CI triggers:
- Environment variables:
- Secrets handling:

## 13) Testing Strategy (MVP)

- Unit:
- Integration:
- Smoke checklist:

## 14) Appendix — File/Folder Tree (complete)

> Provide the full tree including `app/` routes.

- app/
  - \_layout.tsx
  - (auth)/
    - ...
  - (tabs)/
    - \_layout.tsx
    - home.tsx
    - create.tsx
    - history.tsx
    - settings.tsx
  - paywall.tsx
- src/
  - ui/
  - features/
  - lib/
  - state/
  - types/
- docs/
  - 00-\*.md
  - 01-\*.md
  - 02-\*.md
  - 03-\*.md
  - 04-\*.md
