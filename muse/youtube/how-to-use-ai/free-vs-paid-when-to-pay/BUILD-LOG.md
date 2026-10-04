# BUILD-LOG.md — Free vs paid: when to pay.

Dated build steps, including failures, fixes, and judgment calls.

## 2026-10-03 — build

- **Skill switch: cc-explainer → ai-explainer.** The assignment suggested
  cc-explainer, but this film is a general-audience concept explainer about
  AI pricing tiers — there is no Claude Code terminal session to show, and
  cc-explainer's TERMINAL-FIRST and REAL-SESSION laws would force an
  invented session (a DOUBLE-CHECK violation). ai-explainer (vox-style,
  concept-illustrated middle, Manim fragments) is the right chassis and
  matches the sibling how-to-ai films' Manim-only pre-render packages.
  [judgment]
- Read the ai-explainer SKILL.md, the prior film's beat_sheet.json
  (ai-is-a-slot-machine), scenes.py conventions, CHECKS-REPORT.md, and the
  doc templates (PROMPTS, README, ACTS, FACTCHECK, SHOTLIST,
  CLAUDE-CODE-RENDER). [record]
- Researched the factual spine with two web searches (paid-tier benefits,
  free-tier limit shapes, 2026-10-03). Confirmed the four-item menu
  (stronger model, higher limits, longer context, early features) and that
  prices/tiers churn fast — hence the no-prices design decision. [record]
- Wrote make_sheet.py (14 beats, 9 body, 359 s) with contract assertions
  (13–22 beats, 6–12 body, 180–360 s, BIDEA names the voice, BVDT covers
  the full framework, BHTF carries the prompt, MANIM shot classes match
  scene ids). Fixed one authoring bug before first run: the class-matching
  assertion compared against the wrong string (`"MM01"`); corrected to a
  startswith check. [record]
- Regenerated beat_sheet.json twice as narration lines were tuned for the
  read-aloud convention (BIDEA/B03/B05/B07 lines now speak every on-screen
  word; B07 rewritten to match the flowchart's yes/no branches; B07 dur
  27→28 s). Final: 14 beats, 9 body, 359 s. [record]
- Wrote scenes.py (M01–M14). Read the QC stub source first to author to
  its actual rules (distinct shape-states, frame bounds, text exclusion).
  [record]
- QC gate: `python3 -m py_compile` clean on both files. Static checker:
  13/14 clean on the first run; M05_FourThings raised TypeError —
  `P(1.75, 0.75, 0)` passed 3 args to the 2-arg `P()` helper. Fixed to
  `p + np.array([1.75, 0.75, 0])`. Re-ran all 14: **14 clean · 0 warnings
  · 0 errors**. No warnings or errors hidden or waived. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no
  Manim/pangocairo installed) — deferred to Bear's Mac render pass, noted
  in CLAUDE-CODE-RENDER.md. [record]
- Wrote the 9 docs (ACTS, SHOTLIST, FACTCHECK, SOURCES, BUILD-LOG,
  CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README). [record]
- Pushed all 12 files via gh-put-file.py to
  `muse/youtube/how-to-use-ai/free-vs-paid-when-to-pay/` and verified each
  with a Contents API read (HTTP 200). [record]
