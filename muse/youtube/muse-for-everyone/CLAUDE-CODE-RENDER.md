# CLAUDE-CODE-RENDER.md — "Muse making a film about Muse" (general-audience redo)

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/muse-for-everyone/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (22 files). Persona: "Liam, in for Bear";
register: Teardown. The BIDEA line starts "Hallo. This is Liam, in for
Bear." — read it exactly.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-for-everyone \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the 1:1 pairing link draws in M03; the
notebook keeps its slips across the page-flip in M07; the plugs light up
one by one in M08; the recap lines fit inside the plate in M17.

## 3. Final 4K master

```
./art final --reel muse-for-everyone
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 22 beats, ~6m44s. 17 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
