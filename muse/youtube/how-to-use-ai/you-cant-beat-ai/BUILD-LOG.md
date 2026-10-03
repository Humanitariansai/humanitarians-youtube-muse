# BUILD-LOG.md — "You can't beat AI."

## 2026-10-03 — pre-render package build

**Skill chosen:** ai-explainer. The film is one tight insight ("outsource
the work, never the understanding") with the full bookend spine; the
source README itself recommends ai-explainer for one tight insight. The
Kore/af_kore persona and remotion-card shots were translated to Liam /
Manim per the redo rules. [judgment]

**Source read:** fetched `beat_sheet.json` (12 beats), `README.md`,
`PEDAGOGY.md` from the mirror repo via the Contents API. Reused: the
five-step method verbatim, the GPS analogy, the chief-of-staff scenario
(now explicitly labeled illustrative), the "two extra minutes of thinking"
cost framing. Dropped: the Kore meta-ask framing (B00 ASK), remotion
cards. [record]

**Decisions:**
- Step two of the five-step method ("draft first yourself") is the
  narrative and visual hinge — the single terracotta accent of S07.
- "prompt" is the only technical term the script uses; it is defined in
  plain language inside B07 ("the instructions you type"). [judgment]
- B07 ("the tell is the draft") added as the falsifiability beat the
  source lacked: a concrete test — no draft, no constraints = outsourcing
  understanding. [judgment]
- The verdict (B09) returns to the opening chat window with a "YOURS"
  seal — the payoff visibly resolves the cold open. [judgment]
- Runtime: 12 beats, 295 s (4.9 min), 638 words, 12 Manim scenes.

**Failures and fixes:**
- make_sheet.py assertion failure #1: overview word count 48 > 45 cap.
  Trimmed the B01 line to 41 words (cut "The whole rule in one breath"
  throat-clearing); line meaning unchanged. [record]
- make_sheet.py assertion failure #2: five beats' durations under the
  ~150 wpm speech floor (B00/B02/B03/B05/B07/B09/B10). Raised durations
  instead of cutting narration; total 295 s. [record]
- Static QC: 11/12 clean on first run; S12_Outro failed the distinctness
  check (text-only outro: 1 shape-state across 4 frames). Fixed by adding
  evolving non-text shapes (spark star + terracotta underline that grows).
  Re-ran: 12/12 clean, 0 warnings, 0 errors. [record]
- S09 tick positions: replaced an inline `__import__("math")` hack with a
  module-level `import math`. [record]

**Not done (by design):** no MP3/MP4 rendered; no audio durations measured
(the beat_sheet durations are speech estimates, not measured Kokoro
audio); no publish. Bear renders locally per CLAUDE-CODE-RENDER.md.
