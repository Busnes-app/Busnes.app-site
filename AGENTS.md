# Busnes.app public site

## Purpose

The launch website presents the Ky Suite: small self-hosted apps that share one sign-in (KyIdentity) and one sealed backup store (KyRecovery). Busnes.app custom work is secondary and lives under "Custom work" (`how-it-works.html`).

## Ownership

- `tests/test_site.py` and `.github/workflows/site.yml` own the dependency-free checks for root-page references; generated documents and visual/behavioral acceptance stay outside that check's scope. `CHANGELOG.md` records notable source revisions identified by Git commit SHA.
- `README.md`, `CONTRIBUTING.md` and `LICENSE.txt` own repository setup, contribution guidance and source licensing. `SECURITY.md` owns private reporting and the security boundary of this website; product security remains in each product's repository.
- `index.html` owns the public narrative: the suite pitch, the launch-series trailer card (a plain link to the YouTube video with a self-hosted thumbnail, `share/trailer-thumb.jpg`; never an embedded player), the five reasons, the KyIdentity/KyRecovery diagram and the status board. Status labels are `In daily use` and `Tested`; every `status-pill` on `apps.html` and the product pages reads `Open source (MIT) · <label>` with the same label as the board.
- `install.html` owns the three installation paths (KyQuickStart AI, KyQuickStart, one app at a time). Copy commands from those repositories' READMEs; do not invent flags.
- Every page shares the primary navigation Apps · Install · Custom work · About with a GitHub button, and the same footer links (including Privacy policy and Security).
- `apps.html` owns the app directory; `kypost.html`, `kyyard.html`, `kynotes.html`, `kycalendar.html`, `kydrive.html`, `kymessages.html`, `kyidentity.html`, `kyrecovery.html`, `kydns.html`, and `kypulse.html` explain each product, availability, setup requirements and documentation.
- `how-it-works.html` and `about.html` explain the engagement and company; `pages.css` supplies their shared layouts and product-page styles.
- `styles.css` owns the visual system and responsive layout, including the light and dark token sets.
- `theme.js` is the site's only script: it applies the stored or OS colour scheme before first paint and wires the header theme switch. No inline scripts; every page's CSP allows same-origin scripts only.
- `privacy.html` and `privacy.css` own the company privacy notice; `security.html` owns the per-app security summary (what each app protects, what the server can see, third parties, unproven parts, how to report) and reuses `privacy.css`. Source every security claim from the app's own SECURITY.md, docs or code on its default branch, and never claim an audit until one exists. `privacy.css` holds policy layout only and depends on `styles.css` for tokens, header, footer and nav.
- `share/` holds the social share cards (`home.png` for `index.html`, `custom-work.png` for `how-it-works.html`, otherwise the page's own name) and `share/build.py`, which renders them with headless Chrome. Edit its `CARDS` table and rerun `python3 -I share/build.py` when a page title, tagline or status label changes.
- `404.html` is the not-found page; point the host's 404 handler at it.
- `prototype-light-systems.html` is a retained design prototype; it is not linked, not served as part of the site, and not kept in sync.
- `busnes-icon.png` is the Systems stamp brand mark master (1254px) and the GitHub avatar; `kypost-icon.png`, `kyyard-icon.png`, `kynotes-icon.png`, `kyidentity-icon.png`, `kyrecovery-icon.png`, `kydns-icon.png`, `kyauth-icon.png`, `kypulse-icon.png`, `kycalendar-icon.png`, `kydrive-icon.png` and `kymessages-icon.png` are the product icon masters in the same family. Consult `project-icon-prompts.md` when regenerating or extending the family.
- `icons/` holds the web exports (256px, badge cropped to a transparent canvas) the pages actually load: `icons/busnes.png` for the favicon, header and footer mark; `icons/<product>.png` for the directory card, the product-page hero and favicon, and the home foundation bar. Every product shown anywhere on the site uses its `icons/` file, never a glyph or a colour tile. Regenerate with the command in `project-icon-prompts.md`.

## Local Contracts

- Keep the site static and dependency-light.
- Brand direction: 1970s bespoke-software consultancy; use the selected charcoal-and-cream Systems stamp B with square image proportions.
- Use KyMessages (not the repository name KyMessage) as the public name of the chat product.
- Use KyIdentity as the public name of the identity product (formerly KySignOn), including when source repositories use the older name.
- Do not invent customer outcomes; label reference builds accurately. Screenshots from local builds use fictional data and do not establish current release availability or functional acceptance.
- Source product capabilities and requirements from their maintained repositories. Distinguish planned work from implemented features; link to product documentation for installation and current release details. Keep directory summaries, product pages and their social metadata aligned. Use existing README entry points for cross-repository links so independent documentation merges do not create unavailable installation URLs.
- Keep KyPost-specific product details aligned with the maintained KyPost policy.
- Preserve accessible headings, skip navigation, visible focus states, and responsive behavior.
- Keep motion to short hover and focus transitions and honor reduced-motion preferences. If continuous animation is ever added, it needs a pause control.
- One accent: orange. Small orange or grey label text uses the `--orange-text` and `--light` tokens, which meet AA at 11px; `--orange` is for glyphs, dots and rules.
- Dark mode follows `prefers-color-scheme` and the header switch stores an override in localStorage as `html[data-theme]`. Never hardcode a colour outside the two `:root` token blocks; the dark values appear twice (media query and `data-theme`) and must stay identical. Icons are the light masters inverted with `--icon-filter`.
- Interior pages take `body class="interior"` and load `pages.css` after `styles.css`. All pages share the single header rule set in `styles.css`, including the mobile layout under 680px.
- Every page carries canonical, Open Graph and Twitter card metadata pointing at `https://busnes.app/`; the share image is that page's 1200x630 card in `share/` with `summary_large_image`.

## Work Guidance

- Use the strategy in `deep-research-report.md` as the content source.
- Prefer plain HTML and CSS before adding JavaScript or a build system. The theme switch is the one accepted script; keep it dependency-free and keep every page working without it.
- Do not add analytics, embedded third-party content, or intake storage to the static launch site.

## Verification

- Run `python3 -m unittest discover -s tests -v`. Add regression checks with major new functionality and update `CHANGELOG.md` for user-visible or security-related changes.
- Product theme behavior is owned and tested by the sibling `ky-ui` repository (`npm test`); each app verifies its vendored copy with `node <ky-ui dir>/check-vendor.mjs`.

- Serve the folder with a local static server and check the page at desktop and mobile widths.
- Check HTML for broken local links and inspect the console/network output when using a browser preview.
- Run `~/.claude/skills/impeccable/scripts/impeccable detect --json *.html` for mechanical design findings; cream-palette, kicker and section-number findings are accepted brand choices.

## Child DOX Index

None.

- `project-icon-prompts.md` owns icon prompts and platform export contracts. `kypulse-icon.svg`, `kycalendar-icon.svg`, `kydrive-icon.svg` and `kymessages-icon.svg` are the sources for the hand-drawn masters.
- `screenshots/` holds product screenshots, in the Busnes Light theme unless a caption says otherwise, captured from local builds with fictional data only.
- `icon-rollout.md` and `theme-audit.md` are dated 2026-09-24 records; repositories they name have since been renamed or archived.
