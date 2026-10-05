# CLAUDE-CODE-RENDER.md — Talk to your tools

Render instructions for Bear's Mac (Manim + Kokoro TTS, voice `am_onyx`).
This package is pre-render: `beat_sheet.json`, `scenes.py`, `make_sheet.py`
and docs only. Nothing here has been rendered or published.

## 0. Get the package

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/
# the reel lives at muse/youtube/how-to-use-ai/talk-to-your-tools/ in
# Humanitariansai/humanitarians-youtube-muse — clone or copy it to a local reel dir, e.g.
REEL=/Users/bear/Documents/CoWork/bear-textbooks/books/talk-to-your-tools
```

All commands below run from the `brutalist.art` toolkit root unless noted.

## 1. Audio (Kokoro am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Then pad BOUT with a 1.0 s silent tail, and write the ffprobe-measured
durations back into `beat_sheet.json` as `actual_duration_s` (keep
`estimated_duration_s` too — `until()`/`finish()` prefer actual).

Whisper-check BIDEA ("Hallo" must not come out as "hedge"). Re-listen for
fused words generally (watch "read-only" and "one-paragraph").

## 2. Pre-render QA (before any 4K frame)

```bash
cd "$REEL"
# Gate A simulation: scratch dir with ONLY scenes.py + the sheet
mkdir -p /tmp/gatea && cp scenes.py beat_sheet.json /tmp/gatea/
cd /tmp/gatea
for C in B00_TheGap B01_ThePlug B02_Permissions B03_MorningBrief B04_InboxTriage B05_MeetingPrep B06_YouSend B07_PullThePlug B08_StrangerInvite; do
  python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class $C
done
# layout audit (needs the reel dir + real Manim)
cd "$REEL"
for C in B00_TheGap B01_ThePlug B02_Permissions B03_MorningBrief B04_InboxTriage B05_MeetingPrep B06_YouSend B07_PullThePlug B08_StrangerInvite; do
  python3 /path/to/brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class $C --curve-strict
done
```

Require 0 warnings / 0 errors from both. (The static check passed clean in
the pre-render build; the layout audit could not run there — no pangocairo.)

## 3. Stills first

Render each scene's last frame at low res (`manim -ql -s`), build a contact
sheet, and eyeball: label placement (the "the gap"/"the plug"/"permissions"
tags, "strangers' invites" beside the invite), the plug seated in the
socket in B01, the B02 permission rows (checks on the read rows, X on the
send row), the B04 split stacks (no overlap), the lock over the SEND pill in
B06, the plug in the tray in B07, the X over the stranger's invite in B08,
and that every beat has a label up by its midpoint.

## 4. Midpoint guard

With measured audio in hand, confirm no animation spans any clip's 45–55%
window. The `until()` phrases were chosen to keep motion early or late (see
SHOTLIST.md timing notes; B04's split uses `lead=0.5`); re-verify, because
estimated and actual durations will differ.

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
- Cables are drawn in deep kraft (`#9C8462`), never ink-edged, so they do
  not fuse with the dark socket under GATE T §8.6b.
- B08's delete is two plays (shift, then FadeOut) — a FadeOut and an
  `.animate` on the same mobject in one play fight in real Manim.

## 7. STOP

Send the master to Bear. Stage (`art post`) and publish only on his explicit
word, and only from TOPOST. Never commit MP3/MP4/WAV or `__pycache__`.
