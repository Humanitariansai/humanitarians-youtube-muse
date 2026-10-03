# QUESTION

**The question:** "Claude Code, Skill Development." — if you want Claude to
reliably do a repeatable task your way (rotate a PDF a specific way, follow
your team's writing style, run your project's own checklist), is that
something you ask Claude to remember in conversation, or something you
build and hand it? Answered using the `skill-development` plugin skill's
own worked example — a `pdf-editor` skill that rotates PDFs and converts
pages to images — as the concrete case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-skill-development/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register`
not set but content is Teardown in form, `brand: "claude-liam"`,
`source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md`. 7 beats
— B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF
handoff, BOUT outro). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** A skill is a self-contained package: `SKILL.md`
(YAML frontmatter with `name` + `description`, required, plus an imperative
markdown body) and three optional resource folders — `scripts/` (code
Claude runs without reading), `references/` (docs Claude reads while
working), `assets/` (files used in the output, never loaded into context).
Progressive disclosure runs in three levels: level one, the name and
description, sits in context for every conversation (~100 words); level
two, the SKILL.md body, loads only once the skill's description matches
what's being asked (target 1,500–2,000 words, hard ceiling 5,000); level
three, the resource folders, load only when Claude decides it needs them —
no word limit, because a script can run without ever being read into
context. The description is what makes the skill findable: third person,
naming a specific trigger phrase ("this skill should be used when the user
asks to rotate a PDF, convert PDF pages to images") — not a vague summary
("use this skill for PDF tasks"). The body is written in imperative form
("process the file with rotate_pdf.py," not "you should process the
file"). The six-step build process: understand (concrete trigger
examples), plan resources (what would be rewritten every time → script,
reference, or asset), create the structure, edit (resources first, SKILL.md
last), validate, iterate.

**Naive framing (B00, corrected on screen):** "How do I add a reminder so
Claude always follows my PDF workflow?" → corrects "reminder" to "skill"
(telling Claude to remember something in conversation is not the same as
building a package with a description written to be found — a reminder
lives only in that conversation; a skill lives in a file whose name and
description are visible before you ever ask).

**Body facts carried from source (unchanged):**
- a skill = `SKILL.md` (frontmatter: `name` + `description`, required;
  imperative body) + optional `scripts/` (code) + `references/` (docs) +
  `assets/` (output files, never loaded into context)
- progressive disclosure, three levels: metadata always in context
  (~100 words) → body loads on trigger (target 1,500–2,000 words, ceiling
  5,000) → resources load only as needed (no word limit)
- description quality: third person + a specific trigger phrase, not a
  vague summary
- body writing rule: imperative form, not advisory phrasing
- six-step process: understand → plan resources → create structure → edit
  (resources first, SKILL.md last) → validate → iterate
- always reference your resources: a `references/patterns.md` the body
  never mentions is a file Claude doesn't know to look for
- source's worked example: a `pdf-editor` skill — rotating PDFs, converting
  pages to images — checked for a third-person trigger-phrase description,
  imperative body, lean body under 2,000 words that references
  `scripts/rotate_pdf.py` by name rather than embedding it, and explicit
  references to every resource file it creates
