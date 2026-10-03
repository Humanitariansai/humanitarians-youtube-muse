# SHOTLIST — *Twenty Seconds to Decide.*

Typed work order, one row per beat. **Every slot is a pipeline slot.** No
archival data, no screen recordings, no gen-AI clips, nothing to shop for. The
dynamic spectra are generated in-repo by `assets/gen_frb.py`, so even the
data-looking material is a pipeline output. A slate in the cut is a bug.

| Beat | Act | Lane | Owner | Artifact | Slot |
|---|---|---|---|---|---|
| B00 | COLD OPEN | Remotion (ask) | pipeline | `ClaudeComposerAsk` — the ask lands answered with three result lines | `media/B00.mp4` |
| B01 | PRESENTER | Manim | pipeline | `B01_Presenter` — name card; a re-run loop struck, replaced by a one-way arrow | `manim/B01.mp4` |
| B02 | EXECUTIVE SUMMARY | Manim | pipeline | `B02_OneBreath` — kinetic type; one waterfall, then the candidate sheet, then a gate | `manim/B02.mp4` |
| B03 | THE SIGNATURE | Manim | pipeline | `B03_Signature` — a vertical line shears into a nu^-2 curve; the DM trio on one axis | `manim/B03.mp4` |
| B04 | THE HAYSTACK | Manim | pipeline | `B04_Haystack` — candidate sheet + 1.5 PB/day, 10^11 S/N per second, ~10^5 per day | `manim/B04.mp4` |
| B05 | THE IMPOSTORS | Manim | pipeline | `B05_Impostors` — three interference classes + the Parkes microwave-oven callout | `manim/B05.mp4` |
| B06 | THE FRAMEWORK | Manim | pipeline | `B06_Framework` — ring buffer + five stations (BUFFER, DEDISPERSE, CANDIDATE, CLASSIFY, KEEP) + overwrite arc | `manim/B06.mp4` |
| B07 | WORKED EXAMPLE | Manim | pipeline | `B07_TwoPictures` — burst pair vs impostor pair, both images each, one verdict apiece | `manim/B07.mp4` |
| B08 | THE DESIGN TELL | Manim | pipeline | `B08_FakeReal` — simulated positives injected into real noise, real recorded negatives | `manim/B08.mp4` |
| B09 | THE RESULT | Manim | pipeline | `B09_Result` — recall arc past 99.5%, the 10^5-to-a-few funnel, the 536/62/18 counters | `manim/B09.mp4` |
| B10 | WHERE IT FAILS | Manim | pipeline | `B10_TwoLimits` — the simulated boundary with one burst outside it; the overwrite, no re-run | `manim/B10.mp4` |
| B11 | VERDICT | Remotion (bookend) | pipeline | `ClaudeVerdictArtifact` — four recap lines | `media/B11.mp4` |
| B12 | HANDOFF | Remotion (bookend) | pipeline | `ClaudeComposerAsk` — "Your turn." + the prompt + three-item rubric | `media/B12.mp4` |
| B13 | OUTRO | Remotion (bookend) | pipeline | `ClaudeTitleOutro` — title restate, @HumanitariansAI, series subline | `media/B13.mp4` |

## Generated plot assets (inputs, not slots)

`python assets/gen_frb.py` — deterministic, seeded, regenerable. Kept out of
`media/` so they never collide with the beat-slot contract.

| Asset | Used by | What it is |
|---|---|---|
| `plots/burst_dm500.png` · `burst_dm500_big.png` | B02, B03, B07 | the hero burst, own time axis |
| `plots/burst_dm200.png` · `burst_dm500_trio.png` · `burst_dm900.png` | B03 | three DMs on ONE shared axis, so the slopes differ |
| `plots/burst_dedispersed.png` | B06 | the same burst corrected: the pulse stands vertical |
| `plots/burst_scattered.png` | B10 | a scattered burst — the kind a simulator may not have covered |
| `plots/rfi_zero_dm.png` · `rfi_zero_dm_big.png` | B05, B07, B08 | broadband, no sweep — the microwave / power-line signature |
| `plots/rfi_narrowband.png` | B05, B08 | a transmitter, always on |
| `plots/rfi_patch.png` | B05, B08 | bursty, band-limited, no sweep |
| `plots/dmtime_burst.png` | B07 | the bowtie closing to a point at a real DM |
| `plots/dmtime_rfi.png` | B07 | the same plane for zero-DM interference: the apex sits on the bottom edge and never closes |
| `plots/sheet_10x6.png` | B02 | 60 candidates, exactly one of them a burst (terracotta) |
| `plots/sheet_24x14.png` | B04, B09 | 336 candidates, one burst |

## Lane histogram (rhythm lint)

- Remotion / Claude UI: **4** beats — B00, B11, B12, B13, all bookends.
- Manim illustration: **10** beats — B01 to B10.
- Archival data: **0**. Human-supply slots: **0**.
- No two consecutive body beats share a composition. B06 and B07 deliberately
  share the station rail, because the worked example must use the framework
  visibly — that reuse is the teaching move, not wallpaper.

## Standing scene rules (all Manim beats)

- Cream `#F2F0E9` ground, ink `#3D3929`, **one** terracotta `#D97757` event per scene.
- Dynamic spectra are ink-on-white plots **framed** on the cream ground — figures
  in a paper. Deliberately unlike Ep. 04's dark photographic plates.
- Every scene: title at y≈+3.02, citation at y≈−3.20, wordmark bug at y≈−3.12.
  That band plan is LOGO LAW and it is what keeps the content bbox spanning the
  safe area for GATE V's canvas-fill floor.
- Any scene showing generated plots captions them as synthetic.
- No `MathTex` / no LaTeX. No `slant=ITALIC` on multi-word `Text`.
- Terracotta is a MARK, never body text (2.74:1 on cream). Accented words use `#A44A32`.
