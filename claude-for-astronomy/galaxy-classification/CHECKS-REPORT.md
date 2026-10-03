# CHECKS-REPORT — *Learning What the Crowd Would Say.*

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
| B01 | SHOW | `B01_Presenter` | The claim is enacted: the wrong sentence is struck through and replaced, it is not narrated over a headline |
| B02 | SHOW | `B02_OneBreath` | Kinetic type against a real cutout; tallies fan out and collapse into a proportion bar |
| B03 | SHOW | `B03_Shapes` | Five morphologies fill their frames on their spoken labels; the bar is ringed on the spoken word |
| B04 | SHOW | `B04_Crowd` | A survey field, a counter that climbs to its cited value, and 38 marks accumulating on ONE galaxy |
| B05 | SHOW | `B05_Tree` | A decision tree draws level by level and the traversed path lights terracotta |
| B06 | SHOW | `B06_Framework` | Four stations light in narration order; the return arc closes the loop |
| B07 | SHOW | `B07_VoteFraction` | 100 marks fill, 63 tip one way, and the grid collapses into 0.63 — the collapse IS the teaching moment |
| B08 | SHOW | `B08_NoUp` | Four rotations of one galaxy converge on one shared-weights block |
| B09 | SHOW | `B09_Result` | An arc fills to its cited value, a scatter lands inside its band, a counter runs to 8,670,000 |
| B10 | SHOW | `B10_Ceilings` | Two panels, each enacting its own limit: a gap on a number line, and a struck transfer arrow |
| B11 | SHOW | `ClaudeVerdictArtifact` | Verdict artifact page — a bookend where the UI is the subject |
| B12 | SHOW | `ClaudeComposerAsk` | Handoff; the prompt types while it is read, rubric staggers in |
| B13 | SHOW | `ClaudeTitleOutro` | Title restate bookend |

**PUNT count: 0.** No unfilled slate, no gen-AI ask, no "drop an image", no
`SlateCard`, no `DoodleScene`. Every visual the narration names is drawn — and
the galaxy imagery the narration implies is generated in-repo rather than
requested from a human.

## Legibility contract (every SHOW claim beat)

- [x] Each names its on-screen artifact in `shot.show` (ordered event list) —
      all 14 beats carry a `show` block.
- [x] ~15–35% negative space per scene, enforced by the band plan.
- [x] Un-highlighted elements never faded below ~40% opacity — B05's untaken
      branches and B07's 37 "no bar" marks both sit at ~55–90%.
- [x] Comparisons shown side by side and held — B03's five morphologies, B08's
      four rotations, B10's two surveys.

## Teaching arc, item by item

- **FRAMEWORK beat** — B06 presents the four-station loop as a diagram, before
  the worked example. Not named-in-narration-only.
- **WORKED EXAMPLE** — B07 walks one galaxy through that loop with the station
  rail still on screen, and produces the actual training target.
- **FALSIFIABILITY** — B10, a full beat with two independent limits: the crowd
  ceiling and survey-to-survey domain shift.
- **SCAFFOLDED viewer task** — B12 gives a three-part prompt *and* a three-item
  rubric, spoken and on screen.
- **BOOKENDS** — B00 · B11 · B12 · B13, present and in order.
- **NO SOURCE, NO VERDICT** — B04, B05, B08, B09 and B10 each carry an
  on-screen citation beside their figures; B10's citation additionally marks
  which half of the beat is inference rather than a published result.

## Frame-law self-audit

| Law | Status |
|---|---|
| COLD OPEN LAW — B00 opens on the Claude UI, with RESULT lines | ✓ |
| EXECUTIVE-SUMMARY LAW — BLUF immediately after the cold open | **deviation:** B01 (presenter) sits between B00 and the BLUF at B02, carrying forward the human's standing choice from Ep. 03. Logged in `BUILD-LOG.md`. |
| ILLUSTRATE LAW — UI only where the UI is the subject | ✓ 4 UI beats, all bookends; 10 illustrated body beats |
| SPARK-LINE LAW — typing only at cold open + handoff | ✓ B00 and B12 only |
| HANDOFF LAW — prompt read aloud verbatim, then discussed | ✓ B12 |
| OUTRO LAW — title restate, serif, terracotta period, handle beneath | ✓ B13 |
| DOODLE-BANNED LAW | ✓ |
| REBUILD LAW — figures redrawn natively, never lifted | ✓ no published figure is reproduced; all imagery is generated in-repo |
| LOGO LAW — channel mark on every beat, full size on the outro | ✓ wordmark bug in all 10 Manim scenes, folder chip on B00/B12, full handle on B13 |
| FILL-THE-CANVAS / TYPESIZE | ✓ verified by reading frames; the two shared components fixed during Ep. 03 carry over |
| VISUAL QC LAW | ✓ `_qc/REPORT.md` (GATE V) + `_qc/VISUAL-QC.md` (the human-eye pass) |
