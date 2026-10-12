**Repo:** Busnes.app-site and sibling Ky web repositories
**Worktree:** /home/yoshi/git/busnes.app/Busnes.app-site (branch master); sibling checkouts listed below

> Historical record (2026-09-24). Since then KyVault, KyMark and KyForge were archived, PrismKy dropped, several repositories renamed, and theme logic moved to `ky-ui`; `scripts/test-product-themes.mjs` was retired in favor of `ky-ui` tests.

# Ky theme inventory

Reviewed the 23 repositories directly under `/home/yoshi/git/busnes.app` on 2026-09-24. Theme scope: web applications; native themes inventoried only. A subsequent icon pass also updates native assets; see `icon-rollout.md`. `kypost-site` is excluded from changes at the user's request.

## Projects that lacked a selector

| Product | Repository | Result |
| --- | --- | --- |
| KyMark | `kybookmarks-server` | Added System, Busnes Light and Busnes Dark selectors on login and in the app header. |
| KyVault | `kypassword-server` | Added the same selector on login and in the app header; converted fixed dark form/dialog surfaces to theme tokens. |
| KyVault audit checkout | `kyvault-audit` | Applied the same changes independently. |
| KyRecovery | `kyrecovery-server` | Added the selector to the dashboard and key ceremony; repaired mobile header wrapping. |
| KyPost public website | `kypost-site` | Main public pages lack a selector; its documentation already has one. Deferred by request; unchanged by this task. |

## Existing selectors and defaults

| Repository | Previous selection | This pass |
| --- | --- | --- |
| `Busnes.app-site` | Light/dark header toggle; OS default | Palette reference; application source unchanged. Added this inventory and the cross-repository verification script. |
| `KyYard-Server` | Five named themes | Added System and Busnes Light/Dark; preserved saved named themes. |
| `gridlock-server` (KyForge) | Five named themes | Same. |
| `kyforge-audit` | Five named themes | Same. |
| `ky_server_base` | Five named themes | Same, so products built from the base inherit the defaults. |
| `kynotes-server` | Fifteen named themes | Added Busnes Light/Dark; OS default until explicitly selected. |
| `kynotes-audit` | Fifteen named themes | Same; refreshed its embedded bundle too. |
| `kypost-server` | Fifteen named themes | Added Busnes Light/Dark; preserved legacy saved-name aliases. |
| `kysignon-server` (KyIdentity) | Fifteen named themes | Added Busnes Light/Dark; existing Appearance screen retained. |
| `kydns-server` | Fifteen theme swatches | Added Busnes Light/Dark; existing Settings selector retained. |

The source palettes are `Busnes.app-site/styles.css`: cream `#f8f6f0`, charcoal `#182326`, matching raised surfaces and readable orange text (`#bf3f18` / `#f5865f`). Product token names differ and are mapped to these values. Existing typography and layouts are retained.

A missing or invalid browser preference uses the OS light/dark choice. Selection is browser-local, tolerates unavailable localStorage, and preserves existing named selections. The server-base apps no longer overwrite the browser palette when server settings load. The new selectors and server-base selectors also offer System explicitly. KyNotes no longer saves its automatic default as an explicit choice during startup.

## Native inventory — unchanged

| Repository | Selector | Existing default |
| --- | --- | --- |
| `kypost-android` | `ThemesActivity` | Patina Ky |
| `kypost-for-Mac` | `ThemesView` / macOS preferences | Patina Ky |
| `kypost-Linux` | Settings QML / ThemeController | Patina Ky |
| `kypost-linux-v3` | Settings QML / ThemeController | Patina Ky |
| `kyauth-android` | MainActivity theme picker | Patina Ky |
| `PrismKy` | SettingsActivity theme preferences | Material Neutral Dark |

No native repository lacks theme selection. Native defaults were not changed, per the user's scope decision.

`ky-primitives` is a shared Go library and `kypost-demo-IMAP` is a development mail service; neither has a product web interface requiring a selector.

## Verification

- `node scripts/test-product-themes.mjs`: passes across all 13 modified web checkouts. Exercises OS defaults and changes, explicit persistence, blocked storage, invalid stored names and retained legacy themes.
- Production builds pass for all 11 React checkouts. KyPost also passes TypeScript checking; its build uses `/tmp/kypost-theme-dist` because the existing `frontend/dist/assets` is root-owned. No permissions on existing deployment data were changed.
- Existing frontend suites pass: KyPost 913 tests, KyIdentity 162, KyVault 78 in each checkout, KyNotes 26 in each checkout, KyYard/server base 4 each, KyForge 6 in each checkout.
- KyDNS `go test ./internal/web` passes. KyRecovery focused dashboard/static/ceremony/CSP tests pass. Its broader `internal/server` suite fails in `TestNothingInTheServerDecrypts` while walking an existing unreadable `data` directory; this is unrelated to theme source.
- Browser checks covered the new selectors, remembered choices after reload, live OS preference changes, and 390px/1280px layouts. Frontend previews used unauthenticated API responses, not live account sessions. Authenticated vault/mail workflows were covered by the existing tests rather than a live backend login.
- Rebuilt committed frontend artifacts for KyYard, KyForge, the server base, KyIdentity and both KyNotes embedded bundles. KyMark/KyVault/KyPost build outputs follow their existing ignored-artifact convention.

Changes are local and have not been committed, pushed or deployed. Existing unrelated working-tree changes were preserved. The suite and owning AGENTS.md files record the default-theme contract; unrelated domain contracts remain unchanged.
