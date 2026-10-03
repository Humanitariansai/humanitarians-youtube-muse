# SCRIPT.md — Claude, By the Numbers (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-data` (Teardown, Ch.7 "The Data Plugin") — question,
facts, and body argument carried over; narration re-registered to Plain
(explain, then stop); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
People assume understanding a year of revenue means learning spreadsheet
formulas. It doesn't — you just ask, in plain English. So what's actually
sitting in that file you never open?

## Act I — The unopened spreadsheet

**NB01 — The folder you don't open** (source B01)
Solo operators often avoid their own numbers. A folder called Finances,
twelve months of revenue inside it, never opened — because opening it means
formulas, and formulas mean guessing at syntax and still not trusting the
answer.

**NB02 — The loop, and what it costs** (source B02+B03 merged)
Without help, understanding your numbers looks like a loop: export a CSV,
open it, stare at rows and columns, get a vague sense things are up or
down, close the file. So the questions that actually matter go unanswered —
not because they're unanswerable, but because answering felt too hard.
Decisions ride on gut feel instead.

## Act II — Ask it plainly

**NB03 — Point and ask** (source B04)
Point Claude at that same file and ask the way you'd ask a colleague:
which clients bring in the most revenue, and has the mix changed over the
last two quarters?

**NB04 — No formula, no pivot table** (source B05 — WRONG-GUESS PAYOFF)
No formula. No pivot table. Claude reads the data, runs the analysis, and
hands back a sentence you can act on — faster than it takes to write a
single SUM.

**NB05 — Ask it like a question** (source B06)
That's natural-language querying. What were total sales by month? Which
client led last quarter? Am I spending more on software than six months
ago? Claude turns each question into the right analysis, and answers in a
sentence — not a table of raw numbers.

**NB06 — The anchor: specific, not vague** (source B07 — ANCHOR PLANTED)
It turns "I think business is going okay" into something specific: three
clients carry sixty percent of revenue, and one has been sliding since
September. That's the gap between reacting to problems and seeing them
coming.

## Act III — What it actually does

**NB07 — Four kinds of work** (source B08)
Beyond answering, there are four kinds of work: exploration, cleaning,
visualization, and comparison. Not every question needs all four — but
together they turn a raw export into something you can trust and act on.

**NB08 — Explore** (source B09)
Exploration first. Point Claude at a mystery export — column headers that
don't quite make sense — and it describes the structure, flags outliers,
and suggests the questions worth asking. Often the best question isn't the
one you started with.

**NB09 — Clean** (source B10+B11 merged)
Cleaning. Messy data is the norm — inconsistent date formats, duplicate
rows, impossible values like negative sales. The plugin does this tedious
work and reports exactly what it changed. Automate that, and the barrier
to actually working with your numbers falls away.

**NB10 — Visualize** (source B12)
Visualization. Ask for monthly revenue over the past year, and you get a
chart — for a deck, a partner, or just to see your own trajectory. Line
charts for trends, bars for comparisons, and you can always ask for
something different.

**NB11 — Compare** (source B13)
And comparison. How does this quarter stack against last? Is acquisition
cost climbing or falling? Totals tell you where you are; comparisons tell
you where you're heading.

## Act IV — The monthly habit

**NB12 — The avoided question** (source B14)
Every business has a question it's been avoiding. Start there. Point
Claude at your invoices and your expenses and ask: am I profitable, month
to month? It reads both files, correlates them, and gives you a real read
on your financial health.

**NB13 — The monthly ritual** (source B15+B16 merged)
You'll know more about your finances after this five-minute conversation
than after a year of meaning to look. So make it a ritual: first of the
month, ten minutes — point Claude at last month's revenue and expenses and
ask for a health check: total revenue, total expenses, margin, how it
compares to the month before, and anything that looks off.

**NB14 — Stacked reviews** (source B17)
Do it every month, and you're never surprised by your own numbers again.
Each review stacks on the last, until a trend is visible before it becomes
a problem.

**NB15 — How concentrated is your revenue?** (source B18)
For a service business, one question matters most: how concentrated is
your revenue? Ask directly — who are my top clients, what share rides on
the top three, and is anyone quietly spending less than before?

**NB16 — The concentration risk** (source B19)
Concentration is one of the most important things a solo operator can
know. If a single client is, say, forty percent of your income and you
don't know it, you can't plan for the day they leave. The plugin makes
that check trivial.

**NB17 — The anchor returns** (source B20 — ANCHOR PAYOFF, returns to NB06)
And the follow-up is cheap. Of those top clients, which are declining?
What changed last quarter that might explain it? The plugin makes each
next question almost free — so ask it. Remember the client sliding since
September? This is how you'd catch that early.

## Act V — You own the judgment

**NB18 — Only as trustworthy as...** (source B21)
Here's the honest part. The plugin's analysis is only as trustworthy as
two things: the data you fed it, and the assumptions underneath it. Clean
inputs and sound assumptions give a reliable read. Bad inputs give
confident, well-formatted nonsense.

**NB19 — The audit trail** (source B22)
That's exactly why it reports what it cleaned — so you can verify the
fixes before trusting the numbers built on top of them. The change-log
isn't paperwork. It's the audit trail.

**NB20 — What it can't tell you** (source B23 — BOTH-DIRECTIONS)
The plugin can tell you a client is declining. It can't tell you whether
to call them, discount, or let them go. It surfaces the number; you own
the decision.

**NB21 — Four habits** (source B24)
Four habits make it sing: ask a specific question, not "analyze my data."
Iterate — your first question breeds a better one. Compare, don't just
total. And export on a schedule, because the plugin can only work with the
data you actually give it.

## Close

**BCRY — carry-out**
The data plugin turns the spreadsheet you're avoiding into a five-minute
conversation — but the answer is only as trustworthy as your data and your
assumptions, so the judgment stays yours.

**BHTF — your turn**
Your turn. Paste this into Claude: here's a spreadsheet of my invoices and
one of my expenses for the year — tell me what's in each file and flag
anything messy, then give me a business-health check: am I profitable
month to month, which months were strongest and weakest, is any expense
growing faster than revenue — and end with the one follow-up question I
should ask next.

**BOUT — outro**
Claude, By the Numbers — the data plugin. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–NB01 | the spreadsheet you're afraid to open |
| Wrong guess | B00 → NB04 | "you'd need formulas" corrected/paid off |
| Mechanism | NB03–NB11 | point-and-ask, natural-language querying, the four kinds of work |
| Anchor | NB06 → NB17 | three clients / sixty percent / sliding since September — planted, then the follow-up that catches it early |
| Both directions | NB20 | can surface the number, can't make the call |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the plugin does (explore, clean, visualize, compare; report what it
changed), not an inference about hidden internals. Per simple's ONE-FLAG
LAW, when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 33 beats (deep-explainer chassis: 5 act-title cards C01–C05 + 24
numbered body beats B01–B24, of which B07 is a CARD-lane spark beat and
the other 23 are VOX/MANIM/REMOTION + V01/H01/O01 body-close + duplicate
BVDT/BHTF/BOUT bookend tail with blank narration on BHTF/BOUT). hai-simple's
spine has no act-title-card slot and no duplicate bookend tail, so: the 5
act cards were dropped (their titles now land as narration transitions
instead of separate beats); the spark card B07 was kept as a body beat (it
carries the anchor's concrete numbers, not just a segment title); the 24
numbered body beats were merged three times where two source beats carried
one continuous idea (B02+B03→NB02, B10+B11→NB09, B15+B16→NB13) to 21 body
beats, preserving every fact and the full five-act argument; and the
source's body-close (V01 recap / H01 your-turn / O01 outro) was kept as the
reel's one close (BCRY/BHTF/BOUT), dropping the duplicate blank-narration
bookend triad rather than rendering two closes back to back. Logged per
BUILD-LOG.md.
