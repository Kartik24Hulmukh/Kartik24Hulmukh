# Deploy Systems in Motion

1. Back up the current `Kartik24Hulmukh/Kartik24Hulmukh` default branch with a remote branch or tag.
2. Extract this ZIP and copy every file—including `.github`—to the repository root.
3. Remove files from superseded profile designs that are not present in this package.
4. Review `docs/data/projects.json` and keep every role, maturity label, and boundary accurate.
5. Run:

```bash
python scripts/render_assets.py
python scripts/validate.py
node --check docs/app.js
python -m http.server 8000 --directory docs
```

6. Test desktop, 390px mobile, keyboard navigation, motion toggle, all three mechanisms, direct project index, repository links, and browser console.
7. Commit and push:

```bash
git add -A
git commit -m "feat(profile): launch Systems in Motion"
git push origin main
```

8. In Settings → Pages, choose **GitHub Actions**. The included workflow deploys `docs/`.
9. Verify the signed-out profile and `https://kartik24hulmukh.github.io/Kartik24Hulmukh/`.

## Rollback

Reset through a normal revert commit or restore the backup branch. Never force-push shared history.
