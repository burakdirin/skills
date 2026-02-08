# 00-decisions.md (Source of Truth)

## Decision Summary

- Expo Router with tabs + stacks; route names kebab-case.
- NativeWind v4 with a fixed spacing/typography scale.
- Supabase Auth (email + Apple sign-in later), Postgres + RLS.
- RevenueCat entitlements: `pro`.

## Open Questions

- Whether to add offline cache for history thumbnails.

## Assumptions

- [ASSUMPTION-A1] Use email auth for MVP; add Apple Sign In in Phase 2.

## Risks & Mitigations

- [RISK] Expo SDK version changes. Mitigation: pin exact versions in package.json once scaffolded.

## Stack (locked for MVP)

- Expo SDK: 54+
- TypeScript: yes
- Routing: Expo Router
- Styling: NativeWind v4
- Backend: Supabase (Auth + Postgres + RLS)
- Subscriptions: RevenueCat

## UI Design Tokens (locked)

### Colors (hex)

- background: #0B0B0F
- text: #F4F4F5
- primary: #6D28D9
- secondary: #27272A
- destructive: #EF4444
- border: #3F3F46

### Typography scale

- xs=12, sm=14, base=16, lg=18, xl=20, 2xl=24

### Spacing scale

- 4, 8, 12, 16, 24, 32

## Navigation model (Expo Router)

- Root groups: (auth), (tabs)
- Tabs: Home, Create, History, Settings
- Paywall: stack screen modal from any tab

## Verification commands (must pass)

- Install: `pnpm i`
- Lint: `pnpm lint`
- Typecheck: `pnpm typecheck`
- Tests: `pnpm test`
- Build: `eas build --platform ios --profile preview` (or CI equivalent)
