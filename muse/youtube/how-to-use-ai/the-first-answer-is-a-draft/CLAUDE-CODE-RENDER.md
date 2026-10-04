# CLAUDE-CODE-RENDER.md — "The first answer is a draft"

Render instructions for Bear's Mac. Pre-render package only: nothing here renders, publishes, uploads, or stages anything. Bear runs every step below in Claude Code on his Mac (Manim + Kokoro TTS, voice `am_onyx`).

## Package contents
`beat_sheet.json` (13 beats, ~150 s estimated) · `scenes.py` (9 Manim scene classes: B00_DraftOne … B08_Recipe; iso kit pasted at top, no imports) · `ACTS.md` · `SHOTLIST.md` · `FACTCHECK.md` · `SOURCES.md` · `BUILD-LOG.md` · `CHECKS-REPORT.md` · `PROMPTS.md` · `make_sheet.py` · this file · `README.md`.

Film identity: persona Liam ("Liam, in for Bear"); voice `am_onyx`; Teardown register; channel `claude-liam`; watermark `@NikBearBrown`.

## Steps (run from the reel folder on the Mac)
1. **Audio.** `python3 <toolkit>/brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>` — Kokoro voice `am_onyx`. Pad BOUT with a 1.0 s silent tail. Write the ffprobe-measured durations back into `beat_sheet.json` as `actual_duration_s` for every beat. (Note: `generate_audio_kokoro.py` re-voices every beat on each run; use `--only <BID>` for re-voices, then re-pad and re-measure BOUT. Whisper-check BIDEA's greeting "Hallo" — it is on the skill's clean list, but check anyway.)
2. **Layout audit (deferred).** `manim_layout_audit.py --curve-strict` could NOT run in the build VM (no Manim/pangocairo there) — run it on the Mac for every class: `python3 runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict`. Static QC already passed clean in the VM (see CHECKS-REPORT.md: 9 clean · 0 warn · 0 error); the audit is the remaining geometry gate.
3. **Stills first.** Render each scene's last frame at low resolution (`manim -ql -s`) and look at a contact sheet before any 4K render. Check: the draft page reads as one object across B00–B07; tags read "DRAFT 1/2/3"; no label touches its leader line; nothing sits on a terracotta fill.
4. **Pre-audit Gate A.** From a scratch folder holding ONLY `scenes.py` (copy nothing else — that is what `art run`'s Gate A sees), with `beat_sheet.json` beside it, run `runtime/qc/static_scene_check.py scenes.py --class <C>` per class.
5. **Render.** `./brutalist.art/art run <reel> --height 2160` (Gates A, B, V and the review cut), look at frames, then `./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape` (GATE T, then the master). Check the master: sha, 3840×2160, silent tail.
6. **STOP.** Send the master to Bear. Stage (`art post`) and publish only on his word, and only from TOPOST. Never publish from this package.

## Known gotchas for this film
- Scenes use `until("…")`/`finish()` pacing against `beat_sheet.json` — keep the sheet beside `scenes.py` whenever rendering.
- Do not re-run `make_sheet.py` after the final: it wipes build stamps (see the skill's trap list).
- B01's stamp: starts at y=2.9 (safe-area clean) and drops 1.0 with `ease_in` — lands fully opaque before the midpoint (GATE T midpoint trap).
- `art run` only renders scenes whose `manim/<BID>.mp4` is missing; after editing a scene, move the old clip to `_superseded/` and re-run. Leave ~0.05 s slack for 4K frame rounding.
