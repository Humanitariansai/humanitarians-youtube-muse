# CLAUDE-CODE-RENDER.md — "Write with AI, Still Sound Like You"

Render instructions for Bear's Mac. Pre-render package only: nothing here renders,
publishes, uploads, or stages anything. Run these steps locally in Claude Code.

Film: `write-with-ai-sound-like-you` · "Write with AI, Still Sound Like You"
Slug dir (write repo): `muse/youtube/how-to-use-ai/write-with-ai-sound-like-you/`
Persona: Liam ("Liam, in for Bear,") · Voice: Kokoro `am_onyx` · Register: Teardown
Channel: `claude-liam` · Watermark: `@NikBearBrown` (in the Remotion bookends)

## 0. Set up the reel folder
Copy the 12 package files into a reel folder, e.g.
`/Users/bear/Documents/CoWork/bear-textbooks/books/write-with-ai-sound-like-you/`
(all file activity stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`).
`beat_sheet.json` must sit beside `scenes.py` — `until()`/`finish()` pacing reads it.

## 1. Narration audio
```
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>   # voice am_onyx
```
- Pad BOUT with a 1.0 s silent tail (the sheet already declares `tail_silence_s: 1.0`).
- Write the measured ffprobe durations back into `beat_sheet.json` as
  `actual_duration_s` per beat.
- Whisper-check BIDEA ("Hallo" is on the clean-greetings list) and any acronyms.
- Do NOT re-run `make_sheet.py` after this step — it wipes the build stamps.

## 2. Layout audit (deferred — could not run in the build VM)
This VM has no Manim/pangocairo, so the layout audit was NOT run during the build.
Run it on your Mac before rendering:
```
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B00_RobotDraft --curve-strict
# … repeat for B01_NoSample B02_MatchMyVoice B03_BanTheGiveaways B04_DictateThenClean B05_YourFinalPass B06_TheEmail
```
The static checker (`static_scene_check.py`) passed 7/7 clean (0 warn, 0 err) in the
build; coordinates were hand-placed inside ±6.3 × ±3.4, type ≥ 32, labels beside
objects with ≥ 0.3 leader gaps. Fix anything the audit flags, move superseded clips
to `_superseded/`, and re-run.

## 3. Stills first
Render each scene's last frame at low resolution (`manim -ql -s`) and look at a
contact sheet before any 4K render. Check: no label inside an outline, no text on
terracotta, the B03 crosses land on the phrases, the B02 page visibly enters the block.

## 4. Render
```
./brutalist.art/art run <reel> --height 2160        # Gates A, B, V + review cut
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape   # GATE T + master
```
- `art run` only renders scenes whose `manim/<BID>.mp4` is missing; after editing a
  scene, move its old clip to `_superseded/` first. Give each scratch render its own
  `--media_dir` (parallel renders collide on the Text cache).
- Scene classes are literal `class BNN_Name(Scene):` — `run.sh` finds them by that text.
- Leave ~0.05 s slack: frame rounding at 4K can push a clip past its audio, and
  `compile.py` centre-cuts scenes that overrun (dropping the opening and the payoff).

## 5. Check the master
sha, 3840×2160, silent tail present. Then send the master to Bear.

## 6. STOP
Stage (`art post`) and publish only on Bear's explicit word, and only from TOPOST.
Never publish this film without his instruction.
