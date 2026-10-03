# QUESTION

**The question:** "Claude, Closing Checklist." — when Claude runs the
`closing-checklist` skill (a corporate-legal Anthropic skill), does it apply
its own legal judgment to decide what belongs on the checklist, or does it
follow a written instruction file? Answered using the skill's own file
structure and step-by-step execution as the concrete case.

**Mode:** redo — source is
`anthropics/claude-for-legal/youtube/claude-liam-closing-checklist/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `audience: "Claude"`, `source_skill`
pointing at a `corporate-legal/skills/closing-checklist/SKILL.md` path that
does not exist on this machine — `/Users/bear/Documents/CoWork/...` — so
this redo works entirely from the source reel's own narration text, the only
surviving record of the skill's content on this machine. 7 beats — B00 cold
open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff,
BOUT outro. B00 was already `ClaudeComposerAsk` REMOTION, not AI-video or
pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER
LAW swap.

**A note on the source's own gaps:** the source narration carries two
unresolved `>` placeholders, never filled in — B03 ("Claude's job: >") and
BHTF ("I want to >"). The skill's specific legal task was never recorded
anywhere on this machine. Per the honesty rule against inventing specifics,
this redo does not fabricate what those placeholders would have said. It
keeps every fact the source states outright about the mechanism — folder,
`SKILL.md`, steps, linear execution, spec-bound behavior, same input → same
output — and states the checklist's domain purpose only in the plain,
generic terms the title itself gives: helping build and work through the
list of items a legal transaction must clear before it can close.

**Why it earns a reel:** A skill is a folder Claude reads before it acts;
`closing-checklist` is one file, `SKILL.md`, holding the whole instruction
set in plain language — no hidden logic. The pipeline lives in the file's
Steps section: Claude reads each step in order and executes it, linear, no
branching unless a step itself says so. The skill is a specification written
as an instruction set, not open-ended legal reasoning — Claude's job is
bounded by what the file says. That buys repeatable results: the same
request, run twice, produces the same steps every time. It also draws a hard
edge: anything outside what the `SKILL.md` specifies is outside the skill's
job, full stop.

**Naive framing (B00, corrected on screen):** "Does Claude just know how to
build a closing checklist?" → corrects "know" to "read" (the newcomer's
default read is that Claude draws on built-in legal knowledge; instead it
reads a written file that tells it how).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; `closing-checklist` is
  one file total, `SKILL.md`, the whole instruction set in plain language
- the file is the program — Claude reads it, then acts
- the pipeline lives in the Steps section: read each step in order, run it —
  linear, no branching unless the step itself says so
- the skill is a specification written as an instruction set, not legal
  judgment; Claude's job is bounded by what the file specifies
- what it gets right: repeatable results — same input → same output, every
  run
- what it bites: anything outside what the `SKILL.md` specifies
- source's Your Turn worked example: paste a request into Claude, name the
  `closing-checklist` skill, and ask it to walk through what it will do
  before doing it — explaining first surfaces the constraint logic
