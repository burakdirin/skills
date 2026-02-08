# Definition of Done Checklist (MVP)

## Quality gates (must be green)
- [ ] Lint
- [ ] Typecheck
- [ ] Tests (at least smoke/unit where applicable)
- [ ] Build succeeds (EAS preview or equivalent)

## UX baseline
- [ ] Every MVP screen has loading/empty/error states
- [ ] Primary flows have retry on recoverable failures
- [ ] No dead-ends: user can always navigate back or retry
- [ ] Accessibility baseline: tap targets, labels for primary CTAs

## Product baseline
- [ ] Paywall shows correctly and restore purchases works
- [ ] Basic analytics events are fired as defined in glossary
- [ ] Settings/legal pages accessible

## Release readiness
- [ ] Environment variables configured (Supabase, RevenueCat)
- [ ] Build profile configured (preview/production)
- [ ] Smoke checklist executed on device/simulator
