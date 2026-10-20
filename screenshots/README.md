# Product screenshots

Refreshed 20 October 2026: ten products, desktop and phone. These are native browser captures of real application interfaces with fictional local data. No application markup or CSS was replaced for the images. Appearance varies by revision; captures are not release, delivery, uptime or recovery acceptance evidence.

The nine suite products were captured from the updated installation’s executables on 19 October, using separate fixture data directories. All nine source executable hashes were rechecked against the current running installation on 20 October and match. KyDNS was captured from source revision `7faa1480` on 20 October with a loopback-only fixture; it was not part of the nine-product installed campaign. No host DNS, DHCP or installed settings were changed.

Desktop images are 1280×800. Phone images are 780×1688, the native output of a 390×844 CSS-pixel viewport. WebP exports preserve the original dimensions, strip metadata and use quality 90. `manifest.json` records output, source-PNG and installed-executable SHA-256 hashes. Public files contain no fixture credentials or actual installation account addresses.

| Product | Scene |
|---|---|
| KyCalendar | Shared calendars with a generated October schedule; month view on desktop and agenda on phone. |
| KyDrive | A workspace of sample briefs, documents and schedules uploaded to the local fixture. |
| KyIdentity | Alex Morgan’s application launcher with eight example Ky connections. |
| KyMessages | The Agents operator console with three generated agent records. This is the management interface, not a chat conversation. |
| KyNotes | An encrypted Studio notebook with fictional launch notes and planning pages. |
| KyPost | An unsent launch-review message with an example.com recipient and a sample creative brief attached. |
| KyPulse | Eight sample health sources. Displayed availability and latency are generated demonstration data. |
| KyRecovery | The recovery overview with generated capsule metadata and custodians. The sample entries are not recoverable backups. |
| KyYard | The fleet overview with generated Docker and Kubernetes inventory. No real agents or clusters are represented. |
| KyDNS | The service directory with eight fictional names and documentation-only IP addresses. Health checks are unconfigured; the phone view shows the scrollable table. |

KyDNS’s service table scrolls horizontally on a phone; the capture preserves this current behavior. KyMessages shows the operator console rather than Element or calls. KyPost shows an unsent draft, not delivered or signed mail.
