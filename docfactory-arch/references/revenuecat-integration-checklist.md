# RevenueCat Integration Checklist (MVP)

- Choose entitlement name (e.g., `pro`) and document it
- Define paywall trigger moments (from PRD)
- Implement restore purchases flow and document expected behavior
- Cache entitlement state briefly for UX, but treat server as source of truth
- Handle “purchase in progress” and “restore in progress” states in UI
