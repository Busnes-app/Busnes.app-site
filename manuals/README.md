# Published Ky suite manuals

`index.html` and the product directories are committed mdBook 0.5.4 output, served
unchanged by the existing GitHub Pages site. `catalog.json` records the exact public
source repository and commit for each product snapshot. Private/internal products
are not mirrored here.

To refresh a product, check out its recorded source revision in its existing repository,
run `mdbook build docs` and its documented link checker, replace only that product's
directory here with `docs/book/`, then update its catalog revision. Preserve every
other product directory and third-party font/software licence notice.

To refresh the directory page, edit `directory-source/src/index.md`, run
`mdbook build manuals/directory-source`, and copy the generated `.directory-build/`
contents into this directory without deleting the product directories. The intermediate
build directory is ignored. Run `python3 -m unittest discover -s tests -v` before committing.

Products keep their source manuals and CI checks in their own repositories. This site
publishes checked snapshots; a product merge does not silently deploy a new manual.
