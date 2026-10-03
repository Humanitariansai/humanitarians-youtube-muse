# BUILD-PROMPT — *Knowing the Noise by Name.*

The single paste-ready prompt that rebuilds this reel end to end. Run it from
the toolkit root (`brutalist.art/`). Nothing here spends money and nothing here
publishes.

---

## Windows preflight (this machine)

Two environment facts the toolkit's runner does not set for you on Windows.
Export both before anything else or the run dies on the first beat sheet it
reads:

```bash
export PATH="$PWD/.venv/Scripts:$PATH"     # python3 + manim from the venv
export ART_HOME="$PWD"
export PYTHONUTF8=1                        # runtime scripts open() without an
export PYTHONIOENCODING=utf-8              # encoding= ; cp1252 chokes on "·"
```

---

## The prompt

> You are building the reel at
> `D:/study_other/humanitarians-youtube/claude-for-astronomy/claude-hai-gravitational-wave-detection/`
> with the `brutalist.art` toolkit, skill `ai-explainer`, channel `claude-hai`
> (@HumanitariansAI), register Pragmatist, voice Kokoro `af_bella`. Free only —
> if any step asks for an API key, stop: that is a bug in the toolkit, not a
> missing credential.
>
> 1. **Read the doctrine first**, whole: `skills/make/ai-explainer/SKILL.md`,
>    then `skills/make/explainer/SKILL.md`, `skills/make/nopunt/SKILL.md`,
>    `skills/make/your-turn/SKILL.md`, `skills/make/duration-planner/SKILL.md`.
>    The reel folder's own `BUILD-LOG.md` records four authorised deviations —
>    honour them, do not silently re-impose the default.
> 2. **Gate check.** `PEDAGOGY.md` must read `VERDICT: PASS` before audio. If it
>    still reads `PENDING HUMAN SIGNATURE`, either get the signature or generate
>    audio with `--no-gate` and say so in the report — never edit the verdict
>    line yourself.
> 3. **Audio is the clock.**
>    `python3 runtime/scripts/generate_audio_kokoro.py <reel>` — or `--only B0X`
>    for the beats whose narration changed. Never hand-time anything; the
>    measured `actual_duration_s` values are ground truth.
> 4. **Build.** `bash runtime/scripts/run.sh <reel> --height 1080` for the QC
>    loop. That is the whole machine pass: GATE F (paperwork) → GATE L (beat
>    mix) → GATE A (static) → GATE W (WCAG/margins) → Manim at 4K with GATE B
>    per scene → Remotion fill-in → compile → GATE V (frame-level).
>    Never call `npx remotion render` by hand; `remotion_scenes.py` owns it.
> 5. **VISUAL QC LAW — look at the frames.** After the compile, sample and
>    actually **Read** the PNGs: `ffmpeg -i <cut>.mp4 -vf fps=2
>    _qc/frames/%05d.png`, plus each beat at ~15/50/85% of its span. Audit the
>    nine-point rubric in `CLAUDE-CODE-VISUAL-QC-CHECK.md`. The mp4 probe is a
>    file check and never counts as QC. Log defects in `_qc/REPORT.md`, fix the
>    root cause in `scenes.py` (or the scene component), re-render, repeat until
>    zero BLOCKER and zero MAJOR.
> 6. **Master.** `./art final <reel>` → `<slug>-cut.mp4` at 4K, no beat markers.
> 7. **Report** runtime, gate results with their actual numbers, and anything
>    left open. **Do not publish.** The master stays in the reel folder.

---

## Scene-authoring notes that cost a render to learn

Keep these when editing `scenes.py`, or the gates will teach them to you again:

- **`import numpy as np` explicitly.** `from manim import *` re-exports it at
  render time; GATE A's stub does not, so `np.random` raises `NameError` in
  pre-flight.
- **Never derive Line coordinates from `mob.get_left()[0]`.** Under GATE A's
  geometry stub a Text has no real width, so the resulting coordinates land
  outside the frame and fail the pre-flight. Use the file's `_underline()` /
  `_strike()` helpers (LEFT/RIGHT + `set_width` + `next_to`).
- **A strike-through must set `_qc_intentional = True`** or GATE B reads it as a
  text-on-curve defect. `_strike()` already does.
- **Do not run a rule underneath a label**, even when an opaque chip hides it —
  GATE B is geometric. Draw connectors *between* chips (see `B07`'s rail).
- **Clear a hole in any texture a caption sits on** (see `B02`'s `CLEAR` rect).
- **Terracotta `#D97757` is a MARK, never body text** — 2.74:1 on cream, which
  fails WCAG at every size. Accented words use `#A44A32` (4.7:1).
- **Every scene needs a title at y≈+3.02 and the wordmark bug at y≈−3.12.**
  Besides LOGO LAW, that pair is what makes the content bounding box span the
  safe area so GATE V's 55% canvas-fill floor is met.
- **No `MathTex`, no LaTeX** — this machine has no `dvisvgm`, and nothing in the
  reel needs typeset math.

## What "done" looks like

- `<slug>-slate.mp4` (review cut, beat markers) and `<slug>.mp4` / `<slug>-cut.mp4` (master)
- `mp3/` with 14 beat MP3s and `timings.json`
- `manim/B01…B10.mp4` and `media/B00,B11,B12,B13.mp4` — 14/14 slots filled, zero slates
- `_qc/REPORT.md` clean, `_qc/contact_sheet.png` looked at
- Total cost: **$0.00**
