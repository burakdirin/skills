# Deployment Checklist (EAS)

- Define `eas.json` profiles: preview + production
- Decide submission workflow:
  - manual CLI vs CI-triggered
- Decide OTA update strategy (if using expo-updates):
  - channels/branches naming
- Add CI guardrails:
  - `npx expo install --check` (fails CI on mismatch)
  - lint/typecheck/test
- Secrets:
  - keep Supabase keys and RevenueCat API key in env vars / secret store
