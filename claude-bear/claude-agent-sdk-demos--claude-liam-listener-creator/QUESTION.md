# QUESTION

**The question:** "Claude, Listener Creator." — is a Skill's "listener" a live
watcher hovering over your inbox, or a definition Claude writes to a file?
Answered using the `listener-creator` skill (from the email-agent SDK demo)
as the concrete case.

**Mode:** redo — source is
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-listener-creator/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold open, B01 anatomy,
B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all
already REMOTION, no puppet/AI-video/pantry beat to replace beyond the
WRITER LAW swap). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, and closes with the Humanitarians AI skin.

**Why it earns a reel:** `listener-creator` creates event-driven email
listeners that monitor for specific conditions (urgent emails from your
boss, newsletters to archive, package tracking are the source's own worked
examples) and execute custom actions — used when someone wants to be
notified about emails, automatically handle certain emails, or set up email
automation. The skill itself is just two files — a `SKILL.md` instruction
set (about nine kilobytes) and a `templates` folder — no live process, no
hidden logic. Claude reads the `SKILL.md`'s Steps section top to bottom:
read the request, execute the step, return the result, linear, no
branching unless a step says so. Because the condition is fixed in the
file, a listener fires the same way every time an email matches it. The
same fact cuts the other way: an equally urgent email that doesn't match
the written condition (wrong sender, wrong word) never fires the listener,
no matter how well it fits the *spirit* of the request.

**Naive framing (B00, corrected on screen):** "A Skill must be some live
watcher scanning my inbox. Is that it?" → corrects "watcher" to "template"
(a Skill's listener is NOT a live process watching your inbox — it's a
template/definition Claude fills in and files away, that fires later when
its written condition matches).

**Body facts carried from source (unchanged):**
- skill name: `listener-creator`
- description: creates event-driven email listeners that monitor for
  specific conditions (urgent emails from boss, newsletters to archive,
  package tracking are the source's own worked examples) and execute
  custom actions; used when someone wants to be notified about emails,
  automatically handle certain emails, or set up email automation
- anatomy: 2 files — `SKILL.md` (~9k) + a `templates` folder
- pipeline: Steps section, executed top to bottom — read the request,
  execute each step in order, return the result; linear, no branching
  unless a step says so
- design tell: `listener-creator` is a specification written as an
  instruction set — same input produces the same output every run; the
  limit is anything outside what the file specifies
- Your Turn: paste a request, then ask Claude to read the skill and walk
  through what it will do *before* doing it — explaining first surfaces the
  real constraint logic
