# 03-ui-ux-spec.md

## Decision Summary

- Example stub only. Replace with a real spec derived from 00-\* and 02-prd.md.
- Keep routes and screens consistent with the PRD.

## Open Questions

- Which paywall trigger feels least disruptive in the core loop?

## Assumptions

- [ASSUMPTION-A1] MVP uses a tab layout with a modal paywall.

## Risks & Mitigations

- [RISK] Tokens in 00-decisions.md are placeholders. Mitigation: finalize tokens here and patch 00-decisions.md.

## 2) Information Architecture (IA)

- Tabs: Home, Create, History, Settings
- Paywall: modal accessible from Create and Settings

## 3) Expo Router Route Map (MVP)

- (tabs)/home
- (tabs)/create
- (tabs)/history
- (tabs)/settings
- paywall (modal)

## 5) Component Inventory (MVP)

- Button (primary/secondary/ghost/destructive)
- TextField (validation)
- Card
- EmptyState
- LoadingSkeleton

## 6) Screen Specifications (MVP only)

### Screen: Create

- Purpose: Upload a selfie and start generation.
- States: loading/empty/error
- Analytics: `screen.view`, `generation.start`

## 7) State Matrix

| Screen | Loading  | Empty        | Error        | Retry pattern     |
| ------ | -------- | ------------ | ------------ | ----------------- |
| Create | skeleton | empty prompt | inline error | primary retry CTA |

## 9) Accessibility (MVP baseline)

- Tap targets: avoid small icons for primary actions.
- VoiceOver labels for CTAs.

## 10) UI Consistency Rules (testable)

1. Primary CTA uses primary color and full-width on forms.
