# 03-ui-ux-spec.md

## Decision Summary

<!-- One sentence summary of the key UI/UX decisions. -->

- ...

## Open Questions

<!-- List any UI or UX questions that remain unanswered (e.g., specific animation behavior). -->

- ...

## Assumptions

<!-- Tag as [ASSUMPTION-A1], [ASSUMPTION-A2], etc. -->

- [ASSUMPTION-A1] ...

## Risks & Mitigations

<!-- Tag as [RISK] (e.g., [RISK] Complex navigation confuses users). -->

- [RISK] ...

## 1) Product UX Principles (MVP)

<!-- What are the core principles guiding the design? -->

- Principle 1: ...
- Principle 2: ...
- Principle 3: ...
- Notes: Keep consistent with Apple/iOS conventions.

## 2) Information Architecture (IA)

<!-- How is the app structured? -->

- Primary sections:
- Secondary sections:
- Paywall entry points:
- Settings entry points:

## 3) Expo Router Route Map (MVP)

<!-- Use parentheses for route groups (e.g. (auth), (tabs)), kebab-case filenames. -->

### Route groups

- `(auth)/...`
- `(tabs)/...`

### Tabs

- `(tabs)/home`
- `(tabs)/create`
- `(tabs)/history`
- `(tabs)/settings`

### Modal/stack screens

- `paywall` (modal)
- `results/[id]` (stack)
- ...

## 4) Design System (tokens)

<!-- Source of truth is 00-decisions.md. If missing, define tokens here. -->

### Colors (hex)

- background:
- surface:
- text:
- muted_text:
- primary:
- secondary:
- destructive:
- border:

### Typography scale

- xs: <!-- size / line-height -->
- sm:
- base:
- lg:
- xl:
- 2xl:

### Spacing scale

- 4 / 8 / 12 / 16 / 24 / 32

### UI rules

- Radius: <!-- e.g., 12px for cards, 8px for buttons -->
- Shadows/elevation: <!-- Keep minimal for iOS -->
- Icon style: <!-- e.g., Lucide or SF Symbols -->

## 5) Component Inventory (MVP)

<!-- List the reusable components and variants. -->

- **Button**
  - variants: primary / secondary / ghost / destructive
  - states: default / pressed / disabled / loading
- **TextField**
- **Card**
- **ListRow**
- **Modal / BottomSheet**
- **EmptyState**
- **LoadingSkeleton**
- **PaywallBlock**

## 6) Screen Specifications (MVP only)

<!-- For each screen include purpose, primary actions, components, states, edge cases, analytics. -->

### Screen: <Name>

- Purpose:
- Primary actions:
- Components:
- States:
  - Loading: <!-- e.g., Skeleton list -->
  - Empty: <!-- e.g., EmptyState with CTA -->
  - Error: <!-- e.g., Toast + Retry button -->
- Edge cases:
- Analytics:
  - `screen.view`

## 7) State Matrix

<!-- A table mapping Screen x (Loading/Empty/Error) behaviors. -->

| Screen | Loading | Empty | Error | Retry pattern |
| ------ | ------- | ----- | ----- | ------------- |
| ...    | ...     | ...   | ...   | ...           |

## 8) Micro-interactions

- Loading feedback:
- Haptics:
- Animation: <!-- Keep to standard iOS transitions -->

## 9) Accessibility (MVP baseline)

- Tap targets: <!-- Min 44x44 -->
- Contrast: <!-- Min 4.5:1 -->
- Dynamic Type:
- VoiceOver labels:

## 10) UI Consistency Rules (testable)

<!-- 8–12 concrete, testable rules. -->

1. ...

## Token Patch Proposal (update 00-decisions.md)

<!-- Only include if 00-decisions.md tokens are missing or placeholders. -->

- Proposed token changes:
  - ...
