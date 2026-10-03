# CLAUDE-CODE-RENDER.md — Claude, Allowed.

Render instructions for Bear (local Mac). This package is **pre-render**: narration
audio and video are NOT included and must never be committed to the repo.

## 0. Prereqs

- The brutalist.art toolkit cloned locally (see README.md).
- Manim (community edition) + a working Kokoro TTS setup.
- This package's files, e.g. under
  `/Users/bear/Documents/CoWork/bear-textbooks/books/how-to-use-ai/claude-allowed/`
  (all file activity stays inside `books/`).

## 1. Generate narration audio (Kokoro `am_onyx`)

From the toolkit root:

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py \
  "/Users/bear/Documents/CoWork/bear-textbooks/books/how-to-use-ai/claude-allowed"
```

- Voice is fixed: `am_onyx`, Liam ("Liam, in for Bear"), Teardown register.
- BIDEA opens with the greeting `Hallo. This is Liam, in for Bear.` — whisper-check it.
- After generating, measure each MP3 with ffprobe and write the durations back into
  `beat_sheet.json` as `actual_duration_s` (the audio is the master clock).
- BOUT needs a **1.0 s silent tail** (`tail_silence_s: 1.0`); re-pad and re-measure
  after any full re-voice. If re-voicing single beats, use `--only <BID>` (note: it
  silently drops BOUT's pad — re-pad afterwards).

## 2. Pre-render scene audit

```bash
cd <reel>
manim -ql -s scenes.py B00_PolicyPage   # last-frame stills; build a contact sheet
```

- The `until()`/`finish()` pacing in `scenes.py` reads `beat_sheet.json` in the same
  folder — keep them together or pacing silently degrades to fixed waits.
- Gate A sees only `scenes.py`: every class is literally `class BNN_Name(Scene)`.
- Known real-render watch items: GATE T samples each clip at its midpoint — the B00
  highlighter band and the B02 connector lines must be landed before their midpoints;
  EB Garamond must be installed for the `T()` labels.

## 3. Render

```bash
./brutalist.art/art run "<reel>" --height 2160      # Gates A, B, V + review cut
# watch the review cut, refine, repeat
./brutalist.art/art final "<reel>" --height 2160 --out "<reel>/exports/landscape"
```

- Remotion bookends (BIDEA, BDEFS, BHTF, BOUT) render via `runtime/scripts/remotion_scenes.py`.
- Check the master: sha, 3840×2160, 1.0 s silent tail on the outro.

## 4. House rules

- **Never publish from this package.** Stage (`art post`) and publish only on Bear's
  explicit word, and only from TOPOST.
- Never commit MP3/MP4/WAV, `__pycache__`, or `.DS_Store` to the film repo.
- If you edit narration, re-voice and re-measure before `art run` (audio is the clock).
