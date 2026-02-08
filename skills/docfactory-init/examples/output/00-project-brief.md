# 00-project-brief.md

## Decision Summary

- Build a micro-app focused on fast headshot generation for job seekers.
- MVP is a single vertical slice: upload -> generate -> select -> export, with history.
- Monetization is subscription-first with limited free credits.

## Open Questions

- What is the initial free allowance (credits per day/week)?
- Which AI provider is primary (fal.ai vs Replicate) for first iteration?

## Assumptions

- [ASSUMPTION-A1] We will start with 4 preset "styles" rather than a free-form prompt.
- [ASSUMPTION-A2] Users have a stable internet connection for AI processing.

## Risks & Mitigations

- [RISK] AI provider latency may harm UX. Mitigation: background processing + clear progress UI + retry.
- [RISK] Low quality uploads lead to poor results. Mitigation: Add "Selfie Guide" screen before upload.

## Product snapshot

- **Product name:** Headshot Studio
- **Target user:** Job seekers needing professional headshots quickly
- **Core loop (1 sentence):** Upload a single selfie, select a professional style, and receive 4 high-quality headshots ready for LinkedIn.
- **Monetization:** Freemium (2 free generations) + Subscription (Unlimited + Priority Processing)
- **Differentiator:** Fastest results (under 60s) + iOS-native UX with zero prompt engineering required.
- **Target markets:** US/UK/DE/FR
- **Platforms:** iOS + Android

## MVP scope

### IN (Must-have)

- Onboarding (Value prop + camera permission)
- Selfie Guide (Dos and Don'ts)
- Create flow (Upload -> Style Selection -> Processing -> Results)
- Results view (Grid of 4, single image expansion, export to camera roll)
- History (List of previous generations with thumbnails)
- Paywall (RevenueCat integration, monthly/yearly options)
- Settings (Account, Restore Purchases, Privacy Policy, Terms)

### OUT (Explicit non-goals)

- Social feed or sharing to public gallery
- In-app messaging or support chat
- Manual prompt editing or advanced AI parameters
- Web version (Mobile-only for MVP)

## Success criteria (MVP)

- User can go from app launch to first headshot export in under 3 minutes.
- 99.9% crash-free sessions.
- Successful RevenueCat entitlement check on every app launch.

## Key constraints

- Stack: Expo + RN + TS + Expo Router + NativeWind v4 + Supabase + RevenueCat
- Minimalist iOS-native feel, consistent tokens, consistent navigation
