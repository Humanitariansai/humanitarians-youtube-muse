# CLAUDE.md — nik-bear-brown/ (Professor Bear's example folder)

This folder is the instructor's public example work for INFO 7375 Branding and AI, Fall 2026. It keeps the same process record students keep. **Every substantive change here is logged in `FRICTIONAL.md`, and every push adds a line to it.** The repo-root `AGENTS.md` still governs everything else.

## Rule 0 — this folder is NOT the master

The job-search tool here is live-coded in three classes at once, and the canonical copy is in **`info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/`**. Read [`SYNC.md`](SYNC.md) first.

- `collect.py`, `sources.json`, `keywords.json`, `ATS.md`, `facts/professor-bear-cv.json`, `figma/`, and `greenhouse-watch-demo/` are **copies**. Edit them in the master and run its `./lectern/sync.sh`.
- `FRICTIONAL.md`, `README.md`, `CLAUDE.md`, the `assignment-*/` folders, and the dated run outputs belong to this class alone and are never copied in either direction.
- If a shared file was edited here anyway, do not copy it back blindly — follow the recovery steps in `SYNC.md`, and log the drift.

## Rule 1 — log every substantive change in FRICTIONAL.md

Before you report a task in this folder as done, update `FRICTIONAL.md` in the same change set.

**Substantive** means anything a reader of the log would need in order to understand the work:
- a new or deleted file or folder;
- a change to what a result says (a new token set, a changed specimen, a different design direction);
- a decision, a reversal, or something that went wrong.

**Not substantive:** typo, wording, or formatting fixes that don't change meaning. Leave those out rather than padding the log.

**How to log it:**
- **Same day, same work:** extend that day's entry. Don't start a second entry for the same session.
- **New day or new piece of work:** add a new entry under `## Entries`, newest last, headed `### YYYY-MM-DD — <what it was>`, using the course's seven fields, verbatim and in order:
  - Date and what I was working on
  - I tried / expected
  - What happened
  - What I did
  - What Claude or another person contributed
  - What I understand now / still do not understand
  - Evidence and next step
- **Write what happened, not what was hoped.** Include what failed. Name the files that serve as evidence. Never invent a prediction, a result, an approval, or an understanding Professor Bear didn't state.
- **Credit honestly.** Say what Claude Code did and what Professor Bear decided. If he hasn't reviewed something, say so.
- Keep the executive summary at the top current.

## Rule 2 — everything Professor Bear says about this work goes in the log

His words, the same day, as he said them — questions, decisions, corrections, and changes of mind. Quote rather than paraphrase where the wording matters. A request that was later dropped still gets logged, with the reason it was dropped.

## Rule 3 — one line per GitHub push

Every push that touches this folder adds a row to the `## GitHub pushes` table, **in the same commit being pushed**:

```
| YYYY-MM-DD | <commit subject, exactly as committed> |
```

- The note is the commit subject, copied exactly. The repo uses conventional subjects (`feat(fall-2026): …`, `docs(fall-2026): …`).
- No commit ID in the row: a commit can't contain its own ID, and `git log` holds it.

## Rule 4 — executive summary first

Every Markdown file here opens with what it is, why to read it, and what it found, before any table or technical detail. That is the repo-wide rule in `AGENTS.md`; it applies to the brief, the rationale, and this folder's READMEs.

## Rule 5 — every value is labeled, and every JSON file is readable

- **Labels.** Every value in this folder is **record** (from a saved file or the CV facts), **judgment** (someone read the records and decided), or **your input** (only Professor Bear can supply it). Anything not built yet is a typed `[TODO: …]`. Never present a judgment as a record.
- **Readable JSON.** Students must be able to open any file on GitHub and check it, so **every JSON file here is indented** (2 spaces, UTF-8 kept as written, one trailing newline), never minified. Reformat downloads and API responses before committing: parse, write back indented, confirm the parsed data is identical. Only whitespace changes, never the data. Where a file is evidence of what a server sent, its README says it was indented for reading and the data is unchanged.
- **Saved boards and run output are evidence.** Files under `figma/`, `greenhouse-watch-demo/snapshots/`, `runs/`, and `whole-board/` are what the server returned and what the tool wrote. Never hand-edit them; re-run instead, and keep both dates.
- **The facts file is attested.** `facts/professor-bear-cv.json` carries `attested: true` with the date Professor Bear checked it. Any change to it needs his word and a new date, and it is logged.

## Pushing from this folder

- **Approval (given by Professor Bear, 2026-09-26, during a live class demo):** *"When you have something to push to the branding and AI folder, push it."* Push substantive work to `main` without asking again, once the log is updated and the validator passes. This covers **only** `fall-2026/nik-bear-brown/`; anything outside it still needs his word for each push.
- Git on his machine is already authenticated. Never ask for, accept, or write down a GitHub token.
- Stage **only** `fall-2026/nik-bear-brown/` (and the one `.gitignore` line that tracks it). The repo often has other uncommitted instructor edits; never sweep them in.
- Run `python3 scripts/validate_course.py` from the repo root before committing.

## Privacy

This repo is public. The person here is **"Professor Bear."** No contact details, profile links, or other people's names. No absolute local paths (`/Users/…`) in anything committed. Student folders under `fall-2026/` are untracked and stay that way; only this folder is public.
