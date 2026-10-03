# SHOTLIST — *Knowing the Noise by Name.*

Typed work order, one row per beat. **Every slot in this reel is a pipeline slot.**
There are no human-supply slots: no archival stills, no screen recordings, no
gen-AI clips, nothing to shop for. If a slate appears in the cut, it is a bug in
the render, not a request for media.

| Beat | Act | Lane | Owner | Artifact | Slot |
|---|---|---|---|---|---|
| B00 | COLD OPEN | Remotion (ask) | pipeline | `ClaudeComposerAsk` — the ask lands answered with three result lines | `media/B00.mp4` |
| B01 | PRESENTER | Manim | pipeline | `B01_Presenter` — name card, terracotta hairline, wordmark bug | `manim/B01.mp4` |
| B02 | EXECUTIVE SUMMARY | Manim | pipeline | `B02_OneBreath` — kinetic type; noise field → tiles → named tiles | `manim/B02.mp4` |
| B03 | THE STAKES | Manim | pipeline | `B03_NearMiss` — two detector lanes on one time axis; glitch at −1.1 s, Livingston struck out of the joint search, single-detector alert, Fermi marker at +1.7 s | `manim/B03.mp4` |
| B04 | THE PROBLEM | Manim | pipeline | `B04_MillionGlitches` — 51-day bar + counter to 1,000,000 + reviewer-ratio stack | `manim/B04.mp4` |
| B05 | THE PROBLEM | Manim | pipeline | `B05_Impostor` — merger vs blip drawn in the SAME envelope (one leans, one does not), held side by side; the consistency check returns the same verdict twice | `manim/B05.mp4` |
| B06 | THE FRAMEWORK | Manim | pipeline | `B06_Framework` — four stations (RENDER · LABEL · TRAIN · SORT) + terracotta return arc | `manim/B06.mp4` |
| B07 | WORKED EXAMPLE | Manim | pipeline | `B07_WorkedExample` — one blip token walks the same four stations; four time windows | `manim/B07.mp4` |
| B08 | THE RESULT | Manim | pipeline | `B08_Result` — 97.1% arc, 20-class strip, two per-detector bars summing to 613,786 | `manim/B08.mp4` |
| B09 | WHERE IT FAILS | Manim | pipeline | `B09_UnseenClass` — two tiles match no bin; volunteers name Paired Doves and Helix | `manim/B09.mp4` |
| B10 | SCOPE | Manim | pipeline | `B10_Scope` — three lanes, two struck through (matched filtering, BayesWave), one live | `manim/B10.mp4` |
| B11 | VERDICT | Remotion (bookend) | pipeline | `ClaudeVerdictArtifact` — four recap lines | `media/B11.mp4` |
| B12 | HANDOFF | Remotion (bookend) | pipeline | `ClaudeComposerAsk` — "Your turn." + the prompt + three-item rubric | `media/B12.mp4` |
| B13 | OUTRO | Remotion (bookend) | pipeline | `ClaudeTitleOutro` — title restate, @HumanitariansAI, series subline | `media/B13.mp4` |

## Lane histogram (rhythm lint)

- Remotion / Claude UI: **4** beats — B00, B11, B12, B13. All four are bookends;
  the UI is the subject in each (ILLUSTRATE LAW).
- Manim illustration: **10** beats — B01–B10.
- Archival stills: **0**. Human-supply slots: **0**.
- Longest same-scheme run: B01–B10 are all Manim, but no two consecutive scenes
  share a composition (card → kinetic type → timeline → counter → two-up →
  pipeline → pipeline-with-token → chart → bins → lanes). B06→B07 deliberately
  share the four-station rail because the worked example must use the framework
  visibly; that reuse is the teaching move, not wallpaper.

## Standing scene rules (all Manim beats)

- Cream `#F2F0E9` ground, ink `#3D3929`, **one** terracotta `#D97757` event per scene.
- Every scene carries a top-left title and a bottom-right `@HumanitariansAI`
  wordmark bug, both inside the title-safe inset (LOGO LAW; also what keeps the
  content bounding box spanning the safe area for GATE V).
- No `MathTex` / no LaTeX anywhere — this machine has no `dvisvgm`, and nothing
  in the reel needs typeset math.
- No `slant=ITALIC` on multi-word `Text` (Pango collapses the spaces).
- Numbers appear only with a citation line. `~15–35%` negative space.
- Un-highlighted elements never below ~40% opacity.
