# CLAUDE-CODE-RENDER.md — The Second Opinion

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/the-second-opinion/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown.

Whisper-check before the review cut:
- BIDEA "Merhaba" — new greeting for this series; verify it reads naturally.
- B03 "steel-manning" — check it voices as one word, not "steel manning"
  with a strange pause.
- B06 "advocatus diaboli" does NOT appear in the narration (terms beat only
  — no check needed); "cheerleader" should read dry, not arch.
- BHTF: the prompt is read verbatim — "Steelman the case against my plan:
  describe your decision. Give me the strongest argument for the other side,
  fairly stated. Then tell me what evidence would change your answer."
- BOUT: read the title exactly — "The Second Opinion. At Nik Bear Brown."
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
./art run --reel the-second-opinion \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the second answer card lands beside the
first in B00; each route card lands on its spoken route in B01; the check
lands on "Confident. Done." in B02; the steelman card grows its terracotta
rim and the three cost pills pop one per spoken cost in B03; the YOU pill
lands AFTER both cards are on screen in B04; each B05 check lands on its
word and the dinner pill gets the single-answer tag; the "same training"
band bridges the two windows and the shopping-row glow dies BEFORE the X
lands in B06 (never two terracotta moments at once); the dim nod contrasts
with the three flags in B07; the chain assembles in order in B08.

## 4. Final 4K master

```
./art final --reel the-second-opinion
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m58s (measured audio sets the clock). 9 Manim scenes, all
  static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
