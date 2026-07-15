# Implementation guide

1. Back up the current `Kartik24Hulmukh/Kartik24Hulmukh` repository.
2. Create a branch named `profile-redesign`.
3. Copy this package into the repository root.
4. Review `data/projects.json` and correct repository names, branches, and lifecycle labels.
5. Review every sentence in `README.md`; remove anything Kartik cannot explain or prove.
6. Run:

```bash
python3 scripts/validate_profile.py
python3 scripts/render_profile.py
python3 scripts/render_status_svg.py
```

7. Inspect the rendered README in GitHub's preview.
8. Verify light and dark readability of `assets/mission-control.svg`.
9. Test both issue forms in a temporary repository or draft pull request.
10. Confirm workflow permissions are limited to what is required.
11. Open a pull request with screenshots and a before/after summary.
12. Do not merge until links, metrics, roles, maturity labels, and current projects are manually confirmed.

## Repository cleanup before pinning

- Explain Kairo-Phantom's fork and maintainer relationship.
- Use one maturity label consistently.
- Rename `unified-experience` to a product-aligned name if feasible.
- Archive the older duplicate BErozgar repository and link to the maintained successor.
- Fix local `file:///` links.
- Remove adversarial prompt content from Proving Grounds' main README and store fixtures under a clearly labeled test path.
- Publish actual GitHub Releases before advertising version numbers.
- Add demos, social previews, security policies, contribution guides, and issue forms to pinned repositories.

## Suggested pin order

1. Kairo-Phantom
2. Project X-Ray India
3. RGIT Rozgar
4. Proving Grounds
5. One publicly released systems project
6. One meaningful external contribution

Leave weak slots empty rather than pinning scaffolds or unexplained forks.
