# Deploy the Verified Noticeboard

1. Create a rollback tag for the current profile repository.
2. Copy this entire package to the repository root, replacing the Build Console design.
3. Review `data/projects.json`, `data/claims.json`, and all public role language.
4. Run:
   ```bash
   python scripts/render_editorial.py
   python scripts/validate.py
   python -m py_compile scripts/*.py
   ```
5. Commit and push to `main`.
6. In Settings → Pages, deploy from the `main` branch `/docs` folder.
7. In Settings → Actions → General, allow GitHub Actions to create and approve pull requests / read and write contents if the refresh workflow cannot push.
8. Run **Verify profile**, then manually run **Refresh profile evidence**.
9. Confirm `https://kartik24hulmukh.github.io/Kartik24Hulmukh/` loads before treating the Evidence Atlas as live.
10. Check the signed-out profile on desktop and mobile, in light and dark mode.

## Important first-week work
- Fix RGIT Rozgar's failing Deploy workflow before presenting it as stable (do not weaken tests).
- Rename `unified-experience` to a product-aligned repository name if redirects and deployment permit.
- Add a repository description and website link to RGIT Rozgar and Project X-Ray India.
- Clarify Kairo's upstream relationship everywhere.
- Publish releases only when a real release exists; never fabricate one for the profile.

## Optional real demo reel
Record a 12–18 second, silent, captioned GIF showing only real product behavior. Save as `assets/build-reel.gif` only if authentic. Do not use mock screens or generated product footage.

Do not reintroduce terminal UI, cyan dashboards, generic cards, badge walls, generated praise, or unsupported impact claims.
