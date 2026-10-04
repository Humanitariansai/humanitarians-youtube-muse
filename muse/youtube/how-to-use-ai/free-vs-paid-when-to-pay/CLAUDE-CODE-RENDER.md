# CLAUDE-CODE-RENDER.md — Free vs paid: when to pay.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/free-vs-paid-when-to-pay/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (14 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting "Ciao" opens BIDEA — whisper-check it
(known-clean Kokoro greetings include Hallo; Ciao is in the skill's world-
language lexicon but verify it renders cleanly). Read the BOUT line exactly:
"Free vs paid: when to pay. Liam, in for Bear. At Nik Bear Brown. Thanks for
watching."

## 2. Layout audit (deferred — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo, which the
build VM does not have. Run it here on the Mac before the review cut and
fix any curve/overflow findings in `scenes.py` (re-run the static checker
after edits). Watch in particular: M12's longest recap line ("Free is the
real thing — with a meter.", 40 chars at size 30) and M13's prompt card
lines.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel free-vs-paid-when-to-pay \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the strike-through crosses "AI people" in
M01; the meter drains and the limit note stamps on in M03; the fourth coin
bounces off the terracotta bar in M04; all four menu cards unlock in M05;
the X/check split lands on the hard question and double checks on the easy
one in M06; the flowchart's no/yes branches light correctly in M10; the
period dot lands after "pay" in M14.

## 4. Final 4K master

```
./art final --reel free-vs-paid-when-to-pay
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 14 beats, ~5m59s. 14 scenes, all static-QC clean (0 warn, 0 error).
- Skill: ai-explainer (switched from the assigned cc-explainer — no
  terminal session exists to show; see BUILD-LOG.md). Zero cards, all
  drawings; the meter and the flowchart are the recurring visual ideas.
- No prices are quoted in the film; none can go stale.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
