# CLAUDE-CODE-RENDER.md — "You can't beat AI."

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/you-cant-beat-ai/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`, `PROMPTS.md`, `SOURCES.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/B00.mp3` … `audio/B11.mp3` (12 files).
Persona: "Liam, in for Bear"; register: Teardown. Voicing contracts:
- B00 opens "Hallo. This is Liam, in for Bear." — never change the
  introduction or the B11 sign-off ("Liam, in for Bear").
- B05 opens "An illustration." — the chief-of-staff scenario is
  illustrative, never voiced as a real case.
- B10 must read the handoff prompt ALOUD verbatim (see PROMPTS.md), then
  the discussion lines; do not skip the prompt.

Note: `dur_s` in the beat sheet is a speech estimate (~150 wpm), not
measured audio. After synthesis, the measured MP3 durations become the
master clock; re-time the scenes to them.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel you-cant-beat-ai \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the strike-through lands on the spoken
word in S02; the terracotta halo is only on plate 2 in S07; the
"Illustrative example" tag is legible in S06; the YOURS seal reads in
S10; the B01 typing finishes before the narration moves on
(`lead_silence_s: 0.8`).

## 3. Final master

```
./art final --reel you-cant-beat-ai
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 12 beats, 295 s (~4.9 min) by speech estimate; 638 words; 12 Manim
  scenes, all static-QC clean (0 warn, 0 error).
- Skill: ai-explainer. Brand: claude-liam (Kokoro am_onyx, Teardown,
  @NikBearBrown).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
