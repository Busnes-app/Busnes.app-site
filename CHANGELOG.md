# Website changes

The website is distributed as source. A full Git commit SHA identifies each
revision; no packaged or SemVer-tagged releases are currently published.

## Unreleased

- Bring every page in line with the apps' default branches as of 2026-11-03:
  - KyAuth is on Google Play and the App Store, and its Android pushes are now end-to-end encrypted.
  - KyIdentity uses its own KyAuth relays by default, and KyPost's relays moved to `*.relay.kypost.busnes.app`.
  - KyPost has published Android releases, device approval and contact-sync consent; the iPhone tip jar was removed.
  - KyDrive Desktop is released, and KyCalendar invitations through KyPost now work.
  - KyMessages has calls on by default and an optional meeting-notes bot.
  - KyRecovery restores with each app's own command.
  - KyDNS lost its health-check UI and gained an MCP agent endpoint.
  - KyQuickStart publishes releases, and KyQuickStart AI supports Kubernetes clusters.
  - KyPulse is now spelled with a capital K.
  - The privacy policy names every AI agent integration.
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
