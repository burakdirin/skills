# 00-glossary.md

## Decision Summary

- Domain language is optimized for clarity (no internal jargon).

## Open Questions

- None

## Assumptions

- [ASSUMPTION-A1] “Generation” means one upload → N outputs.

## Risks & Mitigations

- [RISK] Inconsistent event names across screens. Mitigation: enforce naming scheme below.

## Domain terms

- **Generation:** A single user request that produces multiple outputs.
- **Credit:** The unit that limits free usage.
- **Entitlement (pro):** RevenueCat access flag for premium features.

## Screen names (MVP)

- Home
- Create
- Results
- History
- Paywall
- Settings

## Analytics event naming

- dot.notation, lowercase:
  - `screen.view`
  - `generation.start`
  - `generation.success`
  - `paywall.open`
  - `subscription.purchase_success`
