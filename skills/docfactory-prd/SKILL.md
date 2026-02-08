---
name: docfactory-prd
description: Creates 02-prd.md (vision, personas, JTBD, MVP scope, user stories, core loop, monetization, metrics, ASO) from 00-* docs and 01-market-research.md. Use after docfactory-init + docfactory-market. Do not do coding.
---

# DocFactory PRD (02-prd.md)

This skill produces a **buildable** Product Requirements Document for a solo indie developer.
It focuses on scope discipline and explicit acceptance criteria so the build can be split into Prompt Packs later.

## Prerequisites (required context)

This skill expects these files already exist:

- `00-project-brief.md`
- `00-decisions.md`
- `00-glossary.md`
- `01-market-research.md`

If any are missing, STOP and tell the user which file is missing and which skill to run first.

## Output (exact file)

Produce exactly one file:

- `02-prd.md`

### Required top sections (in this order)

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag as `[RISK]`)

## Hard rules

- Language: English.
- Never invent market numbers (TAM/SAM/SOM, downloads, revenue, MAU/DAU). If needed: write `[NO_DATA]`.
- Keep MVP scope tiny: 2–4 weeks solo build to a shippable vertical slice.
- The PRD must be internally consistent with:
  - naming conventions in `00-glossary.md`
  - scope boundaries in `00-project-brief.md`
  - constraints/stack in `00-decisions.md`
  - wedge hypothesis + gaps in `01-market-research.md`
- Prefer explicit requirements over “nice prose”.

## What to include in 02-prd.md

Use `templates/02-prd.template.md`.

Minimum requirements:

1. **Vision + positioning**
   - One-sentence value proposition
   - Positioning statement (who/what/why)
   - Target segment (from market wedge)

2. **Personas (2–3)**
   - Goals, context, pain points
   - Why they pay / why they churn

3. **JTBD**
   - 2–4 JTBD statements with triggers, desired outcomes, and anxieties

4. **MVP scope**
   - MUST / SHOULD / NICE lists (strict)
   - Explicit MVP OUT list (non-goals)
   - Definition of Done for MVP (verifiable)

5. **User stories (10–15) grouped into epics**
   - Format: “As a <persona> I want <capability> so that <outcome>”
   - Each story has acceptance criteria (checkboxes)
   - Include edge cases: empty/loading/error states, permissions, auth, paywall, restore purchases

6. **User flows**
   - Onboarding → core loop → paywall → retention loop
   - Include: loading/error/empty states as explicit steps

7. **Monetization design**
   - Free vs Premium feature gates (table)
   - Pricing hypothesis (monthly/yearly), trial length hypothesis
   - Paywall triggers (when shown), upgrade paths, restore purchases
   - If pricing is uncertain, mark `[ASSUMPTION]` and list validation plan

8. **Metrics**
   - North Star metric
   - 3–5 KPIs (activation, conversion, retention, revenue)
   - Instrumentation plan (event names referencing `00-glossary.md` scheme)

9. **ASO draft (MVP)**
   - Primary keywords + 10–20 secondary keywords (hypotheses if needed)
   - Title/subtitle concepts
   - 3 screenshot concepts + key benefit per screenshot

10. **Go/No-Go (solo indie)**

- 1 paragraph recommendation + rationale
- Biggest risk + mitigation

## Optional: structure validator

After producing the file, optionally run:

- `python scripts/validate_docfactory_prd.py`

## Stop & ask conditions

Stop and ask the user if:

- The idea is still ambiguous after reading 00-project-brief.md
- Market wedge is unclear / cannot be derived from 01-market-research.md
- The user asks for UI spec or technical architecture here (out of scope)
