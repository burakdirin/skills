# Dependency Pinning & Verification (Expo)

- Prefer `npx expo install <pkg>` for Expo SDK-compatible versions.
- Use `npx expo install --check` in CI to detect mismatched versions.
- If you must deviate, document why and accept the maintenance risk.
- Record all pinned versions in 04-tech-architecture.md under Dependency Plan.
