# CLAUDE-CODE-RENDER.md — Make It Check Its Own Work.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/make-it-check-its-own-work/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown.

Whisper-check before the review cut:
- BIDEA "Ciao" — new greeting for this series; verify it reads naturally.
- B02/B03 "twenty-eight" — check it voices as words, not "28".
- BHTF: the prompt is read verbatim — "Read your last answer and be your own
  toughest critic. List its three weakest points, and tell me what you would
  change."
- BOUT: read the title exactly — "Make It Check Its Own Work. At Nik Bear Brown."
  — then pad a 1.0 s silent tail.

Write the ffprobe-measured durations back to `actual_duration_s` per beat.

## 2. Static layout audit (deferred to this Mac pass)

`manim_layout_audit.py --curve-strict` could not run in the build VM (no
Manim/pangocairo installed) — run it here before the review cut:

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
python3 runtime/qc/manim_layout_audit.py --curve-strict \
  <film-dir>/scenes.py
```

The render-free static checker already passed 9/9 classes (0 warn, 0 error);
this audit is the real-Manin layout confirmation.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel make-it-check-its-own-work \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the magnifier swings onto the answer card in
B00; the three question cards land one per spoken number in B01; the February
glow dies BEFORE the X lands in B02 (never two terracotta moments at once);
all twelve pills light in the wave in B03 and the card swaps to "All twelve.";
the rude line underlines terracotta in B04; each B05 check lands on its word;
the B06 crack stays dim while the lens passes over it; the YES stamp and the
three flaw flags contrast in B07; the loop closes in B08.

## 4. Final 4K master

```
./art final --reel make-it-check-its-own-work
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m10s (measured audio sets the clock). 9 Manim scenes, all
  static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
