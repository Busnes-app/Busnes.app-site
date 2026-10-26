# Security policy — Busnes.app website

This repository owns the static public website at <https://busnes.app>.
Report website vulnerabilities here, including script injection, unsafe links,
compromised published assets or accidentally published secrets. Vulnerabilities
in a Ky application belong to that application's repository.

## Report privately

Use [Report a vulnerability](https://github.com/Busnes-app/Busnes.app-site/security/advisories/new)
on this repository's Security tab, or email <hello@busnes.app> with "Security"
in the subject. Please do not open a public issue for a vulnerability.

Include the affected URL or commit, reproduction steps, likely impact and
affected versions where applicable. Do not include real user secrets.

As stated on the [published security page](https://busnes.app/security.html#report),
reports are acknowledged within two business days. Target public disclosure
is within 30 days for critical issues, 60 for high and 90 for moderate. A fix
ships before the advisory, and reporters are credited unless they prefer
otherwise. These are response commitments, not a record of past response times.

## Website boundaries

The site serves public pages and local assets. It does not implement Ky
application authentication or store application data. Keep it static, retain
the existing content security policy, and do not introduce analytics or
third-party embeds. Each Ky product's own security policy takes precedence
over the site's product summary.
