# CLAUDE-CODE-RENDER.md — What never to paste into AI.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/what-never-to-paste-into-ai/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (14 files). Persona: "Liam, in for Bear";
register: Teardown. Read the BOUT line exactly:
"What never to paste into AI. Muse, in for Bear. Thanks for watching."

## 2. Layout audit (Mac only)

`manim_layout_audit.py --curve-strict` cannot run in the build VM (no
Manim / pangocairo). Run it on the Mac render pass before the review cut:

```
python3 brutalist.art/runtime/qc/manim_layout_audit.py --curve-strict scenes.py
```

One flagged item to confirm: the M12 recap line "Pasted text can be
stored, reviewed, trained on." is 48 chars at font_size 18 — at the
sibling package's measured limit for the 12.4-wide plate. Shorten to
"Pasted text can be stored or reviewed." if it clips.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-what-never-to-paste-into-ai \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the chat bubble lands inside the postcard in
M01; the three "fate" plates light up in order in M03; the toggle knob
flips to OFF in M04; the credential lines get crossed out before the ban
sign lands in M05/M06; the black bars fully cover the sensitive lines in
M09; the placeholders land after the cross-outs in M10; the recap lines fit
inside the plate in M12.

## 4. Final 4K master

```
./art final --reel muse-what-never-to-paste-into-ai
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 14 beats, ~5m17s. 12 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
- All on-screen example data is obviously fake (test card number, EXAMPLE /
  fake strings, fictional Acme Corp). Nothing real, nothing personal.
