# QUESTION — claude-for-legal--claude-liam-client-intake

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-client-intake/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-07-25), but its narration text carries literal, never-filled
template placeholders (`>`) at every point where the actual skill-specific
fact should be — `"Claude's job: >."` (B03), `"The SKILL.md is the spec —
>."` (BVDT), and `"I want to >."` (BHTF). Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/client-intake/SKILL.md`
— searched the whole `books/` tree on this machine; neither that file nor a
`legal-clinic` folder exists anywhere. So there are no real, skill-specific
facts to carry over: the source is a Teardown-format shell that was
generated from the batch pipeline (per its own `PEDAGOGY.md`: "Batch
build — skill teardown format") but never actually authored.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("CLIENT-INTAKE") and the family (`claude-for-legal`) into a generic,
defensible account of what a legal client-intake process is and what a
skill built to run one has to get right — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically")
rather than inventing specific tool names, UI, or product claims. No fact
here is Claude-specific or unverifiable; it is the general shape of how a
legal-intake conversation is structured (fixed question order, conflict
check ahead of substance) as practiced in legal-clinic and law-firm intake
broadly.

**Question this reel actually answers:** When a legal team runs client
intake, what's the one thing the process has to get right first — and what
does someone new to the process naturally assume it's for instead?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
