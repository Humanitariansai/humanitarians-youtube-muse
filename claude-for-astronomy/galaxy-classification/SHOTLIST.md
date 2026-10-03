# SHOTLIST — *Learning What the Crowd Would Say.*

Typed work order, one row per beat. **Every slot in this reel is a pipeline slot.**
No archival stills, no screen recordings, no gen-AI clips, nothing to shop for.
The galaxy imagery is generated in-repo by `assets/gen_galaxies.py`, so even the
photographic-looking material is a pipeline output. A slate in the cut is a bug.

| Beat | Act | Lane | Owner | Artifact | Slot |
|---|---|---|---|---|---|
| B00 | COLD OPEN | Remotion (ask) | pipeline | `ClaudeComposerAsk` — the ask lands answered with three result lines | `media/B00.mp4` |
| B01 | PRESENTER | Manim | pipeline | `B01_Presenter` — name card; the claim is a struck line replaced by an accented one | `manim/B01.mp4` |
| B02 | EXECUTIVE SUMMARY | Manim | pipeline | `B02_OneBreath` — kinetic type; one cutout, tallies fanning out, then a proportion bar | `manim/B02.mp4` |
| B03 | THE SUBJECT | Manim | pipeline | `B03_Shapes` — five framed cutouts filling in on their spoken labels | `manim/B03.mp4` |
| B04 | THE CROWD | Manim | pipeline | `B04_Crowd` — survey field + 900,000 counter + 20,000/hr rate + the 38-looks row | `manim/B04.mp4` |
| B05 | THE TREE | Manim | pipeline | `B05_Tree` — three-level decision tree, traversed path drawn in terracotta | `manim/B05.mp4` |
| B06 | THE FRAMEWORK | Manim | pipeline | `B06_Framework` — four stations (ASK · TALLY · TRAIN · PREDICT) + active-learning return arc | `manim/B06.mp4` |
| B07 | WORKED EXAMPLE | Manim | pipeline | `B07_VoteFraction` — 10×10 vote grid collapsing to 0.63; the word "barred" struck through | `manim/B07.mp4` |
| B08 | THE DESIGN TELL | Manim | pipeline | `B08_NoUp` — one galaxy at four rotations converging on one shared-weights block | `manim/B08.mp4` |
| B09 | THE RESULT | Manim | pipeline | `B09_Result` — 99% arc, predicted-vs-actual inside a 5–10% band, 8,670,000 counter, Rubin marker | `manim/B09.mp4` |
| B10 | WHERE IT FAILS | Manim | pipeline | `B10_Ceilings` — crowd-vs-truth gap on the left, survey-to-survey mismatch on the right | `manim/B10.mp4` |
| B11 | VERDICT | Remotion (bookend) | pipeline | `ClaudeVerdictArtifact` — four recap lines | `media/B11.mp4` |
| B12 | HANDOFF | Remotion (bookend) | pipeline | `ClaudeComposerAsk` — "Your turn." + the prompt + three-item rubric | `media/B12.mp4` |
| B13 | OUTRO | Remotion (bookend) | pipeline | `ClaudeTitleOutro` — title restate, @HumanitariansAI, series subline | `media/B13.mp4` |

## Generated image assets (inputs, not slots)

Produced by `python assets/gen_galaxies.py` — deterministic, seeded, regenerable.
These are **inputs to the Manim scenes**, deliberately kept out of `media/` so
they never collide with the beat-slot contract.

| Asset | Used by | What it is |
|---|---|---|
| `assets/galaxies/spiral_101…104.png` | B02, B03, B08 | two-arm spirals, 256px |
| `assets/galaxies/barred_201…203.png` | B03, B05, B07 | barred spirals — the "is there a bar?" case |
| `assets/galaxies/elliptical_301…304.png` | B03 | smooth, structureless |
| `assets/galaxies/edgeon_401…403.png` | B03 | edge-on discs with dust lanes |
| `assets/galaxies/merger_501…502.png` | B03 | two cores, tidal bridge and tails |
| `assets/galaxies/spiral3_601…602.png` | B03 (spare) | three-arm variants |
| `assets/galaxies/hero.png` | B05, B07, B10 | the 512px barred spiral the reel votes on |
| `assets/field_12x7.png` | B04 | 84-galaxy survey sheet |
| `assets/field_28x16.png` | B09, B10 | 448-galaxy sheet for the scale beats |

## Lane histogram (rhythm lint)

- Remotion / Claude UI: **4** beats — B00, B11, B12, B13, all bookends where the UI is the subject.
- Manim illustration: **10** beats — B01–B10.
- Archival stills: **0**. Human-supply slots: **0**.
- No two consecutive body beats share a composition. B06→B07 deliberately share
  the four-station rail, because the worked example has to use the framework
  visibly — that reuse is the teaching move, not wallpaper.

## Standing scene rules (all Manim beats)

- Cream `#F2F0E9` ground, ink `#3D3929`, **one** terracotta `#D97757` event per scene.
- Galaxy cutouts are dark tiles **framed** on the cream ground — plates on a page,
  never full-bleed. They never carry the accent colour.
- Every scene: title at y≈+3.02, citation at y≈−3.20, `@HumanitariansAI` bug at
  y≈−3.12 bottom-right. That band plan is LOGO LAW *and* what keeps the content
  bbox spanning the safe area for GATE V's canvas-fill floor.
- Any scene showing generated imagery captions it as synthetic.
- No `MathTex` / no LaTeX (no `dvisvgm` on this machine).
- No `slant=ITALIC` on multi-word `Text` (Pango collapses the spaces).
- Terracotta is a MARK, never body text (2.74:1 on cream). Accented words use `#A44A32`.
