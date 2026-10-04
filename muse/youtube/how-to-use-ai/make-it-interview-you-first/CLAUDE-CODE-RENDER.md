# CLAUDE-CODE-RENDER.md — Make It Interview You First

Render instructions for Bear's Mac (Manim + Kokoro TTS, voice `am_onyx`).
This package is pre-render: `beat_sheet.json`, `scenes.py`, `make_sheet.py`
and docs only. Nothing here has been rendered or published.

## 0. Get the package

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/
# the reel lives at muse/youtube/how-to-use-ai/make-it-interview-you-first/ in
# Humanitariansai/humanitarians-youtube-muse — clone or copy it to a local reel dir, e.g.
REEL=/Users/bear/Documents/CoWork/bear-textbooks/books/make-it-interview-you-first
```

All commands below run from the `brutalist.art` toolkit root unless noted.

## 1. Audio (Kokoro am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Then pad BOUT with a 1.0 s silent tail, and write the ffprobe-measured
durations back into `beat_sheet.json` as `actual_duration_s` (keep
`estimated_duration_s` too — `until()`/`finish()` prefer actual).

Whisper-check BIDEA ("Hallo" must not come out as "hedge") and re-listen for
fused words (the "number + Claude" trap, e.g. "five questions" — should be
clean, but check; "favourite colour" and "apologise" are British spellings,
verify Kokoro voices them naturally or reword).

## 2. Pre-render QA (before any 4K frame)

```bash
cd "$REEL"
# Gate A simulation: scratch dir with ONLY scenes.py + the sheet
mkdir -p /tmp/gatea && cp scenes.py beat_sheet.json /tmp/gatea/
cd /tmp/gatea
for C in B00_AskOnce B01_AskFirst B02_FiveQuestions B03_BriefBuilt B04_TailoredPlan B05_SecondDemo B06_SharpQuestions B07_TheRule; do
  python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class $C
done
# layout audit (needs the reel dir + real Manim)
cd "$REEL"
for C in B00_AskOnce B01_AskFirst B02_FiveQuestions B03_BriefBuilt B04_TailoredPlan B05_SecondDemo B06_SharpQuestions B07_TheRule; do
  python3 /path/to/brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class $C --curve-strict
done
```

Require 0 warnings / 0 errors from both. (The static check passed clean in
the pre-render build; the layout audit could not run there — no
Manim/pangocairo in that VM — so hand-placed labels used ≥0.3 leader gaps,
no curve/label crossings, coords inside ±6.2 × ±3.3, type ≥ 32.)

## 3. Stills first

Render each scene's last frame at low res (`manim -ql -s`), build a contact
sheet, and eyeball: the five question cards in a row (B02), the chips inside
the brief box (B03, tucked behind the front wall), the thin dimmed generic
page vs the full tailored page (B04), the struck lazy card vs the sharp card
(B06), the two rule cards (B07), and that every beat has a label up by its
midpoint.

## 4. Midpoint guard

With measured audio in hand, confirm no animation spans any clip's 45–55%
window. The `until()` phrases were chosen to keep motion early or late (see
SHOTLIST.md timing notes); B03's later chips may drift toward the midpoint
depending on Kokoro pacing — re-verify, because estimated and actual
durations will differ.

## 5. Render

```bash
./brutalist.art/art run "$REEL" --height 2160     # Gates A, B, V + review cut
# watch the review cut, fix, re-run as needed
./brutalist.art/art final "$REEL" --height 2160 --out "$REEL/exports/landscape"
```

Check the master: sha, 3840×2160, 1.0 s silent tail on BOUT.

## 6. Notes / traps already handled in the scenes

- `until()`/`finish()` are the kit's module-level functions, called as
  `until(self, "phrase")` — not methods (the stub raises AttributeError
  otherwise; caught in pre-render QC).
- Every `until()` phrase was verified verbatim against its beat's
  `narration_text` by script in the pre-render build.
- `until()`/`finish()` read `beat_sheet.json` beside `scenes.py` — keep them
  together; do NOT re-run `make_sheet.py` after the final (it wipes build stamps).
- Parallel manim renders sharing one media dir collide on the Text cache —
  give each its own `--media_dir`.
- If a scene is edited after a render, move its old `manim/<BID>.mp4` and the
  stale `<reel>/media/videos` cache to `_superseded/` before re-rendering.
- `art run` renders only scenes whose `manim/<BID>.mp4` is missing.

## 7. STOP

Send the master to Bear. Stage (`art post`) and publish only on his explicit
word, and only from TOPOST. Never commit MP3/MP4/WAV or `__pycache__`.
