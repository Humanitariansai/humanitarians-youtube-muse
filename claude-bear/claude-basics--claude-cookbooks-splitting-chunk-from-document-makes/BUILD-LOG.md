# BUILD-LOG — claude-basics--claude-cookbooks-splitting-chunk-from-document-makes

## 2026-08-28 — hai-simple redo, built end to end

**Mode:** redo, per SUBJECT.json (`source_sheet`: `anthropics/youtube/claude-basics/claude-cookbooks-splitting-chunk-from-document-makes/beat_sheet.json`).
The source reel was an unbuilt claude-basics scaffold (only `beat_sheet.json` + empty `mp3/`/`clips/` dirs existed, no `SCRIPT.md`, all beats SLATE). Kept the source's question, facts, and body argument (chunk-context RAG fix: prepend a document-level summary before embedding; medical-paper "mortality" chunk example; precision 33% → 90% across ten test queries). Re-registered narration Teardown → Plain (explain, stop — no verdict language was actually present in the source narration, so this was mostly a register carry-over, not a rewrite).

**What changed from source (per hai-simple SKILL.md):**
- B00 replaced: was a plain GRAPHIC cold-open card; now `BrutalistHesitantWriter` — writer types "Why does **shrinking** a chunk / make it retrieve / for the wrong question?", corrects "shrinking" → "splitting" on screen (the newcomer's actual wrong guess: blaming chunk *size* rather than chunk *isolation from its document*). Narration 33 words + `lead_silence_s: 0.8`; verified `media/B00.mp4` = 9.92s (≥8s) and the correction is visible on screen by t≈4s, well before the 9.9s end (frame-pulled at 0.2/2/4/6/8/9.5s to confirm).
- Body compressed onto the hai-simple spine (stakes → wrong guess → break it → mechanism → anchor payoff → both directions ×2 → carry-out) as 7 GRAPHIC (`FormBCard`) beats, S01–S07, each ≤40 words / one idea.
- BOTH-DIRECTIONS beats (S06, S07) are new content not in the source — honestly derived from the source's own `exclusions` field (chunking strategy, embedding-model comparisons, full-pipeline benchmarking are out of scope), not fabricated.
- Carry-out (`WantQuote`) is new: "A chunk answers the question inside it. Prepending its document's context is what lets it also answer the right question."
- Your Turn (`ClaudeComposerAsk`) keeps the source's exact paste-ready prompt verbatim; `folderLabel`/`topic` swapped to @HumanitariansAI.
- Outro swapped `ClaudeTitleOutro` → `OutroSeries` + `OutroCTA` (Humanitarians AI skin per `skills/make/hai`), closing narration "…Liam, in for Bear."

**Gate L:** `./art scenes --check` confirmed `BrutalistHesitantWriter`, `FormBCard`, `WantQuote`, `ClaudeComposerAsk`, `OutroSeries`, `OutroCTA` all RENDERABLE before slating — no new component needed.

**Build:** `generate_audio_kokoro.py` (12 beats, am_onyx, $0.00) → `remotion_scenes.py` (12/12 rendered, foreground, waited on exit code) → `compile.py` (4K master forced, 12/12 real, 123.6s).

**GATE T caught one real defect:** `OutroSeries`'s eyebrow line (`fontSize: height * 0.026`) rendered a 39px cap-height text run against a 41px (1.9% of 2160) floor — a genuine sub-floor bug in the shared component, not specific to this reel's content (the ratio is fixed, not a prop). Fixed at the root: bumped the ratio to `height * 0.034` in `runtime/remotion/src/scenes/OutroSeries.tsx` (affects future renders of this shared component only; already-shipped mp4s are untouched). Re-rendered BOUT, recompiled, GATE T → PASS, 0 FAILs. (§8.10 redundancy advisories on S01–S07 are expected/accepted — FormBCard is a discuss-and-show pattern by design in this series, per prior HAILOOP-LOG entries.)

**Gate V:** frame-pulled every ~6s across the full 123.6s master + targeted B00 pulls — all 12 beats legible, correctly inset, no text overlap, correction visible in B00.

**Audio presence:** `ffmpeg -af volumedetect` → mean_volume −23.9 dB, max_volume −3.0 dB (well above the −40 dB floor). Master mtime newer than `beat_sheet.json`.

**Result:** `claude-basics--claude-cookbooks-splitting-chunk-from-document-makes.mp4` — 123.6s, 3840×2160, 12/12 real beats, GATE T PASS, Gate V PASS, audio PASS. Review cut DONE.
