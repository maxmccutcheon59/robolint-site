# Compliance notes (for human/lawyer review): DRAFT

## Data inventory
| Data | Collected? | Notes |
|---|---|---|
| Cookies / local storage | No | none set |
| Analytics / trackers | No | none |
| Forms / email capture | No | CTA is a `mailto:` link only |
| Third-party requests | No | CSP blocks all non-self loads; no CDNs, no external fonts |
| Server logs | Host-dependent | GitHub Pages (or another host) may keep standard access logs; outside our control |
| Email sent via mailto | Yes, by the visitor's own mail client | Goes to MaxMcCutcheon1@outlook.com; used only to reply |

## Items flagged for review before going live
1. **Privacy note** in the footer is a short DRAFT ("this site collects nothing…"). Not a full privacy policy. Get it reviewed before any data collection is added.
2. **Paid pilot offer.** Pricing is "scoped by email"; no terms of service exist yet. Before taking money: decide the legal entity (none is claimed on the site), and draft a simple services agreement / terms, invoicing, and taxes. Pilots that receive **private customer datasets** need a written data-handling agreement (access, storage, retention, deletion, confidentiality/NDA). The site says only that "how data gets shared" is agreed by email before work starts.
3. **Third-party dataset names.** The audit table names public Hugging Face datasets and their owners, with findings taken from AUDIT.md. The wording is factual and carries the caveat "findings are a starting point for review, not a verdict" plus an issue link for maintainers. Keep it that way; don't add disparaging language.
4. **Trademarks.** "LeRobot" and "Hugging Face" are referenced descriptively (nominative use), with no logos used.
5. **Accessibility.** Semantic headings, skip link, focus-visible styles, high-contrast palette, scrollable table region with a caption. A full WCAG 2.2 AA audit hasn't been done.
6. **Possible offer mismatch.** The HF Space currently offers "free for early teams" dataset audits by email, and this site offers *paid* pilots. Max should make the two consistent before launch.

## Publishing (only after Max explicitly says yes)
Free GitHub Pages on a personal account needs a **public** repo.
- Option A, GitHub Pages: `gh repo edit maxmccutcheon59/robolint-site --visibility public --accept-visibility-change-consequences`, then `gh api -X POST repos/maxmccutcheon59/robolint-site/pages -f 'source[branch]=main' -f 'source[path]=/docs'`. Live at https://maxmccutcheon59.github.io/robolint-site/ (matches canonical/OG URLs). Remove the "Preview draft" banner first.
- Option B, keep the repo private: deploy `docs/` to Cloudflare Pages (free; also supports a `_headers` file for HSTS/frame-ancestors) or Netlify. If you do, update `canonical`, `og:url`, and `og:image` to the new URL.
