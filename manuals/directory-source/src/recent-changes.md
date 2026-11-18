# Recent changes — November 17, 2026

This review updates the suite overview and public site for changes since the November 3
site synchronization. It covers the public application/installer repositories, shared
libraries and documentation sites below. Internal application documentation stays private;
retired products, duplicate worktrees and unmerged feature branches are excluded.

Each source link pins the exact default-branch revision inspected. A source version or
merged feature does not establish that an app-store build, container deployment or
production acceptance has been completed. Use the release record for the artifact you
install. The table records reviewed source, not test execution by this documentation task.

## Changes by product

| Product | What changed or still needs care | Reviewed source |
| --- | --- | --- |
| KyIdentity | Replicas on shared PostgreSQL, suite groups, HR email reservation, forward-auth, and proof-based QR pairing/sign-on. | [ee3a59270ef8](https://github.com/Busnes-app/KyIdentity-server/blob/ee3a59270ef8404aae27062b64f617e9ea47df34/docs/HR-PROVISIONING.md) |
| KyPost Server | Native direct MX delivery remains opt-in; invitations/RSVP, Drive picker, chat, out-of-office, flagged-mail tasks, alert mail, and receiver/storage performance fixes landed. Existing relay settings remain supported. | [7b067ded42ca](https://github.com/Busnes-app/KyPost-Server/blob/7b067ded42ca0ede5f3efdfd649cd6ffc3be3cad/docs/DIRECT_DELIVERY.md) |
| KyCalendar | Tasks, planning/board/insights, booking pages, rooms/equipment, invitations, meeting rooms, file links and colleague status. SQLite capsule and PostgreSQL backup limits remain distinct. | [814feb8cb9ce](https://github.com/Busnes-app/KyCalendar/blob/814feb8cb9ce723916fa632e5f13e2b078215e8f/docs/SUITE-INTEGRATIONS.md) |
| KyDrive Server | Content/prefix/phrase search, Shared with me search, Drive picker and guest-link workflows, phone linking, required device signatures and signed TLS rollover. | [cb492e0a0200](https://github.com/Busnes-app/kydrive-server/blob/cb492e0a0200d0ed9d478f0c700fdc872074d2f6/docs/CLIENTS-AND-EDITOR.md) |
| KyMessages | Calendar meeting rooms and administrator-enabled guests, suite chat links, groups and member-only status from Calendar/OOO. Full Matrix/media setup is still required. | [a981652f57b6](https://github.com/Busnes-app/KyMessage-Server/blob/a981652f57b6abf2230b5199dcf0ad373bd91370/docs/KYCALENDAR.md) |
| KyNotes | Compatible dependency refresh and the published manual; recovery still needs the encrypted blob copy as well as metadata and user recovery material. | [ba93e8281b3f](https://github.com/Busnes-app/KyNotes-server/blob/ba93e8281b3f64a9b0c5a4b786971da56180dc65/README.md) |
| KyRecovery | Compatible dependency refresh and manual publication. It remains a blind store; a deposit or file count does not verify a restore. | [e80df0f6426f](https://github.com/Busnes-app/KyRecovery-server/blob/e80df0f6426fc5e9723e4f604cd0a348e88cd13a/README.md) |
| KyDNS | Local DNSSEC validation and optional IPv6 RDNSS/DNSSL advertisements. Upgrades keep prior validation settings; privileged/native networking and real-device limits are documented. | [087a81d121eb](https://github.com/Busnes-app/KyDNS-server/blob/087a81d121eb44fa578c229d091c7eeea14be631/docs/CONFIGURATION.md) |
| KyPulse | Certificate expiry tracking and TLS-only targets, plus consent-based alert mail through KyPost alongside webhooks. | [56438bbdd8ef](https://github.com/Busnes-app/KyPulse-server/blob/56438bbdd8ef7da94fa8ce4cc95ec746878ad851/docs/MONITORING.md) |
| KyYard | Revoked-endpoint deletion frees names; dependency/manual refresh. Suite management still requires a separate runner handoff. | [ade9e2d5cf57](https://github.com/Busnes-app/KyYard-server/blob/ade9e2d5cf57bdb5f3d599b90d7655a6c3eb5074/README.md) |
| KyAuth Android | Proof-based QR pairing and bound app sign-on, compatible dependencies and 0.6.1.1 release preparation. No TOTP backup/export/sync. | [b2ae53de673f](https://github.com/Busnes-app/kyauth-android/blob/b2ae53de673f3decffd9cfc7fc547a4007c49a37/README.md) |
| KyAuth iOS | Proof-based QR pairing, bound app sign-on and 0.6.1 build 5 source version. Platform HTTPS trust is deliberately unpinned. | [e1783bef0bf7](https://github.com/Yoshiofthewire/KyAuth-iOS/blob/e1783bef0bf7d2fc64add52027f3f921beb47a76/docs/ASSURANCE-CASE.md) |
| KyAuth Linux | Proof-based QR pairing, documented unpinned-channel limits, dependency and manual refresh. Native app sign-on remains unimplemented. | [d3e6a9b4af6a](https://github.com/Busnes-app/KyAuth-Linux/blob/d3e6a9b4af6a57bc3ed4f95f5f8fe87fbf80a61f/README.md) |
| KyPost Android | Native Calendar RSVP, proof-bound app sign-on, signed TLS pin rollover, dependencies and 0.6.1.1 release preparation. | [0cf4cc75b7af](https://github.com/Busnes-app/KyPost-for-Android/blob/0cf4cc75b7afbe049bfc221f325b2038f3eba565/README.md) |
| KyPost macOS/iOS | Proof-bound app sign-on and a task manual; source builds and actual release distribution remain separate. | [38a7b18e2806](https://github.com/Busnes-app/KyPost-for-Mac/blob/38a7b18e2806308e83a88446fe195f01b6c7d659/README.md) |
| KyPost Linux | Native Calendar RSVP, protected-subject support, packaged dependencies and a task manual. | [9f7e439a31c0](https://github.com/Busnes-app/KyPost-for-Linux/blob/9f7e439a31c074a188098bc73644892808f6b117/README.md) |
| KyDrive Desktop | Published packages, signed requests and pinned TLS with signed rollover. OS-keyring custody, pending edits and re-link behavior remain documented limits. | [76cf0b29aa41](https://github.com/Busnes-app/kydrive-desktop/blob/76cf0b29aa41902bcc0eef00e3ab2efef554387e/README.md) |
| KyDrive Android | Pre-release QR linking, workspace browsing and transfers, app lock, signed requests and pinned TLS. Photo backup, persistent offline copies and DocumentsProvider remain planned. | [6ee3d2be2de0](https://github.com/Busnes-app/KyDrive-for-Android/blob/6ee3d2be2de0c755a02c1e8912727be70519f2ad/README.md) |
| KyQuickStart | Verified image pins, public-chain copy/runner refresh, Identity replica/CloudNativePG placement, and pinned-image upgrade/recovery acceptance improvements. Docker-only bulk recovery and product placement limits remain. | [f2af41f11840](https://github.com/Busnes-app/KyQuickStart/blob/f2af41f118405a23a2f5d44407bc3f1d3b2dd87f/docs/redirect.md) |
| KyQuickStart AI | Primary guided installation path, Docker and Kubernetes onboarding, manual and CI updates. Findings and handover must retain failed/blocked checks. | [a98922c2fa6a](https://github.com/Busnes-app/KyQuickStart-AI/blob/a98922c2fa6ab66257fb8b80347238cef9c589c1/README.md) |
| ky-primitives | Suite people/groups helpers, compatible dependency refresh and the separate offsite v0.3.0 release preparation. Product adapters keep their own payload and recovery responsibilities. | [e7786b9541d3](https://github.com/Busnes-app/ky-primitives/blob/e7786b9541d316ac892000079019e835d64cef62/README.md) |
| ky-ui | Compatible dependency refresh and shared theme/navigation support. UI source changes and historical screenshot scores are not new owner acceptance. | [cde8d38a181b](https://github.com/Yoshiofthewire/ky-ui/blob/cde8d38a181b25d6d6fbe990cafc98047f25bdb2/README.md) |
| ky-server-base | Upstream dependency/CI maintenance; a shared library, outside the active-application manual inventory and the November 16 app dependency rollout. | [467c147ae96f](https://github.com/Busnes-app/ky-server-base/blob/467c147ae96fc676a7aef2a39b89b8ee9c9d590f/README.md) |
| KyPost documentation site | Existing ecosystem manual checked, policy links repaired and published as a pinned snapshot; its product-specific chapters remain owned here. | [3ecc8b41dfcb](https://github.com/Busnes-app/kypost-site/blob/3ecc8b41dfcb77d64059f600f1e9c1a15db8d243/README.md) |
| Busnes.app site | Twenty public manuals published November 16; this documentation refresh follows the later default-branch product changes. | [24754c8457bb](https://github.com/Busnes-app/Busnes.app-site/blob/24754c8457bb2981312219c882f09e4ab0c7d3a7/manuals/catalog.json) |

## Shared maintenance and release limits

The November 16–17 dependency pass refreshed compatible versions and bumped application
patch versions. Shared-library pins newer than stable tags were retained, and SQLite stays
paired with its required libc/runtime dependencies. Later patch releases and catalog pins
may be newer than the initial 0.6.1 rollout; use the installer's checked catalog, not this
page as an image-version matrix. The server base was outside that coordinated app pass.

Twenty public manuals were published on November 16 with source revisions recorded in the
[manual catalog](catalog.json). Nineteen product snapshots remain intact. The KyPost book is refreshed for the identity
product naming correction, with its new source commit recorded in the catalog.
The new [suite connections guide](suite-connections.md) describes cross-app tasks from the
source review above; it does not silently repin the individual product books. Read the
linked repository guides for later changes and exact commands.

Recent security changes need compatible server and client versions. In particular, current
Drive servers require device signatures and older links may need re-linking. Preserve server
identity keys and configure the public certificate-chain source for signed rollover. KyAuth's
proof-based QR enrollment differs from its short-PIN fallback, and supported app sign-on now
requires the consumer's proof key. These mechanisms have different trust boundaries; see the
[security summary](../security.html).

## What this review does not claim

- Native KyPost receiving/direct delivery is implemented but not a whole workforce-mail
  qualification. Preserve the deployed provider/relay path until the intended mode is tested.
- Installer upgrade and recovery fixtures cover their documented cases, not every provider,
  edge, physical device, storage driver or a production stack's complete restore.
- Calendar PostgreSQL deployments still require their own protected database backup;
  SQLite capsules do not cover that driver. Drive files, Matrix media/keys and Notes blobs
  have additional recovery requirements.
- Android Drive's roadmap is not its current feature list. Its document provider, persistent
  offline files and automatic photo backup are not shipped features.
- Historical UI review scores, generated screenshots, manuals, badges and passing builds
  are not evidence of a new production deployment or independent security audit.
