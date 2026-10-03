# CLAUDE-CODE-RENDER.md — Muse proves it scales

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/nikbearbrown/humanitarians-youtube-muse`,
then:

```
cd info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/part-3-proving-it-scales/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3` … `audio/BOUT.mp3` (14 files).
Persona: "Liam, in for Bear"; register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel part-3-proving-it-scales \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the results table numbers match
SCALE-TESTS.md (2.37 / 23.8 / 119.1 s; 3.72 ms; 52–65 MB); the "NOT FOUND"
stamp reads clearly.

## 3. Final 4K master

```
./art final --reel part-3-proving-it-scales
```

## 4. Publish

Only on Nik's explicit instruction.

## Film facts

- 14 beats, ~4m54s. 12 scenes, all static-QC clean.
- No MP3/MP4 files are committed to the repo.
