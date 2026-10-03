# BUILD-LOG — claude-basics--claude-quickstarts-50-turn-agent-pays-same

## 2026-08-28 — hai-simple redo, built end to end

**Mode:** redo, per SUBJECT.json (`source_sheet`: `anthropics/youtube/claude-basics/claude-quickstarts-50-turn-agent-pays-same/beat_sheet.json`).
The source reel was an unbuilt claude-basics scaffold (only `beat_sheet.json` + empty `mp3/`/`clips/` dirs existed, no `SCRIPT.md`, all beats SLATE, register Teardown/gap-form). Kept the source's question, facts, and body argument (prompt caching for repeated computer-use screenshots: hash the screenshot, mark `cache_control={"type":"ephemeral"}` on first send, later identical turns hit the cache instead of reprocessing; the 50-turn / 5-state anchor with its 100,000-vs-10,000-token arithmetic). Re-registered narration Teardown → Plain (explain, stop — no verdict language was present in the source narration to begin with).

**What changed from source (per hai-simple SKILL.md):**
- B00 replaced: was a plain GRAPHIC cold-open card restating the token math; now `BrutalistHesitantWriter` — writer types "Why does a 50-turn / agent waste **bandwidth** / resending the same / screenshot?", corrects "bandwidth" → "tokens" on screen (the newcomer's actual wrong guess: framing this as a network/data-transfer problem rather than a token/reprocessing-cost problem). Narration 34 words + `lead_silence_s: 0.8`; measured `media/B00.mp4` = 10.8s (≥8s / ≥9s window). Frame-pulled at 0.2/2/4/6/8/9.5/10.5s: the correction ("bandwidth"→"tokens") is already resolved by t≈6s, well before the beat ends.
- The source had no explicit wrong-guess beat (Teardown gap-form register: cold open → question → setup → mechanism → example → recap). S02/S03 are new content, honestly derived from the source's own mechanism — `cache_control` only matters if repeat sends are otherwise NOT free, so the wrong guess ("the model already saw it, it must be free") and its break (API calls are stateless; every turn resends and reprocesses the full conversation) follow directly from the source's own premise, not fabricated facts.
- S06/S07 (both directions) are new — derived from the source's own `exclusions` field ("full caching protocol, cache eviction policies" out of scope) by stating the plain boundary of the win (exact byte-for-byte repeats only; a moved cursor or genuine navigation is a new state) without touching protocol/eviction internals.
- Carry-out (`WantQuote`) is new phrasing of the source's own `purpose` field.
- Your Turn (`ClaudeComposerAsk`) keeps the source's exact paste-ready prompt verbatim; `folderLabel`/`topic`/`segment` swapped to @HumanitariansAI.
- Outro swapped the source's `ClaudeTitleOutro` → `OutroSeries` + `OutroCTA` (Humanitarians AI skin per `skills/make/hai`), closing narration "…Liam, in for Bear." The source's leftover `BVDT`/`BHTF`/`BOUT` bookend-lane stub beats (empty narration, artifacts of a different scaffold) were dropped rather than carried over, matching the prior `claude-cookbooks-splitting-chunk` redo's precedent.
- Dropped the source's literal `cache_control={"type":"ephemeral"}` code-syntax phrasing from spoken narration (S04) in favor of a speakable paraphrase ("mark it as cached … using the API's ephemeral cache setting"); the exact syntax is preserved on-screen in the FormBCard sub-text and verbatim in the Your Turn prompt.

**Gate L:** `./art scenes --check` confirmed `BrutalistHesitantWriter`, `FormBCard`, `WantQuote`, `ClaudeComposerAsk`, `OutroSeries`, `OutroCTA` all RENDERABLE before slating — no new component needed.

**Build:** `generate_audio_kokoro.py` (12 beats, am_onyx, $0.00) → `remotion_scenes.py` (12/12 rendered, foreground, waited on exit code, ~10m43s) → `compile.py` (4K master forced 3840×2160, 12/12 real, 141.1s).

**GATE T:** PASS, 0 FAILs. §8.10 redundancy advisories on S01–S07 (narration closely recites the FormBCard text) are expected/accepted — FormBCard is a discuss-and-show pattern by design in this series, per prior HAILOOP-LOG entries (same disposition as the `claude-cookbooks-splitting-chunk` redo).

**Gate V:** frame-pulled every 8s across the full 141.1s master + targeted B00 pulls (0.2/2/4/6/8/9.5/10.5s) — all 12 beats legible, correctly inset, no text overlap; B00 correction confirmed visible well before the beat ends; OutroSeries/OutroCTA render cleanly in the humanitarians skin.

**Audio presence:** `ffmpeg -af volumedetect` → mean_volume −23.8 dB, max_volume −2.9 dB (well above the −40 dB floor). Master mtime (04:12:58) newer than `beat_sheet.json` (04:12:10).

**Non-blocking:** compile.py's motion-histogram check flagged `fade` at 7/12 beats (58%, over the ~40% pantry-language cap) — structural to this FormBCard-heavy body-beat design, consistent with the accepted disposition in prior hai-simple redos (e.g. `claude-cookbooks-splitting-chunk-from-document-makes`). Not treated as a defect.

**Result:** `claude-basics--claude-quickstarts-50-turn-agent-pays-same.mp4` — 141.1s, 3840×2160, 12/12 real beats, GATE T PASS, Gate V PASS, audio PASS. Review cut DONE.
