# 00-decisions.md — Template (Source of Truth)

## Decision Summary

<!-- Summary of the technical and design system decisions made here. -->

- (fill in)

## Open Questions

<!-- List any technical or design questions that remain unanswered. -->

- (fill in)

## Assumptions

<!-- Tag as [ASSUMPTION-A1], [ASSUMPTION-A2], etc. -->

- [ASSUMPTION-A1] ...

## Risks & Mitigations

<!-- Tag as [RISK] and provide a mitigation strategy. -->

- [RISK] ...

## Stack (locked for MVP)

<!-- Do not change these unless explicitly requested. -->

- Expo SDK: ...
- React Native: ...
- TypeScript: yes
- Routing: Expo Router (file-based)
- Styling: NativeWind v4
- Backend: Supabase (Auth + Postgres + RLS)
- Subscriptions: RevenueCat

## UI Design Tokens (locked)

<!-- Use concrete hex codes and numeric scales. No "clean" or "modern" placeholders. -->

### Colors (hex)

- background: ...
- text: ...
- primary: ...
- secondary: ...
- destructive: ...
- border: ...

### Typography scale

- xs / sm / base / lg / xl / 2xl

### Spacing scale

- 4 / 8 / 12 / 16 / 24 / 32

## Navigation model (Expo Router)

- Root: (tabs) + (stack)
- Naming conventions:
  - routes use kebab-case
  - groups in parentheses: (tabs), (auth)

## State & data access

- Supabase client location: ...
- Auth session handling: ...
- Data fetching strategy: ...

## Verification commands (must pass)

- Install: ...
- Lint: ...
- Typecheck: ...
- Tests: ...
- Build: ...

## Definition of Done (MVP task-level)

- [ ] Lint + typecheck + tests + build are green
- [ ] Loading/empty/error states implemented for new screens
- [ ] No TODOs without tracking issue link
- [ ] No new deps without explicit approval
