# BUILD-LOG.md — Make It Interview You First

## 2026-10-03 — pre-render package build (subagent)

### What I did
1. Read the show-tell skill (`skills/make/show-tell/SKILL.md`), the iso kit,
   `reference/example-make_sheet.py`, and the finished how-to-use-claude
   package (12-file layout, bookend contracts, QC format). Kept the
   **show-tell** skill as assigned: the film is a visual explainer for
   non-experts — one image per beat, minimal text, the voice explains.
2. Designed the film from scratch (no mirror source): 8 body beats —
   the one-line ask (B00), the interview move (B01), the five questions
   (B02), the brief built from answers (B03), the tailored payoff vs the
   thin generic page (B04), a difficult-email second demo (B05), the
   "ask for answer-changing questions" sharpening (B06), and the rule of
   thumb + skip-for-plain-facts (B07) — plus the three mandated bookends
   and the spoken outro.
3. Fact-checked into FACTCHECK.md: advice film, no statistics cited
   deliberately; all substantive claims EXEMPT (craft guidance, original
   worked example) or PASS (reproducible Claude behavior, "Hallo" clean per
   skill notes). No plan/price claims, so nothing can go stale.
4. Wrote `make_sheet.py` (asserts: 12 beats, beat-id order, 170–220 s total,
   manim class per body beat, hesitant-writer trigger mechanics, BDEFS term
   length ≤ 17, BHTF composer contract incl. prompt-read-in-full, BOUT outro
   contract). Ran it: **12 beats, 194.8 s (~3:14)**.
5. Wrote `scenes.py`: iso kit pasted verbatim + film helpers
   (`composer_at`, `typed_in`, `page`, `qbubble`, `qcard`, `chip`,
   `envelope`, `shadow`, `label`, `leader`) + 8 scene classes
   (`B00_AskOnce` … `B07_TheRule`), all `until(self, …)`/`finish(self)`
   paced. Phrases for `until()` verified verbatim against the narration
   by script.
6. QC: `py_compile` clean on both files; `static_scene_check.py` run from
   `/tmp/gatea/` holding ONLY `scenes.py` (Gate A simulation) for all 8
   classes — **0 warnings, 0 errors**. Also ran once with `beat_sheet.json`
   beside it to confirm the `until()`/`finish()` pacing path executes.
7. Wrote the 10 doc files; pushing all 12 package files to
   `Humanitariansai/humanitarians-youtube-muse` under
   `muse/youtube/how-to-use-ai/make-it-interview-you-first/`; verifying
   each with a Contents API read (HTTP 200).

### Failures and fixes
- First draft of the film-helpers header used a decorative `""""""`
  docstring containing an em dash; Python rejected the file at
  `py_compile`. Replaced with plain `#` comments.
- First draft called `self.until(...)` / `self.finish()` — the kit defines
  them as module-level functions (`until(self, "phrase")`), so the stub
  raised `AttributeError: ... has no attribute 'until'` for all 8 classes.
  Fixed with sed to `until(self, …)` / `finish(self)`; matches the
  how-to-use-claude reference pattern. Caught before any push.
- B04's continuity chips reused `chip()` text at size 30 scaled to 0.6 —
  sub-floor text (GATE T risk). Replaced with plain ink-outlined pills
  (no text) for the small brief box.
- `manim_layout_audit.py --curve-strict` could not be run here (no Manim /
  pangocairo in this VM). Labels were placed by hand with ≥0.3 leader gaps,
  no curves cross any label, all coords inside ±6.2 × ±3.3, type ≥ 32.
  **Must be run on Bear's Mac before the 4K render** (see CLAUDE-CODE-RENDER.md).
- No midpoint render-guard verification possible without measured audio;
  event phrases were placed to keep motion off the midpoint (see SHOTLIST.md;
  B03's later chips flagged for re-check), but the guard pass must be
  re-done after Kokoro audio is measured.

### What I did NOT do
- No audio generated, no MP4 rendered, nothing staged or published.
  Pre-render package only, per the film brief.
- `muse/FRICTIONAL.md` not touched (concurrent-edit policy); the seven-field
  entry is returned in the final report instead.
- `muse/README.md` and `muse/QUEUE.md` not touched (explicitly excluded).
