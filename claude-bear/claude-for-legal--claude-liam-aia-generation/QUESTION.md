# QUESTION — claude-for-legal--claude-liam-aia-generation

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-aia-generation/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25), but its narration text carries **literal, never-filled template
placeholders** (`>`) at every point where the actual skill-specific fact
should be — `"the skill is aia-generation. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."` The `source_skill` field it
names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ai-governance-legal/skills/aia-generation/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `aia-generation` SKILL.md, no `ai-governance-legal` folder). So there are
no real facts to carry over: the source is a teardown-format shell that was
never actually authored — the identical defect class as the
`claude-for-legal--claude-liam-ai-inventory` and
`claude-for-legal--claude-liam-ai-tool-handoff` siblings already built in
this batch (see their BUILD-LOG.md entries).

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title and
category ("AIA-GENERATION," filed under `ai-governance-legal`) into a
generic, defensible account of what an AI Impact Assessment is and when it
counts as finished — described generically per the fresh-script Phase 1
rule ("when in doubt, describe behavior generically") rather than inventing
a specific skill's steps, UI, or product claims. "AIA" is used here in its
ordinary sense across AI-governance practice — a structured risk-and-oversight
write-up produced before or during deployment of an AI-powered feature,
covering what the system does, what data feeds it, and who it affects. No
fact in this script is Claude-specific or unverifiable; it is the general
shape of what makes such a document accurate versus merely fluent.

**Question this reel actually answers:** You ask Claude to draft an AI
Impact Assessment and it comes back complete and well-written. Is the
assessment done at that point, or does something else still have to happen?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
