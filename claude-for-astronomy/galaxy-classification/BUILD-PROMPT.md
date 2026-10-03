# BUILD-PROMPT — *Learning What the Crowd Would Say.*

The single paste-ready prompt that rebuilds this reel end to end. Run it from
the toolkit root (`brutalist.art/`). Nothing here spends money and nothing here
publishes.

---

## Windows preflight (this machine)

```bash
export PATH="$PWD/.venv/Scripts:$PATH"     # python3 + manim from the venv
export ART_HOME="$PWD"
export PYTHONUTF8=1                        # run.sh's inline Python opens the beat
export PYTHONIOENCODING=utf-8              # sheet without encoding=; cp1252 fails on "·"
```

---

## The prompt

> You are building the reel at
> `D:/study_other/humanitarians-youtube/claude-for-astronomy/claude-hai-galaxy-classification/`
> with the `brutalist.art` toolkit, skill `ai-explainer`, channel `claude-hai`
> (@HumanitariansAI), register Pragmatist, voice Kokoro `af_bella`. It is **Ep. 04**
> of the AI in Astronomy & Space Science series. Free only — if any step asks for
> an API key, stop: that is a bug in the toolkit, not a missing credential.
>
> 1. **Read the doctrine first**, whole: `skills/make/ai-explainer/SKILL.md`, then
>    `skills/make/explainer/SKILL.md`, `skills/make/nopunt/SKILL.md`,
>    `skills/make/your-turn/SKILL.md`, `skills/make/duration-planner/SKILL.md`.
>    This reel's `BUILD-LOG.md` records four authorised deviations and the
>    conventions carried forward from Ep. 03 — honour them, do not silently
>    re-impose the defaults.
> 2. **Generate the imagery first.** `python assets/gen_galaxies.py`. It is
>    deterministic; the seeds are logged in `SOURCES.md`. Nothing downloads.
> 3. **Gate check.** `PEDAGOGY.md` must read `VERDICT: PASS` before audio. If it
>    still reads `PENDING HUMAN SIGNATURE`, either get the signature or generate
>    with `--no-gate` and say so in the report — never edit the verdict line
>    yourself.
> 4. **Audio is the clock.** `python3 runtime/scripts/generate_audio_kokoro.py <reel>`,
>    or `--only B0X` for beats whose narration changed. Never hand-time anything.
> 5. **Build.** `bash runtime/scripts/run.sh <reel> --height 1080` for the QC loop:
>    GATE F → GATE L → GATE A → GATE W → Manim at 4K with GATE B per scene →
>    Remotion fill-in → compile → GATE V. Never call `npx remotion render` by hand.
> 6. **VISUAL QC LAW — look at the frames.** Sample and actually **Read** the PNGs.
>    The mp4 probe is a file check and never counts as QC. Log defects in
>    `_qc/REPORT.md`, fix root causes, re-render until zero BLOCKER and zero MAJOR.
> 7. **Master.** `./art final <reel>` → 4K, no beat markers.
> 8. **Report** runtime, gate results with their actual numbers, and anything left
>    open. **Do not publish.**

---

## Scene-authoring notes that cost a render to learn

- **`import numpy as np` explicitly** — `from manim import *` re-exports it at
  render time; GATE A's stub does not, so `np.random` raises `NameError`.
- **Never derive Line coordinates from `mob.get_left()[0]`** — under GATE A's
  geometry stub a Text has no width. Use `_underline()` / `_strike()`.
- **A strike-through must set `_qc_intentional`** or GATE B calls it text-on-curve.
  `_strike()` already does.
- **Do not run a stroke behind or through a label** — GATE B is geometric, and it
  caught exactly this on B08's bus.
- **`ImageMobject` is not a VMobject** — group it with `Group`, never `VGroup`.
- **Do not rotate an `ImageMobject` for a "rotated view"** — the tile becomes a
  diamond and desyncs from its frame. Pre-bake rotations into the assets, which
  is what the real augmentation does anyway.
- **Terracotta `#D97757` is a MARK, never body text** (2.74:1 on cream). Accented
  words use `#A44A32` (4.7:1). `GHOST` is strokes and fills only.
- **Every scene needs a title at y≈+3.02 and the wordmark bug at y≈−3.12** —
  LOGO LAW, and it is what makes the content bbox span the safe area for GATE V's
  55% canvas-fill floor.
- **No `MathTex`, no LaTeX** — no `dvisvgm` on this machine.

## Image-generation notes

- Accumulate light in **linear flux**, then apply ONE fixed asinh stretch at the
  end (`SOFT=8`, `FMAX=1100`). Stretching per-image, or accumulating in display
  space, blows every core to white and hides the arms.
- `SKY` is a **flux** level, not a display level. Set it high and the stretch
  lifts every tile to mid-grey.
- Spiral arms need many small low-amplitude knots with a small pitch. Few large
  bright knots read as commas, not arms.

## What "done" looks like

- `<slug>-slate.mp4` (review cut) and `<slug>.mp4` (4K master)
- `mp3/` with 14 beat MP3s and `timings.json`
- `manim/B01…B10.mp4` and `media/B00,B11,B12,B13.mp4` — 14/14 slots, zero slates
- `assets/` regenerable from one script
- `_qc/REPORT.md` clean, `_qc/VISUAL-QC.md` written, `_qc/contact_sheet.png` looked at
- Total cost: **$0.00**
