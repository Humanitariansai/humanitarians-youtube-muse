# QUESTION — claude-for-legal--claude-liam-board-minutes

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-board-minutes/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25), but its narration text carries **literal, never-filled template
placeholders** (`>`) at every point where the actual skill-specific fact
should be — `"The skill is board-minutes. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >. Read the board-minutes skill..."`
The `source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/board-minutes/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `board-minutes` SKILL.md, no `corporate-legal` folder). So there are no
real facts to carry over: the source is a teardown-format shell that was
never actually authored — the identical defect class already logged for the
`claude-for-legal--claude-liam-ai-tool-handoff`, `-ai-inventory`, and
`-dsar-response` siblings in this same batch.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("BOARD MINUTES") into a generic, defensible account of what board minutes
actually are and what a drafting handoff to Claude can and can't finish by
itself — described generically per the fresh-script Phase 1 rule ("when in
doubt, describe behavior generically") rather than inventing a specific
skill's steps, UI, or product claims. The one fact this reel leans on —
that board minutes are a record of decisions and actions, not a verbatim
transcript, and that they are conventionally reviewed and approved by the
board at a later meeting before they count as the official record — is
ordinary corporate-governance practice, not a Claude-specific or
unverifiable claim.

**Question this reel actually answers:** If Claude drafts your board
minutes from a set of raw meeting notes, is that draft the official minutes,
or does something else still have to happen first?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
