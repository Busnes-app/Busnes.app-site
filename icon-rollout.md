**Repo:** Busnes.app-site and sibling Ky application repositories
**Worktree:** /home/yoshi/git/busnes.app/Busnes.app-site (branch master); sibling checkouts below

> Historical record (2026-09-24). Since then KyVault, KyMark and KyForge were archived, PrismKy dropped, several repositories renamed, and theme logic moved to `ky-ui`; `scripts/test-product-themes.mjs` was retired in favor of `ky-ui` tests.

# Shared product icon rollout

Applied the Busnes Systems stamp family locally on 2026-09-24. KyPost-Site is excluded. Native launcher/app assets are included in this icon pass; native theme defaults remain unchanged.

## Application mapping

| Product mark | Web checkouts | Native checkouts |
| --- | --- | --- |
| KyPost envelope | `kypost-server` | `kypost-android`, `kypost-for-Mac` (macOS/iOS), `kypost-Linux`, `kypost-linux-v3` |
| KyYard server rack | `KyYard-Server` | — |
| KyNotes notebook | `kynotes-server`, `kynotes-audit` | — |
| KyVault safe | `kypassword-server`, `kyvault-audit` | — |
| KyIdentity identity card | `kysignon-server` | — |
| KyRecovery restore box | `kyrecovery-server` | — |
| KyMark bookmark — new | `kybookmarks-server` | — |
| KyDNS network hub — new | `kydns-server` | — |
| KyForge anvil — new | `gridlock-server`, `kyforge-audit` | — |
| KyAuth shield/keyhole — new | — | `kyauth-android` |
| PrismKy keyboard — new | — | `PrismKy` |
| Busnes stamp | `ky_server_base` | — |

The five new masters were created with the built-in image-generation tool. They use charcoal, ivory and an orange detail. Masters, 256px previews, prompts and export conventions live in Busnes.app-site (`*-icon.png`, `icons/`, `project-icon-prompts.md`). No image-generation service is required at build or runtime.

Web changes cover browser icons, app/login branding and existing PWA manifests. KyMark's old cyan logo glow and KyPost's circular crop were removed. KyNotes login/setup screens also show its product mark. Server-base service-worker cache versions were advanced to refresh previously cached branding and theme assets. Existing logo filenames and native resource identities remain stable; action/notification glyphs were not replaced.

Android adaptive icons retain a safe centered foreground and density-specific exports. Apple catalog filenames and declared dimensions are retained; iOS icons are opaque. Linux hicolor icons retain the installed `com.kysecurity.mail` name. SVG compatibility paths embed the raster master rather than tracing new artwork.

## Verification

- All 11 React production builds pass; KyPost TypeScript check passes. KyPost builds to `/tmp/kypost-theme-dist` because its existing output directory contains root-owned deployment files.
- Rebuilt the committed web bundles and both KyNotes embedded bundles. Other build output remains subject to each repository's existing ignore rules.
- Theme verification still passes across all 13 web checkouts: `node scripts/test-product-themes.mjs`.
- KyDNS web tests pass after updating the obsolete cyan-favicon assertion to the embedded product stamp. KyRecovery dashboard/static/ceremony/CSP tests pass. The pre-existing broad Recovery test limitation is recorded in `theme-audit.md`.
- Browser previews load the shared images on KyMark, KyVault, KyPost, KyYard, KyNotes, KyIdentity, KyForge and the server base. Previews use mocked unauthenticated API responses.
- Android resource builds pass: KyPost `:app:processPlayDebugResources`; KyAuth and PrismKy `:app:processDebugResources`.
- Both Linux RelWithDebInfo builds pass with SQLCipher configured. CTest: 102/102 pass in `kypost-Linux`; 104/104 pass in `kypost-linux-v3`. The SVG icon renders through librsvg.
- Apple catalog and Linux hicolor dimensions, Android foreground dimensions and resource XML validate. No Xcode build or physical-device launcher review was possible in this Linux environment.

All changes remain local: no commit, push, deployment or app-store release. Existing unrelated modifications were preserved. Repositories need their normal release pipelines before users receive these assets. Native icon caches may refresh only after an app update/reinstall.

The suite parent and relevant owning contracts record the shared asset source. Other application contracts were left unchanged because these are branding exports, not domain or authentication changes. See `theme-audit.md` for the complete theme inventory and the projects that originally lacked selection.
