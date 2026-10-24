# Logo Asset Catalog

This repository contains static brand previews and reusable visual assets for the Velclaw ecosystem. Existing asset paths are preserved; add new variants alongside originals rather than replacing them without review.

## OCode.js
- [OCode.js logo preview](OCode.js/ocodejs-logo.html)
- [OCode.js SVG wordmark](OCode.js/ocodejs-logo.svg)
- [OCode.js logo library preview](OCode.js/bo-logo-thu-vien.html)
- [OCode.js asset directory](OCode.js/)

Canonical raw SVG URL:
`https://raw.githubusercontent.com/zskbot/pages_logo/main/OCode.js/ocodejs-logo.svg`

Brand guidance:
- Use the exact wordmark spelling **OCODE.js** where that wordmark is intended.
- For dark pages, use a white wordmark with a genuinely transparent background when the asset supports it.
- Do not claim GIF alpha transparency without checking actual frames; GIF transparency is palette-based and may not match SVG alpha.
- Keep original animation and static exports available for consumers that need either format.

## X-BO Bot
- [Panda brand preview](index.html)
- [Source repository](https://github.com/zskbot/X-BO)

Keep the X-BO panda mascot and OCode.js wordmark as distinct identities. Add expression variants (left/right/up/down gaze, happy, sad, crying) as separate assets with clear filenames and consistent canvas dimensions.

## Asset contribution checklist
- [ ] Use descriptive, stable filenames where practical.
- [ ] Preserve original files; add new versions instead of overwriting.
- [ ] Include a preview or source file for generated vector artwork.
- [ ] Verify dimensions, animation duration, frame count, and transparency on the actual exported file.
- [ ] Use relative links in this catalog and test them on GitHub Pages.
- [ ] Avoid embedding secrets, tracking pixels, or remote scripts in preview HTML.
- [ ] Record intended use, source, and license/attribution for third-party artwork.

## Deployment
This is an asset/catalog repository. Do not add app runtime dependencies or replace the root page without checking existing consumers and GitHub Pages behavior.
