# 03-ui-ux-spec.md

## Decision Summary

- ...

## Open Questions

- ...

## Assumptions

- [ASSUMPTION-A1] ...

## Risks & Mitigations

- [RISK] ...

## 1) Product UX Principles (MVP)

- Principle 1: ...
- Principle 2: ...
- Principle 3: ...
- Notes: Keep consistent with Apple/iOS conventions.

## 2) Information Architecture (IA)

- Primary sections:
- Secondary sections:
- Paywall entry points:
- Settings entry points:

## 3) Expo Router Route Map (MVP)

> Use parentheses for route groups (e.g. `(auth)`, `(tabs)`), kebab-case filenames, and a root `_layout.tsx` conceptually.

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

### Deep link notes

- ...

## 4) Design System (tokens)

> Source of truth is `00-decisions.md`. If missing, define tokens and include “Token Patch Proposal”.

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

- xs:
- sm:
- base:
- lg:
- xl:
- 2xl:

### Spacing scale

- 4 / 8 / 12 / 16 / 24 / 32

### UI rules

- Radius:
- Shadows/elevation:
- Dividers/borders:
- Icon style:
- Imagery style:

## 5) Component Inventory (MVP)

List the reusable components and variants.

- **Button**
  - variants: primary / secondary / ghost / destructive / link
  - states: default / pressed / disabled / loading
- **TextField**
  - validation: inline error message + helper
- **Card**
- **ListRow**
- **Modal / BottomSheet**
- **Toast**
- **EmptyState**
- **LoadingSkeleton**
- **PaywallBlock** (pricing + benefits + CTA)
- ...

## 6) Screen Specifications (MVP only)

> For each screen include purpose, primary actions, components, states, edge cases, analytics events.

### Screen: <Name>

- Purpose:
- Primary actions:
- Components:
- States:
  - Loading:
  - Empty:
  - Error:
- Edge cases:
- Analytics:
  - `screen.view`
  - ...

(Repeat for all MVP screens.)

## 7) State Matrix

| Screen | Loading | Empty | Error | Retry pattern |
| ------ | ------- | ----- | ----- | ------------- |
| ...    | ...     | ...   | ...   | ...           |

## 8) Micro-interactions

- Loading feedback guidelines:
- Haptics guidelines:
- Animation guidelines (minimal):
- Motion reduction:

## 9) Accessibility (MVP baseline)

- Tap targets:
- Contrast:
- Dynamic Type:
- VoiceOver labels:
- Focus order:

## 10) UI Consistency Rules (testable)

1. ...
2. ...
3. ...
   (8–12 rules)

## Token Patch Proposal (update 00-decisions.md)

> Only include this section if 00-decisions.md tokens are missing or placeholders.

- Proposed token changes:
  - ...
