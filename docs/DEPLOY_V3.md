# Deploy the Verified Noticeboard

1. Create a rollback tag for the current profile repository.
2. Copy this entire package to the repository root, replacing the current README and Build Console assets.
3. Run `python scripts/render_editorial.py` and `python scripts/validate.py`.
4. Commit and push.
5. In Settings → Pages, deploy from the `main` branch `/docs` folder.
6. Confirm `https://kartik24hulmukh.github.io/Kartik24Hulmukh/` loads before keeping the Evidence Atlas link prominent.
7. Inspect the README signed out, on mobile, and in both color themes.

Do not reintroduce terminal UI, cyan dashboards, generic cards, badge walls, generated praise, or unsupported impact claims.