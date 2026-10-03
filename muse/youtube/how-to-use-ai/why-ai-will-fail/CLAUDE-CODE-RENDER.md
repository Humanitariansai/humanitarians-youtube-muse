# CLAUDE-CODE-RENDER.md — "AI will fail." (why-ai-will-fail)

Instructions for Bear to render the film locally on his Mac
(Manim + Kokoro TTS, voice `am_onyx`). Pre-render package only: this repo
folder holds everything except the final MP3/MP4 — nothing here is
rendered, published, or staged for publication.

## 0. Get the package

The 12 files live at
`muse/youtube/how-to-use-ai/why-ai-will-fail/` in the
`Humanitariansai/humanitarians-youtube-muse` repo. On Bear's Mac, all file
activity stays inside `/Users/bear/Documents/CoWork/bear-textbooks/books/`
(standing rule). Suggested local path:

```
/Users/bear/Documents/CoWork/bear-textbooks/books/humanitarians-youtube-muse/muse/youtube/how-to-use-ai/why-ai-will-fail/
```

## 1. Regenerate the beat sheet (sanity)

```bash
cd <film-dir>
python3 make_sheet.py
```

Asserts 14 beats, per-beat durations in band, total 240–420 s, and that
every beat's scene class exists in `scenes.py`. It rewrites
`beat_sheet.json` deterministically.

## 2. Narration audio (Kokoro, free, local)

Generate one MP3 per beat with Kokoro voice `am_onyx`, using the exact
`narration_text` strings from `beat_sheet.json` (also listed in
PROMPTS.md). Suggested: the brutalist.art `generate_audio_kokoro.py`
pipeline, or any local Kokoro runner:

```bash
# example shape — adapt to your local Kokoro setup
python3 <toolkit>/runtime/scripts/generate_audio_kokoro.py <film-dir>  # voice am_onyx
```

- Name files `mp3/B00.mp3` … `mp3/B13.mp3`. **Never commit MP3s.**
- The measured MP3 durations are the master clock. If a beat's audio
  differs from `estimated_duration_s`, conform the visuals to the audio,
  not the reverse.

## 3. Render the Manim scenes

```bash
cd <film-dir>
for c in SceneColdOpen SceneOverview SceneTheList SceneBlockbuster \
         SceneEllisonValenti ScenePenicillin SceneInsiderTrap SceneToyCurve \
         SceneFamiliarForm SceneHonestPart SceneAsymmetricBet SceneVerdict \
         SceneYourTurn SceneOutro; do
  manim -qm --format=mp4 scenes.py $c
done
```

- `-qm` = 720p draft; use `-qk` for the 1080p/4K final. 16:9 is the
  default config; scenes set the cream background themselves.
- Scene classes map 1:1 to beats B00–B13 in order.
- Static QC already passed render-free
  (`static_scene_check.py`, 14/14 clean, 0 warnings, 0 errors); still do a
  real frame check on first render — sample frames at ~2 fps and eyeball
  text fit, title-safe margins, and the terracotta accent (one per beat).

## 4. Assemble

Conform each scene's MP4 to its beat's measured MP3 (trim/pad, never
stretch audio), concatenate B00→B13, mux, add captions. The repo's usual
`compile.py` conform pipeline applies.

## 5. Do NOT

- Do not publish or upload anything from this package without Bear's
  explicit instruction (standing rule).
- Do not commit MP3/MP4/WAV, `__pycache__`, `.pyc`, or `.DS_Store`.
- Do not "fix" the Watson "five computers" quote back in as fact — it is
  apocryphal (see FACTCHECK.md C1).

## Troubleshooting

- `make_sheet.py` assertion failure → the beat table was edited; keep
  14 beats and the 240–420 s band, or update the band deliberately.
- Manim `Text` overflow on a card → shorten the line or drop `font_size`;
  all card lines were authored ≤ 46 chars, inside the 16:9 safe area.
- If Kokoro isn't installed locally: `pip install kokoro` (or the
  toolkit's `./setup`); voice `am_onyx`, default rate.
