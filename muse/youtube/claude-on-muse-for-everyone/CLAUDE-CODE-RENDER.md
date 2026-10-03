# CLAUDE-CODE-RENDER.md — "Claude making a film about Muse" (general-audience redo)

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/claude-on-muse-for-everyone/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (21 files). Persona: "Liam, in for Bear";
register: Teardown. Attribution matters: beats marked "their document
reports", "researchers report", "in Nik's experience", "their read" must
keep that voicing — never flatten to narrator fact.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel claude-on-muse-for-everyone \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the two bouncers read clearly in M11
(banned-list crowd vs guest-list door); the hidden text glows red in M14;
the shield cracks land with their qualifier labels in M12; the recap
lines fit the plate in M19.

## 3. Final 4K master

```
./art final --reel claude-on-muse-for-everyone
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 21 beats, ~6m58s. 19 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
