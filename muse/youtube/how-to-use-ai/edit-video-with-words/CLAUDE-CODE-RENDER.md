# CLAUDE-CODE-RENDER.md — Edit video with words

Render prompt for Bear's Mac. Paste into Claude Code in
`/Users/bear/Documents/CoWork/bear-textbooks/books/humanitarians-youtube-muse/`.

## 0. Fetch the package

The 12-file package is at
`muse/youtube/how-to-use-ai/edit-video-with-words/` in the
`Humanitariansai/humanitarians-youtube-muse` repo. Copy it to a reel
folder, e.g. `reels/edit-video-with-words/`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `mp3/beat-BIDEA.mp3`,
`mp3/beat-BDEFS.mp3`, `mp3/beat-B00.mp3` … `mp3/beat-B09.mp3`,
`mp3/beat-BHTF.mp3`, `mp3/beat-BOUT.mp3` (14 files). Persona: "Liam, in
for Bear"; register: Teardown. Greeting note: BIDEA opens "Hallo."
(Kokoro says it cleanly — do not substitute "Hej").

Kokoro-safety notes, verified at build time:
- "twenty twenty-seven" is written out in B06/B09 narration — keep the
  words, do not substitute "2027" (Kokoro reads bare "2027" fine, but the
  written form is the checked one).
- Whisper-check the BHTF prompt read-back (longest beat, 20.78 s).
- BOUT gets a 1.0 s silent tail; write the final 4.11 s back to
  `actual_duration_s` (already set in this sheet).

## 2. Manim scenes

`scenes.py` holds 10 scene classes (`B00_HeroChat` … `B09_Today`),
1920×1080, Claude palette. Render per class:

```
manim -qh scenes.py B00_HeroChat B01_TenHours B02_Announced B03_Demo B04_Fiddly \
  B05_YourHands B06_Early2027 B07_MetaShips B08_TheLine B09_Today
```

Copy each render to `manim/<BID>.mp4` (B00.mp4 … B09.mp4).

Mac-only checks the VM could not run:
- `manim_layout_audit.py --curve-strict` per class (no pangocairo in the
  build VM) — fix any layout warnings before the review cut.

## 3. Remotion bookends

Render the 4 bookend beats in the brutalist.art Remotion project:
`BrutalistHesitantWriter` (BIDEA), `ClaudeDefinitions` (BDEFS),
`ClaudeComposerAsk` (BHTF), `ClaudeTitleOutro` (BOUT). Props are in
`beat_sheet.json`. Then assemble per the project's standard pipeline.

## 4. Assemble

`compile.py --review` for the review cut (bookends real, timecode
burned), then the final master. Check the master: 3840×2160, runtime
equals the sum of the audio (177.2 s incl. the 1.0 s outro tail), silent
tail present. `python3 brutalist.art/runtime/scripts/bookend_check.py
<reel>` — expect PASS (show-tell spine, cold-open + verdict exempt).

## 5. Before publish

Re-verify the launch status: YouTube's conversational editing was a
preview with a *reported* early-2027 window at build time (2026-10-07).
If it has launched, gone quiet, or slipped, re-cut B06/B09 rather than
shipping a stale window.

Never publish without Bear's explicit instruction.
