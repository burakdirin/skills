# 03-ui-ux-spec.md

## Decision Summary

- Use a minimalist, goal-oriented mobile design system with a focus on high-quality headshot previews.
- Navigation: Tab-based for core features, modal for the paywall.
- Design Tokens: Finalized hex codes and spacing scale.

## Open Questions

- Should the "Selfie Guide" be a swipeable carousel or a single scrollable list? (Decision: single scrollable list for speed).

## Assumptions

- [ASSUMPTION-A1] Users prefer a dark-mode-first aesthetic for "AI" tools.
- [ASSUMPTION-A2] Standard platform transitions (slide/fade) are sufficient for MVP.

## Risks & Mitigations

- [RISK] Large image previews might slow down the Results screen. Mitigation: Use `expo-image` for optimized caching and blurred placeholders.

## 1) Product UX Principles (MVP)

- **Content-First**: Headshots are displayed at 100% width in the Results view.
- **Progressive Disclosure**: The "Create" flow is split into 4 distinct steps.
- **Single Primary Action**: Every screen has a fixed bottom-aligned primary button.

## 2) Information Architecture (IA)

- **Primary sections**: Home, Create, History, Settings (Tabs).
- **Secondary sections**: Results (Stack), SelfieGuide (Stack).
- **Paywall entry points**: Home (CTA), Create (after 2 credits), Settings.

## 3) Expo Router Route Map (MVP)

### Route groups

- `(auth)/login`
- `(tabs)/home`, `(tabs)/create`, `(tabs)/history`, `(tabs)/settings`

### Modal/stack screens

- `paywall` (modal)
- `results/[id]` (stack)
- `selfie-guide` (stack)

## 4) Design System (tokens)

### Colors (hex)

- background: #0B0B0F
- surface: #18181B
- text: #F4F4F5
- muted_text: #A1A1AA
- primary: #6D28D9
- secondary: #27272A
- destructive: #EF4444
- border: #3F3F46

### Typography scale

- xs: 12/16
- sm: 14/20
- base: 16/24
- lg: 18/28
- xl: 20/28
- 2xl: 24/32

### Spacing scale

- 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64

### UI rules

- Radius: 12px for cards, 8px for buttons.
- Shadows: None (use borders for separation).
- Icon style: Lucide React Native.

## 5) Component Inventory (MVP)

- **Button**: Primary (solid), Secondary (outline), Ghost (text-only).
- **Card**: Surface color, 12px radius, 1px border.
- **EmptyState**: Icon + Title + Subtitle + Primary CTA.
- **LoadingSkeleton**: Pulsing surface color for image placeholders.
- **PaywallBlock**: Pricing table with "Best Value" badge.

## 6) Screen Specifications (MVP only)

### Screen: Create

- Purpose: Upload a selfie and start generation.
- Primary actions: "Upload Selfie", "Select Style", "Generate".
- Components: Button, Card, LoadingSkeleton.
- States:
  - Loading: Skeleton grid while uploading.
  - Empty: "Upload your first selfie" prompt.
  - Error: "Upload failed" Toast with "Retry" button.
- Analytics: `screen.view`, `generation.start`.

### Screen: Results

- Purpose: Show the 4 generated headshots.
- Primary actions: "Save to Camera Roll", "Share".
- Components: 2x2 Image Grid, Primary Button.
- States:
  - Loading: Blurred placeholders while images load.
  - Error: "Failed to load results" alert.

## 7) State Matrix

| Screen  | Loading       | Empty         | Error          | Retry pattern   |
| ------- | ------------- | ------------- | -------------- | --------------- |
| Home    | Skeleton list | "No activity" | Toast          | Pull-to-refresh |
| Create  | Progress bar  | N/A           | Inline message | Primary CTA     |
| History | Skeleton grid | "No history"  | Toast          | Pull-to-refresh |

## 9) Accessibility & Platform Baseline

- Tap targets: All buttons are min 48px high.
- Contrast: All text meets WCAG AA (4.5:1).
- VoiceOver/TalkBack: All images have descriptive `accessibilityLabel`.
- Android Back: Hardware/gesture back button returns to the previous screen or exits the app from the Home tab.
- Edge-to-Edge: UI accounts for system navigation bar on Android.

## 10) UI Consistency Rules (testable)

1. Primary CTA is always bottom-aligned with 16px padding.
2. All screen titles use `2xl` typography.
3. Every error state must include a "Retry" or "Back" action.
