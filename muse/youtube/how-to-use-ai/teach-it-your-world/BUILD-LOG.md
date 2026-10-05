# BUILD-LOG.md — "Teach it your world"

## 2026-10-04 — skill decision (recorded reasoning)

Assigned skill was `cc-explainer`. I switched to `ai-explainer`. Reasons:

1. **cc-explainer is unauthorable here.** Its REAL-SESSION LAW requires an
   actually-run Claude Code session, transcribed to `SESSION.md`, with every
   `CCSession` block traceable to that run; an invented tool result is a
   DOUBLE-CHECK LAW violation. The `claude` CLI is not installed in this VM
   (`which claude` → nothing) and cannot be authenticated — no credentials
   exist in the store for it, and the credential policy forbids collecting
   raw credentials from the user. Installing the CLI would still leave
   sign-in impossible. A terminal-first reconstruction without a real
   session would be fabrication, not a receipt.
2. **The pitch is ai-explainer's lane.** "Upload your docs so AI answers from
   YOUR material — personal knowledge bases, explained non-technically" is a
   concept walkthrough for a smart non-technical audience. ai-explainer is
   the skill for exactly that ("a Claude-branded concept walkthrough"),
   with the same persona (Liam, "in for Bear"), voice (`am_onyx`), register
   (Teardown), and channel constants as the assignment.
3. The task permits switching with recorded reasoning — this is the record.

## 2026-10-04 — build order (all [record])

1. Read the assigned skill, the ai-explainer skill, and three sibling
   packages (`just-talk-to-it` show-tell, `dont-get-fooled` and
   `keep-instructions-and-data-apart` ai-explainer) for the series'
   conventions: 12-file package, `make_sheet.py` → `beat_sheet.json`,
   `scenes.py` with the pasted iso kit, `until()`/`finish()` pacing.
2. Verified facts via web search + one live page open (Anthropic's RAG-for-
   projects help article). Drafted ACTS.md, then `make_sheet.py` with
   assertions (13 beats, spine order, 180–360 s window, B01 ≥ 9 s, every
   `until()` phrase present verbatim in its narration). First run: 13
   beats, 335.6 s.
3. Wrote `scenes.py`: iso kit block pasted verbatim (lines 1–143 of the
   sibling file), new module docstring, local helpers (`bug`, `label`,
   `leader`, `squig`, `solid`, `page_rect`), 7 scene classes B02–B08.
4. QC gate: `py_compile` clean on both scripts; `static_scene_check.py`
   clean for all 7 classes on the first pass — 7 clean · 0 warn · 0 error.
5. Wrote the doc files (FACTCHECK, SOURCES, SHOTLIST, PROMPTS, CHECKS-REPORT,
   CLAUDE-CODE-RENDER, README), pushed all 12 files to
   Humanitariansai/humanitarians-youtube-muse under
   `muse/youtube/how-to-use-ai/teach-it-your-world/`, and verified each with
   a Contents API read (HTTP 200).

## Narration decisions

- B00's composer exchange is illustrative (a drawn generic list), framed by
  "Watch:" — it is not presented as a recorded session. Noted in
  CHECKS-REPORT.md §5 and FACTCHECK.md.
- The librarian metaphor (B04) and meaning-map (B05) are flagged in the
  narration as explanations ("in plain words"), not product claims; the RAG
  definition itself follows Anthropic's help article.
- No model names, plan names, file-type lists, or pricing anywhere (standing
  rules + DOUBLE-CHECK LAW).
- Greeting for B00: "Konnichiwa, Liam" — rotates the world-language hello
  (siblings used Hola, Hallo, Ciao, Hej).

## What I did not do

- No SESSION.md (no real session exists; the film is a concept explainer,
  not a session reconstruction).
- No MP3/MP4/WAV, no `__pycache__`, no secrets in any file.
- Did not touch `muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md`
  (coordinator's).
