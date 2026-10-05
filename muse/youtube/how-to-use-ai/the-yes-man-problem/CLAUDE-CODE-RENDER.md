# CLAUDE-CODE-RENDER.md — The yes-man problem.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/the-yes-man-problem/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text`
field with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`,
`audio/BDEFS.mp3`, `audio/B00.mp3`, …, `audio/B08.mp3`,
`audio/BHTF.mp3`, `audio/BOUT.mp3` (13 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting "Hallo" opens BIDEA — whisper-check
it (known-clean Kokoro greetings include Hallo). The BHTF line names
"Paste this into Claude" — read it exactly. Read the BOUT line exactly:
"The yes-man problem. Liam, in for Bear. At Nik Bear Brown. Thanks for
watching."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel the-yes-man-problem \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the naive line corrects to "it wants
your approval" in BIDEA; the three terms land in BDEFS; the
"You're absolutely right!" bubble stamps in B00; the dashed mirror line
draws between the two chats in B01; five curved arrows bend toward "your
view" in B02; the agreement dial sweeps into the red in B03; the mask
card flips to "here's the flaw:" in B04; the "?" card stays face-down
in B05; the terracotta steel bar towers over the straw bar in B06; the
idea card slides to the stranger's frame in B07; the terracotta pin
drops on "the flaw in your plan" in B08.

Note: the four bookend beats (BIDEA/BDEFS/BHTF/BOUT) are REMOTION
patterns (`BrutalistHesitantWriter`, `ClaudeDefinitions`,
`ClaudeComposerAsk`, `ClaudeTitleOutro` — props in `beat_sheet.json`);
only B00–B08 are Manim scenes.

## 3. Type and layout audit

Run on the Mac (cannot run in this VM — no Manim/pangocairo here):

```
python3 runtime/qc/manim_layout_audit.py --curve-strict
```

This checks per-rendered-frame type size, overflow, contrast, kerning,
and layout curves. Fix any FAIL before the final master. The scenes
were authored to the drawing laws (labels beside objects, ≥30pt, inside
±6.3×±3.4) — see CHECKS-REPORT.md for the two width hazards already
fixed.

## 4. Final 4K master

```
./art final --reel the-yes-man-problem
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~4m33s (estimated; measured audio is the clock). 9 Manim
  scenes, all static-QC clean (0 warn, 0 error).
- Skill: ai-explainer (switched from the suggested deep-explainer; see
  BUILD-LOG.md) — zero cards, all drawings; the chat window is the
  recurring cast object; "You're absolutely right!" is the recurring
  punchline object.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
