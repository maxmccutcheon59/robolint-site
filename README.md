# robolint-site (PRIVATE PREVIEW, NOT PUBLISHED)

Static product site for [robolint](https://github.com/maxmccutcheon59/robolint), the open-source (MIT) quality checker for LeRobot v2/v3 datasets.

**Status:** draft preview. Do not enable GitHub Pages or deploy anywhere until Max McCutcheon explicitly approves.

## Layout
- `docs/`: the whole site (plain HTML/CSS, one tiny optional `copy.js` for copy buttons). Relative asset paths, so it works at a GitHub Pages project path (`/robolint-site/`).
- `build_table.py`: regenerates the audit results table in `docs/index.html` from the AUDIT.md numbers (asserts 18 datasets / 4,218 episodes).

## Preview locally
```bash
cd docs && python3 -m http.server 8765 --bind 127.0.0.1
# open http://127.0.0.1:8765/
```

## Content sources
Every number and claim comes from the robolint repo: `README.md`, `AUDIT.md`, `datasets.txt`, `pyproject.toml` (version 0.1.0), and `robolint --help`. The terminal sample in the hero is copied verbatim from the robolint README (test dataset with injected faults). No customers, logos, testimonials, or traffic numbers.

## Third-party assets
None. System font stack; favicon, OG image, and CSS are original to this repo. Data in the audit table comes from robolint's AUDIT.md (MIT, © Max McCutcheon).

## Publish (only after Max says yes)
See "Publishing" in `COMPLIANCE_NOTES.md`.
