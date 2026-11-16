"""Check every committed book, including its search/print assets and local fragments."""

from html.parser import HTMLParser
import json
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANUALS = ROOT / "manuals"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        self.references.extend(attrs[key] for key in ("href", "src") if attrs.get(key))


class ManualTests(unittest.TestCase):
    def test_catalog_and_book_assets(self):
        catalog = json.loads((MANUALS / "catalog.json").read_text())
        self.assertEqual(len(catalog), 20)
        slugs = [entry["slug"] for entry in catalog]
        self.assertEqual(len(set(slugs)), len(slugs))
        self.assertNotIn("ky-dashboard", slugs, "Internal documentation must stay private")
        directory = Page(MANUALS / "index.html")
        for entry in catalog:
            slug = entry["slug"]
            with self.subTest(book=slug):
                self.assertRegex(slug, r"^[a-z0-9-]+$")
                self.assertRegex(entry["source_commit"], r"^[0-9a-f]{40}$")
                self.assertTrue(entry["repository"].startswith("https://github.com/"))
                self.assertEqual(entry["url"], f"https://busnes.app/manuals/{slug}/")
                self.assertIn(f"{slug}/index.html", directory.references)
                for filename in ("index.html", "print.html", "toc.html"):
                    self.assertTrue((MANUALS / slug / filename).is_file(), filename)
                self.assertTrue(list((MANUALS / slug).glob("searchindex-*.js")))

    def test_every_local_file_and_fragment(self):
        # The intermediate directory is an ignored local build, not a published book.
        paths = [p for p in MANUALS.rglob("*.html") if ".directory-build" not in p.parts]
        pages = {p.resolve(): Page(p) for p in paths}
        self.assertGreater(len(pages), 200)
        for source, page in pages.items():
            for reference in page.references:
                with self.subTest(page=str(source.relative_to(ROOT)), reference=reference):
                    url = urlsplit(reference)
                    if url.scheme or url.netloc:
                        continue
                    path = unquote(url.path)
                    target = ((ROOT / path.lstrip("/")) if path.startswith("/")
                              else source.parent / path).resolve() if path else source
                    self.assertTrue(target.is_relative_to(ROOT), "Reference leaves website")
                    if target.is_dir():
                        target /= "index.html"
                    self.assertTrue(target.is_file(), "Missing local page or asset")
                    if url.fragment and target in pages:
                        self.assertIn(unquote(url.fragment), pages[target].ids,
                                      "Missing local heading/anchor")


if __name__ == "__main__":
    unittest.main()
