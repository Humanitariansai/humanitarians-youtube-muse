# BUILD-LOG.md — How to Use Claude

## 2026-10-03 — pre-render package build (subagent)

### What I did
1. Fetched the source beat sheet + README from the mirror repo
   (`nikbearbrown/humanitarians-youtube-muse`,
   `claude/claude-youtube/claude-liam-how-to-use-claude/`) via the GitHub
   Contents API with the surrogate credential flow. Ignored `mp3/` (policy).
2. Chose the **show-tell** skill over lecture: the film is a visual explainer
   for non-experts — one image per beat, minimal text, the voice explains.
   Read `skills/make/show-tell/SKILL.md`, the iso kit, and
   `reference/example-make_sheet.py`; followed them.
3. Rewrote the film from zero for the channel audience (smart, pragmatic,
   may never have used an AI chat tool). Kept the source's argument
   (context > prompt templates; Projects as the fix; artifacts / analysis /
   rewriting as the three strengths; your-turn prompt) and dropped the
   "why it matters" tangent beat and the cold-open/verdict cards per
   show-tell bookends. Split the old B04 (three strengths + failure modes,
   25 s) into B05/B06/B07 (one strength each) + B08 (the check-it warning),
   per law 9 (no beat past ~15 s should carry two ideas).
4. Fact-checked into FACTCHECK.md (web search 2026-10-03): Projects custom
   instructions + knowledge base (Anthropic support), Artifacts side panel
   (2026 guides), Eiffel Tower 330 m example, hallucination warning. No
   plan/price claims made, so nothing about the 2026 plan lineup can go stale.
5. Wrote `make_sheet.py` (asserts: 13 beats, beat-id order, 180–220 s total,
   manim class per body beat, hesitant-writer trigger mechanics, BDEFS term
   length ≤ 17, BHTF composer contract, BOUT outro contract). Ran it:
   **13 beats, 196.4 s (~3:16)**.
6. Wrote `scenes.py`: iso kit pasted verbatim + film helpers
   (`chat_window`, `doc_card`, `tag`) + 9 scene classes
   (`B00_ChatWindow` … `B08_CheckIt`), all `until()`/`finish()` paced.
   Phrases for `until()` verified verbatim against the narration.
7. QC: `py_compile` clean on both files; `static_scene_check.py` run from a
   scratch folder holding ONLY `scenes.py` (Gate A simulation) for all 9
   classes — **0 warnings, 0 errors**. Also ran once with `beat_sheet.json`
   beside it to confirm `until()` pacing executes cleanly.
8. Wrote the 10 doc files; pushed all 12 package files to
   `Humanitariansai/humanitarians-youtube-muse` under
   `muse/youtube/how-to-use-ai/how-to-use-claude/`; verified each with a
   Contents API read (HTTP 200).

### Failures and fixes
- First `beat()` draft for B03 used the window's composer pill under the
  reply card (overlap). Fixed by adding `composer=False` to `chat_window()`.
- B04's three card captions ("style", "rules", "example") plus the "project"
  tag = 4 one-word labels in one beat, slightly over the 2–3 guidance.
  Kept: each is one word, the voice names them anyway, and the captions are
  what make three identical cards distinct. Noted in SHOTLIST.md.
- B07's natural trigger phrase ("first pass") lands inside the clip's 45–55%
  GATE T sampling window; switched the final-page trigger to "and you spend
  your time" (post-midpoint). Noted in SHOTLIST.md timing notes.
- `manim_layout_audit.py --curve-strict` could not be run here (no Manim /
  pangocairo in this VM). Labels were placed by hand with ≥0.3 leader gaps,
  no curves cross any label, all coords inside ±6.2 × ±3.3, type ≥ 32.
  **Must be run on Bear's Mac before the 4K render** (see CLAUDE-CODE-RENDER.md).
- No midpoint render-guard verification possible without measured audio;
  event phrases were placed to keep motion off the midpoint (see SHOTLIST.md),
  but the guard pass must be re-done after Kokoro audio is measured.

### What I did NOT do
- No audio generated, no MP4 rendered, nothing staged or published.
  Pre-render package only, per the film brief.
- `muse/FRICTIONAL.md` not touched (concurrent-edit policy); the seven-field
  entry is returned in the final report instead.
