# CAJAL SVG Run Log — Branding and AI

Run: 2026-06-18 · Full-book figure pass (all chapters, rewritten edition)
Mode: scan + render, maximum density, greyscale-first house style

## Setup

- Old figure set (165 files from prior chapter versions) moved to `images/_archive/`.
- `sharp` installed for PNG conversion.
- Style authorities: `brutalist/DESIGN.md` (incl. new Greyscale-first hard gate) + cajal `svg-style.md`.

## Output

- **181 figures** rendered across 25 content chapters (00, 01–23, 97).
- Each figure: `images/[chapter-slug]-fig-NN.svg` + matching `.png` (300 DPI).
- Figure plans: `pantry/[chapter-slug]-cajal.md` (one report per chapter).

## Per-chapter figure counts

| Chapter | Figures |
|---|---|
| 00 introduction | 5 |
| 01 the-creative-engineer | 9 |
| 02 what-a-brand-is-equity | 7 |
| 03 the-ai-toolchain | 8 |
| 04 the-brand-audience | 7 |
| 05 brand-archetypes | 9 |
| 06 brand-strategy-and-positioning | 8 |
| 07 brand-architecture-and-portfolio | 7 |
| 08 naming-trademark-and-protection | 7 |
| 09 visual-identity-systems | 8 |
| 10 brand-voice-and-storytelling | 8 |
| 11 brand-experience-and-touchpoints | 6 |
| 12 content-media-and-campaigns | 7 |
| 13 measuring-brand-equity | 6 |
| 14 governance-and-rebranding | 7 |
| 15 brand-ethics-purpose | 6 |
| 16 crisis-and-reputation | 6 |
| 17 global-and-cross-cultural | 7 |
| 18 portfolio-as-product | 6 |
| 19 professional-presence-and-launch | 6 |
| 20 shipit-prd-and-scope | 7 |
| 21 shipit-pipelines-and-workflow | 8 |
| 22 shipit-ai-and-multiagent | 10 |
| 23 shipit-interface-and-deployment | 8 |
| 97 fundamental-themes | 8 |

## Verification

- Well-formedness: 181/181 valid XML (xmllint, 0 malformed).
- Accessibility: 181/181 carry `role="img"` + unique `aria-labelledby` + `<title>` + `<desc>`.
- Fonts: 0 banned families (no Arial / Roboto / system-ui / unquoted Helvetica).
- PNG: 181/181 SVGs have a matching PNG.
- Greyscale-first compliance: red accent (#C8102E) used in **53 of 181 figures (29%)** — a clean minority, under the ~1/3 ceiling. Batch ch10/12/14 was corrected post-render from 15→7 red figures.
- Red is never used to encode danger/negative (incl. crisis ch 16) — brand/emphasis only.

## Notes for the author

- Chapter files were NOT modified — no image references were inserted into chapters. Embedding figures into the chapter markdown is a separate step if you want it.
- Two slug mismatches to be aware of when embedding: ch 09 body references `09-visual-identity-systems-fig-01.png` (rendered); ch 10 old body refs used slug `10-brand-storytelling-fig-NN` while figures were rendered under the file-derived slug `10-brand-voice-and-storytelling-fig-NN`.
- Previous figures preserved in `images/_archive/` (not deleted).
