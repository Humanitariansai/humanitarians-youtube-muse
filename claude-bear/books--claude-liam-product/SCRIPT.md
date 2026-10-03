# SCRIPT.md — Claude, Shipping (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-product` (Teardown, "The Product Plugin" chapter) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
People assume the product plugin decides what to build next for you. It
doesn't — it narrows the options. So what does it actually do, and who
makes the final call?

## Act I — The role you lack

**NB01 — The missing product manager** (source B01)
Big teams have a product manager — the person who asks who this is for,
what problem it solves, and what you're deliberately not building. Build
solo and nobody asks those questions. The product plugin is that
discipline, installed.

**NB02 — Fun isn't the same as important** (source B02+B03 merged —
WRONG-GUESS + correction)
Picture the solo builder: ten ideas on sticky notes, a few hours a week,
and a steady pull toward whatever's most fun to build. Left alone, you
chase the interesting feature. Discipline points the other way — toward
the one that actually moves the product — and the plugin keeps pulling you
back toward it.

**NB03 — It pushes back** (source B04)
It works as the structured thinking partner you don't have on your own. It
doesn't just agree with you — it pushes back, asks the awkward question,
and makes you justify the plan before you sink a week into building it.

**NB04 — Four hard questions** (source B05)
Four questions a good product manager always asks. Who is this for? What
problem does it solve? How will you know it's working? And what are you
not building — and why?

## Act II — What it makes

**NB05 — Five things it ships** (source B06)
The discipline lands as documents you can act on: feature specs, user
stories, feedback synthesis, a roadmap, release notes. Not paperwork for
its own sake — the artifacts that keep you from building blind.

**NB06 — Idea becomes spec** (source B07)
Give it a rough idea — add booking to my site, people pick a slot and get
a confirmation — and it returns a real spec: what the feature does, who
it's for, the user flow, the edge cases, and how you'll know it's done.

**NB07 — Decide before you code** (source B08)
That spec is what saves you. It forces the edge case — what happens when
two people book the same slot — out into the open before you're halfway
through the code and blindsided by it.

## Act III — Break it into stories

**NB08 — One want, many stories** (source B09)
So it breaks the feature down. "I want users to book calls" fans out into
small, testable pieces: see the open slots, pick one, enter details, get a
confirmation, reschedule if needed. Each one buildable in a single focused
session.

**NB09 — Build story by story** (source B10)
Written out, it reads like a checklist you can execute against — one
story per line, each with a clear definition of done. You build story by
story, testing as you go, instead of shipping the whole thing at once.

**NB10 — Small wins accrue** (source B11)
And the stories stack. Ship one, confirm it works, move to the next — the
feature accretes from small wins instead of arriving as one risky
big-bang launch that either works or doesn't.

## Act IV — What should I build next

**NB11 — The anchor: ten ideas, few hours** (source B12 — ANCHOR PLANTED)
Here's the real bottleneck. Ten features you could build, and a fixed
slice of hours a month to build them. You cannot do all ten. Something has
to be first, something has to wait, and something should probably never
get built at all.

**NB12 — Feedback, ranked** (source B13)
First it synthesizes. Point it at three months of feedback — emails,
surveys, support tickets — and it reads all of it, then ranks the patterns
by how often they come up and how much they hurt.

**NB13 — A wall of voices** (source B14 — the trap)
Because the trap is loudness. A folder of feedback is a wall of voices —
and the voice that shouts the most always feels like the most urgent
thing to fix.

**NB14 — Common beats loud** (source B15+B16 merged — the correction)
But the plugin counts instead of listening for volume. The loudest request
often isn't the most common need — it surfaces the quiet pattern a dozen
users quietly share, the one you'd have missed straining to hear the
shout. Optimize for loud and you build for a handful; optimize for common
and you build for the many.

## Act V — Ship it, remember why

**NB15 — Their side, not yours** (source B17+B18 merged)
Release notes. You wrote "optimized the rendering pipeline" — nobody
outside your own head cares. It rewrites that into what the user actually
feels: your dashboard now loads in under a second. Same change, told from
their side, so a quiet bug fix reads as "they actually heard me."

**NB16 — Write down the why** (source B19+B20 merged)
Then document the decision. Building your own login system, or leaning on
an outside service? It lays out the trade-offs — cost, complexity,
flexibility, upkeep — in one clean comparison, and you make the call. Six
months on, when you wonder why you went this way, the reasons are written
down, not a mystery to reverse-engineer.

## Act VI — Who makes the call

**NB17 — It does the grunt work** (source B21)
Be precise about what it does. It gathers the feedback, structures the
spec, ranks the options, and drafts the notes. Four kinds of grunt work,
done fast and done well.

**NB18 — Ranks, doesn't decide** (source B22 — ANCHOR PAYOFF)
But ranking is not deciding. It can tell you this feature scores higher on
impact and feasibility — it cannot know your bet, your users, or your gut
about where the product is going. Of the ten ideas from before, it narrows
the field; the pick is still yours.

**NB19 — You keep the call** (source B23 — BOTH DIRECTIONS)
So it hands you a shortlist, not a verdict. The prioritization is a
judgment call, and the human at the desk still makes it. That caveat isn't
fine print — it's the whole point.

## Close

**BCRY — carry-out**
The product plugin turns scattered ideas and feedback into a ranked
shortlist of what to build next — but ranking isn't deciding, and the call
at the desk stays yours.

## Beat-count note (redo)

Source `claude-liam-product` is a 36-beat Teardown/deep-explainer chassis:
B00 (puppet-ask via `ClaudeComposerAsk`) + 6 act-title cards (C01-C06) + 24
numbered body beats (B01-B24) + a Teardown verdict-recap (V01) + an
old-style your-turn (H01) + an old-style outro (O01) + a vestigial
blank-narration bookend pair (BHTF/BOUT, empty `narration_text` — a
leftover schema-migration artifact never actually carrying content). Per
hai-simple's spine, this redo drops the 6 act cards (their titles now land
as narration transitions and act headers inside this script), drops the
dead blank BHTF/BOUT pair, and replaces the separate V01 Teardown
verdict-recap and the short B24 coda card ("It accelerates the call. You
still make it.") with a single CARRY-OUT LAW sentence that carries the
same point. Four beat-pairs carrying one continuous idea were merged
(B02+B03→NB02, B15+B16→NB14, B17+B18→NB15, B19+B20→NB16), landing at 19
GRAPHIC body beats + B00 + BCRY/BHTF/BOUT = 23 beats total. Body substance
is a 1:1 carry — every fact, question, and workflow from the source's 24
body beats survives in the 19 merged beats (B24's line is folded into
BCRY).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | NB01-NB02; the workflow mechanics wait until NB03 onward |
| Wrong guess surfaced *and corrected* | B00 types "decides," corrects to "narrows"; NB02 states the fun-vs-important pull and NB18/NB19 land the correction that ranking narrows but never decides |
| Anchor, planted early, paid off late | NB11 (ten ideas, few hours — you can't build them all) → NB18 (of the ten ideas, it narrows the field; the pick is still yours) |
| Both failure directions | NB19 — what it gives (a shortlist, a judgment call surfaced) and what it withholds (a verdict, the decision itself) |
| No design judgment | NB08/NB17/NB19 describe what the plugin does and its limits; they never rule on whether Anthropic built it well |

## Deliberately not claimed

- **No plugin version number or specific UI labels invented.** The source
  never named one, and neither does this redo — behavior is described
  generically ("connect your analytics," "point it at three months of
  feedback").
- **No claim it replaces judgment.** NB18, NB19, and the carry-out are
  explicit: it ranks and drafts; the final call — what to build, what to
  skip — stays a stated human decision, not softened into a sales pitch.
- **No accusation and no design critique.** The reel explains what the
  plugin does and where its edge sits; it never judges why Anthropic built
  it that way (Teardown territory, excluded from Plain).

## Handoff prompt (BHTF, read aloud)

> "I'm building my product solo and I have more feature ideas than time.
> Here are the features I'm considering for next quarter: [list them]. I
> have about [N] hours a month to build. My users are mostly [who they are
> and what they use it for]. Help me prioritize: (1) which should I build
> first, (2) which can wait, and (3) which is a distraction dressed up as a
> good idea — and tell me why for each."

Why it's worth running: it's the same shortlist-not-verdict move NB11-NB18
walks through — naming your real constraints out loud is what turns ten
sticky notes into an actual plan, and the ranking is only a starting point
for the argument you have with it next.

---
**GATE P — signed:** N/A (hai-simple, no human puppet-host gate; the slate
cut IS the review per VOICE-LOCK.md)
