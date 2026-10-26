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
