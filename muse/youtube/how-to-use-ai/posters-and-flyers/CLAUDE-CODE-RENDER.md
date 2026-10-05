# CLAUDE-CODE-RENDER.md — Posters and Flyers

Render instructions for Bear's Mac. Pre-render package: beat sheet, Manim
scenes, narration prompts. Nothing here is staged for publication.

## 1. Narration (Kokoro, voice `am_onyx`)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
```

- Every beat in `beat_sheet.json` carries `narration_text`, `voice:
  "am_onyx"`, `engine: "kokoro"` and `estimated_duration_s`.
- After generating, write the ffprobe-measured durations back to
  `actual_duration_s` on each beat.
- Pad BOUT with a 1.0 s silent tail (the sheet already declares
  `tail_silence_s: 1.0`).
- Spot-check the first beat's whisper transcript (greeting "Hallo" is
  known-clean); whisper-check "Saturday, nine in the morning" and "twelve
  Maple Street" on B02.

## 2. Manim scenes

9 classes in `scenes.py`, one per GRAPHIC body beat:

`B00_Hero`, `B01_Companion`, `B02_Facts`, `B03_ExactWords`, `B04_Layout`,
`B05_Split`, `B06_PrintCheck`, `B07_Label`, `BVDT_Recap`

Class names start with the beat id (`<BID>_<Name>`) — the render stage
finds scenes by that exact text. Render with Manim at 3840×2160 and place
each clip as `manim/<BID>.mp4`. The bookends (BIDEA, BDEFS, BHTF, BOUT) are
REMOTION patterns (`BrutalistHesitantWriter`, `ClaudeDefinitions`,
`ClaudeComposerAsk`, `ClaudeTitleOutro`) — render via
`runtime/scripts/remotion_scenes.py`.

## 3. Layout audit (deferred to this Mac pass)

`manim_layout_audit.py --curve-strict` **cannot run in the build VM** (no
Manim/pangocairo) and was not run for this package. Run it here per class:

```bash
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict
```

Hand-review the frames it flags: B04's left-side labels ("headline",
"details") sit near x = −4.35 and B02's right-aligned chips reach x = 6.0 —
both inside the ±6.2 safe area but worth a visual confirm at 4K.

## 4. Assemble

Compile with `./brutalist.art/art run <reel> --height 2160`, review the
review cut, then `./brutalist.art/art final <reel> --height 2160 --out
<reel>/exports/landscape`. Verify the master: sha, 3840×2160, 1.0 s silent
tail.

## 5. Never

Stage (`art post`) or publish only on Bear's explicit word, and only from
TOPOST. Never commit MP3/MP4/WAV or `__pycache__` to the repo.
