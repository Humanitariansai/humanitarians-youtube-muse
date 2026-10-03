# CLAUDE-CODE-RENDER.md — rendering "Claude, On the Job." on Bear's Mac

Pre-render package only: this folder contains everything except the final
audio and video. Bear renders locally with Manim + Kokoro TTS (voice
`am_onyx`).

## 0. Get the package onto the Mac

All file activity stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`
per the standing rule. Clone or copy this package's 12 files there, e.g.:

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/
# copy the 12 files of claude-on-the-job/ into a working dir, e.g. reels/claude-on-the-job/
```

Required beside them: the toolkit at `brutalist.art/` (skills + runtime), since
the bookends and the render pipeline live there.

## 1. Sanity checks (fast)

```bash
cd <this package>
python3 make_sheet.py            # regenerates beat_sheet.json; asserts 13 beats, ~176 s total
python3 -m py_compile make_sheet.py scenes.py
```

## 2. Narration audio (Kokoro am_onyx)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
```

- Voice `am_onyx`, persona Liam, Teardown register. BIDEA opens
  "Hallo. This is Liam, in for Bear."
- Whisper-check the first beat every time; also spot-check the words
  "four-tier", "superhuman", "irreducible" (Kokoro fuses/confuses some
  compounds — reword if the transcript is wrong).
- Pad BOUT with a 1.0 s silent tail (`tail_silence_s: 1.0`), then write the
  ffprobe durations back to each beat's `actual_duration_s` in
  `beat_sheet.json`. Re-voice single beats with `--only <BID>`; a full rerun
  re-voices everything and drops BOUT's pad unless re-added.
- Do NOT re-run `make_sheet.py` after this step (it wipes build stamps).

## 3. Stills first, then the review cut

```bash
# last-frame stills at low res for a contact sheet (own --media_dir per parallel render)
manim -ql -s scenes.py <ClassName> --media_dir /tmp/stills-<ClassName>
# then the review cut
./brutalist.art/art run <reel> --height 2160
```

- Every scene's run time must stay within its `actual_duration_s`
  (`finish()` handles this as long as the `play` calls fit); an over-long
  clip gets centre-cut, silently dropping the opening and payoff.
- After editing a scene, move its old `manim/<BID>.mp4` to `_superseded/`
  and clear the stale cache in `<reel>/media/videos` before re-rendering.

## 4. QC gates

- Gate A (from a scratch folder holding ONLY `scenes.py`): with
  `beat_sheet.json` beside it, `until()` pacing runs.
- `runtime/qc/static_scene_check.py scenes.py --class <Class>` — must stay
  0 warnings / 0 errors (it was, at package time).
- `runtime/qc/manim_layout_audit.py scenes.py --class <Class> --curve-strict`
  in the reel folder; `bookend_check.py` and `factcheck_check.py` per Gate F.
- Keep every animation off the clip midpoint (±0.22 s margin); GATE T and
  Gate V sample there.

## 5. Final master

```bash
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```

Check the master: sha, 3840×2160, silent tail present. Then STOP — stage
(`art post`) and publish only on Bear's explicit word, and only from TOPOST.

## Known package-time notes for the renderer

- B01's pages enter with `FadeIn(..., shift=DOWN*1.4)` (fast drops), not
  moves — the static checker requires a new non-text shape per play.
- No acronyms or version numbers in narration (deliberate, to dodge Kokoro
  misreads); "plugin dot json"-style issues do not apply here.
- The `ShowTellCard` family was not used; SHOTLIST.md records the card-test
  outcome per beat (all drawn).
