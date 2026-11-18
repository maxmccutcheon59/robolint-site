# Security

Report vulnerabilities to MaxMcCutcheon1@outlook.com. Please include steps to reproduce. Expect an acknowledgement within a few days.

## Scope
Static site: no backend, no forms, no cookies, no analytics, no third-party scripts or fonts.

## Controls
- CSP via `<meta http-equiv>`: `default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'`. No inline scripts or styles.
- `referrer` meta: `strict-origin-when-cross-origin`.
- All external links use `rel="noopener noreferrer"`.
- No secrets in the repo; `.gitignore` excludes `.env*` and key files.
- Limits: GitHub Pages can't set response headers, so `frame-ancestors`, HSTS, `X-Content-Type-Options`, and `Permissions-Policy` can't be set from a meta tag there. If those matter, front the site with a host that supports custom headers (for example Cloudflare Pages `_headers`).

## Incident response (basic)
1. If a secret is ever committed, rotate it first, then purge history.
2. If the site is defaced, revert to the last good commit and redeploy; review repo access and tokens.
