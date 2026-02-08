# 00-project-brief.md

## Decision Summary

- Build a micro-app focused on fast headshot generation for job seekers.
- MVP is a single vertical slice: upload -> generate -> select -> export, with history.
- Monetization is subscription-first with limited free credits.

## Open Questions

- What is the initial free allowance (credits per day/week)?
- Which AI provider is primary (fal.ai vs Replicate) for first iteration?

## Assumptions

- [ASSUMPTION-A1] We will start with 4 preset “styles” rather than a free-form prompt.

## Risks & Mitigations

- [RISK] AI provider latency may harm UX. Mitigation: background processing + clear progress UI + retry.

## Product snapshot

- **Product name:** Headshot Studio
- **Target user:** Job seekers needing professional headshots quickly
- **Core loop (1 sentence):** Upload selfie → generate 4 headshots → pick → export
- **Monetization:** Freemium + subscription
- **Differentiator:** Fastest results + iOS-native UX
- **Target markets:** US/UK/DE/FR
- **Platforms:** iOS + Android

## MVP scope

### IN (Must-have)

- Onboarding (permission + expectations)
- Create flow (upload → generate → results)
- History (previous generations, re-download)
- Paywall (subscribe, restore purchases)
- Settings (legal, account, help)

### OUT (Explicit non-goals)

- Social feed / sharing network
- Messaging
- Marketplace or creator economy features

## Success criteria (MVP)

- Users can complete the loop end-to-end without manual intervention
- Crash-free sessions and predictable loading/error states for all screens
