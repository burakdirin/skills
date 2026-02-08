# Supabase RLS Checklist (MVP)

- RLS enabled on every user-owned table
- Policies for SELECT/INSERT/UPDATE/DELETE explicitly defined
- Use `auth.uid()` for per-user ownership checks
- Consider indexes on columns used in policies (e.g., `user_id`)
- Test with anon vs authenticated contexts
- Verify “defense in depth”: even if client is compromised, DB blocks cross-user access
