# Error Taxonomy (React Native)

## 1. Network Errors

- **Category**: `NETWORK_ERROR`
- **Trigger**: No internet, timeout, DNS failure.
- **UX Pattern**: Toast or Full-screen EmptyState with "Retry" button.
- **Logging**: Log status code (if any) and endpoint.

## 2. Authentication Errors

- **Category**: `AUTH_ERROR`
- **Trigger**: Expired session, invalid credentials, unauthorized access.
- **UX Pattern**: Redirect to Login screen with a "Session expired" message.
- **Logging**: Log the reason (e.g., `JWT_EXPIRED`).

## 3. API / Business Logic Errors

- **Category**: `API_ERROR`
- **Trigger**: 400/500 responses from Supabase or AI providers.
- **UX Pattern**: Inline error message or Modal explaining the issue (e.g., "AI provider is busy").
- **Logging**: Log the full response body (scrubbed of PII) and status code.

## 4. Permission Errors

- **Category**: `PERMISSION_ERROR`
- **Trigger**: User denied Camera or MediaLibrary access.
- **UX Pattern**: Modal with "Open Settings" button.
- **Logging**: Log which permission was denied.

## 5. Subscription / IAP Errors

- **Category**: `PAYMENT_ERROR`
- **Trigger**: RevenueCat purchase failure, restore failure.
- **UX Pattern**: Alert with specific error message (e.g., "Payment cancelled").
- **Logging**: Log the RevenueCat error code.

## 6. Unexpected Runtime Errors

- **Category**: `RUNTIME_ERROR`
- **Trigger**: JS crashes, undefined is not a function.
- **UX Pattern**: Global Error Boundary (Fallback UI).
- **Logging**: Full stack trace to Sentry/Bugsnag.
