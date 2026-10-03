# QUESTION

**The question:** "Claude, Action Creator." — is a Claude Skill special code
Claude runs, or a file it reads? Answered using the `action-creator` skill
(from the email-agent SDK demo) as the concrete case.

**Mode:** redo — source is
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-action-creator/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold open, B01 anatomy,
B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all
already REMOTION, no puppet/AI-video/pantry beat to replace beyond the
WRITER LAW swap). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, and closes with the Humanitarians AI skin.

**Why it earns a reel:** `action-creator` creates user-specific one-click
action templates that execute email operations when clicked in the chat
interface (e.g. send a payment reminder to a specific vendor, forward bugs
to engineering, archive newsletters from a specific source). The skill
itself is just two files — a `SKILL.md` instruction set and a `templates`
folder — no executable, no compiled logic. Claude reads the `SKILL.md`'s
Steps section top to bottom: read the request, run the step, return the
result, linear, no branching unless a step says so. Because the steps are
fixed in the file, a saved one-click button produces the same result on
every click. The same fact cuts the other way: ask that button to do
something the file never described (negotiate the invoice instead of just
sending the reminder), and nothing happens beyond what's already there.

**Naive framing (B00, corrected on screen):** "A Skill must be some code
Claude runs automatically. Is that it?" → corrects "code" to "file" (a Skill
is NOT compiled/executable code — it's a plain-text file of instructions
Claude reads before acting).

**Body facts carried from source (unchanged):**
- skill name: `action-creator`
- description: creates user-specific one-click action templates that
  execute email operations when clicked in the chat interface (payment
  reminders, bug forwarding, newsletter archiving are the source's own
  worked examples)
- anatomy: 2 files — `SKILL.md` (~12k) + a `templates` folder
- pipeline: Steps section, executed top to bottom — read SKILL.md, execute
  each step in order, return the result; linear, no branching unless a step
  says so
- design tell: `action-creator` is a specification written as an
  instruction set — same input produces the same output every run; the
  limit is anything outside what the file specifies
- Your Turn: paste a request, then ask Claude to read the skill and walk
  through what it will do *before* doing it — explaining first surfaces the
  real constraint logic
