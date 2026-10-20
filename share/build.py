#!/usr/bin/env python3
"""Render the 1200x630 social share cards in share/ with headless Chrome.

Run from the repository root: python3 -I share/build.py
Needs google-chrome (or set CHROME) and ImageMagick 7 (`magick`). Text comes from CARDS below; keep it in
line with each page's title and the home status board.
"""
import html
import os
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "share"
CHROME = os.environ.get("CHROME", "google-chrome")

KICKER = "Ky Suite · Open source (MIT) · Self-hosted"

# file stem: (title, tagline, icon master, status or None)
CARDS = {
    "home": ("Your own apps.", "One sign-in. One backup. On hardware you control.", "busnes-icon.png", None),
    "apps": ("The Ky apps", "Mail, sign-in, DNS, calendars, notes, files and chat on your own hardware.", "busnes-icon.png", None),
    "install": ("Install Ky", "With your AI agent, with the installer, or one app at a time.", "busnes-icon.png", None),
    "custom-work": ("Custom work", "The person who built Ky can build your last mile.", "busnes-icon.png", None),
    "about": ("About Busnes.app", "One person building the Ky Suite in the open.", "busnes-icon.png", None),
    "privacy": ("Privacy policy", "One policy for every Ky app and how each one handles your data.", "busnes-icon.png", None),
    "kyidentity": ("KyIdentity", "Sign-in, MFA and user directory", "kyidentity-icon.png", "In daily use"),
    "kypost": ("KyPost", "Webmail with PGP and local AI labels", "kypost-icon.png", "In daily use"),
    "kydns": ("KyDNS", "Local names and DNS blocklists", "kydns-icon.png", "In daily use"),
    "kyrecovery": ("KyRecovery", "Blind store for sealed backups", "kyrecovery-icon.png", "Tested"),
    "kycalendar": ("KyCalendar", "CalDAV calendars with MCP access", "kycalendar-icon.png", "Tested"),
    "kyyard": ("KyYard", "Docker and Kubernetes console", "kyyard-icon.png", "Tested"),
    "kynotes": ("KyNotes", "End-to-end encrypted notes", "kynotes-icon.png", "Tested"),
    "kypulse": ("kyPulse", "Health checks and alerts", "kypulse-icon.png", "Tested"),
    "kydrive": ("KyDrive", "Files, WebDAV and document editing", "kydrive-icon.png", "Tested"),
    "kymessages": ("KyMessages", "Team chat on Matrix", "kymessages-icon.png", "Tested"),
}

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{background:#f8f6f0;color:#182326;font-family:"Adwaita Sans",Inter,"Helvetica Neue",Arial,sans-serif;
font-feature-settings:"cv08";
display:grid;grid-template-columns:1fr 360px;gap:48px;padding:72px 80px 64px;box-sizing:border-box;
border-top:12px solid #e65124}}
.text{{display:flex;flex-direction:column;min-width:0}}
.kicker{{font-size:22px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#bf3f18}}
h1{{font-size:{size}px;line-height:1.02;letter-spacing:-.03em;margin:28px 0 22px;font-weight:800}}
p{{font-size:38px;line-height:1.25;color:#566461;margin:0}}
.foot{{margin-top:auto;display:flex;align-items:center;gap:24px;font-size:28px}}
.brand{{font-weight:800;letter-spacing:-.01em}} .dot{{color:#e65124}}
.pill{{border:2px solid rgba(24,35,38,.22);border-radius:999px;padding:6px 20px;font-size:24px;font-weight:700;color:#182326}}
.pill::before{{content:"";display:inline-block;width:12px;height:12px;border-radius:50%;background:{dot};margin-right:12px;vertical-align:2px}}
img{{width:360px;height:360px;align-self:center;object-fit:contain}}
</style></head><body>
<div class="text"><div class="kicker">{kicker}</div><h1>{title}</h1><p>{tagline}</p>
<div class="foot"><span class="brand">busnes<span class="dot">.</span>app</span>{pill}</div></div>
<img src="{icon}" alt="">
</body></html>"""


def badge(icon, tmp):
    """Cut the badge off the master's ivory canvas, as the icons/ exports do, at card size."""
    out = pathlib.Path(tmp) / f"badge-{icon}"
    if not out.exists():
        subprocess.run(
            ["magick", str(ROOT / icon), "-alpha", "set", "-fuzz", "10%", "-fill", "none",
             "-draw", "color 0,0 floodfill", "-trim", "+repage", "-resize", "360x360",
             "-background", "none", "-gravity", "center", "-extent", "360x360", "-strip", str(out)],
            check=True,
        )
    return out


def render(stem, title, tagline, icon, status, tmp):
    pill = f'<span class="pill">{html.escape(status)}</span>' if status else ""
    page = TEMPLATE.format(
        size=112 if len(title) <= 12 else 92,
        dot="#8cae68" if status == "In daily use" else "#e65124",
        kicker=html.escape(KICKER),
        title=html.escape(title),
        tagline=html.escape(tagline),
        pill=pill,
        icon=badge(icon, tmp).as_uri(),
    )
    src = pathlib.Path(tmp) / f"{stem}.html"
    src.write_text(page, encoding="utf-8")
    out = OUT / f"{stem}.png"
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
         "--allow-file-access-from-files", "--window-size=1200,630", f"--screenshot={out}", src.as_uri()],
        check=True, capture_output=True,
    )
    print(out.relative_to(ROOT))


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for stem, card in CARDS.items():
            render(stem, *card, tmp)


if __name__ == "__main__":
    main()
