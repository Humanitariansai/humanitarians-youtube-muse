# QUESTION.md

**Question:** Can Claude give my trademark or brand name final legal clearance to use?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's `clearance`
skill for IP-legal work).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be: `"The skill is clearance. >."`, `"Claude's job: >."`, `"clearance is a
specification written as an instruction set."` (body left as `>`), `"Same input, same
output, every run. Know the limit: only what the file says."` (artifact line left as
`>`), `"I want to >."`. Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/clearance/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an `ip-legal`
folder exists anywhere. So there were no real facts to carry over beyond the topic
(CLEARANCE, an Anthropic skill for IP-legal work — file size 26k per the source's own
`SkillTeardownAnatomy` props) and the shape (Teardown skill-teardown format, 7 beats:
cold open, anatomy, pipeline, design tell, verdict, handoff, outro) — same defect class
as the `ai-inventory`/`ai-tool-handoff`/`aia-generation`/`amendment-history` siblings in
this family.

**The call:** reconstructed a generic, defensible account of what an IP clearance skill
does — screening a proposed name, mark, or creative element against a checklist of
sources and criteria a SKILL.md defines, and returning a structured clearance report —
described generically per the fresh-script Phase 1 rule ("when in doubt, describe
behavior generically") rather than inventing specific database names, product UI, or
legal-outcome claims. No fact in the resulting script is Claude-specific or unverifiable;
the central fact (a screening checklist is not a legal sign-off) is true of any such
skill regardless of its exact source text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-clearance/beat_sheet.json` (7-beat
Teardown skill-teardown, register "Teardown"). Shape and beat count are locked from that
source; this build re-registers the narration to Plain, replaces the cold open with
BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
