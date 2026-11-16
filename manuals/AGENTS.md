# Published manuals

## Purpose

Own the public suite manual directory and checked product-book snapshots.

## Ownership

- `catalog.json` records the public source commit of each product book.
- `directory-source/` owns the directory's mdBook source. Root HTML/assets and product directories are generated output.
- Product repositories own their original chapters, policies and documentation CI.

## Local Contracts

- Mirror only public product documentation. KyDash remains internal and is not listed or copied.
- Rebuild with mdBook 0.5.4. Preserve relative links, search/print assets and third-party licence notices.
- `.gitattributes` exempts only mdBook's clipboard, table-of-contents and font-licence files from whitespace checks so their generated/upstream bytes remain unchanged.
- Refresh one product directory at a time; preserve the rest. Record its exact source commit in the catalog.
- Generate the directory page in `.directory-build/`, then copy its contents here; do not build the directory directly over the product books.

## Work Guidance

- Follow README.md for refresh steps. Publication is a reviewed website commit served by existing GitHub Pages.

## Verification

- `python3 -m unittest discover -s tests -v` from the website root checks pages and every mirrored book's local files/fragments.

## Child DOX Index

None. Product snapshots keep their source contracts in their original repositories.
