# SCRIPT.md — Claude, Client Letter. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-client-letter` (Teardown, skill-teardown format) —
question and true generic facts carried over; narration re-registered to
Plain (explain, then stop); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

**Source-fidelity note:** the source never filled in client-letter's
specific "Claude's job: ___" line (literal `>` placeholder survives in four
spots), and its SKILL.md is not reachable from this machine (see
QUESTION.md / BUILD-LOG.md). This script keeps every fact the source DOES
establish — a skill is a folder Claude reads before it acts; it executes
the file's steps in order; it is a specification with a payoff and a
limit — and uses "client-letter" only as the named anchor example (a
skill-shaped folder aimed at producing the well-known client-letter shape:
what happened, what it means, what happens next), never asserting invented
detail about the actual legal-clinic procedure inside its unread SKILL.md.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude learned how to write client letters from a skill called
client-letter. It didn't — it was handed a file of instructions.
Client-letter just names one such file. Let's see what's actually inside it.

## Act I — the wrong guess

**B01 — Sounds like a writing upgrade**
Hear "Claude has a client-letter skill" and it sounds like a writing
upgrade — like it studied real client letters and came back knowing how to
counsel someone in its own words.

**B02 — Broken, with a case** (pays off B00)
But nothing in the model changes. Delete the skill's folder and Claude
doesn't forget how to write — there was nothing to learn. It just stops
following that one routine.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. Client-letter, for instance, is
a folder holding a single SKILL.md — instructions for turning a case update
into a clear client letter, written in plain language Claude reads before
it starts.

**B04 — Read it, then follow it in order**
Claude reads that file top to bottom and works through it step by step, in
the order it's written — no branching, unless the file itself says branch.

**B05 — Spec, not power**
That makes a skill a specification, not a new power. The payoff: the same
structure, every letter — what happened, what it means, what happens next.
The limit: anything outside those written steps, and Claude is off the map.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So client-letter never taught Claude how to counsel a client. It just
guarantees that every time client-letter runs, Claude reads that same file
and produces the same letter structure — that's the whole trick.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude produce a clear client letter doesn't prove it understood
the matter — a file can be followed to the letter on a case it never really
grasped. And watching it produce a clumsy one doesn't prove the skill is
broken — it may just be a case the file's structure doesn't fit.

## Close

**BCRY — carry-out**
A skill doesn't teach Claude how to counsel a client — it's a file of
steps Claude reads before it starts, so every letter comes out with the
same structure, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: pick one document I produce the same
way every time. Write me a SKILL.md for it — plain language, ordered
steps — then read it back to me and walk me through exactly what you'll
do, before you do it.

**BOUT — outro**
Claude, Client Letter. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a client-letter skill" sounds like the model learned client correspondence |
| Wrong guess | B00 → B02 | "learned" corrected to "was given"; broken with the delete-the-folder case |
| Mechanism | B03–B05 | one file, read top to bottom, spec not power |
| Anchor | B03 → B06 | client-letter's single SKILL.md, planted then returned to |
| Both directions | B07 | a clear letter proves nothing about understanding; a clumsy one proves nothing about breakage |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — a compact skill-teardown format with
no explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW), so this redo expands modestly: B01 (stakes) and B02
(wrong guess, broken) are new; B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts across to the anchor; B06 is a new anchor-payoff
beat restating the design tell against the named anchor; B07 (both
directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11 beats —
a small, proportionate expansion of a 7-beat source, not a scale mismatch
(matches the identical-shape expansion on the `claude-for-legal--claude-
liam-case-brief` and `claude-for-legal--claude-liam-build-guide` sibling
redos, which hit the same source-fidelity gap). No new legal-specific fact
was invented anywhere in this expansion beyond the well-known generic shape
of a client letter (what happened, what it means, what happens next).

## One-flag audit

No inference-flag beat: every claim here is about the generic, verifiable
mechanism of a Claude skill (folder + SKILL.md, read-then-execute,
specification semantics) plus the well-known, generic shape of a client
letter — not an inference about an unread source. Nothing in this script
asserts what client-letter's specific legal-clinic procedure actually does.
