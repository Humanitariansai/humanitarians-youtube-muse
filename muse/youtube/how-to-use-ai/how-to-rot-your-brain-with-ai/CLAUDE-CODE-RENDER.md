# CLAUDE-CODE-RENDER.md — render instructions for Bear's Mac

Pre-render package for **"How to outsource everything to AI & get dumb"**
(slug `how-to-rot-your-brain-with-ai`). Everything is authored; nothing is rendered.
Render locally on your Mac with Manim + Kokoro. Keep all file activity inside
`/Users/bear/Documents/CoWork/bear-textbooks/books/`.

## 0. Fetch the package
Pull the film folder from the write repo (or copy this folder):
`muse/youtube/how-to-use-ai/how-to-rot-your-brain-with-ai/`
You need: `beat_sheet.json`, `scenes.py`. (Never commit MP3/MP4/WAV, `__pycache__`,
`.DS_Store` back to the repo.)

## 1. Narration audio (Kokoro am_onyx) — the master clock
From your `brutalist.art` checkout:
```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>   # Kokoro am_onyx, free
```
- 14 beats: BIDEA, BDEFS, B00–B09, BHTF, BOUT. Narration text is in `beat_sheet.json`.
- Pad BOUT with a 1.0 s silent tail after voicing.
- Whisper-check BIDEA ("Hallo. This is Liam, in for Bear."), B07 (no acronyms spoken),
  and B08 ("eighty-three percent", "eleven percent", "preprint").
- Write the ffprobe-measured durations back into each beat's `actual_duration_s`
  (keep `audio_file` on every beat or `art run` refuses).
- Do NOT re-run `make_sheet.py` after this — it wipes the build stamps.

## 2. Pre-audit the scenes (from a scratch folder holding ONLY scenes.py + beat_sheet.json)
```bash
python3 brutalist.art/runtime/qc/static_scene_check.py scenes.py --class B00_Hero   # …all 10 classes
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict
```
Static check passed 10/10 clean on 2026-10-03; re-run after any edit. Render stills
first (`manim -ql -s`) and eyeball a contact sheet before any 4K render.

## 3. Render
```bash
./brutalist.art/art run <reel> --height 2160     # Gates A, B, V + review cut
# …look at frames, fix, re-run…
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape   # GATE T, master
```
- The 10 Manim classes are `B00_Hero` … `B09_FastTrap` (literal `class BNN_Name(Scene):`).
- The 4 bookends are Remotion: BrutalistHesitantWriter (BIDEA), ClaudeDefinitions
  (BDEFS), ClaudeComposerAsk (BHTF), ClaudeTitleOutro (BOUT) — render via
  `runtime/scripts/remotion_scenes.py`.
- ffprobe each `manim/<BID>.mp4` against its beat audio before the final.

## 4. Fact-check gate (before final)
Verify FACTCHECK.md claim #6 (the 11% no-AI figure) against arXiv:2506.08872. If it
doesn't check out, drop the right meter from B08_EightyThree (the beat works with 83% alone).

## 5. Never publish
The master goes to you for review. Stage (`art post`) and publish only on your word,
and only from TOPOST. This package stages nothing.
