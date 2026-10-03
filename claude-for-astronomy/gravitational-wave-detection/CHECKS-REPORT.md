# CHECKS-REPORT — *Knowing the Noise by Name.*

Written **before** the first slate compiled, per the ai-explainer PROOF GATE.
The frame-law table at the foot was completed after the QC loop closed; nothing
above it changed.

```
14 beats:  14 SHOW  /  0 justified-HOLD  /  0 PUNT-flagged

Teaching arc:  FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
               SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification (nopunt § SHOW / HOLD / CARD)

| Beat | Class | Named artifact | Why not a CARD |
|---|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` | The interface IS the subject; the ask types and lands answered with three result lines |
| B01 | SHOW | `B01_Presenter` | Presenter identity is the content; name draws on, hairline sweeps, claim sets — motion enacts the line |
| B02 | SHOW | `B02_OneBreath` | Kinetic type with an enacting noise field, not a headline over narration |
| B03 | SHOW | `B03_NearMiss` | Timeline mechanism; glitch lands on the spoken "1.1 seconds before", lane greys, alert routes |
| B04 | SHOW | `B04_MillionGlitches` | Counter moves to its value on the spoken figure; ratio stack carries the scale claim |
| B05 | SHOW | `B05_Impostor` | Side-by-side comparison, held ≥2 s, verdict flips on the spoken contrast |
| B06 | SHOW | `B06_Framework` | Four stations light in narration order; the return arc closes the loop |
| B07 | SHOW | `B07_WorkedExample` | The token walks the framework rail — the example USES the framework visibly |
| B08 | SHOW | `B08_Result` | Two bars grow to their real values, each figure landing with its bar |
| B09 | SHOW | `B09_UnseenClass` | The out-of-distribution tiles stall, the network answers wrongly, people name them |
| B10 | SHOW | `B10_Scope` | Three lanes; two get struck through as the voice rules them out |
| B11 | SHOW | `ClaudeVerdictArtifact` | Verdict artifact page — a bookend where the UI is the subject |
| B12 | SHOW | `ClaudeComposerAsk` | Handoff; the prompt types while it is read, rubric staggers in |
| B13 | SHOW | `ClaudeTitleOutro` | Title restate bookend |

**PUNT count: 0.** No unfilled slate, no gen-AI ask, no "drop an image", no
`SlateCard`, no `DoodleScene`. No beat's narration names a visual the reel does
not draw.

## Legibility contract (every SHOW claim beat)

- [x] Each names its on-screen artifact in `shot.show` (ordered event list) —
      all 14 beats carry a `show` block.
- [x] ~15–35% negative space budgeted per scene; enforced by eye at GATE V and by
      `final_frame_check.py`'s canvas-fill floor from the other direction.
- [x] Un-highlighted elements never faded below ~40% opacity (the greyed
      Livingston lane in B03 and the struck lanes in B10 both sit at ~45%).
- [x] Comparisons shown side by side and held ≥2 s — B05 (chirp vs blip) and
      B08 (Hanford vs Livingston).

## Teaching arc, item by item

- **FRAMEWORK beat** — B06 presents the four-station method as a diagram, and it
  comes *before* the worked example. Not named-in-narration-only.
- **WORKED EXAMPLE** — B07 walks one blip through the framework with the
  four-station rail still on screen. The example uses the framework, visibly.
- **FALSIFIABILITY** — two full beats, not a caveat: B09 is the out-of-distribution
  failure (a class the network cannot name) and B10 is the scope boundary (two
  jobs this tool does not do, each named with its actual owner).
- **SCAFFOLDED viewer task** — B12 gives a real three-part prompt *and* a
  three-item rubric for grading the answer, spoken and on screen.
- **BOOKENDS** — B00 cold open on the Claude composer · B11 verdict artifact ·
  B12 YOUR TURN · B13 title restate. Present and in order.
- **NO SOURCE, NO VERDICT** — B04 and B08 carry author/year citations on screen
  next to their figures; B05, B09 and B10 name the tool or class they assert.
  B11 and B12 recapitulate and are exempt.

## Frame-law self-audit (pre-render)

| Law | Status |
|---|---|
| COLD OPEN LAW — B00 opens on the Claude UI, with RESULT lines | ✓ |
| EXECUTIVE-SUMMARY LAW — BLUF immediately after the cold open | **deviation:** B01 (presenter) sits between B00 and the BLUF at B02, at the human's explicit request. Logged in `BUILD-LOG.md`. |
| ILLUSTRATE LAW — UI only where the UI is the subject | ✓ 4 UI beats, all bookends; 10 illustrated body beats |
| SPARK-LINE LAW — no lonely asterisk; typing only at cold open + handoff | ✓ typing appears in B00 and B12 only |
| HANDOFF LAW — prompt read aloud verbatim, then discussed | ✓ B12 |
| OUTRO LAW — title restate, serif, terracotta period, handle beneath | ✓ B13 |
| DOODLE-BANNED LAW | ✓ no `DoodleScene` / `DoodleChart` |
| REBUILD LAW — figures redrawn natively, never lifted | ✓ the source reel's two archival stills are gone; see `SOURCES.md` |
| LOGO LAW — channel mark on every beat, full size on the outro | ✓ wordmark bug in all 10 Manim scenes, folder chip on B00/B12, full handle on B13 |
| FILL-THE-CANVAS / TYPESIZE | ✓ verified after the fact by reading frames — two shared components were under the floor and were fixed at the root (`_qc/VISUAL-QC.md` item 9) |
| VISUAL QC LAW | ✓ `_qc/REPORT.md` (GATE V: 28 frames, 0 BLOCKER, 0 MAJOR) + `_qc/VISUAL-QC.md` (the human-eye pass and the eight defects it caught) |
