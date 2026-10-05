# CLAUDE-CODE-RENDER.md — Tame your inbox

Render instructions for Bear's Mac (Manim + Kokoro TTS, voice `am_onyx`).
This package is pre-render: `beat_sheet.json`, `scenes.py`, `make_sheet.py`
and docs only. Nothing here has been rendered or published.

## 0. Get the package

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/
# the reel lives at muse/youtube/how-to-use-ai/tame-your-inbox/ in
# Humanitariansai/humanitarians-youtube-muse — clone or copy it to a local reel dir, e.g.
REEL=/Users/bear/Documents/CoWork/bear-textbooks/books/tame-your-inbox
```

All commands below run from the `brutalist.art` toolkit root unless noted.

## 1. Audio (Kokoro am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Then pad BOUT with a 1.0 s silent tail, and write the ffprobe-measured
durations back into `beat_sheet.json` as `actual_duration_s` (keep
`estimated_duration_s` too — `until()`/`finish()` prefer actual).

Whisper-check BIDEA ("Ciao" must not come out mangled; also check the
hyphenated "first-pass" in the BIDEA correction). Re-listen for fused words
generally (watch "read-only" in BHTF).

## 2. Pre-render QA (before any 4K frame)

```bash
cd "$REEL"
# Gate A simulation: scratch dir with ONLY scenes.py + the sheet
mkdir -p /tmp/gatea && cp scenes.py beat_sheet.json /tmp/gatea/
cd /tmp/gatea
for C in B00_ThePile B01_Triage B02_TheSummary B03_TheDraft B04_NeverAutoSend B05_NeverAutoDelete; do
  python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class $C
done
# layout audit (needs the reel dir + real Manim)
cd "$REEL"
for C in B00_ThePile B01_Triage B02_TheSummary B03_TheDraft B04_NeverAutoSend B05_NeverAutoDelete; do
  python3 /path/to/brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class $C --curve-strict
done
```

Require 0 warnings / 0 errors from both. (The static check passed clean in
the pre-render build; the layout audit could not run there — no pangocairo.)

## 3. Stills first

Render each scene's last frame at low res (`manim -ql -s`), build a contact
sheet, and eyeball: the tray and overflowing pile in B00 (three terracotta
dots on the buried cards), the scan-line split in B01 ("needs you" ink,
"noise" dim, no overlap), the thread-to-brief lines in B02, the draft card
with ghost reply lines in B03, the lock over the SEND pill in B04, the X over
the bin and the card in the archive tray in B05, and that every beat has a
label up by its midpoint.

## 4. Midpoint guard

With measured audio in hand, confirm no animation spans any clip's 45–55%
window. The `until()` phrases were chosen to keep motion early or late (see
SHOTLIST.md timing notes); re-verify, because estimated and actual durations
will differ.

## 5. Render

```bash
./brutalist.art/art run "$REEL" --height 2160     # Gates A, B, V + review cut
# watch the review cut, fix, re-run as needed
./brutalist.art/art final "$REEL" --height 2160 --out "$REEL/exports/landscape"
```

Check the master: sha, 3840×2160, 1.0 s silent tail on BOUT.

## 6. Notes / traps already handled in the scenes

- `until()`/`finish()` read `beat_sheet.json` beside `scenes.py` — keep them
  together; do NOT re-run `make_sheet.py` after the final (it wipes build stamps).
- Parallel manim renders sharing one media dir collide on the Text cache —
  give each its own `--media_dir`.
- If a scene is edited after a render, move its old `manim/<BID>.mp4` and the
  stale `<reel>/media/videos` cache to `_superseded/` before re-rendering.
- `art run` renders only scenes whose `manim/<BID>.mp4` is missing.
- B00's pile cards start their drop at y=2.7 (inside the safe area) — the
  static check warns on off-stage starts, so don't move them back off-stage.
- The bin is grey (BAR2), not near-black — keep it that way (GATE T §8.6b).
- B05's archive move is two changes in one play (tray grows + card moves):
  legal — `MoveAlongPath` + `.animate` on the same object is what breaks.
- B01's split is FadeOut(pile) + FadeIn of both stacks in one play; the
  terracotta scan line is faded out in the same play so it can't sit at the
  midpoint.

## 7. STOP

Send the master to Bear. Stage (`art post`) and publish only on his explicit
word, and only from TOPOST. Never commit MP3/MP4/WAV or `__pycache__`.
