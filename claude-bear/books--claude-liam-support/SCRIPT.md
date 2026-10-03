# SCRIPT.md — Claude, On Call (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-support` (Teardown, Ch.10 "Support") — question, facts,
and body argument carried over; narration re-registered to Plain (explain,
then stop); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked if Claude can just answer their support tickets, fully on its
own. Not quite — it drafts them. So here's the real question: can Claude
just draft my support tickets?

## Act I — The reactive burden

**NB01 — The queue arrives anytime** (source B01)
If you have customers, you have support — and it doesn't wait. A queue that
fills overnight, questions that don't clock out. Left alone, it eats your
day in fragments.

**NB02 — Burden, or process** (source B02)
The support plugin turns that burden into a process. For a solo operator,
it's the difference between reacting all day and running a system that
handles the queue for you.

**NB03 — Five voices, one** (source B03)
For a small team, it does something else: one consistent voice. Instead of
five people answering five different ways, every reply carries the same
tone and the same facts.

## Act II — The wrong guess, and the case that breaks it

**NB04 — "So it just answers them?"** (WRONG GUESS)
So the natural read is that it's fully automatic: it reads the ticket,
writes the reply, and sends it — support on autopilot, no human in the
loop.

**NB05 — The customer who breaks that** (ANCHOR PLANTED, BREAK)
Here's a case: a customer's payment has failed three times, they've been
with you two years, and they're angry. Send that on autopilot and you risk
getting the tone wrong on the one account that can't afford it. So it
doesn't send. It drafts, and waits for you.

## Act III — What it actually does

**NB06 — Four jobs, one plugin** (source B04)
Under the hood, it does four concrete jobs: triage the queue, draft the
replies, build a knowledge base, and read sentiment. Not magic — four jobs
it does well.

**NB07 — Sort the wall** (source B05)
Triage first. As requests land, it sorts them: what needs you now, what can
wait, and what's a known issue with a standard answer. The queue stops
being a wall and becomes a sorted list.

**NB08 — Draft, on-brand** (source B06)
Then drafting. It generates replies that fit the moment — pulling from your
configured tone, your knowledge base, and the specific request in front of
it. A first draft, not a form letter.

**NB09 — Find the ones who matter** (source B07)
Third, sentiment. Not every request is equal — it flags the frustrated and
the at-risk, the customer who needs a human now. It points your attention
at the messages that actually need it.

**NB10 — Real conversations, not a blank slate** (source B08+B09 merged)
And it doesn't start from nothing: it reads your existing support inbox for
context, and mines the questions you've already answered to draft a
structured FAQ. Your scattered experience becomes a help center.

**NB11 — Set the tone, set the tripwires** (source B10)
One setup step makes it yours: you set the tone — warm, efficient, or both
— and escalation triggers, the words and situations that skip the standard
answer and route straight to you. You decide what always reaches a human.

**NB12 — Thirty focused minutes** (source B11+B12 merged)
In practice: hand it the overnight queue and ask what's urgent, what's
routine, and what you can answer in a line. The payoff is time — a morning
that might otherwise stretch into two fragmented hours compresses into
thirty focused minutes.

## Act IV — The anchor returns

**NB13 — The plugin caught the tone; you caught the context** (ANCHOR PAYOFF, source B13+B14)
Back to that angry customer. Claude drafts in your tone — acknowledges the
frustration, explains the issue, proposes a fix. You read it, add a
personal line only you would know to add, and send. The plugin caught the
tone; you caught the context.

**NB14 — Answer once, reuse forever** (source B15+B16 merged)
And every FAQ entry pays forward: Claude finds the questions you keep
answering, ranks the top ten, and drafts each one. Publish it, and that's
one question you never field again — volume that quietly falls instead of
climbing.

## Act V — Both directions

**NB15 — Review, every time** (source B18 — DIRECTION A)
For a live reply to an actual customer, the rule never relaxes: draft,
review, then send. That's where your judgment catches what the plugin
can't see — the exception, the fragile account, the case autopilot would
get wrong.

**NB16 — Publish once, runs alone** (DIRECTION B — the rule flips)
But for the FAQ, the rule flips: you review an answer once, publish it, and
it serves every future customer who asks that question without you
touching it again. Same drafts, a different rule once they go public.

## Close

**BCRY — carry-out**
Claude drafts every reply — you're still the one who decides what actually
gets sent.

**BHTF — your turn**
Your turn. Paste this into Claude: I run support for a small business and
want to set up the support plugin. First, ask me the five questions my
customers ask most, the tone my replies should carry, and the situations
that must always reach me personally. Then draft FAQ answers for those
five, a reusable reply template in my tone, and a short list of escalation
triggers I should configure.

**BOUT — outro**
Claude, On Call — the support plugin. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–NB01 | support arrives whether you're ready or not; the naive guess is that it's fully automatic |
| Wrong guess | NB04 → NB05 | "it just answers them, fully automatic" corrected/broken by the angry three-failed-payments customer |
| Mechanism | NB06–NB12 | the four jobs, each unpacked, plus setup and the morning-triage payoff |
| Anchor | NB05 → NB13 | the angry customer — planted as the case that breaks autopilot, paid off as the actual drafted-and-reviewed reply |
| Both directions | NB15 / NB16 | review-before-send holds for live replies; it flips for a published FAQ entry, which then runs unsupervised |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the product does (triage, draft, build a knowledge base, read sentiment,
configure tone/escalation, review before send, FAQ deflects future
tickets) — not an inference about hidden internals. Per simple's ONE-FLAG
LAW, when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 31 beats (deep-explainer chassis: 4 act-title cards C01–C04 + 20
numbered body beats B01–B20 + V01 verdict recap + H01 your-turn + O01
outro + a duplicate blank-narration BVDT/BHTF/BOUT bookend tail — same
"duplicate close" pattern already logged on the `books--claude-liam-
installing-plugins` sibling). hai-simple's spine has no act-title-card
slot, no separate verdict-recap beat (Plain register carries one carry-out
sentence, not a bulleted recap — CARRY-OUT LAW), and no duplicate bookend
tail, so: the 4 act cards were dropped (their titles now land as narration
transitions instead of separate beats); B20 (already a spark/summary line —
"the plugin drafts, you decide what sends" — not a distinct fact) folded
into the carry-out instead of being kept as its own beat, since keeping it
would say the same thing as BCRY twice; the 20 numbered body beats were
merged three times where two source beats carried one continuous idea
(B08+B09→NB10, B11+B12→NB12, B13+B14→NB13, B15+B16→NB14 — four merges) to
16 body beats, preserving every fact and the full four-act argument; the
source's own "draft, don't autosend" rule (B17/B18) and "patterns are
feedback" rule (B19) were re-expressed as the BOTH-DIRECTIONS pair
NB15/NB16 (review-before-send holds for live replies, flips for a
published FAQ entry) rather than kept as three separate beats, since Plain
register's spine wants one both-directions beat pair, not a three-beat
list of rules; and the source's body-close (V01 recap / H01 your-turn / O01
outro) was kept as the reel's one close (BCRY/BHTF/BOUT, V01's bullet
recap re-expressed as BCRY's single sentence), dropping the duplicate
blank-narration bookend triad rather than rendering two closes back to
back. Logged per BUILD-LOG.md.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (ChipGrid/SegmentCard/
SourceFlow/FormACard patterns) and MANIM (including four "doodle" stills
that carried a leftover `pantry_note` in planning metadata but were
actually built as rendered Manim scenes, not photos) — NO-GENAI/NO-PANTRY
LAW required no substitution beyond B00.
