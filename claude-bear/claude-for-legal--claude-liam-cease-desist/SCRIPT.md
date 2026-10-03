# SCRIPT.md — Claude, Cease Desist. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-cease-desist` (Teardown, walks the Anthropic
`cease-desist` legal Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude decides on its own when it writes a cease and
desist letter. It doesn't decide — it follows steps. So: when Claude writes
one, is it just following steps?

*(Text typed on screen: "When Claude writes / a cease and desist, / is it
deciding?" — trigger word "deciding" corrects to "following steps",
landing on: "When Claude writes a cease and desist, is it following
steps?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
cease-desist. Its one file, SKILL.md, holds the whole instruction set,
written in plain language — no hidden logic. Claude reads it, then acts.
The file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — What carries the header, and what doesn't** (source B03, design
tell — re-registered Teardown → Plain)
One instruction inside it is specific: the internal draft, the pre-send
brief, and the triage memo are all marked as attorney work product —
internal legal material. The letter that actually goes out isn't marked
that way, because it's written to be read by the other side, not kept as
an internal file.

## Close

**BCRY — carry-out**
Claude isn't deciding what belongs in the letter — it's following the
SKILL.md, one step at a time, and only doing what that file says.

**BHTF — your turn**
Your turn. Paste this into Claude: I think someone is using my brand name
without permission. Read the cease-desist skill, and before you draft
anything, walk me through exactly what you'll do — what steps you'll
follow, what you need from me, and what stays out of the letter.

**BOUT — outro**
Claude, Cease Desist. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a legal question — is Claude deciding? |
| Wrong guess | B00 (WRITER LAW) | "deciding" corrected to "following steps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; one specific rule governs the work-product header |
| Anchor | the cease-desist Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "follows the file, only what it says" states both what the mechanism does (execute reliably) and its limit (only what the file says) in one sentence, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Skill's SKILL.md specifies (a folder, one file, a Steps section executed
in order, the work-product header rule) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (puppet cold open) + B01/B02/B03 (anatomy / pipeline
/ design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) — already
the shortest of the `claude-liam-*` Teardown family, a single-example skill
walkthrough with no wrong-guess, anchor, or both-directions beats of its
own to redistribute (unlike the `books--claude-liam-support` sibling, whose
much longer deep-explainer source supplied material for those). This redo
keeps that same 7-beat shape: B00 replaced 1:1 with BrutalistHesitantWriter
(carrying the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat); B01→NB01, B02→NB02, B03→NB03 kept as one beat each, Teardown framing
("the design tell," "a deliberate trade-off") stripped to a plain
mechanism description; BVDT's two verdict facts (reliable execution, and
the file-only limit) merged into the single BCRY carry-out sentence rather
than kept as a separate artifact-card beat, since Plain register carries
one carry-out sentence, not a bulleted verdict (CARRY-OUT LAW); BHTF kept
as the your-turn handoff, with the source's bracketed placeholder ("I want
to >") replaced by a concrete, paste-ready scenario so the prompt is
actually runnable today; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (SkillTeardownAnatomy /
SkillTeardownPipeline / SkillTeardownMechanism / ClaudeVerdictArtifact /
ClaudeComposerAsk / ClaudeTitleOutro patterns) with B00 as the puppet host
(REMOTION `ClaudeComposerAsk`, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00's cold open, which this redo replaces per hai-simple's mandate anyway.
