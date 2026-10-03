# BUILD-LOG — the-creative-engineer

**Label: previz-grade.** First-pass full-length watchable cut, per Gate D1 of
`deep-explainer` — real Kokoro audio, real Manim/Remotion beats, no pantry
(the loop waives Tier 2/3 shopping-list beats to zero by design).

## What shipped

- `the-creative-engineer.mp4` — 401 s (≈ 6:41), 1920×1080, 24 fps.
- 28 beats, 28/28 filled as VIDEO (zero slates in the master cut).
- Audio: Kokoro `am_onyx` (Liam), free/local. Mean volume −23.7 dB. Non-silent.
- Palette: `claude` (cream / warm-ink / terracotta), FILL palette locked.
- Narration lint (STANDALONE-IDEA LAW): **clean**, 0 hard / 0 soft hits.

## The film

Title: **When the Signal Stops Sorting.** Standalone idea — the film is
about signals collapsing under a cheap tool, not about a chapter, not about
a book, not about a course. The chapter is the SOURCE; the idea is the
SUBJECT. A stranger who has read nothing can follow the whole thing.

Three acts on the ai-explainer bookended chassis (cold open · hesitant-writer
executive summary · body · verdict · YOUR TURN · title outro):

- **Act I — Signals and What Breaks Them.** Employers can't measure
  productivity directly, so they lean on proxies. Spence's 1973 mechanism:
  a signal informs only while producing it stays costly. The public-repo
  signal for software was that. The 2023 Peng et al. RCT (161 vs 71 min)
  and the 2024 82% adoption data collapse the cost-structure. Proof
  everyone can produce cheaply stops being proof.
- **Act II — What the Tool Did Not Touch.** Four verbs — Ideate, Build,
  Brand, Ship. Build is where the tool lives. Ideate (choosing the right
  problem), Brand (being recognizable to an audience), and Ship (real
  users, real feedback) are the ends of the pipe the tool didn't reach.
- **Act III — Being Legible on Purpose.** The 12-archetype wheel as a map
  of "who am I to the audience I want." Descriptive first — read from the
  evidence you already produced. Two worked engineer profiles (Engineer A →
  Outlaw/Rebel; Engineer B → Everyman) demonstrate the reading.

## Beat sheet at a glance

| Range | Lane | Component(s) |
|---|---|---|
| B00 (cold open) | Remotion | `ClaudeComposerAsk` — Ola, Liam |
| B01 (BLUF) | Remotion | `BrutalistHesitantWriter` — typing corrects the misconception |
| B02, B10, B16 (act cards) | Remotion | `ClaudeSegmentCard` |
| B03, B04 (Spence theory) | Remotion | `BrandSignalMatrix` (phase: theory) |
| B05, B06, B09, B24 (collapse) | Remotion | `BrandB01SignalCollapse` |
| B07, B08 (the numbers) | Remotion | `BarChart` (161/71 min; 82% survey) |
| B11 (four verbs) | Remotion | `BrandVerbScorecard` |
| B12, B13, B15 (verb beats) | Remotion | `BrandB01VerbGap` |
| B14, B17, B18 (brand / firms) | Remotion | `BrandB01AlignmentDrift` |
| B19–B22 (archetype work) | Remotion | `BrandArchetypeWheel` (Sage/Rebel; Explorer; Outlaw; Everyman) |
| B23 (three lenses) | Remotion | `BrandRepricingTable` |
| BVDT (verdict) | Remotion | `ClaudeVerdictArtifact` |
| BHTF (your turn) | Remotion | `ClaudeComposerAsk` — read-aloud handoff prompt |
| BOUT (title restate) | Remotion | `ClaudeTitleOutro` |

Everything renders through registered components; nothing slates.

## Fixes made during the build

1. **B01 seed type.** Initial pass wrote `seed: 731` (number).
   `BrutalistHesitantWriter`'s zod schema takes `seed: string`. First
   render errored with a ZodError. Swapped to `"seed": "731"` and
   re-rendered `--only B01 --force`. No effect on any other beat.

## Swaps and slates

None. Every beat has a registered Remotion component; every component
rendered on the first try (after the B01 seed fix). No pantry shopping,
no gen-AI fallback, no slates in the master.

## Lint and gates

- **STANDALONE-IDEA LAW:** clean — `narration_lint.py` returned 0 hard /
  0 soft against title "Branding and AI".
- **GATE LANE:** PASS — 28/28 beats, no pipeline-slate violations, no
  gen-AI-in-master violations.
- **GATE AUDIO:** PASS — mean volume −23.7 dB (well above the −40 dB floor).
- **Motion histogram warning** noted: 100% "?" motion tag. Benign — this
  loop does not author `shot.motion` pantry classifications (no pantry).

## Known gaps vs the full skill

- **Gate T (type-lock)** and **Gate V (visual QC)** were not run — the
  loop's minimal contract is "audible cut, mp4 newer than sheet, lint
  clean". A reviewer promoting this to the final channel cut should
  `type_check.py` per frame and sample-audit for edge bleed / undersized
  type / brand-bug placement per VISUAL QC LAW before publishing.
- **BUILD-PROMPT.md** and **CHECKS-REPORT.md** were not authored — this
  is a previz-grade first pass, not a final review artifact package.
- Only the four core Brand components were reused (`SignalMatrix`,
  `B01SignalCollapse`, `VerbScorecard`, `ArchetypeWheel`, plus the
  `B01VerbGap`, `B01AlignmentDrift`, and `RepricingTable`). Several beats
  reuse the same component with different `sparkLine` — a review pass
  may want to author beat-specific illustrations to break the visual
  monotony inside long stretches (B12/B13/B15 all use `B01VerbGap`,
  B14/B17/B18 all use `B01AlignmentDrift`, B19/B20/B21/B22 all use
  `BrandArchetypeWheel`).
- **PROOF GATE / nopunt** classification was not written per beat.

## Verifications the supervisor will re-run

```bash
ls -la the-creative-engineer/beat_sheet.json the-creative-engineer/the-creative-engineer.mp4
#   mp4 mtime (12:52) > beat_sheet mtime (12:30) ✓

ffprobe -v error -show_entries format=duration \
  -of csv=p=0 the-creative-engineer/the-creative-engineer.mp4
#   401.121 s ✓

python3 books/anthropics/narration_lint.py \
  the-creative-engineer/beat_sheet.json "Branding and AI"
#   STANDALONE-IDEA LAW: clean ✓
```
