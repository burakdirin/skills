# 00-decisions.md (Source of Truth)

## Decision Summary

- Expo Router with tabs + stacks; route names kebab-case.
- NativeWind v4 with a fixed spacing/typography scale.
- Supabase Auth (email + Apple sign-in), Postgres + RLS.
- RevenueCat entitlements: `pro`.

## Open Questions

- Whether to add offline cache for history thumbnails.
- Exact fal.ai model to use for the first 4 styles.

## Assumptions

- [ASSUMPTION-A1] Use email auth for MVP; add Apple Sign In as a secondary option.
- [ASSUMPTION-A2] NativeWind v4 is stable enough for production use in this scope.

## Risks & Mitigations

- [RISK] Expo SDK version changes. Mitigation: pin exact versions in package.json once scaffolded.
- [RISK] Supabase RLS misconfiguration. Mitigation: Add automated tests for RLS policies.

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
- surface: #18181B

### Typography scale

- xs: 12px (line-height: 16px)
- sm: 14px (line-height: 20px)
- base: 16px (line-height: 24px)
- lg: 18px (line-height: 28px)
- xl: 20px (line-height: 28px)
- 2xl: 24px (line-height: 32px)

### Spacing scale

- 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64

## Navigation model (Expo Router)

- Root groups: (auth), (tabs)
- Tabs: Home, Create, History, Settings
- Paywall: stack screen modal accessible from any tab
- Results: stack screen from Create or History

## State & data access

- Supabase client location: `src/lib/supabase.ts`
- Auth session handling: `src/context/auth.tsx` (React Context)
- Data fetching strategy: TanStack Query (React Query) v5

## Verification commands (must pass)

- Install: `pnpm i`
- Lint: `pnpm lint`
- Typecheck: `pnpm typecheck`
- Tests: `pnpm test`
- Build: `eas build --platform ios --profile preview`

## Definition of Done (MVP task-level)

- [ ] Lint + typecheck + tests + build are green
- [ ] Loading/empty/error states implemented for new screens
- [ ] No TODOs without tracking issue link
- [ ] No new deps without explicit approval
- [ ] Accessibility: Tap targets >= 44x44, contrast ratio >= 4.5:1
