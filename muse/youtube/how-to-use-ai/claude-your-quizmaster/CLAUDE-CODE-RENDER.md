# CLAUDE-CODE-RENDER.md — Claude, Your Quizmaster

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/claude-your-quizmaster/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/BOUT.mp3` (10 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting note: BIDEA opens "Hallo." (Kokoro says
it cleanly — do not substitute "Hej"). Read the BOUT line exactly:
"Claude, Your Quizmaster. Liam, in for Bear. At Nik Bear Brown."

Read the BHTF prompt in full, exactly as written in the beat sheet
("Quiz me on your topic…"), pausing slightly before and after the quoted
prompt.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel claude-your-quizmaster \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the naive ask is corrected to the quiz ask
in M01; the 61% vs 40% number lands tagged "memory researchers" in M03;
the face-down card flips to the definition in M04; the sawtooth lifts at
each quiz dot in M05; the check / "?" / "study this" marks land on the
explanation lines in M06; the full 8-line prompt fits the composer card in
M08.

## 3. Final 4K master

```
./art final --reel claude-your-quizmaster
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 10 beats, ~4m03s. 8 scenes, all static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
