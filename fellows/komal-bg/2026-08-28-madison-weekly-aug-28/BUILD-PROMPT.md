# BUILD-PROMPT — Madison Weekly — Aug 28. (Komal · 4K)

```
Build the claude-liam hybrid weekly "Madison Weekly — Aug 28."
(slug: madison-weekly-aug-28) — creator cut for Komal.

Ground truth:
1. loon-book/youtube/madison-weekly-aug-28/beat_sheet.json
2. PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK.md + SOURCES.md
3. brutalist.art/skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md
4. 9:16 companion: short/beat_sheet.json

Hard stops:
- No house audio until PEDAGOGY.md shows VERDICT: PASS.
- Kokoro am_onyx only on B00–B02, B04, B06–B08.
- B03 and B05 are team clips: own video + own audio. No Kokoro.
- keep_review_labels must stay false — never ship a --review cut as the master.
- Master is 4K: compile with --height 2160. Also render the 9:16 short.

Steps after GATE P PASS:
1. Restore pantry/sai-ground-truth.mp4 as media/B03.mp4 (own audio → mp3/beat-B03.mp3)
2. Restore pantry/swara-weekly-update.mp4 as media/B05.mp4 (own audio → mp3/beat-B05.mp3)
3. python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B00 B01 B02 B04 B06 B07 B08
4. python3 runtime/scripts/remotion_scenes.py <reel>
5. ./art final <reel>        # clean 4K master
6. Visual QC LAW on frames; fix; re-render. Never publish.
```
