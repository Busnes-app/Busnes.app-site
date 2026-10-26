"""Check the committed public pages without fetching third-party sites."""

from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.references = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        self.references.extend(value for key, value in attrs
                               if key in ("href", "src") and value)


class SiteTests(unittest.TestCase):
    def test_public_page_references(self):
        pages = sorted(ROOT.glob("*.html"))
        self.assertTrue(pages, "No public pages found")
        for page in pages:
            if page.name == "prototype-light-systems.html":
                continue  # Retained prototype, excluded from the published site.
            for reference in Page(page).references:
                url = urlsplit(reference)
                with self.subTest(page=page.name, reference=reference):
                    self.assertFalse(url.netloc.lower() == "github.com" and
                                     url.path.strip("/").split("/", 1)[0].lower() == "busness-app",
                                     "Misspelled GitHub organization")
                    if url.scheme or url.netloc or not url.path:
                        continue
                    target = (ROOT / unquote(url.path.lstrip("/"))).resolve()
                    self.assertTrue(target.is_relative_to(ROOT), "Reference leaves repository")
                    if target.is_dir():
                        target /= "index.html"
                    self.assertTrue(target.is_file(), "Missing local page or asset")


if __name__ == "__main__":
    unittest.main()
