# CLAUDE-CODE-RENDER.md — Register for Muse with a privacy.com card

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/register-muse-privacy-card/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (15 files). Persona: "Liam, in for Bear";
register: Teardown. Read the BOUT line exactly:
"Muse, in for Bear. Thanks for watching. Next film: connecting Gmail without
the mess."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-register-privacy-card \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the $1 coin lands on the card in M05; the
limit slider stops at $10 and the $50 charge is declined in M08; the toggle
switches flip green in M11; the recap lines fit inside the plate in M13.

## 3. Final 4K master

```
./art final --reel muse-register-privacy-card
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 15 beats, ~4m56s. 13 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
