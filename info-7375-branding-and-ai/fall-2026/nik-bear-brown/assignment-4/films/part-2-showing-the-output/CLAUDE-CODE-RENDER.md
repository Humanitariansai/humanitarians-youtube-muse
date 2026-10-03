# CLAUDE-CODE-RENDER.md — Muse shows the output

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/nikbearbrown/humanitarians-youtube-muse`,
then:

```
cd info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/part-2-showing-the-output/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (15 files). Persona: "Liam, in for Bear";
register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel part-2-showing-the-output \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: brief cards show real titles/fits/links; the
run-report bars match 22/37/325/330; the TODO stamp reads clearly.

## 3. Final 4K master

```
./art final --reel part-2-showing-the-output
```

## 4. Publish

Only on Nik's explicit instruction. The film is not published by default.

## Film facts

- 15 beats, ~5m16s. 13 scenes, all static-QC clean.
- No MP3/MP4 files are committed to the repo.
