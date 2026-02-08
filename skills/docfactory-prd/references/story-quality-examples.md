# Story Quality Examples

## 🔴 Bad Examples (Avoid These)

### 1. The "And" Chain

**Story:** As a user I want to upload a photo and select a style and see the results and save them.
**Why it's bad:** Too big. This is an entire epic, not a story. It's impossible to estimate or test as a single unit.

### 2. The Vague Requirement

**Story:** As a user I want the upload to work correctly.
**Why it's bad:** What does "correctly" mean? Does it handle large files? Does it show progress? Does it handle network failures?

### 3. Missing Acceptance Criteria

**Story:** As a job seeker I want to see my history.
**Why it's bad:** No checkboxes. No mention of empty states. No mention of thumbnails vs full images.

---

## 🟢 Good Examples (Do These)

### 1. Atomic & Specific

**Story:** As a job seeker I want to upload a single selfie so that it can be processed by the AI.
**Acceptance Criteria:**

- [ ] User can pick an image from the camera roll.
- [ ] App requests `MediaLibrary` permissions gracefully if not granted.
- [ ] Upload progress is shown as a percentage or progress bar.
- [ ] Success redirects user to the Style Selection screen.

### 2. Includes Edge Cases

**Story:** As a job seeker I want to see my generation history so I can re-download previous results.
**Acceptance Criteria:**

- [ ] History list shows generations ordered by date (newest first).
- [ ] **Empty State:** If no generations exist, show a "Start your first generation" CTA.
- [ ] **Loading State:** Show skeletons while fetching from Supabase.
- [ ] **Error State:** Show "Failed to load history" with a "Retry" button.
- [ ] Each row shows a thumbnail and the style name used.

### 3. Verifiable Acceptance Criteria

**Story:** As a user I want to restore my previous purchases so I don't lose access on a new device.
**Acceptance Criteria:**

- [ ] "Restore Purchases" button is visible on the Paywall and Settings.
- [ ] Tapping "Restore" triggers the RevenueCat restore flow.
- [ ] Success shows a "Purchases Restored" toast and unlocks Pro features.
- [ ] Failure shows a specific error message (e.g., "No purchases found").
