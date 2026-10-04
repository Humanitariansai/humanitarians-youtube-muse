# SOURCES.md — "Ask for the Shape You Want Back"

## Refactor source (read-only mirror repo)

- `nikbearbrown/humanitarians-youtube-muse`, folder
  `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-05-formatting-output/`
  (fetched via GitHub Contents API, 2026-10-03).
- Files read: `README.md` (topic: "Output Formatting: The Prefill Technique and When
  to Control Format"; source: Anthropic Prompt Engineering Interactive Tutorial,
  Lesson 05: Formatting Output), `description.txt` (the argument: "Output format is
  not cosmetic… The prefill technique locks it… Match format to consumer"), `STATUS.md`,
  `ToDo.md`, `BUILD-LOG.md`, `todo.json`, `beat_sheet.json`.
- **Anomaly [record]:** that folder's `beat_sheet.json` (metadata title "Output
  Formatting…", 10 beats) carries narrations about grounding/hallucinations — the
  content of a different lesson, likely pasted in by mistake. The topic, README, and
  description.txt all describe formatting output, so this refactor rebuilds from the
  intended argument (description.txt) and treats the mismatched narrations as unusable.
  Ignored `mp3/`; no audio downloaded.

## Primary source for the prefill claim

- Anthropic documentation, "Prefill Claude's response for greater output control"
  (https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response
  — also mirrored at platform.claude.com/docs/en/…). Read via search-result mirrors of
  the same page (fetched 2026-10-03; several GitHub mirrors of the docs page confirm
  identical wording). Key documented points used: prefill = include the desired initial
  text in the Assistant message; Claude continues from where it left off; directs
  actions, skips preambles, enforces formats like JSON/XML; API technique.

## Everything else

- The how-to moves (ask for a table, set a word limit, pick a tone, don't over-ask)
  are standard prompting practice and presented as instructions the viewer can verify
  in one try — no external source needed, marked EXEMPT in FACTCHECK.md.
