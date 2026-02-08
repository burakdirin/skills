# 04-tech-architecture.md

## Decision Summary

<!-- One sentence summary of the key technical architecture decisions. -->

- ...

## Open Questions

<!-- List any technical questions that remain unanswered (e.g., specific library choice). -->

- ...

## Assumptions

<!-- Tag as [ASSUMPTION-A1], [ASSUMPTION-A2], etc. -->

- [ASSUMPTION-A1] ...

## Risks & Mitigations

<!-- Tag as [RISK] (e.g., [RISK] AI provider latency). -->

- [RISK] ...

## 1) System Overview

<!-- High-level diagram or description of the system layers. -->

- High-level diagram (text):
  - UI (screens) → Data layer → Integrations
- Core principles:
  - ...

## 2) Stack Decisions (with reasons)

<!-- Use the ADR-Lite format: Decision, Rationale, Alternatives Rejected, Risks. -->

- Expo SDK: [PENDING_PIN] (pin after scaffold)
- Routing: Expo Router (file-based)
- Styling: NativeWind v4
- Backend: Supabase (Auth + Postgres + RLS)
- Subscriptions: RevenueCat
- AI providers: ...

## 3) Dependency Plan (packages)

<!-- Do not invent versions. Use [PENDING_PIN] and list the command to obtain exact versions. -->

| Package (npm)                       | Why     | Risk                  | Alternatives            | Version       |
| ----------------------------------- | ------- | --------------------- | ----------------------- | ------------- |
| expo                                | core    | low                   | -                       | [PENDING_PIN] |
| expo-router                         | routing | low                   | react-navigation manual | [PENDING_PIN] |
| nativewind                          | styling | medium (config drift) | styled-components       | [PENDING_PIN] |
| @supabase/supabase-js               | backend | low                   | firebase                | [PENDING_PIN] |
| react-native-purchases (RevenueCat) | IAP     | medium                | StoreKit direct         | [PENDING_PIN] |

## 4) App Architecture (layers)

<!-- Define the folder structure and responsibilities. -->

- `app/` (navigation only)
- `src/ui/` (reusable components)
- `src/features/` (feature-specific logic)
- `src/lib/` (third-party SDK wrappers)
- `src/state/` (data fetching and global state)
- `src/types/` (shared TypeScript types)

## 5) Navigation & Route Protection

<!-- How are routes organized and secured? -->

- Route groups: `(auth)`, `(tabs)` per UI/UX spec
- Auth guard strategy: <!-- e.g., Root layout check for session -->
- Modal screens:

## 6) Data Model (Supabase) — Conceptual

<!-- No SQL here. Define entities and RLS intent. -->

### Entities & relationships

- Entity A: <!-- e.g., profiles (id, email, credits) -->
- Entity B:

### RLS policy intent (per table)

- SELECT: <!-- e.g., auth.uid() = user_id -->
- INSERT:
- UPDATE:
- DELETE:

## 7) Auth (Supabase)

- Session storage: <!-- e.g., SecureStore via Supabase client -->
- Refresh strategy:
- Error states:

## 8) Integrations

### RevenueCat

- Entitlement name(s): <!-- e.g., pro -->
- Paywall triggers:
- Restore behavior:

### AI provider boundary (if applicable)

- Provider:
- Boundary location: <!-- e.g., src/lib/fal.ts -->
- Error handling:

## 9) State, Caching, Offline

- Strategy: <!-- e.g., TanStack Query -->
- Offline stance: <!-- e.g., Read-only history while offline -->

## 10) Error Handling & Observability

<!-- Use the Error Taxonomy reference. -->

- Error normalization:
- User-facing errors:

## 11) Performance Plan

- Budgets:
- Image optimization: <!-- e.g., expo-image -->

## 12) Deployment & CI/CD

- EAS Build profiles:
- CI triggers: <!-- e.g., GitHub Actions on PR -->

## 13) Testing Strategy (MVP)

- Unit: <!-- e.g., pure logic in src/features/ -->
- Smoke checklist:

## 14) Appendix — File/Folder Tree (complete)

<!-- Provide the full tree including app/ routes. -->

- app/
- src/
