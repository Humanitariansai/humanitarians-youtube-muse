# CLAUDE-CODE-RENDER.md — Muse packages it

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/nikbearbrown/humanitarians-youtube-muse`,
then:

```
cd info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/part-4-packaging-it/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3` … `audio/BOUT.mp3` (13 files).
Persona: "Liam, in for Bear"; register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel part-4-packaging-it \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the evaluation cards read clearly; the
architecture flow matches package/architecture.svg; the TODO stamp is legible.

## 3. Final 4K master

```
./art final --reel part-4-packaging-it
```

## 4. Publish

Only on Nik's explicit instruction.

## Film facts

- 13 beats, ~4m44s. 11 scenes, all static-QC clean (first pass).
- No MP3/MP4 files are committed to the repo.
