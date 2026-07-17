# Security notes

- Runtime data is local, static, and repository-owned.
- No user-controlled issue, pull-request, branch, or commit text is executed.
- The Pages workflow has only `contents: read`, `pages: write`, and `id-token: write`.
- The validation workflow has `contents: read` only.
- The application makes no authenticated API calls and stores no credentials.
- Evidence strings are escaped before insertion into generated HTML.
- The public manifest contains no private URLs or student data.
- Sound is generated locally with Web Audio after explicit user opt-in.
- Challenge states are client-side explanatory controls and do not alter repositories.

Review workflow action versions and pin them to audited immutable SHAs if required by your security policy.
