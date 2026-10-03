# SCRIPT.md — Claude, Built (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-building-plugins` (Teardown, Ch.12 "Building Your Own
Plugins") — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
People assume building your own Claude plugin means learning to code. It
doesn't — you describe the workflow, and a guided builder assembles it
around you. So how do you actually build one?

## Act I — Why build your own

**B01 — No box fits you**
The official plugin catalog covers what most businesses share — marketing,
sales, data, support. But your work has a shape none of them anticipated:
how you onboard a client, how your proposals are structured, the checklist
you review against. No off-the-shelf plugin knows that.

**B02 — The process, transferred**
Right now, that process lives in your head, or in a scattered document. It
works because you've internalized it. A custom plugin is the transfer — it
lifts those steps into something Claude can follow the same way, every time.

**B03 — You are the business**
This matters most if you're the whole business — every hat, every method
that makes the work good, carried around in your head all day. A plugin
draws that out and makes it repeatable, so the standard survives a busy
week, a handoff, a bad night's sleep.

**B04 — Scatter, then converge**
Hand that process to a new hire, and results scatter — the method never
fully transfers by word of mouth. Encode it once, and every run converges
on the same standard, without you re-explaining it from scratch.

## Act II — What's inside

**B05 — Four parts** (ANCHOR PLANTED)
Underneath, a plugin bundles up to four things: skills — your expertise,
written down. Commands — the shortcuts that trigger it. Connectors — the
links to your tools and data. And subagents — the ability to run the whole
job on its own.

**B06 — A folder of text**
And it's nothing exotic — a plugin is a folder. Plain text and
configuration, organized: one instructions file at the root, and a
directory for each kind of part. Because it's just text, it's easy to read,
edit, or hand to someone else.

**B07 — Skills are the expertise**
Skills are the expertise itself — your proposal structure, your pricing
logic, your standard terms, the way you scope a job — written as
instructions Claude can follow.

**B08 — Commands are the shortcuts**
Commands are the shortcuts. Slash-new-proposal runs your whole proposal
workflow. Slash-client-onboard starts your onboarding sequence — each one, a
capability one keystroke away.

**B09 — Connectors are the reach**
Connectors are the reach. If the plugin needs your pricing spreadsheet, or
has to file documents in a specific folder, a connector makes that link —
so it works on your actual tools, not a generic stand-in.

**B10 — Subagents are the autonomy**
And subagents are the autonomy. Ask it to run the whole onboarding, and it
quietly coordinates the steps — creating folders, drafting the welcome
note, building the tracker — then hands you one finished result.

## Act III — How you build it

**B11 — No code — a conversation** (pays off B00)
Here's the part that sounds technical and isn't: you don't write code, and
you don't edit configuration files. There's a guided builder — itself a
plugin you install — and you build yours by having a conversation with it.

**B12 — Describe it in plain language** (concrete anchor example)
You describe the workflow in plain language: when I sign a new client, I
create a project folder, draft a welcome email with the timeline, generate
a kickoff questionnaire, and open a tracking document.

**B13 — Four steps**
From there, it's four steps: describe the process, answer its follow-up
questions, refine it against a real case, then use it.

**B14 — Assemble** (ANCHOR PAYOFF — returns to B05)
As you answer, the builder sorts what you said into those same four parts —
your standards become skills, your triggers become commands, your tools
become connectors. The conversation goes in; a structured plugin comes out.

**B15 — Test, then run**
Test it on a real scenario — onboard a new client, see if it matches what
you'd do by hand — and adjust what's off. After that, one command runs the
entire process: consistently, completely, in minutes.

## Act IV — What to build for

**B16 — Four signals**
Look for four signals: you follow the same steps every time. Consistency
actually matters. You'd rather not think about it. And the quiet one —
you've caught yourself wishing you could just hand this off.

**B17 — Wishing you could hand it off**
That last phrase — I wish I could hand this off — is usually a plugin
pointing at itself. The task you'd delegate if you had someone to delegate
to is exactly the task a plugin can hold.

**B18 — The leverage**
That's the leverage: the administrative work — the setup, the formatting,
the standard messages — gets done the same way, whether it's the first
time this month or the tenth.

**B19 — Scope it to the real work**
But point it at the right work: automate the repeatable scaffolding, and
keep the judgment calls for yourself — the ones that actually need you.
Scope a plugin to a real, repeated workflow, not for its own sake.

## Act V — Share and evolve

**B20 — It travels**
Once it works, it travels. It's just a folder of text — share it with your
team so everyone onboards the same way, or publish it to the wider
directory. If it solved your problem, it likely solves someone else's.

**B21 — Refined, shared, evolving**
That's the quiet upside of a file-based tool: years of refining a process
become something a peer installs in a minute. And it keeps evolving — after
a few weeks you'll see what's thin or missing, and update it.

**B22 — Look first**
One thing before you build anything: look first. A growing community has
already published plugins for specific roles and industries — adopting one
and adjusting it to your specifics is often faster than starting from
scratch.

## Close

**BCRY — carry-out**
When no official plugin fits, build your own: describe your workflow, and a
guided builder turns it into skills, commands, connectors, and subagents —
no code required.

**BHTF — your turn**
Your turn. Paste this into Claude: I run a small business, and there's one
workflow I repeat constantly and keep wishing I could hand off. Help me
turn it into a custom plugin — first ask me to describe it step by step,
then tell me which steps become skills, which become commands, and which
need a connector to my tools, and give me the exact first message to send a
plugin builder to start assembling it.

**BOUT — outro**
Claude, Built — building your own plugins. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | catalog doesn't fit your specific workflow |
| Wrong guess | B00 → B11 | "you'd need to code it" corrected/paid off |
| Mechanism | B02–B15 | the transfer, the four parts, the conversation |
| Anchor | B05 → B14 | four parts planted, returned to as the assembly payoff |
| Both directions | B19 | automate the repeatable half, keep the judgment half |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 37 beats (deep-explainer chassis: 5 act-title cards + 25 body
beats + V01/H01/O01 body-close + duplicate BVDT/BHTF/BOUT bookend tail with
blank narration on BHTF/BOUT). hai-simple's spine has no act-title-card slot
and no duplicate bookend tail, so: the 5 act cards were dropped (their
titles now land as narration transitions instead of separate beats); the
25 body beats were merged where two source beats carried one continuous
idea (B03+B04→B03, B20+B21→B19, B23+B24→B21) to 22 body beats, preserving
every fact and the full five-act argument; and the source's body-close
(V01 recap / H01 your-turn / O01 outro) was kept as the reel's one close
(BCRY/BHTF/BOUT), dropping the duplicate blank-narration bookend triad
rather than rendering two closes back to back. Logged per BUILD-LOG.md.
