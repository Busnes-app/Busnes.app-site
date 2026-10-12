# Busnes.app public site

## Purpose

The launch website presents Busnes.app as a focused software studio, with Ky as its reusable foundation and the Ky applications as proof of work.

## Ownership

- `index.html` owns the public narrative and links to the maintained KyPost site.
- `apps.html` owns the app directory; `kypost.html`, `kyyard.html`, `kynotes.html`, `kycalendar.html`, `kydrive.html`, `kymessages.html`, `kyidentity.html`, `kyrecovery.html`, `kydns.html`, and `kypulse.html` explain each product, availability, setup requirements and documentation.
- `how-it-works.html` and `about.html` explain the engagement and company; `pages.css` supplies their shared layouts and product-page styles.
- `styles.css` owns the visual system and responsive layout, including the light and dark token sets.
- `theme.js` is the site's only script: it applies the stored or OS colour scheme before first paint and wires the header theme switch. No inline scripts; every page's CSP allows same-origin scripts only.
- `privacy.html` and `privacy.css` own the company privacy notice; `privacy.css` holds policy layout only and depends on `styles.css` for tokens, header, footer and nav.
- `404.html` is the not-found page; point the host's 404 handler at it.
- `prototype-light-systems.html` is a retained design prototype; it is not linked, not served as part of the site, and not kept in sync.
- `busnes-icon.png` is the Systems stamp brand mark master (1254px) and the GitHub avatar; `kypost-icon.png`, `kyyard-icon.png`, `kynotes-icon.png`, `kyidentity-icon.png`, `kyrecovery-icon.png`, `kydns-icon.png`, `kyauth-icon.png`, `kypulse-icon.png`, `kycalendar-icon.png`, `kydrive-icon.png` and `kymessages-icon.png` are the product icon masters in the same family. Consult `project-icon-prompts.md` when regenerating or extending the family.
- `icons/` holds the web exports (256px, badge cropped to a transparent canvas) the pages actually load: `icons/busnes.png` for the favicon, header and footer mark; `icons/<product>.png` for the directory card, the product-page hero and favicon, and the home foundation bar. Every product shown anywhere on the site uses its `icons/` file, never a glyph or a colour tile. Regenerate with the command in `project-icon-prompts.md`.

## Local Contracts

- Keep the site static and dependency-light.
- Brand direction: 1970s bespoke-software consultancy; use the selected charcoal-and-cream Systems stamp B with square image proportions.
- Use KyMessages (not the repository name KyMessage) as the public name of the chat product.
- Use KyIdentity as the public name of the identity product (formerly KySignOn), including when source repositories use the older name.
- Do not invent customer outcomes; label reference builds accurately.
- Source product capabilities and requirements from their maintained repositories. Distinguish planned work from implemented features; link to product documentation for installation and current release details.
- Keep KyPost-specific product details aligned with the maintained KyPost policy.
- Preserve accessible headings, skip navigation, visible focus states, and responsive behavior.
- Keep motion to short hover and focus transitions and honor reduced-motion preferences. If continuous animation is ever added, it needs a pause control.
- One accent: orange. Small orange or grey label text uses the `--orange-text` and `--light` tokens, which meet AA at 11px; `--orange` is for glyphs, dots and rules.
- Dark mode follows `prefers-color-scheme` and the header switch stores an override in localStorage as `html[data-theme]`. Never hardcode a colour outside the two `:root` token blocks; the dark values appear twice (media query and `data-theme`) and must stay identical. Icons are the light masters inverted with `--icon-filter`.
- Interior pages take `body class="interior"` and load `pages.css` after `styles.css`. All pages share the single header rule set in `styles.css`, including the mobile layout under 680px.
- Every page carries canonical, Open Graph and Twitter card metadata pointing at `https://busnes.app/`; product pages use their own icon as the share image.

## Work Guidance

- Use the strategy in `deep-research-report.md` as the content source.
- Prefer plain HTML and CSS before adding JavaScript or a build system. The theme switch is the one accepted script; keep it dependency-free and keep every page working without it.
- Do not add analytics, embedded third-party content, or intake storage to the static launch site.

## Verification

- Product theme behavior is owned and tested by the sibling `ky-ui` repository (`npm test`); each app verifies its vendored copy with `node <ky-ui dir>/check-vendor.mjs`.

- Serve the folder with a local static server and check the page at desktop and mobile widths.
- Check HTML for broken local links and inspect the console/network output when using a browser preview.
- Run `~/.claude/skills/impeccable/scripts/impeccable detect --json *.html` for mechanical design findings; cream-palette, kicker and section-number findings are accepted brand choices.

## Child DOX Index

None.

- `project-icon-prompts.md` owns icon prompts and platform export contracts. `kypulse-icon.svg`, `kycalendar-icon.svg`, `kydrive-icon.svg` and `kymessages-icon.svg` are the sources for the hand-drawn masters.
- `screenshots/` holds product screenshots, in the Busnes Light theme unless a caption says otherwise, captured from local builds with fictional data only.
- `icon-rollout.md` and `theme-audit.md` are dated 2026-09-24 records; repositories they name have since been renamed or archived.
