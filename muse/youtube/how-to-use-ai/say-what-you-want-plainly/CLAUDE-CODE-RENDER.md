# CLAUDE-CODE-RENDER.md — Say what you want, plainly

Render instructions for Bear's Mac. This package is pre-render: everything
except the final MP3/MP4. Never publish without Bear's explicit instruction.

## 0. Get the package

Clone or pull `Humanitariansai/humanitarians-youtube-muse` and work in
`muse/youtube/how-to-use-ai/say-what-you-want-plainly/`. All file activity
stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`.

## 1. Audio (Kokoro, voice `am_onyx`)

From `books/`:

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py muse/youtube/how-to-use-ai/say-what-you-want-plainly
```

Then pad BOUT with a 1.0 s silent tail, and write the ffprobe-measured
durations back into `beat_sheet.json` as `actual_duration_s` per beat
(`make_sheet.py` wrote `estimated_duration_s`; the scenes' `until()`
pacing reads `actual_duration_s` when present).

Whisper-check the first beat ("Hallo" is on the clean list, but check it
anyway) and any number/acronym-adjacent phrasing. Re-voice single beats
with `--only <BID>` (note: `--only` silently drops BOUT's 1.0 s pad, so
re-pad and re-measure BOUT after any full run).

## 2. Pre-audit (before any 4K render)

```bash
# Gate A from a scratch folder holding ONLY scenes.py (that is what art run sees)
mkdir /tmp/st && cp muse/youtube/how-to-use-ai/say-what-you-want-plainly/scenes.py /tmp/st/
python3 brutalist.art/runtime/qc/static_scene_check.py /tmp/st/scenes.py --class B00_PromptSlip
# … repeat for B01_Guesses B02_MostCommon B03_TheFix B04_FourQuestions B05_NewHire B06_BriefRewrite B07_Compare
# Layout audit (could NOT run in the build VM — no Manim/pangocairo there):
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict
```

Every scene passed the static checker in the build VM (8/8, 0 warnings,
0 errors — see CHECKS-REPORT.md); the layout audit still needs its first
run here.

## 3. Stills first

Render each scene's last frame at low resolution (`manim -ql -s`) into a
scratchpad and look at a contact sheet before any 4K render. Check:
labels sit beside objects (never inside outlines, never on terracotta),
type ≥ 32, everything inside ±6.2 × ±3.3, the four B04 chips don't
overlap, B02's crowd pages sit in a clean horizontal row.

## 4. Render

```bash
./brutalist.art/art run muse/youtube/how-to-use-ai/say-what-you-want-plainly --height 2160
# look at frames, then:
./brutalist.art/art final muse/youtube/how-to-use-ai/say-what-you-want-plainly --height 2160 \
  --out muse/youtube/how-to-use-ai/say-what-you-want-plainly/exports/landscape
```

Check the master: sha, 3840×2160, silent tail present. Keep every scene's
run time within its `actual_duration_s` (`finish()` handles this as long
as the `play` calls fit) — a clip longer than its audio gets centre-cut.

## 5. Bookends

BIDEA (`BrutalistHesitantWriter`), BDEFS (`ClaudeDefinitions`), BHTF
(`ClaudeComposerAsk`) and BOUT (`ClaudeTitleOutro`) are Remotion
compositions driven by `beat_sheet.json`; render only via
`runtime/scripts/remotion_scenes.py`. The hesitant-writer trigger
("write a summary" → "a three-sentence summary of this page, in plain
words, for a teammate") must appear verbatim and punctuation-free.

## 6. STOP

Send Bear the master. Stage (`art post`) and publish only on his word,
and only from TOPOST. Never commit MP3/MP4/WAV or `__pycache__` to the repo.
