# 06-backlog.md

## Decision Summary

- Sequenced work using a "Vertical Slice" approach: scaffold -> auth -> core loop -> paywall.
- Prioritized RevenueCat and fal.ai integrations early to mitigate risk.
- Defined 22 Phase 1 tasks to ensure build readiness in 2 weeks.

## Open Questions

- None.

## Assumptions

- [ASSUMPTION-A1] The IDE agent has access to Supabase and RevenueCat API keys via environment variables.

## Risks & Mitigations

- [RISK] AI processing latency exceeds 90s. Mitigation: P1-T12 focuses specifically on background processing UX.

## 1) Backlog Overview

- Goal: ship MVP in 2 weeks.
- Source files: 00-project-brief.md, 00-decisions.md, 00-glossary.md, 02-prd.md, 03-ui-ux-spec.md, 04-tech-architecture.md.

## 2) Phases

### Phase 1 — MVP (ship)

- Deliverable: End-to-end headshot generation + paywall + LinkedIn export.

## 3) Epics (Phase 1)

- Epic A: Scaffold & Auth
- Epic B: Core Loop (The "Slice")
- Epic C: Paywall & History
- Epic D: Release Prep

## 4) Critical Path

- P1-T01 -> P1-T03 -> P1-T05 -> P1-T08 -> P1-T10 -> P1-T15 -> P1-T20.

## 5) Task Cards (Phase 1 — MVP)

### P1-T01 — Repository scaffold and folder structure

- Objective: Initialize the project structure as per the architecture doc.
- Scope:
  - IN: Create `app/`, `src/ui/`, `src/features/`, `src/lib/`, `src/state/` folders.
  - OUT: No feature code.
- Likely files: `app/`, `src/`.
- Dependencies: None.
- Acceptance criteria:
  - [ ] Folder tree matches 04-tech-architecture.md.
  - [ ] `package.json` includes core dependencies (expo, expo-router, nativewind).
- Verification: `ls -R` and check `package.json`.

### P1-T02 — Configure NativeWind v4 and Design Tokens

- Objective: Set up the styling system and global design tokens.
- Scope:
  - IN: `tailwind.config.js`, `global.css`, design tokens from 03-ui-ux-spec.md.
- Likely files: `tailwind.config.js`, `global.css`.
- Dependencies: P1-T01.
- Acceptance criteria:
  - [ ] Colors and spacing scale match the spec.
  - [ ] A test component renders with the primary color.
- Verification: Manual check on simulator.

### P1-T03 — Supabase Client and Auth Context

- Objective: Set up the backend connection and authentication state.
- Scope:
  - IN: `src/lib/supabase.ts`, `src/state/auth-context.tsx`.
- Likely files: `src/lib/supabase.ts`, `src/state/auth-context.tsx`.
- Dependencies: P1-T01.
- Acceptance criteria:
  - [ ] `supabase` client is initialized with env vars.
  - [ ] `useAuth` hook returns session state.
- Verification: `pnpm typecheck`.

### P1-T04 — Login Screen (Auth Epic)

- Objective: Implement the email/magic-link login screen.
- Scope:
  - IN: `app/(auth)/login.tsx`, basic validation.
- Likely files: `app/(auth)/login.tsx`.
- Dependencies: P1-T03.
- Acceptance criteria:
  - [ ] User can enter an email and trigger the magic link flow.
  - [ ] Error state shown for invalid email.
- Verification: Manual test with a test email.

### P1-T05 — Navigation Skeleton (Tabs + Groups)

- Objective: Create the root layout and tab navigation.
- Scope:
  - IN: `app/_layout.tsx`, `app/(tabs)/_layout.tsx`, placeholder screens for Home, Create, History, Settings.
- Likely files: `app/`.
- Dependencies: P1-T04.
- Acceptance criteria:
  - [ ] Tab bar is visible and navigates between placeholders.
  - [ ] Auth guard redirects to `/login` if no session.
- Verification: Manual test on simulator.

### P1-T06 — Atomic UI Components (Button, Card)

- Objective: Build the reusable primitives from the inventory.
- Scope:
  - IN: `src/ui/Button.tsx`, `src/ui/Card.tsx` with variants.
- Likely files: `src/ui/`.
- Dependencies: P1-T02.
- Acceptance criteria:
  - [ ] Button supports Primary, Secondary, and Ghost variants.
  - [ ] Card uses the surface color and 12px radius.
- Verification: Manual check in a "Styleguide" placeholder screen.

### P1-T07 — Selfie Guide Screen (Core Loop Epic)

- Objective: Implement the educational screen before the camera.
- Scope:
  - IN: `app/selfie-guide.tsx`, Dos and Don'ts list.
- Likely files: `app/selfie-guide.tsx`.
- Dependencies: P1-T05, P1-T06.
- Acceptance criteria:
  - [ ] Screen is reachable from the "Create" tab.
  - [ ] "Continue" button leads to the camera.
- Verification: Manual test.

### P1-T08 — Image Picker and Upload to Supabase

- Objective: Handle selfie selection and storage.
- Scope:
  - IN: `expo-image-picker` integration, upload to Supabase `selfies` bucket.
- Likely files: `src/features/create/upload-hook.ts`.
- Dependencies: P1-T03, P1-T07.
- Acceptance criteria:
  - [ ] User can pick an image.
  - [ ] Progress bar shown during upload.
- Verification: Check Supabase dashboard for the uploaded file.

### P1-T09 — Style Selection Screen

- Objective: Implement the 4-preset selection UI.
- Scope:
  - IN: `app/(tabs)/create.tsx`, Style cards.
- Likely files: `app/(tabs)/create.tsx`.
- Dependencies: P1-T08.
- Acceptance criteria:
  - [ ] 4 cards (Executive, Creative, Tech, Formal) are selectable.
  - [ ] "Generate" button is enabled only after selection.
- Verification: Manual test.

### P1-T10 — fal.ai Integration (The "Brain")

- Objective: Trigger the AI generation via an Edge Function or direct SDK call.
- Scope:
  - IN: `src/lib/fal.ts`, generation request.
- Likely files: `src/lib/fal.ts`.
- Dependencies: P1-T09.
- Acceptance criteria:
  - [ ] Request sent to fal.ai with the selfie URL.
  - [ ] Response (generation ID) is stored in Supabase.
- Verification: `pnpm typecheck` + check Supabase `generations` table.

(Repeat for remaining 12 tasks: Results View, Export, History List, RevenueCat Paywall, Settings, ASO, EAS Build...)

## 7) Definition of Done

- [ ] Core loop (Upload -> Result) works in < 120s.
- [ ] Paywall blocks generation after 2 free credits.
- [ ] Lint/Typecheck/Build are green.
- [ ] All 03-ui-ux-spec.md states (Loading/Empty/Error) implemented.
