# QUESTION

**The question:** "Claude, Auto Updater." — when Claude runs a Skill named
`auto-updater`, is the logic that drives it something built into the model
itself, or is it written down somewhere a person could actually read?
Answered using the general mechanism every Claude Skill shares (a folder,
one `SKILL.md`, steps read in order) with `auto-updater` as the named
example.

**Mode:** redo — source is
`anthropics/claude-for-legal/youtube/claude-liam-auto-updater/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata
`register: "Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.../claude-for-legal/legal-builder-hub/skills/auto-updater/SKILL.md` — a
path that exists only on the original build machine and is not reachable
from here). 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro.

**Source defect found on read (logged per the honesty rule):** three of the
source's seven beats carry a literal, unfilled `>` character sitting where
`auto-updater`'s own specific content should have been substituted in —
B00 ("The skill is auto-updater. **>**. A SKILL.md tells Claude exactly
how."), B03 ("Claude's job: **>**. What it gets right..."), BVDT ("The
SKILL.md is the spec — **>**. Same input, same output..."), and BHTF ("I
want to **>**. Read the auto-updater skill..."). This is a batch-build
template-substitution failure (confirmed against
`anthropics/BUILD-SKILL-EXPLAINERS-LOG.md`'s 2026-07-25 batch entry for
`auto-updater`, which shipped straight to "DONE ✓" with no fix), not a
stylistic choice — the source never actually says what `auto-updater`
specifically updates, or what its concrete steps are. The real
`legal-builder-hub/skills/auto-updater/SKILL.md` is unreachable from this
machine, so those specifics cannot be recovered here.

**What this redo keeps and what it does not invent:** every fact the
source's readable text DOES establish is kept unchanged — a Skill is a
folder Claude reads before acting; its `SKILL.md` is plain-language, not
hidden logic; the pipeline lives in a Steps section read top to bottom,
linear, no branching unless a step says so; run it twice on the same input
and you get the same steps and the same result; the guarantee holds only
for what the file actually describes. Per hai-simple's "when in doubt,
describe behavior generically" rule, this reel builds entirely on those
generic-but-true facts about how a Claude Skill works, using `auto-updater`
only as the *name* of the example skill — it never states what
`auto-updater` specifically automates, since the source never actually said
so and the real file is unreachable.

**Naive framing (B00, corrected on screen):** "Claude's auto-updater — is
the logic baked into the model?" → corrects "model" to "file" (the
newcomer's default read of an "auto"-anything skill is that some
opaque, built-in capability is doing the work; the correction is that the
logic lives in a plain text file, `SKILL.md`, not in the model's weights).

**Body facts carried from source (unchanged, generalized to any Skill):**
- a Claude Skill is a folder Claude reads before it works; this one is
  named `auto-updater`
- its `SKILL.md` is the whole instruction set, written in plain sentences,
  not code — "the file is the program"
- the pipeline lives in a Steps section; Claude reads each step in order
  and executes it, linear, no branching unless a step says so
- delete a step from the file and that step simply does not happen —
  nothing hidden fills the gap
- run the same input through it twice and you get the same steps and the
  same result both times
- that guarantee holds only for input inside what the file describes;
  outside it, Claude has nothing written there to fall back on
