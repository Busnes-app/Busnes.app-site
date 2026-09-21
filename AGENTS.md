# Busnes.app public site

## Purpose

The launch website presents Busnes.app as a focused software studio, with Ky as its reusable foundation and the Ky applications as proof of work.

## Ownership

- `index.html` owns the public narrative and links to the maintained KyPost site.
- `apps.html` owns the app directory; `kypost.html`, `kyyard.html`, `kynotes.html`, `kyvault.html`, `kyidentity.html`, and `kyrecovery.html` explain each product, availability, setup requirements and documentation.
- `how-it-works.html` and `about.html` explain the engagement and company; `pages.css` supplies their shared layouts and product-page styles.
- `styles.css` owns the visual system and responsive layout.
- `privacy.html` and `privacy.css` own the company privacy notice.
- `busnes-icon.png` is the selected Systems stamp brand mark and standalone GitHub avatar; `busnessB.png` is retained as the original artwork.
- `kypost-icon.png`, `kyyard-icon.png`, `kynotes-icon.png`, `kyvault-icon.png`, `kyidentity-icon.png`, and `kyrecovery-icon.png` are standalone project artwork exports. Consult `project-icon-prompts.md` when regenerating or extending this icon family.

## Local Contracts

- Keep the site static and dependency-light.
- Brand direction: 1970s bespoke-software consultancy; use the selected charcoal-and-cream Systems stamp B with square image proportions.
- Use KyIdentity as the public name of the identity product (formerly KySignOn), including when source repositories use the older name.
- Do not invent customer outcomes; label reference builds accurately.
- Source product capabilities and requirements from their maintained repositories. Distinguish planned work from implemented features; link to product documentation for installation and current release details.
- Keep KyPost-specific product details aligned with the maintained KyPost policy.
- Preserve accessible headings, skip navigation, visible focus states, and responsive behavior.
- Favor expressive graphics and subtle CSS motion; provide a pause control and honor reduced-motion preferences.

## Work Guidance

- Use the strategy in `deep-research-report.md` as the content source.
- Prefer plain HTML and CSS before adding JavaScript or a build system.
- Do not add analytics, embedded third-party content, or intake storage to the static launch site.

## Verification

- Serve the folder with a local static server and check the page at desktop and mobile widths.
- Check HTML for broken local links and inspect the console/network output when using a browser preview.

## Child DOX Index

None.
