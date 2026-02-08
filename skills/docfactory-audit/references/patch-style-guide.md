# Patch Style Guide (for Proposed Patches)

Principles:

- Keep patches small and localized
- Prefer explicit edits over vague recommendations
- Use the doc’s existing headings; avoid reorganizing unless necessary
- When proposing text, keep it copy-pasteable

Formats:

1. Bullet edits:
   - Change X to Y in section Z
2. Mini diff-like blocks:
   - Before:
     - ...
   - After:
     - ...

Avoid:

- Writing new code
- Introducing new features
- Large rewrites unless the doc is structurally broken
