# UX Philosophy (Mobile)

## 1. Content-First Design

The content (the headshot, the styles) is the hero. The UI should be a quiet, consistent frame.

- Use high-quality imagery.
- Minimize borders and heavy shadows.
- Use whitespace to separate sections, not lines.

## 2. Progressive Disclosure

Don't overwhelm the user. Show only what is necessary for the current step.

- Hide advanced settings behind a "More" or "Settings" icon.
- Use multi-step flows (e.g., Upload -> Style -> Results) rather than one long form.

## 3. Single Primary Action

Every screen should have one clear, primary CTA (Call to Action).

- Use the `primary` color for the main action.
- Use `secondary` or `ghost` for destructive or secondary actions.
- Place the primary CTA in a consistent location (usually bottom-aligned on mobile).

## 4. Visual Hierarchy

Guide the user's eye through the screen.

- **Primary**: High contrast, bold typography, primary color.
- **Secondary**: Medium contrast, regular typography, secondary color.
- **Tertiary**: Low contrast, muted text, ghost/link variants.

## 5. Micro-Copy Basics

The words in the UI are as important as the pixels.

- **Button Labels**: Use verbs (e.g., "Generate Headshots", not "Submit").
- **Empty States**: Don't just say "No data". Explain _why_ and provide a CTA (e.g., "You haven't generated any headshots yet. Start now!").
- **Error Messages**: Be helpful, not technical. Explain the issue and how to fix it (e.g., "Upload failed. Please check your internet connection and try again.").

## 6. Platform-Adaptive Design

Respect the conventions of the platform while maintaining product identity.

- **Navigation**: Use platform-standard back button behavior (iOS swipe-to-back vs Android hardware/gesture back).
- **System UI**: Account for the status bar and system navigation bar (especially on Android).
- **Typography**: Use platform-standard fonts (San Francisco on iOS, Roboto on Android) or a highly legible cross-platform font.

## 7. Haptics & Feedback

Provide physical confirmation for digital actions.

- **Success**: Light haptic on completion.
- **Error**: Distinct haptic on failure.
- **Action**: Subtle haptic on button press.
