# Deploy in under five minutes

1. Back up the current `Kartik24Hulmukh/Kartik24Hulmukh` repository.
2. Copy every file in this package to the repository root.
3. Review `data/projects.json`, `data/claims.json`, and all public role language.
4. Run:
   ```bash
   python scripts/render_now.py
   python scripts/render_assets.py
   python scripts/validate.py
   ```
5. Commit and push to `main`.
6. In repository Settings → Actions → General, allow workflows to read and write repository contents if the refresh workflow cannot push.
7. Run **Verify profile**, then manually run **Refresh profile evidence**.
8. Check the signed-out profile on desktop and mobile, in light and dark mode.

## Important first-week work
- Fix RGIT Rozgar's failing CI before presenting it as stable.
- Rename `unified-experience` to a product-aligned repository name if redirects and deployment permits.
- Add a repository description and social preview to RGIT Rozgar.
- Clarify Kairo's upstream relationship everywhere.
- Publish releases only when a real release exists; never fabricate one for the profile.

## Optional real demo reel
Record a 12–18 second, silent, captioned GIF showing only real product behavior: RGIT Rozgar flow, a Kairo receipt and verification, X-Ray evidence view, and a Proving Grounds capsule. Save as `assets/build-reel.gif`, then place it below the hero. Do not use mock screens or generated product footage.
