# CLAUDE-CODE-RENDER.md — "Claude, When Not."

Render instructions for Bear's Mac. **Do not publish or stage anything**
without Bear's explicit instruction — this is a pre-render package.

## Prereqs

- The brutalist.art toolkit cloned and set up (`./setup --install && ./setup`).
- Manim (community edition) working, Kokoro TTS available.
- This film's folder copied to a render working directory. On Bear's Mac all
  file activity stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`.

## Files in this package

`make_sheet.py` (generates `beat_sheet.json`), `scenes.py` (13 Manim scenes,
show-tell kit pasted at the top — do not split it out), plus ACTS, SHOTLIST,
FACTCHECK, SOURCES, PROMPTS, BUILD-LOG, CHECKS-REPORT, README.

## Step 1 — beat sheet

```bash
python3 make_sheet.py   # writes beat_sheet.json (13 beats, 244 s estimated)
```

## Step 2 — narration audio (Kokoro, voice am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel> --voice am_onyx
```

One MP3 per beat: `mp3/beat-<BEATID>.mp3` (see `audio_file` in beat_sheet.json).
Whisper-check BIDEA's greeting ("Hallo" must not come out as "hedge") and
B06's "hallucination" before proceeding.

## Step 3 — write measured durations back

ffprobe each `mp3/beat-*.mp3` and write the real durations into
`beat_sheet.json` as `actual_duration_s` per beat. The kit's `until()` /
`finish()` pacing reads `actual_duration_s` first, `estimated_duration_s`
as fallback.

## Step 4 — render scenes

Scene classes (beat id = class prefix): `BIDEA_HesitantWriter`,
`BDEFS_Terms`, `B01_Thesis`, `B02_UseList`, `B03_DontList`, `B04_HideTest`,
`B05_DraftExample`, `B06_Verify`, `B07_Predict`, `B08_Answer`, `B09_Line`,
`BHTF_YourTurn`, `BOUT_Outro`.

```bash
manim -qh -s scenes.py <ClassName>   # stills first; look at a contact sheet
./brutalist.art/art run <reel> --height 2160
```

BOUT carries its 1.0 s spoken-outro tail in the beat sheet — verify it is
present in the final audio before the master.

## Step 5 — master

`./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape`.
Check: sha, 3840×2160, silent tail present. Send Bear the master; stage and
publish only on his word.

## Notes

- The film's bookends are drawn Manim scenes (see `bookend_exempt_reason` in
  beat_sheet.json metadata) — no Remotion compositions to render.
- The sparse-by-design QC waiver on body beats covers Gate V underfill only;
  edge-bleed, empty-frame, and contrast still apply at render time.
