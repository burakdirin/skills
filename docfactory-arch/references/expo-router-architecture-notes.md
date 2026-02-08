# Expo Router Architecture Notes

- All screens/pages are files inside `app/`
- Root `app/_layout.tsx` defines top-level layout
- Layout files (`_layout.tsx`) define how routes inside a directory are arranged (stack/tabs/etc.)
- Non-navigation components should live outside `app/`
- Use route groups with parentheses like `(auth)` and `(tabs)`
