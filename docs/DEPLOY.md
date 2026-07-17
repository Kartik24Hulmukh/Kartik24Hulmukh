# Deployment

## Before pushing

1. Back up the existing `Kartik24Hulmukh/Kartik24Hulmukh` repository with a branch or tag.
2. Review every statement in `docs/data/evidence.json`.
3. Remove old Build Console and Verified Noticeboard files that are not in this package.
4. Copy the complete contents of this package—including `.github`—to the repository root.

## Local validation

```bash
python scripts/render_profile.py
python scripts/validate.py
python -m http.server 8000 --directory docs
```

Open `http://localhost:8000` and inspect:

- desktop and mobile widths;
- keyboard-only navigation;
- Simple view;
- Reduce motion;
- Sound opt-in;
- each project strand;
- each controlled challenge;
- the direct project index;
- all external links.

## Push

```bash
git add -A
git commit -m "feat(profile): launch the Proof Loom"
git push origin main
```

## GitHub Pages

In repository Settings → Pages, select **GitHub Actions** as the source. The included `pages.yml` workflow uploads and deploys the `docs` directory.

Expected URL:

`https://kartik24hulmukh.github.io/Kartik24Hulmukh/`

If Pages is not yet live, temporarily change the two prominent experience links in `README.md` so they do not lead to a broken route.

## Labels

Create these labels if they do not exist:

- `evidence/challenge`
- `evidence/reproduction`
- `needs-triage`
- `needs-review`

If labels cannot be created, remove unavailable labels from the issue-form YAML before deployment so form creation is not blocked.

## Final public checks

- Signed-out profile view
- Light and dark README artwork
- Pages deployment
- Mobile controls
- Browser console
- GitHub Actions validation
- No stale Build Console or Verified Noticeboard references
- No secrets in current files or Git history
