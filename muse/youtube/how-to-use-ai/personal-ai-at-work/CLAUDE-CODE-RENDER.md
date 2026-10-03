# CLAUDE-CODE-RENDER.md — Stop using your own Claude at work.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/personal-ai-at-work/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (14 files). Persona: "Liam, in for Bear";
register: Teardown. Read the BOUT line exactly:
"Stop using your own Claude at work. Muse, in for Bear. Thanks for
watching."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-personal-ai-at-work \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the three leak pips land on the timeline in
M03; the toggle knob flips to OFF in M05 and M07; the two retention bars in
M06 read as "5 years" vs "~30 days" at a glance; the document lines in M10
get crossed out before the placeholders appear; the recap lines fit inside
the plate in M12.

## 3. Final 4K master

```
./art final --reel muse-personal-ai-at-work
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 14 beats, ~4m44s. 12 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
