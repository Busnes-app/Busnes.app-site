# Project icon generation

Standalone project PNGs generated with the built-in image-generation tool, using `busnes-icon.png` as the visual reference. Masters live here; web and native applications carry platform-sized exports. Preserve square proportions.

## Shared prompt

Use case: logo-brand. Create one finished standalone square PNG project icon, matching the attached approved Busnes.app Systems stamp icon as a FAMILY STYLE REFERENCE. Retain its exact charcoal #182326 rounded square badge on a uniform light ivory #f2efe8 square canvas, same generous outer margin, same corner radius and bold 1970s bespoke software engineering-manual aesthetic. Replace the B entirely with the project symbol described below. Render symbol as a chunky simple ivory silhouette with charcoal negative-space cuts, optically centered, readily identifiable at 32 pixels, limited broad shapes rather than fine linework. Same two-color palette, same flat style and internal padding across the family. Image 1024x1024 square. Absolutely no letters, names, labels, wordmarks, B, text, shadows, gradients, texture, 3D or mockup. Output only ONE icon, not a sheet. Project symbol: 

## Project-specific prompt suffixes

### kypost-icon.png

KyPost email: a bold closed envelope with a crisp V-shaped flap cut into its face, small softened corners and generous negative-space seams. Plain iconic envelope, no arrows or extra badges.

### kyyard-icon.png

KyYard container infrastructure: three wide horizontal server modules stacked vertically, each with one large charcoal status-light cutout on the left. Bold geometric rack silhouette, no wires or fine vents.

### kynotes-icon.png

KyNotes notes: a chunky upright notebook silhouette with a distinct left binding and three broad horizontal charcoal writing-line cutouts, last line shorter. No pencil, no tiny spiral details.

### kyidentity-icon.png

KyIdentity accounts and access: a broad horizontal identity-card silhouette, with a circular head and rounded shoulders cut out in charcoal on the left, two short broad charcoal information bars on the right. No letters, no badge lanyard, no small details. Clear identity-card pictogram.

### kyrecovery-icon.png

KyRecovery sealed backups and restore: a broad counterclockwise circular restore arrow surrounding one simple archive box. Arrow has one clearly formed large triangular arrowhead at upper left; archive box has a single dark horizontal slot. Generous gap between arrow and box. No clock hands, no shield, no tiny detail. Clear recovery and archived-backup pictogram.

## Web exports

The pages load `icons/<name>.png`, not the masters. Regenerate after changing a master:

```sh
for f in busnes kypost kyyard kynotes kyidentity kyrecovery kydns kyauth kypulse kycalendar kydrive kymessages; do
  magick "$f-icon.png" -alpha set -fuzz 10% -fill none -draw 'color 0,0 floodfill' \
    -trim +repage -resize 256x256 -background none -gravity center -extent 256x256 -strip "icons/$f.png"
done
```

## Extended family

Generated with the built-in image-generation tool using the approved Busnes stamp as a visual reference. Each prompt retains the charcoal `#182326` badge, ivory `#f2efe8` glyph and canvas, flat geometry, generous padding, and no lettering, texture or shadows. These additions use one orange `#bf3f18` detail:

- `kydns-icon.png`: network hub with three broad ivory endpoints, connected by thick ivory bars to one orange central node. All interior ivory shapes are opaque; only the outer canvas is removed for exports.
- `kyauth-icon.png`: chunky ivory shield containing a single orange keyhole.
- `kypulse-icon.png`: hand-drawn in `kypulse-icon.svg` (render with `rsvg-convert`), not generated: a thick ivory heartbeat line ending in one orange live dot.
- `kycalendar-icon.png`: hand-drawn in `kycalendar-icon.svg`: an ivory calendar page with two binder rings, a header seam and a grid of charcoal day cells, one of them orange.
- `kydrive-icon.png`: hand-drawn in `kydrive-icon.svg`: an ivory folder with a charcoal flap seam and one orange upload arrow.
- `kymessages-icon.png`: hand-drawn in `kymessages-icon.svg`: an ivory speech bubble with three typing dots, the last one orange.

## Application exports

Product checkouts own copied assets so builds do not depend on this sibling directory. Keep product marks at square proportions; do not recolor them with a theme accent or reuse action glyphs as branding. Existing two-color product stamps work on both Busnes palettes.

Web public/static folders hold `app-icon.png` (256), favicons, and existing logo filenames. Where a manifest exists, its icons are 192 and 512 pixels. Legacy SVG favicon URLs contain an embedded PNG to preserve routes. Android adaptive foregrounds use a 64dp badge centered on a transparent 108dp canvas with an ivory background; legacy launchers retain 48dp density exports. Apple asset catalogs retain their declared filenames and pixel sizes, with opaque iOS images. Linux retains the installed `com.kysecurity.mail` icon name and hicolor sizes.
