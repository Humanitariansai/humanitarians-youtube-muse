# CLAUDE-CODE-RENDER.md — "Ask for the Shape You Want Back" (How to AI #4)

Pre-render package for Bear's Mac. Everything is built except the final MP3/MP4.

## What is in this folder

| file | role |
|---|---|
| `make_sheet.py` | generates `beat_sheet.json`; asserts 13 beats / 9 manim / 4 bookends / 200–360 s |
| `beat_sheet.json` | the sheet (estimated durations; see below) |
| `scenes.py` | iso_kit.py pasted at top + 9 Manim scene classes, one per visual beat |
| `ACTS.md`, `SHOTLIST.md` | the spine and per-beat shots |
| `FACTCHECK.md`, `SOURCES.md` | claims table and sources |
| `PROMPTS.md` | "no generation prompts" |
| `BUILD-LOG.md`, `CHECKS-REPORT.md` | what was built, what QC found |
| `README.md` | film summary |

Film identity: persona Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
Teardown register; channel `claude-liam`; watermark `@NikBearBrown`.
13 beats, 9 Manim scenes, est. 246 s (~4.1 min).

## Render steps (run from the reel folder on your Mac)

```bash
# 1. Audio — Kokoro am_onyx, one file per beat; pad BOUT with a 1.0 s silent tail
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>

# 2. Write the ffprobe-measured durations back to actual_duration_s in beat_sheet.json
#    (make_sheet.py's estimates are only the clock until the audio exists)

# 3. Layout audit — REQUIRED, could not run in the build VM (no Manim/pangocairo)
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B00_BlocksBox --curve-strict
#    … repeat for all 9 classes (B00..B08); fix any warnings before 4K

# 4. Stills first: render each scene's last frame low-res and eyeball a contact sheet

# 5. Render + final
./brutalist.art/art run <reel> --height 2160
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape

# 6. ffprobe every manim/<BID>.mp4 against its audio: a clip longer than its audio
#    gets centre-cut silently, dropping the opening and the payoff. Keep each
#    scene's run time within its actual_duration_s (finish() handles this if the
#    measured audio is written back).
```

## Known watch-outs for this film

- B06 says "API — the programming interface" and "curly brace" spelled out; the
  on-screen brace is a single ink `{` glyph (not terracotta).
- B02/B07 table header bands are BAR1 grey, inset inside the card corners — do not
  darken them (GATE T reads dark bands as overlapping labels).
- `until()` phrases are verbatim from the narration; if you reword narration,
  update the matching `until()` call or the pacing silently no-ops.
- Do NOT re-run `make_sheet.py` after the final: it wipes build stamps
  (see SKILL.md); if it happens, re-run `art final` (master comes out byte-identical).
- The hesitant-writer bookend (BIDEA): `triggerWords` "tell me everything" must
  appear verbatim in `text`, and neither may end in punctuation — it does.
- Greeting "Hallo" is on the clean list; no re-voicing needed.

## Never

Never publish, upload, or stage anything for publication from this package.
No MP3/MP4/WAV, `__pycache__`, or `.DS_Store` goes into the repo.
