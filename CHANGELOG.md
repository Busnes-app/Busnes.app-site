# Website changes

The website is distributed as source. A full Git commit SHA identifies each
revision; no packaged or SemVer-tagged releases are currently published.

## Unreleased

- Add the KyDash gauge icon (`kydash-icon.svg`, `kydash-icon.png`, `icons/kydash.png`) to the
  icon family. KyDash is an internal tool, so no page shows it.
- Link the @busnesapp@mastodon.social account in every page footer, with
  `rel="me"` so Mastodon can verify the site.
- Point the Bluesky footer link at the new `@busnes.app` handle.
- Add public, dependency-free checks for root-page links and local assets,
  including a guard against misspelled suite repository links, and run them in CI.
- Document the website interface, verification command and source-version policy.

## 2026-10-25

- Publish the existing suite MIT license in this repository.
- Add local-preview and contribution guidance and a website-specific private
  vulnerability-reporting policy.
