---
name: docfactory-arch
description: Creates 04-tech-architecture.md (stack decisions, data layer, Supabase schema + RLS approach, integrations, folder tree, deployment, performance, security) from 00-* docs + PRD + UI/UX spec. Use after docfactory-uiux. Do not generate code.
---

# DocFactory Technical Architecture (04-tech-architecture.md)

This skill produces a **build-ready** technical architecture document for a solo indie mobile app project.

## Prerequisites (required context)

This skill expects these files already exist:

- `00-project-brief.md`
- `00-decisions.md` (Source of Truth; stack & tokens)
- `00-glossary.md` (domain terms + event naming)
- `02-prd.md` (scope + user stories + flows)
- `03-ui-ux-spec.md` (routes + screens + components + states)

Optional but recommended:

- `01-market-research.md` (wedge positioning, competitors)
- Any provider docs links chosen by the team (fal.ai / Replicate etc.)

If any required file is missing, STOP and tell the user which file is missing and which skill to run first.

## Output (exact file)

Produce exactly one file:

- `04-tech-architecture.md`

### Required top sections (in this order)

- `## Decision Summary`
- `## Open Questions`
- `## Assumptions` (tag as `[ASSUMPTION-A1]`, `[ASSUMPTION-A2]`, ...)
- `## Risks & Mitigations` (tag as `[RISK]`)

## Hard rules

- Language: English.
- Do NOT generate code or migrations here. This is a design/spec artifact.
- Architecture must be consistent with:
  - navigation conventions (Expo Router) and route map from `03-ui-ux-spec.md`
  - scope and flows from `02-prd.md`
  - stack constraints from `00-decisions.md`
- Do not invent package versions. If exact versions are unknown, write `[PENDING_PIN]` and list the command to obtain them (e.g., `npx expo install --check`, lockfile inspection).
- Prefer choices that reduce maintenance for a solo dev.

## What to include in 04-tech-architecture.md

Use the template in `templates/04-tech-architecture.template.md`.

Minimum requirements:

1. **Architecture overview**
   - Modules/layers: UI, navigation, state, data access, integrations
   - Principles: small surface area, typed boundaries, testable core logic

2. **Stack decisions (with reasons)**
   - Expo SDK (pinned after scaffold)
   - Expo Router layout strategy (groups, tabs, modals)
   - NativeWind v4 setup constraints (global.css, metro config notes)
   - Supabase Auth + DB + RLS approach
   - RevenueCat entitlement model (`pro`, etc.)

3. **Dependency plan**
   - List required packages (by npm name)
   - For each: why it exists, risk, alternatives, and how to pin versions

4. **Data model overview (Supabase)**
   - High-level tables/entities and relationships (no SQL here)
   - Indexing considerations
   - RLS approach per table:
     - SELECT/INSERT/UPDATE/DELETE policy intent
     - Use of `auth.uid()` where appropriate

5. **Authentication & authorization**
   - Session handling strategy (where session is stored, refresh)
   - Route protection (auth group vs tabs group)
   - Handling auth expiry

6. **Core integrations**
   - RevenueCat (purchase flow, restore flow, entitlement checks)
   - Analytics (event naming from glossary, batching, privacy notes)
   - Push notifications (if in PRD; otherwise explicitly OUT)
   - AI provider calls (fal.ai / Replicate etc.) — boundary design and rate limiting

7. **Folder structure**
   - Provide a full tree, including `app/` routes and non-navigation code outside `app/` (Expo Router convention)
   - File naming conventions

8. **State management & data fetching**
   - Minimal approach (React Query or plain hooks) with rationale
   - Caching strategy, retries, offline expectations

9. **Error handling**
   - Global error boundary strategy
   - API error normalization
   - User-facing error patterns consistent with UI/UX spec

10. **Performance goals**

- Budget targets (e.g., first render, navigation latency)
- Image and network optimization strategies

11. **Deployment & CI/CD**

- EAS Build profiles (preview/production)
- EAS Submit basics
- CI trigger strategy (GitHub Actions etc.)
- Secrets management (env vars)

12. **Testing strategy (MVP)**

- Unit tests for pure logic
- Basic integration tests (if feasible)
- Smoke checklist for release candidates

## Optional: structure validator

After producing the file, optionally run:

- `python scripts/validate_docfactory_arch.py`

## Stop & ask conditions

Stop and ask the user if:

- The PRD or UI/UX spec is not specific enough to derive routes/screens
- The data model cannot be derived from the PRD/user stories
- Integrations are ambiguous (RevenueCat vs other IAP; which analytics)
