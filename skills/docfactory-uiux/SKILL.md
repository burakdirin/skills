---
name: docfactory-uiux
description: Creates 03-ui-ux-spec.md (IA, Expo Router route map, screen list, states, design tokens, component inventory, micro-interactions, accessibility) from 00-* docs and 02-prd.md. Use after docfactory-prd or when the user asks for a UI spec, UX design, screens, or a design system. Do not generate code.
---

# DocFactory UI/UX Spec (03-ui-ux-spec.md)

This skill produces a **build-ready** UI/UX specification that keeps the UI consistent and minimizes drift during implementation.

## Prerequisites (required context)

This skill expects these files already exist:

- `00-project-brief.md`
- `00-decisions.md` (Source of Truth; especially tokens + navigation rules)
- `00-glossary.md` (naming + analytics/event naming)
- `02-prd.md` (scope + stories + flows)

Optional but recommended:

- `01-market-research.md` (positioning / wedge)

If any required file is missing, STOP and tell the user which file is missing and which skill to run first.

## Output (exact file)

Produce exactly one file:

- `03-ui-ux-spec.md`

### Required top sections (in this order)

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag as `[RISK]`)

## Hard rules

- Language: English.
- Do NOT add MVP screens beyond what `02-prd.md` requires.
- Maintain internal consistency with:
  - screen names and event naming in `00-glossary.md`
  - scope boundaries in `00-project-brief.md`
  - tokens + navigation conventions in `00-decisions.md`
- If `00-decisions.md` has missing/placeholder UI tokens, define concrete tokens in this spec AND include a section called:
  - `## Token Patch Proposal (update 00-decisions.md)`
    (Do NOT create additional files; just propose the patch in this doc.)
- Do not generate code. This is a design/spec artifact.

## Design principles reference (non-normative)

Align with iOS design principles and platform conventions (Apple Human Interface Guidelines). Keep the UI minimalist and content-first.
(Reference: Apple HIG)

## What to include in 03-ui-ux-spec.md

Use `templates/03-ui-ux-spec.template.md`.

Minimum requirements:

1. **Information Architecture**
   - Sections/tabs (if any), stacks/modals
   - Where paywall can be opened from

2. **Expo Router Route Map (MVP)**
   - Route groups using parentheses: e.g. `(auth)`, `(tabs)`
   - Tab routes and stack routes
   - Deep link / URL notes (high-level)

3. **Screen list (MVP only)**
   For each screen include:
   - Purpose (1 sentence)
   - Primary actions
   - Components used
   - States: loading / empty / error (explicit)
   - Edge cases (permissions, network fail, auth expired)
   - Analytics events (use glossary naming)

4. **Design System**
   - Tokens: colors (hex), typography scale, spacing scale
   - Component rules: radius, shadows, borders, elevation usage (minimal)
   - “Visual hierarchy” rules (what is primary vs secondary)

5. **Component Inventory (MVP)**
   Provide a list of reusable components with variants:
   - Button (primary/secondary/destructive/ghost)
   - Text field (with validation)
   - Card
   - List row
   - Modal / bottom sheet
   - Toast
   - Empty state component
   - Loading skeleton
   - Paywall block(s)

6. **State Matrix**
   - A table mapping Screen × (Loading/Empty/Error) behaviors

7. **Micro-interactions**
   - Minimal animations guidelines (duration, easing in plain language)
   - Haptics usage (when to use, when not)

8. **Accessibility**
   - Minimum tap targets, contrast guidance, dynamic type guidance
   - VoiceOver labels basics for key controls
   - Motion-reduction considerations

9. **UI Consistency Rules**
   - 8–12 concrete, testable rules (e.g., “Primary CTA always bottom-aligned on forms”)

## Optional: structure validator

After producing the file, optionally run:

- `python scripts/validate_docfactory_uiux.py`

## Stop & ask conditions

Stop and ask the user if:

- The PRD scope is ambiguous (cannot list MVP screens)
- Token decisions conflict (00-decisions vs PRD vs brief)
- The user asks for technical architecture or DB schema here (out of scope)

## Additional Resources

- For the UI/UX spec template, see [templates/03-ui-ux-spec.template.md](templates/03-ui-ux-spec.template.md)
- For accessibility checklist, see [references/accessibility-checklist.md](references/accessibility-checklist.md)
- For component inventory guidance, see [references/component-inventory-guidance.md](references/component-inventory-guidance.md)
- For IA and routing checklist, see [references/ia-routing-checklist.md](references/ia-routing-checklist.md)
- For screen spec checklist, see [references/screen-spec-checklist.md](references/screen-spec-checklist.md)
- For a complete example, see [examples/idea.example.yaml](examples/idea.example.yaml)
- For example output, see [examples/output/03-ui-ux-spec.md](examples/output/03-ui-ux-spec.md)
- For validation script, see [scripts/validate_docfactory_uiux.py](scripts/validate_docfactory_uiux.py)
