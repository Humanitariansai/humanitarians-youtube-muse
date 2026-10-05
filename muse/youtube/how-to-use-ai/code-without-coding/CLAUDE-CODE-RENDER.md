# CLAUDE-CODE-RENDER — Code without coding

Render instructions for Bear's Mac. This package is pre-render: script, sheet,
drawings, and docs only. Nothing here renders, publishes, or uploads anything.

## 0. Get the package

Clone/pull `Humanitariansai/humanitarians-youtube-muse` and work in
`muse/youtube/how-to-use-ai/code-without-coding/`.

## 1. Narration (Kokoro `am_onyx`)

From the toolkit root (`brutalist.art`), following the show-tell skill:

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
```

- Voice is `am_onyx`, persona Liam ("Liam, in for Bear"). BIDEA opens
  "Hallo. This is Liam, in for Bear." — "Hallo" is on the skill's clean list.
- The narration spells out "twenty twenty-five" and "ninety-five percent"
  (Kokoro misreads digits/version numbers); no acronyms or version numbers
  are spoken; "AI" is on the skill's clean list.
- After generating, pad BOUT with a 1.0 s silent tail, then write the measured
  ffprobe durations back into `beat_sheet.json` as `actual_duration_s`
  (the sheet currently carries `estimated_duration_s` from the house
  `words/2.5` convention, which runs ~1.6× long vs real Kokoro — the measured
  audio is the master clock).
- If any narration line changes afterwards, re-voice that beat with
  `--only <BID>` (a full re-run re-voices everything and silently drops BOUT's
  pad — re-pad BOUT after any full run).

## 2. Layout audit (deferred — could not run in the build VM)

This VM has no Manim/pangocairo, so the GATE T layout audit was NOT run here:

```bash
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
```

Run it for every scene class in the reel folder before the 4K render. The
static checker (`static_scene_check.py`) already passed 9/9 clean in the VM;
the audit is the remaining gate. Watch B08's ink curve + terracotta end dot
and B04's falling pages at their midpoints.

## 3. Stills first, then render

Per the skill workflow: render each scene's last frame at low resolution
(`manim -ql -s`) into a scratchpad and eyeball a contact sheet before any 4K
render. Then:

```bash
./brutalist.art/art run <reel> --height 2160     # Gates A, B, V + review cut
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```

- `manim_layout_audit.py --curve-strict` cannot run in the build VM
  (no Manim/pangocairo); it is deferred to this render pass.
- The scenes pace themselves with `until()`/`finish()` against the beat
  sheet's durations; keep every scene's run time within its
  `actual_duration_s` (`finish()` handles this as long as the `play` calls
  fit) and ffprobe each `manim/<BID>.mp4` against its audio before the final —
  a clip longer than its audio gets centre-cut.
- Do NOT re-run `make_sheet.py` after the final (it wipes build stamps).

## 4. Review + publish

Watch the master, check the 1.0 s silent tail, then send it to Bear. Stage
(`art post`) and publish only on his explicit word. Never publish from this
package alone.
