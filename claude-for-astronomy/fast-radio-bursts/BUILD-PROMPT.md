# BUILD-PROMPT — *Twenty Seconds to Decide.*

The single paste-ready prompt that rebuilds this reel end to end. Run from the
toolkit root (`brutalist.art/`). Nothing spends money; nothing publishes.

---

## Windows preflight

```bash
export PATH="$PWD/.venv/Scripts:$PATH"
export ART_HOME="$PWD"
export PYTHONUTF8=1          # run.sh opens the beat sheet without encoding=
export PYTHONIOENCODING=utf-8
```

---

## The prompt

> You are building the reel at
> `D:/study_other/humanitarians-youtube/claude-for-astronomy/fast-radio-bursts/`
> with the `brutalist.art` toolkit, skill `ai-explainer`, channel `claude-hai`
> (@HumanitariansAI), register Pragmatist, voice Kokoro `af_bella`. **Ep. 05** of
> the AI in Astronomy & Space Science series. Free only.
>
> 1. **Read the doctrine whole**: `skills/make/ai-explainer/SKILL.md`, then
>    `explainer`, `nopunt`, `your-turn`, `duration-planner`. `BUILD-LOG.md` here
>    records four authorised deviations — honour them.
> 2. **Generate the plots first**: `python assets/gen_frb.py`. Deterministic;
>    seeds in `SOURCES.md`. Nothing downloads.
> 3. **Gate check**: `PEDAGOGY.md` must read `VERDICT: PASS` before audio. It
>    does — signed 2026-08-23. If a future edit reopens the gate, get a fresh
>    signature or generate with `--no-gate` and say so. Never edit that line
>    yourself.
> 4. **Audio is the clock**: `generate_audio_kokoro.py <reel>`, or `--only B0X`.
> 5. **Build**: `bash runtime/scripts/run.sh <reel> --height 1080`.
> 6. **VISUAL QC LAW**: sample frames and actually Read the PNGs. The mp4 probe
>    is a file check and never counts as QC.
> 7. **Master**: `./art final <reel>` → 4K.
> 8. **Report** gate numbers and anything open. **Do not publish.**

---

## Things that cost a render to learn

**Scene authoring**

- `import numpy as np` explicitly — GATE A's stub does not re-export it.
- Never derive Line coordinates from `mob.get_left()[0]`; use `_underline()` / `_strike()`.
- A strike-through needs `_qc_intentional` or GATE B calls it text-on-curve.
- Never run a stroke behind or through a label.
- `ImageMobject` is not a VMobject — use `Group`, never `VGroup`.
- Do not rotate an `ImageMobject`; pre-bake rotations into the assets.
- A 3:2 plot at width `w` is `0.667w` tall. Two stacked inside a 2.7-unit card do
  not fit. Check the arithmetic before rendering, not after.

**Plot generation**

- At 400-800 MHz a DM of 500 sweeps about **9.7 seconds**. A fixed 100 ms window
  puts the burst off-panel. Derive the time axis from the sweep.
- A DM error of 1 pc cm^-3 smears the pulse ~19 ms across this band, so a DM-time
  bowtie spans only a couple of DM units. Derive that window too.
- To show DMs differing, put them on ONE shared axis. Auto-scaled panels all look
  identical.
- Keep the noise faint. GATE V's ink threshold is per-channel against a quantised
  warm page colour whose red is ~248, so a neutral grey pixel counts as ink below
  ~223. Realistic speckle fails the whole beat as low-contrast.

**Rendering**

- **Manim's cache does not hash image contents.** If you change a PNG a scene
  loads, delete `media/videos/` as well as `manim/*.mp4`, or pass
  `--disable_caching`. Otherwise you re-render the old frames.
- `./art run` at 4K on a 10-scene reel exceeds a 10-minute call. Run the Remotion
  bookends individually and let the Manim stage run under `timeout`; run.sh skips
  filled slots on re-entry, so it is safe to resume.

## What "done" looks like

- `fast-radio-bursts-slate.mp4` (review cut) and `fast-radio-bursts.mp4` (4K master)
- `mp3/` with 14 beat MP3s and `timings.json`
- `manim/B01…B10.mp4` and `media/B00,B11,B12,B13.mp4` — 14/14, zero slates
- `assets/` regenerable from one script
- `_qc/REPORT.md` clean, `_qc/VISUAL-QC.md` written
- Total cost: **$0.00**
