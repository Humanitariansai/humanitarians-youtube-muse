# BUILD-LOG.md — Claude, Allowed.

2026-10-03 · subagent build (parent orchestrator, label 7c3313fc-8be2-48a9-b88a-d31d5fab9a)
Source: mirror repo `nikbearbrown/humanitarians-youtube-muse`,
`claude-for-artificial-intelligence/hai-claude-allowed/`
Write repo: `Humanitariansai/humanitarians-youtube-muse` → `muse/youtube/how-to-use-ai/claude-allowed/`

## Decisions

1. **Skill: show-tell** (over cc-explainer, the suggested alternative). The film is a
   concept teardown — scope, trap, habit — not a terminal session, so cc-explainer's
   terminal-first body would be the wrong tool. show-tell's "image every beat, minimal
   text, the voice explains" matches the source's own GATE-P note that all inner beats
   are custom illustrations on the cream stage. The ClaudeComposerAsk Your-Turn bookend
   is the natural home for the source's email-draft handoff.
2. **Reframe, not translation.** Kept the school AI policy as the concrete running
   example (it is where the language is most standardized), but the narration addresses
   adults: schools AND employers named in B00/BIDEA, and BHTF closes with "At work,
   swap in your manager." No content beat is student-only.
3. **10 beats, ~2:50.** Source had 11 beats (~2:11 estimated). Dropped the source's ASK
   cold-open (show-tell has no cold-open) and verdict card (bookend-exempt); kept the
   predict/reveal pair and the handoff. No "why now" number beat — there is no
   fact-checked number this film needs, and show-tell law 9 forbids filler.
4. **BIDEA correction.** Naive "is AI banned everywhere" → "what does the ban actually
   cover". Trigger/replacement words have no trailing punctuation (skill law).
5. **Terms (BDEFS):** policy · disclosure · AI fluency — all ≤17 chars (ClaudeDefinitions
   truncation rule).
6. **Kokoro-safe wording.** Avoided acronyms and version numbers in narration. The phrase
   "except for educational purposes" is quoted speech, kept verbatim as the object of B02.

## Build steps (all in ~/workspace/film-builds/how-to-use-ai/claude-allowed/)

1. Fetched `beat_sheet.json`, `README.md`, `PEDAGOGY.md`, `NARRATION-GATE-P.md` from the
   mirror repo via the GitHub Contents API + surrogate credential flow (read-only; mp3/
   untouched).
2. Wrote `make_sheet.py` → ran → `beat_sheet.json` (10 beats, 6 Manim body beats,
   170.0 s estimated, all asserts green).
3. Wrote `scenes.py` = iso_kit.py (verbatim paste) + 6 scene classes
   (`B00_PolicyPage`, `B01_Scope`, `B02_Trap`, `B03_Fluency`, `B04_Predict`, `B05_Reveal`).
4. QC: `python3 -m py_compile` clean on both files; `static_scene_check.py` for all 6
   classes → 6 clean, 0 warnings, 0 errors, first run. See CHECKS-REPORT.md.
5. Wrote the 9 doc files; pushed all 12 to GitHub; verified each via Contents API (200).

## Notes for the render step (Bear's side)

- `until()` pacing reads `beat_sheet.json` next to `scenes.py`; keep them together.
- BOUT carries `tail_silence_s: 1.0`; re-pad if audio is regenerated with `--only`.
- Real-render watch items (pre-render cannot verify): GATE T midpoint frames for the
  B00 highlighter band and B02 connector lines; EB Garamond availability on the Mac.
