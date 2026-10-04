# CLAUDE-CODE-RENDER.md — Don't get fooled.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/dont-get-fooled/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/B00.mp3`, `audio/B01.mp3`, …,
`audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear"; register:
Teardown. Greeting "Olá" opens B00 — whisper-check it. B01 carries
`lead_silence_s: 0.8` — keep that head start so the hesitant-writer
correction lands before the cut. Read the BHTF prompt aloud verbatim (the
three quoted sentences), then the discussion after it. Read the BOUT line
exactly: "Don't get fooled. Liam, in for Bear. At Nik Bear Brown. Thanks
for watching."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel dont-get-fooled \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the composer asks and answers in M01; the
strike-through crosses "badly trained" in M02; the Paris bar selects and
the caption lands in M03; both cards stamp (X "made up" / check "true") in
M04; all three "NOT A REAL CASE" stamps land in M05; the tether pins the
answer to the document in M06; the ring circles "I don't know" in M07; the
magnifier carries the quote and the failed quote gets its X in M08; the
badge drops in M09; all three sentence cards + checks land in M10; the
three prompt lines type in fully in M12; the terracotta rule + period land
in M13.

## 3. Layout audit (deferred to this Mac pass)

`manim_layout_audit.py --curve-strict` could not run in the build VM (no
Manim/pangocairo installed). Run it here before the final master:

```
python3 runtime/qc/manim_layout_audit.py --curve-strict <film-dir>/scenes.py
```

## 4. Final 4K master

```
./art final --reel dont-get-fooled
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~5m11s. 13 scenes, all static-QC clean (0 warn, 0 error).
- Skill: ai-explainer — composer bookends (M01 cold open, M12 handoff),
  hesitant-writer BLUF (M02), verdict recap (M11), title-restate outro
  (M13); every inner beat illustrates its idea.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
