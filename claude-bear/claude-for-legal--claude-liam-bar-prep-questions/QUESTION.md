# QUESTION — claude-for-legal--claude-liam-bar-prep-questions

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-bar-prep-questions/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-07-25), but its narration text carries **literal, never-filled
template placeholders** (`>`) at every point where the actual skill-specific
fact should be — `"The skill is bar-prep-questions. >."`, `"Claude's job:
>."`, `"The SKILL.md is the spec — >."`, `"I want to >."` The
`source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/law-student/skills/bar-prep-questions/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `bar-prep-questions` SKILL.md, no `law-student` folder under
`claude-for-legal`). So there are no real facts to carry over: the source is
a Teardown-format shell that was never actually authored — the same
source-gap already logged for the sibling
`claude-for-legal--claude-liam-amendment-history` and
`claude-for-legal--claude-liam-ai-inventory` redos in this same family.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("BAR-PREP-QUESTIONS") and the family (`claude-for-legal`, a law-student
skill set) into a generic, defensible account of what asking Claude for
bar-exam-style practice questions actually gets you and what it doesn't —
described generically per the fresh-script Phase 1 rule ("when in doubt,
describe behavior generically") rather than inventing a specific tool's UI,
output format, or undocumented behavior. The facts used are public and
uncontroversial: the bar exam includes a standardized multiple-choice
component tested across a fixed set of law-school subjects (evidence,
contracts, torts, and the like), each question pairs a fact pattern with
several answer choices and an explanation, and law students commonly drill
on large volumes of practice questions before sitting the exam. No fact
here is Claude-specific, product-specific, or unverifiable.

**Question this reel actually answers:** A law student asks Claude to
generate bar-exam-style practice questions to drill on. The questions come
back formatted exactly like the real exam — should the student trust the
rule stated in the explanation the same way they'd trust a certified
bar-review company's material, or is there a catch?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
