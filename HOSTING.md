# Site hosting and runtime

Busnes.app is a static site: HTML, CSS, images and the dependency-free browser
script `theme.js`. It has no Node server, npm dependencies or Node build step.

## GitHub Pages

GitHub Pages publishes the repository's `master` branch from `/` using its legacy
Pages build. GitHub supplies the `pages-build-deployment` workflow and its Jekyll
container; there is no deployment workflow to edit in this repository. The custom
domain is recorded in `CNAME`.

Serve a checkout locally without installing Node:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open `http://127.0.0.1:8080/`. See `AGENTS.md` for the site's verification checks.

## The Node 20 Actions warning

The successful Pages run
[39372243893](https://github.com/Busnes-app/Busnes.app-site/actions/runs/39372243893)
reported on October 20, 2026:

> Node.js 20 is deprecated. The following actions target Node.js 20 but are being
> forced to run on Node.js 24: actions/upload-artifact@v4.

This is a dependency of GitHub's managed Pages artifact-upload step, not the
website's runtime. That run used Node 24 for the action, despite its Node 20 target.
Checkout and Pages deployment also use actions declaring Node 24.

Adding `.nvmrc` or `setup-node` with Node 26 would not change a JavaScript action's
runtime or GitHub's managed Pages workflow. There is no site runtime to upgrade
to Node 26. Updating this managed action is GitHub's responsibility. Replacing
legacy Pages with a repository-owned workflow would be a separate hosting change;
it is not required to serve this static site.

To inspect hosting and the latest run without changing settings:

```sh
gh api repos/Busnes-app/Busnes.app-site/pages
gh run list --repo Busnes-app/Busnes.app-site --workflow pages-build-deployment --limit 1
```
