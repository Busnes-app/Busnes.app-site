# Contributing to the Busnes.app website

Use [GitHub Issues](https://github.com/Busnes-app/Busnes.app-site/issues) for
bugs and suggestions, and submit changes through a pull request. Discuss a
substantial change in an issue first. Report vulnerabilities privately as
described in [SECURITY.md](SECURITY.md).

## Development

Follow [README.md](README.md) to serve the site locally. Read [AGENTS.md](AGENTS.md)
for page ownership, design rules and existing verification commands.

- Keep HTML semantic and accessible, with heading order, skip navigation,
  keyboard focus and descriptive links preserved.
- Reuse the existing CSS tokens and layouts. Keep light and dark themes aligned.
- Keep JavaScript dependency-free and compatible with the existing content
  security policy. Keep pages usable without it.
- Source product descriptions and security claims from the maintained product
  repositories. Distinguish implemented behavior from plans.
- Preserve third-party license notices.

## Verification and pull requests

Run `python3 -m unittest discover -s tests -v`. Add automated regression checks
with major new functionality, and update [CHANGELOG.md](CHANGELOG.md) for
user-visible or security-related changes.

Check changed links and local asset paths. For page, style or script changes,
inspect light and dark themes at desktop and mobile widths and check the
browser console and network requests. Run the existing checks in AGENTS.md
that apply to the change.

Explain the user-visible effect and record the checks and results in the pull
request. Disclose material AI assistance and what you personally verified.

Contributions are licensed under the repository's [MIT License](LICENSE.txt).
