# CLAUDE-CODE-RENDER.md — AI is a slot machine.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/ai-is-a-slot-machine/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (16 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting "Hallo" opens BIDEA — whisper-check it
(known-clean Kokoro greetings include Hallo). Read the BOUT line exactly:
"AI is a slot machine. Liam, in for Bear. At Nik Bear Brown. Thanks for
watching."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel ai-is-a-slot-machine \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the strike-through crosses "truth machine"
in M01; the lever pulls three times and three different answer cards land
in M04; all five stage dots light in M05; the five best cards rise with
checks while the rest fade in M10; the three-line prompt types in fully in
M15; the terracotta rule draws under the title in M16.

## 3. Final 4K master

```
./art final --reel ai-is-a-slot-machine
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 16 beats, ~4m46s. 16 scenes, all static-QC clean (0 warn, 0 error).
- Skill: show-tell — zero cards, all drawings; the slot machine is the
  recurring cast object.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
