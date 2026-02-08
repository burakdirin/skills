# 04-tech-architecture.md

## Decision Summary

- Use a managed stack (Supabase + RevenueCat) to minimize solo-dev maintenance.
- Navigation: Expo Router with `(auth)` and `(tabs)` groups.
- Data Layer: TanStack Query for caching and Supabase for persistence.

## Open Questions

- Exact fal.ai model for the first 4 styles (Decision: `fal-ai/flux-lora` with custom LoRAs).

## Assumptions

- [ASSUMPTION-A1] Users will always have a stable internet connection for AI processing.
- [ASSUMPTION-A2] SecureStore is sufficient for Supabase session persistence on iOS.

## Risks & Mitigations

- [RISK] AI provider latency (>30s). Mitigation: Use background processing + local notifications to alert user when results are ready.
- [RISK] Supabase RLS bypass. Mitigation: Enforce RLS on all tables and add automated policy tests.

## 1) System Overview

- High-level diagram (text):
  - **UI**: React Native (Expo) + NativeWind v4.
  - **Navigation**: Expo Router (File-based).
  - **State**: TanStack Query v5 + React Context (Auth).
  - **Backend**: Supabase (Auth, Postgres, RLS).
  - **Integrations**: RevenueCat (IAP), fal.ai (AI).

## 2) Stack Decisions (with reasons)

- **Decision**: Expo Router.
  - **Rationale**: Best-in-class file-based routing for React Native; handles deep linking and modals out of the box.
  - **Alternatives Rejected**: `react-navigation` (too much boilerplate).
  - **Risks**: Newer API, some edge cases with complex nested layouts.
- **Decision**: TanStack Query.
  - **Rationale**: Handles caching, retries, and loading states automatically.
  - **Alternatives Rejected**: `useEffect` + `useState` (manual state management is error-prone).
  - **Risks**: Learning curve for complex cache invalidation.

## 3) Dependency Plan (packages)

| Package (npm)                       | Why     | Risk                  | Alternatives            | Version       |
| ----------------------------------- | ------- | --------------------- | ----------------------- | ------------- |
| expo                                | core    | low                   | -                       | [PENDING_PIN] |
| expo-router                         | routing | low                   | react-navigation manual | [PENDING_PIN] |
| nativewind                          | styling | medium (config drift) | styled-components       | [PENDING_PIN] |
| @supabase/supabase-js               | backend | low                   | firebase                | [PENDING_PIN] |
| react-native-purchases (RevenueCat) | IAP     | medium                | StoreKit direct         | [PENDING_PIN] |
| @tanstack/react-query               | state   | low                   | SWR                     | [PENDING_PIN] |

## 4) App Architecture (layers)

- `app/`: Navigation routes only.
- `src/ui/`: Atomic components (Button, Card, Input).
- `src/features/`: Feature modules (e.g., `create/`, `history/`).
- `src/lib/`: SDK wrappers (`supabase.ts`, `revenuecat.ts`, `fal.ts`).
- `src/state/`: Query hooks and Auth context.
- `src/types/`: Shared TS interfaces.

## 6) Data Model (Supabase) — Conceptual

### Entities & relationships

- **profiles**: `id` (PK, auth.uid), `email`, `credits` (int), `is_pro` (bool).
- **generations**: `id` (PK), `user_id` (FK -> profiles.id), `style_id` (string), `status` (pending/success/failed).
- **images**: `id` (PK), `generation_id` (FK -> generations.id), `url` (string).

### RLS policy intent (per table)

- **profiles**: `SELECT/UPDATE` where `auth.uid() = id`.
- **generations**: `SELECT/INSERT` where `auth.uid() = user_id`.
- **images**: `SELECT` where `auth.uid() = (SELECT user_id FROM generations WHERE id = generation_id)`.

## 8) Integrations

### RevenueCat

- **Entitlement name**: `pro`.
- **Paywall triggers**: When `credits <= 0` in the Create flow.
- **Restore behavior**: Silent restore on app launch; manual button in Settings.

### AI provider boundary

- **Provider**: fal.ai.
- **Boundary location**: `src/lib/fal.ts`.
- **Error handling**: Normalize fal.ai errors into `API_ERROR` (from Error Taxonomy).

## 10) Error Handling & Observability

- **Error normalization**: Use a central `handleError(error)` utility in `src/lib/errors.ts`.
- **User-facing errors**: Use `react-native-toast-message` for non-blocking errors; full-screen fallback for `RUNTIME_ERROR`.

## 14) Appendix — File/Folder Tree (complete)

- app/
  - \_layout.tsx
  - (auth)/
    - login.tsx
  - (tabs)/
    - \_layout.tsx
    - home.tsx
    - create.tsx
    - history.tsx
    - settings.tsx
  - paywall.tsx
  - results/[id].tsx
- src/
  - ui/
  - features/
  - lib/
  - state/
  - types/
