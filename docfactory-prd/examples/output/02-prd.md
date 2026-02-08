# 02-prd.md

## Decision Summary

- Example stub PRD. Replace with a real PRD derived from 00-\* and 01-market-research.md.
- Keep MVP scope tiny and measurable.

## Open Questions

- What is the free credit limit that still yields conversions?
- Which paywall trigger converts best (after first export vs after first generation)?

## Assumptions

- [ASSUMPTION-A1] MVP supports email auth only; Apple Sign-In is Phase 2.

## Risks & Mitigations

- [RISK] Pricing hypothesis is unvalidated. Mitigation: launch with A/Bable paywall copy and monitor conversion.

## 1) Vision & positioning

- One-sentence value proposition: Fast, professional headshots in minutes from a single selfie.
- Target wedge segment: job seekers needing a headshot in < 1 hour.

## 4) MVP scope (strict)

### MUST-HAVE

- Upload selfie + generate 4 results
- Export
- History
- Paywall + restore purchases
- Settings (legal + help)

### OUT

- Social feed
- Messaging

### MVP Definition of Done

- [ ] Core loop works end-to-end in a production build
- [ ] Paywall + restore purchases works
- [ ] Loading/empty/error states for all MVP screens

## 5) User stories (example)

### Epic: Core Loop

1. As a job seeker I want to upload a selfie so that I can generate headshots.
   - Acceptance criteria:
     - [ ] Camera roll permission requested gracefully
     - [ ] Upload shows progress and error state with retry
