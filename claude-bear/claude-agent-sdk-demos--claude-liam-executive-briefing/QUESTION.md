# QUESTION

**The question:** "Claude, Executive Briefing." — does Claude sense on its own
when a piece of writing needs boardroom polish, or is that switch flipped by
something more mechanical? Answered using the `executive-briefing` skill
(from the email-agent SDK demo) as the concrete case.

**Mode:** redo — source is
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-executive-briefing/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold open, B01 anatomy,
B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all
already REMOTION, no puppet/AI-video/pantry beat to replace beyond the
WRITER LAW swap). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, and closes with the Humanitarians AI skin.

**Why it earns a reel:** `executive-briefing` transforms research findings
into executive-ready briefings, and per the source's own description it is
"automatically activated when user mentions 'executive', 'briefing',
'C-suite', 'board', 'leadership', or 'presentation'." The skill itself is one
file — `SKILL.md`, about 4k — with no hidden logic beyond that trigger-word
list and a linear Steps section: read the file, execute the step, return the
result. Because activation is keyed to that literal list rather than to
Claude's read of your intent, the exact same request can fire the skill or
not depending only on which words you happened to use — a fact the source's
verdict beat states as "know the limit: only what the file says."

**Naive framing (B00, corrected on screen):** "A Skill must be some judgment
Claude applies automatically. Is that it?" → corrects "judgment" to "list"
(the skill does NOT sense intent — it matches a fixed, printed list of
trigger words in `SKILL.md`).

**Body facts carried from source (unchanged):**
- skill name: `executive-briefing`
- description: transforms research findings into executive-ready briefings;
  automatically activated on the words executive, briefing, C-suite, board,
  leadership, presentation
- anatomy: 1 file — `SKILL.md`, ~4k, no other files
- pipeline: read `SKILL.md`, execute each step in order, return the result;
  linear, no branching unless a step says so
- design tell: `executive-briefing` is a specification written as an
  instruction set — same input produces the same output every run; the
  limit is anything outside what the file specifies
- Your Turn: paste a request, then ask Claude to read the skill and walk
  through what it will do *before* doing it — explaining first surfaces the
  real constraint logic

**Added for this reel (not asserted as fact beyond the source's own
description, consistent with it):** the anchor — the same research memo,
requested two ways. "Turn this into a board presentation" hits two words on
the trigger list (board, presentation) and fires the skill. "Make this
shorter for my boss" carries the identical intent but touches none of the
listed words, and the skill does not fire. This dramatizes the source's own
stated activation rule; it invents no new mechanism.
