# CLAUDE-CODE-RENDER.md — "Think one step ahead"

Render instructions for Bear's Mac. **Do not publish or stage anything**
without Bear's explicit instruction — this is a pre-render package.

## Prereqs

- The brutalist.art toolkit cloned and set up (`./setup --install && ./setup`).
- Manim (community edition) working, Kokoro TTS available.
- This film's folder copied to a render working directory. On Bear's Mac all
  file activity stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`.

## Files in this package

`make_sheet.py` (generates `beat_sheet.json`), `scenes.py` (6 Manim scenes,
show-tell iso_kit pasted at the top — do not split it out), plus ACTS,
SHOTLIST, FACTCHECK, SOURCES, PROMPTS, BUILD-LOG, CHECKS-REPORT, README.

## Step 1 — beat sheet

```bash
python3 make_sheet.py   # writes beat_sheet.json (10 beats, 189.6 s estimated)
```

## Step 2 — narration audio (Kokoro, voice am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel> --voice am_onyx
```

One MP3 per beat: `mp3/beat-<BEATID>.mp3` (see `audio_file` in beat_sheet.json).
Whisper-check BIDEA's greeting ("Hallo" must come out clean, not "hedge")
before proceeding.

## Step 3 — write measured durations back

ffprobe each `mp3/beat-*.mp3` and write the real durations into
`beat_sheet.json` as `actual_duration_s` per beat. The kit's `until()` /
`finish()` pacing reads `actual_duration_s` first, `estimated_duration_s`
as fallback. **Do not re-run make_sheet.py after this step** — it wipes the
build stamps (see the skill's warning; re-run `art final` if it happens).

## Step 4 — render scenes

Scene classes (beat id = class prefix): `B00_Window`, `B01_Before`,
`B02_Scratchpad`, `B03_After`, `B04_When`, `B05_Ahead`.

```bash
manim -qh -s scenes.py <ClassName>   # stills first; look at a contact sheet
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
./brutalist.art/art run <reel> --height 2160
```

The layout audit could not run in the build VM (no Manim/pangocairo) — run
it here for every class before the review cut. The static scene check
(`runtime/qc/static_scene_check.py`) already passed 6 clean · 0 warn · 0 error.

Bookends (BIDEA, BDEFS, BHTF, BOUT) are Remotion compositions
(`BrutalistHesitantWriter`, `ClaudeDefinitions`, `ClaudeComposerAsk`,
`ClaudeTitleOutro`) — render via `runtime/scripts/remotion_scenes.py`, not Manim.

BOUT carries its 1.0 s spoken-outro tail in the beat sheet — verify it is
present in the final audio before the master.

## Step 5 — master

`./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape`.
Check: sha, 3840×2160, silent tail present. Send Bear the master; stage and
publish only on his word.

## Notes

- The sparse-by-design QC waiver on body beats covers Gate V underfill and
  clustered only; edge-bleed, empty-frame, and contrast still apply at render.
- Kokoro reads "claude.ai" style tokens fine, but whisper-check any acronym;
  this film's narration avoids acronyms entirely.
