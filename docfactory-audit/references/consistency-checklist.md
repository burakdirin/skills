# Consistency Checklist (DocFactory)

## A) Identity & scope

- Product name identical across docs
- Target user and core loop identical across docs
- Monetization model and premium gates consistent (PRD vs UI vs backlog)
- MVP IN/OUT consistent (brief vs PRD vs backlog)

## B) Screens & navigation

- Glossary screen names match UI/UX screen list
- PRD flows map to screens (no missing screen)
- UI/UX route map matches Arch folder tree (app/ pages)
- Paywall route and triggers consistent across PRD/UI/UX/Backlog

## C) Design system

- Tokens exist and are concrete (hex, sizes, spacing)
- Component inventory covers all screens
- State matrix covers all MVP screens (loading/empty/error)

## D) Data & security

- Entities/tables cover the user stories
- RLS intent documented for all user-owned entities
- Auth/route protection consistent with route groups

## E) Integrations

- RevenueCat entitlement naming consistent
- Restore purchases path specified
- Analytics events named consistently and referenced in PRD/UI spec
- Push notifications only if explicitly in scope

## F) Execution plan quality

- Backlog Phase 1 tasks >= 20 and each has acceptance criteria + verification
- Critical path exists
- Tasks are sized 30–90 minutes (split if larger)
