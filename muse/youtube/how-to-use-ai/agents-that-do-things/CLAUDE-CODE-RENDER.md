# CLAUDE-CODE-RENDER.md — Agents: AI that does things.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/agents-that-do-things/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/B00.mp3` … `audio/B11.mp3`
(12 files). Persona: "Liam, in for Bear"; register: Teardown. Greeting
"Hola" opens B00 — it is in the skill's world-language lexicon; verify it
renders cleanly before the review cut. B01 carries `lead_silence_s: 0.8`
— keep it, so the hesitant writer's typing starts before the voice.
Read the B11 line exactly: "Agents: AI that does things. Liam, in for
Bear. At Nik Bear Brown. Thanks for watching."

## 2. Layout audit (deferred — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo, which the
build VM does not have. Run it here on the Mac before the review cut and
fix any curve/overflow findings in `scenes.py` (re-run the static checker
after edits). Watch in particular: B03's CurvedArrows between the loop
nodes (check the arcs land on the circle rims), B04's longest card line
("approve the irreversible", 22 chars at size 30) against the number
circles, B06's flagged hidden-instruction line (31 chars at size 24)
inside its terracotta flag, and B09's widest recap line
("good at: boring multi-step errands", 33 chars at size 32).

## 3. Review cut

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel agents-that-do-things \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: B00's composer types the ask and the
answer line lands; B01's writer strikes "a smarter chatbot" and writes
"a chatbot with hands" before the cut; B02's three ingredient cards stamp
the AGENT card on beneath them; B03's terracotta dot travels the full
SEE→THINK→ACT→CHECK loop; B04's three rule cards land numbered;
B05's four step chips check off and the terracotta "waits for your yes"
gate lands; B06's hidden instruction flags terracotta before the X stamps
the action panel; B07's error bars swell from the step-2 dot to the
wreck; B08's counter climbs 12 → 28 → 40 before the 10-minute stop card;
B09's five bullets reveal with terracotta dots; B10's prompt stays
readable while it is read aloud; B11's terracotta period lands after
"things".

## 4. Final 4K master

```bash
./art final --reel agents-that-do-things
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 12 beats, ~5m24s (324 s estimated). 8 Manim scenes (B02–B09), all
  static-QC clean (0 warn, 0 error); 4 Remotion bookends
  (ClaudeComposerAsk ×2, BrutalistHesitantWriter, ClaudeTitleOutro)
  render on this pass.
- Skill: ai-explainer (as assigned — no switch).
- No products named, no prices quoted, no version-specific features
  asserted — nothing in the film can go stale.
- Outro mascot index 4 (slug-seeded: char-sum of "agents-that-do-things"
  mod 18).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
