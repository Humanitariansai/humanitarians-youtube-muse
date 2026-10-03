# Madison Weekly — Aug 28.

**Fellow:** Komal BG
**Date:** 2026-08-28
**Format:** Hybrid weekly — Liam bookends + unedited team clips
**Runtime:** ~5:48 · **Master:** 4K (3840×2160) + 9:16 short
**Narrator:** Liam (`am_onyx`), in for Komal; B03 / B05 are team clips (own audio)
**Channel chip / handle on cut:** Komal

## What this video is about

Loon project update for Madison. Sai locked a ground-truth-first order
(repos → architecture doc → hand-drawn boxes). Swara moved into **CVAT**
annotation and a Lovable researcher prototype (upload · analyze · review ·
save). No trained model yet — by design.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `short/beat_sheet.json` | 9:16 companion plan |
| `README.md` | This file |
| `SOURCES.md` | Team clips (only source of claims) |
| `FACTCHECK.md` | Claim-level verdicts |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `PEDAGOGY.md` | GATE P — narration signed **PASS** |
| `NARRATION-GATE-P.md` | Line-by-line house-narration review sheet |
| `description.txt` | Short blurb / caption draft |

The clean 4K master (`madison-weekly-aug-28.mp4`) and 9:16 short stay local
and are gitignored. Production source for this cut also lives locally at
`loon-book/youtube/madison-weekly-aug-28/` and is **not** part of this PR.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only on house beats, no API keys. Full rebuild path is in
`BUILD-PROMPT.md`.

## Publishing

Not authorized by this package. Master stays local until a human decides to share
or upload.
