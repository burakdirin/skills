# 02-prd.md

## Decision Summary

- Focus MVP on "Speed to LinkedIn" for Job Seekers.
- Limit MVP to 12 user stories across 4 epics.
- Monetization: 2 free generations, then $9.99/mo subscription.

## Open Questions

- Should we include a "Style Quiz" or just 4 presets? (Decision: 4 presets for MVP).
- Exact RevenueCat entitlement name (Decision: `pro`).

## Assumptions

- [ASSUMPTION-A1] Users are willing to pay $9.99/mo for a high-quality LinkedIn photo.
- [ASSUMPTION-A2] 2 free generations is enough to prove value without giving away the farm.

## Risks & Mitigations

- [RISK] High churn after the first generation. Mitigation: Add "Pro Tips" for LinkedIn profile optimization in the Results view.
- [RISK] AI processing time exceeds 2 minutes. Mitigation: Implement background processing with local notifications.

## 1) Vision & positioning

- **One-sentence value proposition:** Get professional, LinkedIn-ready headshots in under 2 minutes from a single selfie.
- **Positioning statement:** For **job seekers** who **need a professional photo quickly**, **Headshot Studio** is an **AI-powered utility** that **delivers high-quality results in seconds**, unlike **web-based competitors**, because **it's an iOS-native, 1-click experience**.
- **Target wedge segment:** Tech and corporate job seekers in the US/UK.

## 2) Personas (2–3)

### Persona 1: "The Urgent Job Seeker" (Alex)

- Context: Just saw a dream job posting; needs to update LinkedIn profile _now_.
- Goals: Get a professional-looking photo without booking a photographer.
- Pain points: Most AI tools are slow or require 20+ uploads.
- Why they pay: Speed and convenience.
- Why they churn: Once the job is found, the need disappears.

### Persona 2: "The Budget Professional" (Sarah)

- Context: Freelancer wanting to look more professional but can't afford a $200 headshot session.
- Goals: High-quality results at a fraction of the cost.
- Pain points: Aragon/HeadshotPro are too expensive for a single person.
- Why they pay: Value for money.

## 3) Jobs To Be Done (JTBD)

- JTBD 1:
  - Trigger: Applying for a new job.
  - Desired outcome: Feeling confident about my profile's visual first impression.
  - Anxieties / barriers: "Will this look like AI?" "Is it worth $10?"

## 4) MVP scope (strict)

### MUST-HAVE (MVP)

- Single selfie upload.
- 4 preset professional styles (Executive, Creative, Tech, Formal).
- Results grid with 1-click export.
- Generation history.
- Paywall with monthly/yearly options.

### OUT (explicit non-goals)

- Manual prompt editing.
- Team/Corporate accounts.
- Background removal tools.

### MVP Definition of Done (verifiable)

- [ ] Core loop (Upload -> Style -> Result) works in < 120s.
- [ ] Paywall blocks generation after 2 free credits.
- [ ] Exported image is 1024x1024px.
- [ ] Analytics events fire for `generation.start` and `subscription.purchase_success`.

## 5) User stories (10–15) grouped into epics

### Epic A: Onboarding & Account

1. As a new user I want to see a quick value-prop carousel so I understand what the app does.
   - Acceptance criteria:
     - [ ] 3-screen onboarding showing "Before/After" results.
     - [ ] "Get Started" button leads to Home.
2. As a user I want to sign in with email so my history is synced across devices.
   - Acceptance criteria:
     - [ ] Supabase Auth integration.
     - [ ] Magic link or password-less login.

### Epic B: Core Loop

3. As a job seeker I want to upload a selfie so the AI can generate my headshots.
   - Acceptance criteria:
     - [ ] MediaLibrary permission request.
     - [ ] Progress bar shown during upload.
4. As a job seeker I want to select a "Style" so my headshot matches my industry.
   - Acceptance criteria:
     - [ ] 4 selectable cards (Executive, Creative, Tech, Formal).
     - [ ] Tooltip explaining each style.
5. As a job seeker I want to see my results in a grid so I can pick the best one.
   - Acceptance criteria:
     - [ ] 2x2 grid of 1024px images.
     - [ ] Tap to expand to full screen.
     - [ ] "Save to Camera Roll" button.

### Epic C: Paywall & Subscription

6. As a free user I want to know when I've used my credits so I can choose to subscribe.
   - Acceptance criteria:
     - [ ] Credit counter shown on Home/Create.
     - [ ] Paywall triggers automatically when credits = 0.

## 6) User flows

### Core loop flow

1. Home -> Tap "Create" -> Selfie Guide -> Camera/Upload -> Style Selection -> Processing (Loading State) -> Results View -> Export.

## 7) Monetization design

### Free vs Premium gates

| Capability  | Free     | Premium   |
| ----------- | -------- | --------- |
| Generations | 2 total  | Unlimited |
| Processing  | Standard | Priority  |
| Quality     | 512px    | 1024px    |

## 8) Metrics & analytics

- **North Star metric:** `generation.success` per weekly active user.
- KPIs:
  - Activation: % of users who complete 1st generation.
  - Conversion: % of users who subscribe after 2nd generation.

## 9) ASO draft (MVP)

- Primary keywords: AI Headshot, Professional Photo, LinkedIn Photo.
- Secondary keywords: Business Portrait, Resume Photo, AI Portrait, Profile Picture.
- Screenshot concepts (3):
  1. "Professional Headshots in 2 Minutes" (Before/After).
  2. "4 Styles for Every Industry" (Grid of styles).
  3. "LinkedIn Ready. 1-Click Export." (Results view).

## 10) Go/No-Go (solo indie)

- Recommendation: **GO**.
- Rationale: High demand, low technical complexity for MVP, clear monetization.
