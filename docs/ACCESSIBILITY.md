# Accessibility and fallback contract

- The complete project index is semantic HTML and is canonical.
- A skip link bypasses the interactive canvas.
- The canvas is keyboard operable and has an accessible label.
- Every essential project statement, role, link, evidence item, and limitation exists outside the canvas.
- The experience honors `prefers-reduced-motion` and provides a persistent manual motion toggle.
- Audio is off by default and requires a user gesture.
- No information depends on sound or color alone.
- Buttons meet a 44px target size on normal layouts.
- Focus states are visible.
- Mobile users receive the same evidence and project links.
- If the manifest or canvas fails, visitors can continue through the direct index and GitHub README.

Before release, perform manual keyboard testing and a screen-reader smoke test in addition to automated checks.
