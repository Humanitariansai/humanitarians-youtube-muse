# CLAUDE-CODE-RENDER.md — Pictures from Words

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/pictures-from-words/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (14 files). Persona: "Liam, in for Bear";
register: Teardown. Read the BIDEA line exactly, opening with
"This is Liam, in for Bear." Read the BOUT line exactly:
"Liam, in for Bear. Pictures from words. Thanks for watching — next film:
what never to paste into AI."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-pictures-from-words \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the grey dog in M03 reads as deliberately
plain next to the warm M04 picture; the "warmer light" sun grows and the
frame widens in M05; the garbled "HAPPPY BIRTHDAAY" sign and the six-finger
hand are clearly visible in M09/M10; the AI-MADE stamp drops onto the frame
in M11; the M12 recap lines fit inside their plates.

## 3. Layout audit (deferred — cannot run in this VM)

`manim_layout_audit.py --curve-strict` could not run during the build: the
VM has no Manim/pangocairo install. Run it on the Mac render pass before
the final master and fix any findings in `scenes.py`.

## 4. Final 4K master

```
./art final --reel muse-pictures-from-words
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 14 beats, ~4m42s. 12 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
- No AI-generated images are used anywhere: every "result" on screen is a
  drawn Manim placeholder in house style.
