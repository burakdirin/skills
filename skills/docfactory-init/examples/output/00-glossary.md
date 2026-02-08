# 00-glossary.md

## Decision Summary

- Domain language is optimized for clarity (no internal jargon).
- Screen names and analytics events are strictly enforced.

## Open Questions

- None.

## Assumptions

- [ASSUMPTION-A1] "Generation" means one upload → 4 outputs.
- [ASSUMPTION-A2] "Style" refers to a specific AI prompt preset (e.g., "Executive", "Creative").

## Risks & Mitigations

- [RISK] Inconsistent event names across screens. Mitigation: enforce naming scheme below.

## Domain terms

- **Generation:** A single user request that produces multiple outputs (4 headshots).
- **Credit:** The unit that limits free usage (1 generation = 1 credit).
- **Entitlement (pro):** RevenueCat access flag for premium features.
- **Style:** A curated set of AI parameters that define the look of the headshot.
- **Selfie:** The input image provided by the user.

## Screen names (MVP)

- **Home:** The landing tab with recent activity and CTA to create.
- **Create:** The multi-step flow for uploading and selecting styles.
- **Results:** The view showing the 4 generated headshots.
- **History:** The list of all past generations.
- **Paywall:** The subscription offer screen.
- **Settings:** App configuration, account, and legal.
- **SelfieGuide:** Educational screen before the camera opens.

## Analytics event naming

- dot.notation, lowercase:
  - `screen.view`
  - `generation.start`
  - `generation.success`
  - `generation.failure`
  - `paywall.open`
  - `subscription.purchase_success`
  - `export.image`
