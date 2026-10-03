# SHOPPING.md — claude-liam-madison-brand-guidebook
# Gate D2: durations locked from Kokoro audio · 2026-08-11

Total locked duration: ~406s (6:46) · 40 beats · Kokoro am_onyx

---

## VOX STILLS — 9 pantry files (one InDesign export action)

All stills: own material (Tier 1) — File → Export → PNG from
`books/branding-and-ai/guidebook/brand-guidebook-000-nbb.idml`
Resolution: 2× (double the canvas size — 1920×1080px source → 3840×2160 export)
Naming convention: drop into `pantry/` as `<beat-id>-still.png`

**One InDesign action fills ALL 9 slots.** Export these pages in one pass:

| Beat | Page # | Subject | Filename | Duration |
|---|---|---|---|---|
| B02 | p1 | Cover | `pantry/B02-still.png` | 10.90s |
| B08 | p3 | Welcome (Nik Bear Brown, Founder) | `pantry/B08-still.png` | 10.84s |
| B04 | p4 | Contents (sections 01–08) | `pantry/B04-still.png` | 11.09s |
| B09 | p7 | Logo / elements key | `pantry/B09-still.png` | 9.83s |
| B15 | p11 | Color theme (four swatches, tint ladders) | `pantry/B15-still.png` | 10.90s |
| B19 | p16 | Typography specimen (AaBb, 60pt) | `pantry/B19-still.png` | 10.75s |
| B21 | p18 | Triple typeface (sizes + weights) | `pantry/B21-still.png` | 8.15s |
| B23 | p20 | Online post / post style | `pantry/B23-still.png` | 10.03s |
| B25 | p25 | Stationery (cards, letterhead, envelope) | `pantry/B25-still.png` | 10.03s |
| B31 | p29 | Imagery section | `pantry/B31-still.png` | 10.71s |
| B32 | p31 | Contact page | `pantry/B32-still.png` | 10.22s |

**Reuse (no extra export needed):**
- B10 reuses B09's still (`pantry/B09-still.png`) — vox run R1, camera zooms out
- B26 reuses B25's still (`pantry/B25-still.png`) — vox run R2, camera zooms out

---

## MANIM BEATS — machine builds

| Beat | Label | Duration | Status |
|---|---|---|---|
| B05 | 32 PAGES · 8 SECTIONS — isotype grid | 10.56s | build on `art run` |
| B12 | PRIMARY / SECONDARY — signature vs monogram | 12.67s | build on `art run` |
| B16 | TINTS 40 / 60 / 80 / 100 — bars per color | 8.85s | build on `art run` |
| B18 | 3:1 OR IT DECORATES — contrast gate | 12.93s | build on `art run` |
| B28 | 3 SURFACES · 1 MARK · 1 BROWN — isotype count | 9.60s | build on `art run` |
| B36 | BEFORE / AFTER — template → adapted | 10.73s | build on `art run` |

---

## REMOTION BEATS — machine builds

| Beat | Pattern | Duration | Status |
|---|---|---|---|
| B00 | ClaudeComposerAsk | 18.43s | build on `art run` |
| B01 | ClaudeSegmentCard (ACT I) | 4.48s | build on `art run` |
| B03 | THE THREE FILES | 12.44s | build on `art run` |
| B06 | DELETE IS A FEATURE | 10.09s | build on `art run` |
| B07 | ClaudeSegmentCard (ACT II) | 2.26s | build on `art run` |
| B11 | CLEAR SPACE | 11.52s | build on `art run` |
| B13 | THE DON'TS | 10.77s | build on `art run` |
| B14 | ClaudeSegmentCard (ACT III) | 2.22s | build on `art run` |
| B17 | ORANGE → BEAR BROWN | 12.03s | build on `art run` |
| B20 | TWO FACES, TWO JOBS | 10.75s | build on `art run` |
| B22 | ClaudeSegmentCard (ACT IV) | 2.82s | build on `art run` |
| B24 | ONE MARK, EVERY CROP | 9.32s | build on `art run` |
| B27 | LIVE FRAMES | 9.43s | build on `art run` |
| B29 | RULES THAT BEND | 9.83s | build on `art run` |
| B30 | ClaudeSegmentCard (ACT V) | 2.65s | build on `art run` |
| B33 | IT'S JUST XML | 12.63s | build on `art run` |
| B34 | THREE STEPS | 12.05s | build on `art run` |
| B35 | SIX BRACKETS | 9.64s | build on `art run` |
| B37 | ClaudeVerdictArtifact | 19.39s | build on `art run` |
| B38 | ClaudeComposerAsk (YOUR TURN) | 20.74s | build on `art run` |
| B39 | ClaudeTitleOutro | 4.27s + 1.0s tail | build on `art run` |

---

## Summary

- **Pantry (human action):** 11 InDesign page exports → 9 unique files (B10 reuses B09, B26 reuses B25)
- **Machine (art run):** 6 Manim beats + 21 Remotion beats — all auto-built
- **No gen-AI media needed** — all visuals are own material or pipeline-generated
- **No paid spend** — Kokoro audio complete; Manim and Remotion are free

**After pantry is filled:**
`./brutalist-art/art run branding-and-ai/youtube/claude-liam-madison-brand-guidebook`
