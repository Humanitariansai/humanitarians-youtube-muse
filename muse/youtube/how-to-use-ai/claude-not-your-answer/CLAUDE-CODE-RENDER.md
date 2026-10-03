# CLAUDE-CODE-RENDER.md — Claude, Not Your Answer.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/claude-not-your-answer/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown.

Whisper-check before the review cut (Kokoro gotchas from prior films):
- BIDEA "Hallo" — came out clean before; still verify.
- B06 "NDA" — check it voices as letters, not a word.
- B01/B04 "ChatGPT" — verify.
- B04 "Google's My Activity page" — the URL is on screen only, never voiced.
- BOUT: read the title exactly — "Claude, Not Your Answer. At Nik Bear Brown."
  — then pad a 1.0 s silent tail.

Write the ffprobe-measured durations back to `actual_duration_s` per beat.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel claude-not-your-answer \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the paste ring lands on the document in B00;
the three documents drop one by one before the ban stamp in B01; the cable
reaches the server and the "5 years" chip lands in B02; the toggle knob
slides left and OFF appears in B03; all three toggles flip in B04; the
"already used" box stays shut in B05; the name swaps to [CLIENT] in B07.

## 3. Final 4K master

```
./art final --reel claude-not-your-answer
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m06s (measured audio sets the clock). 9 Manim scenes, all
  static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
