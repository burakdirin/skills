# 02-prd.md

## Decision Summary

<!-- One sentence summary of the key product requirements decisions. -->

- ...

## Open Questions

<!-- List any product-level questions that remain unanswered (e.g., specific feature behavior). -->

- ...

## Assumptions

<!-- Tag as [ASSUMPTION-A1], [ASSUMPTION-A2], etc. -->

- [ASSUMPTION-A1] ...

## Risks & Mitigations

<!-- Tag as [RISK] (e.g., [RISK] High user churn at paywall). -->

- [RISK] ...

## 1) Vision & positioning

- **One-sentence value proposition:** <!-- What is the single biggest benefit? -->
- **Positioning statement:** For <target user> who <need>, <product> is a <category> that <benefit>, unlike <alternative>, because <differentiator>.
- **Target wedge segment:** <!-- From 01-market-research.md. -->

## 2) Personas (2–3)

<!-- Who are we building for? Be specific about their context. -->

### Persona 1: ...

- Context:
- Goals:
- Pain points:
- Why they pay:
- Why they churn:

## 3) Jobs To Be Done (JTBD)

<!-- What "job" is the user hiring this app to do? -->

- JTBD 1:
  - Trigger:
  - Desired outcome:
  - Anxieties / barriers:

## 4) MVP scope (strict)

<!-- Ruthlessly cut anything that isn't required for the core loop. -->

### MUST-HAVE (MVP)

- ...

### SHOULD-HAVE (if time)

- ...

### NICE-TO-HAVE (post-MVP)

- ...

### OUT (explicit non-goals)

- ...

### MVP Definition of Done (verifiable)

- [ ] Core loop works end-to-end in production build
- [ ] Paywall + restore purchases works
- [ ] Loading/empty/error states for all MVP screens
- [ ] Basic analytics events implemented
- [ ] Crash-free baseline (no known blocking crashes)

## 5) User stories (10–15) grouped into epics

<!-- Format: As a <persona> I want <capability> so that <outcome>. -->
<!-- Every story MUST have acceptance criteria checkboxes. -->

### Epic A: Onboarding & Account

1. Story: ...
   - Acceptance criteria:
     - [ ] ...
   - Edge cases:
     - [ ] ...

## 6) User flows

<!-- Map the step-by-step journey. Include error/loading states. -->

### Onboarding flow

1. ...

### Core loop flow

1. ...

### Paywall flow

1. trigger: <!-- When does the user see the paywall? -->
2. ...

## 7) Monetization design

### Free vs Premium gates

| Capability | Free | Premium |
| ---------- | ---- | ------- |
| ...        | ...  | ...     |

### Pricing hypothesis

- Monthly: ...
- Yearly: ...
- Trial: ...
- Notes: [NO_DATA] if needs validation.

## 8) Metrics & analytics

- **North Star metric:** <!-- The one metric that matters most. -->
- KPIs:
  - Activation: ...
  - Conversion: ...
  - Retention: ...
  - Revenue: ...
- Event plan (use glossary naming):
  - `screen.view`
  - `...`

## 9) ASO draft (MVP)

- Primary keywords: ...
- Secondary keywords (10–20): ...
- Title concepts:
- Subtitle concepts:
- Screenshot concepts (3):
  1. <!-- Core benefit -->
  2. <!-- Speed/Trust -->
  3. <!-- Premium value -->

## 10) Go/No-Go (solo indie)

- Recommendation:
- Rationale:
- Biggest risks:
- Mitigations:
