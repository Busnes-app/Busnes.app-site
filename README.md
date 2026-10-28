# Busnes.app website

The public website at <https://busnes.app> introduces the Ky Suite, links to
each application's source and installation guide, and describes Busnes.app's
custom software work. This repository contains the static website, not the Ky
applications.

## Run locally

Clone this repository and serve it with Python 3:

```sh
git clone https://github.com/Busnes-app/Busnes.app-site.git
cd Busnes.app-site
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000>. The site has no build step or runtime dependencies.
HTML, CSS, JavaScript and local assets are served directly. `theme.js` applies
the saved or operating-system theme; pages remain readable without JavaScript.

## Website interface

Start at [index.html](index.html). [apps.html](apps.html) lists the product pages;
[install.html](install.html) explains installation choices. Custom-work information
is in [how-it-works.html](how-it-works.html) and [about.html](about.html). The
[privacy notice](privacy.html) and [security summary](security.html) describe
their respective policies. Navigation uses ordinary links. The theme button
switches light/dark appearance and saves the browser-local choice; without a
saved choice the site follows the operating system. This static site exposes no
application REST API or account-management interface.

## Checks and versions

Run the public page/link checks with Python 3.9 or newer:

```sh
python3 -m unittest discover -s tests -v
```

These checks examine the published root pages, their local destinations and
known misspelled repository links. They do not fetch external websites, check
every generated document, or replace browser/accessibility checks. GitHub Actions
runs the suite on pushes and pull requests. Add regression checks when major new
functionality is introduced.

The site is distributed as source, with each revision identified by its full Git
commit SHA. It currently has no packaged or SemVer-tagged releases. Record the
deployed SHA and read [CHANGELOG.md](CHANGELOG.md) for notable user-visible or
security-related changes; update those notes when making such changes.

## Feedback and contributions

Use [GitHub Issues](https://github.com/Busnes-app/Busnes.app-site/issues) for
bugs and suggestions. See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and
verification, and [SECURITY.md](SECURITY.md) for private vulnerability reports.

The page and asset ownership rules are in [AGENTS.md](AGENTS.md). The website's
[security summary](https://busnes.app/security.html) links readers to the Ky
products; each product's own repository owns its implementation and policy.

## License

The website source is available under the [MIT License](LICENSE.txt).
Third-party assets retain their accompanying license notices.

[![OctoCounts](https://api.octocounts.com/badge/Busnes-app/Busnes.app-site/branch/master)](https://octocounts.com/github/Busnes-app/Busnes.app-site/tree/master)
