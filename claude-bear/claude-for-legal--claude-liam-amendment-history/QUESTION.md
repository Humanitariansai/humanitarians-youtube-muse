# QUESTION — claude-for-legal--claude-liam-amendment-history

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-amendment-history/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-07-25), but its narration text carries **literal, never-filled
template placeholders** (`>`) at every point where the actual skill-specific
fact should be — `"The skill is amendment-history. >."`, `"Claude's job:
>."`, `"The SKILL.md is the spec — >."`, `"I want to >."` The
`source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/amendment-history/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `amendment-history` SKILL.md, no `commercial-legal` folder). So there are
no real facts to carry over: the source is a Teardown-format shell that was
never actually authored, the same source-gap already logged for the sibling
`claude-for-legal--claude-liam-ai-inventory` redo in this same family.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("AMENDMENT-HISTORY") and the family (`claude-for-legal`, a commercial-legal
skill set) into a generic, defensible account of what "amendment history"
means for a legal document and why it matters — the ordinary legal-practice
fact that an amended contract's current terms are not printed on any single
page, described generically per the fresh-script Phase 1 rule ("when in
doubt, describe behavior generically") rather than inventing a specific
tool's UI, output format, or undocumented behavior. No fact here is
Claude-specific or unverifiable; it is the general shape of tracking a
document through a chain of amendments, clause by clause.

**Question this reel actually answers:** A contract has been signed, then
amended more than once since. Someone needs to know what it says today —
what should they open: the original document, or something else?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
