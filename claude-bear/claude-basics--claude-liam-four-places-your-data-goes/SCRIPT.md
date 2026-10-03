# Three You Can Take Back. One You Can't. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`claude-basics/claude-liam-four-places-your-data-goes`, Teardown register,
`ai-explainer` skill). Register: **Plain**. 26 beats, matching the source's
beat count exactly. Carry-out carried over from the source's verdict beat
(CARRY-OUT.md, GATE C) — it was already a factual recap, not a design
judgment, so it needed no rewriting, only a register label change.*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Act | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer cold open | "Someone assumes they can just delete what they told an AI. Wrong question — there are four places, and only three let you take it back. So which one can't you undo?" | Writer types "I told an AI where I live. Can I delete it?"; "delete it" hesitates and corrects to "take it back" |
| B01 | THE-DETAIL | Start with the detail. One sentence, three facts: you have a partner, they hike, you live near Denver. Harmless on its own. Also enough to put you, roughly, on a map. | `ClaudeDescent` mode=detail, three facts |
| B02 | THE-DETAIL | Those three facts don't go to one place. They go to four, and the four are stacked. Each level is narrower than the one above it, because each level keeps less of what you said — and keeps it for longer. | `ClaudeDescent` mode=establish, four levels |
| B03 | THE-DETAIL | Anthropic's education team laid these four out and the taxonomy is correct — I'm borrowing it. What they don't draw is the axis that actually decides how careful you should be. | `ClaudeDescent` mode=establish, gates unresolved |
| B04 | THE-DETAIL | Not where does it go. Which of these can I walk back out of. Every level has a door. Three of them open both ways. | `ClaudeDescent` mode=establish, highlightGates |
| B05 | LEVEL-1-CONVERSATION | Level one is the conversation itself. While the window is open the model is working with your three facts. When the window closes, it isn't holding them anywhere, because it wasn't holding them anywhere else to begin with. | `ClaudeDescent` mode=level, activeLevel=0 |
| B06 | LEVEL-1-CONVERSATION | Open a fresh chat tomorrow and it starts blank. Not discreet — empty. On its own, the model has no idea your partner hikes, and no way to find out unless you tell it again. | `ClaudeDescent` mode=level, emptied |
| B07 | LEVEL-1-CONVERSATION | So the first door swings both ways. Close the tab and the detail is gone from the only place it was living. Level one costs you nothing. Almost everything you ever type stops here. | `ClaudeDescent` resolveGate=door-both |
| B08 | LEVEL-2-MEMORY | Level two is where the language gets loose. So let's ask for the mechanism instead of the marketing. | `ClaudeComposerAsk` — "the mechanism," |
| B09 | LEVEL-2-MEMORY | Here's what that phrase hides. The model did not remember you. A file on your account did — and that file gets read into the blank chat before you finish typing your first word. | `ClaudeMemoryReread` |
| B10 | LEVEL-2-MEMORY | That distinction isn't pedantry, it's the whole point. A memory you can open is a memory you can edit. In most products you can read the file, change a line, clear it, or switch the whole thing off. | `ClaudeDescent` mode=level, activeLevel=1 |
| B11 | LEVEL-2-MEMORY | Second door still swings both ways — but somebody set the latch before you got here. Depending on the product, memory is on by default or waiting to be switched on. That's a setting, and settings are checkable. | `ClaudeDescent` resolveGate=door-both-latch |
| B12 | LEVEL-3-PROVIDER | Level three isn't the model at all. It's the provider's own machinery — keeping the service up, reviewing for abuse, fixing bugs, research, and depending on the company, commercial uses too. | `ClaudeDescent` mode=level, activeLevel=2 |
| B13 | LEVEL-3-PROVIDER | Your three facts sit in that machinery for a retention period. And here is the part worth saying plainly: the period is real, it's usually written down, and it is not yours. | `ClaudeDescent` clock=true |
| B14 | LEVEL-3-PROVIDER | Third door still opens both ways — past a clock you don't wind. You can ask for deletion. You don't set the interval. | `ClaudeDescent` resolveGate=door-both-clock *(trimmed: source's "That's not sinister, it's operational" was a design-verdict clause, cut under Plain register)* |
| B15 | LEVEL-3-PROVIDER | But notice what changed. This is the first level where being in control stops meaning you can undo it, and starts meaning you can file a request and wait. | `ClaudeDescent` resolveGate=door-both-clock |
| B16 | LEVEL-4-TRAINING | Level four is training. Some providers use conversations to improve the next model. Personal details are generally stripped out first — generally, and that hedge belongs to them, not to me. | `ClaudeDescent` mode=level, activeLevel=3 |
| B17 | LEVEL-4-TRAINING | And then your sentence stops being a sentence. It becomes a very small adjustment to how likely certain words are to follow other words. Not a record of you. A pattern. | MANIM `B17_WordsBecomePattern` |
| B18 | LEVEL-4-TRAINING | That's offered as reassurance, and it is one — nobody can read your words back out. It's also the door that doesn't swing. You cannot un-train a model on a conversation it has already learned from. | `ClaudeDescent` resolveGate=arch-oneway |
| B19 | LEVEL-4-TRAINING | Where providers train on conversations, most let you opt out — and you should go find that toggle. But understand what it buys. It protects every conversation after you flip it. Not one before. | `ClaudeDescent` prospectiveOnly |
| B20 | WHAT-FOLLOWS | Four levels. Three doors that open both ways. One arch. | `ClaudeDescent` mode=pullback |
| B21 | WHAT-FOLLOWS | That gives you a rule to work from: price what you share against the least reversible place it could reach, not the most likely one. Most of what you type never leaves level one. Decide as though it might. | `ClaudeDescent` mode=pullback, emphasis=3 *(trimmed: source's "beats any blanket policy" comparison cut — a heuristic, kept; the comparative judgment, cut)* |
| B22 | WHAT-FOLLOWS | And the cheapest habit on the list costs you nothing. If the tool doesn't need the real name to do the job, don't give it the real name. Rewording an email works exactly as well with a placeholder in it. | `ClaudeDescent` mode=compare |
| **BVDT** | **6 CARRY-OUT** | Four places, and they are not the same kind of place. The conversation forgets when you close it. Memory is a file you can open and edit. Provider systems hold it on a clock you don't set. Training turns it into a pattern, and that one is permanent. Opt-outs are forward-looking. Everything else is a setting you can go check in about five minutes. | `ClaudeVerdictArtifact` — heading retitled "In short" (was "The verdict") |
| BHTF | your turn handoff | Your turn. Open the privacy and data settings for the AI tool you use most, and find four specific things: whether it keeps conversation history, whether it has a memory feature and whether it's on, what retention period it states, and whether training on your conversations is on or off. Then ask which of those four you could reverse tomorrow and which one you couldn't. That last clause is the whole exercise — you'll find the first three are toggles and the fourth is a date. | `ClaudeComposerAsk` — "Your turn." |
| BOUT | outro | Three you can take back. One you can't. Liam, in for Bear. | `OutroCTA` — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, `ai-explainer`) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Three You Can Take Back. One You Can't." | unchanged |
| Facts | four-level descent (conversation / product memory / provider systems / training), ranked by reversibility, not secrecy | unchanged |
| Beat count | 26 (B00–B22, BVDT, BHTF, BOUT) | 26 (same beat IDs) |
| B00 | `ClaudeComposerAsk` — puppet-free but still the Claude-composer cold open | `BrutalistHesitantWriter` (WRITER LAW) — "delete it" → "take it back" |
| Register | Teardown (metadata; narration itself was mostly factual) | Plain — two design-judgment clauses cut (B14, B21); see below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off (unchanged line) |
| BVDT heading | "The verdict" | "In short" — same recap lines, judgment-flavored heading word removed |
| Body B01–B22 | `ClaudeDescent` / `ClaudeMemoryReread` (Claude-fidelity REMOTION) | **unchanged component choice** — already valid REMOTION, not AI-video/pantry/human-drop, so NO-GENAI/NO-PANTRY LAW required no substitution; only `folderLabel` updated to `@HumanitariansAI` throughout |
| Your Turn prompt | privacy-settings audit prompt | unchanged verbatim |

**Known mixed-skin note:** `ClaudeDescent`, `ClaudeMemoryReread`, and
`ClaudeVerdictArtifact` are locked to the Claude fidelity token palette
(`#FAF9F5` cream / `#D97757` terracotta) — their prop schemas expose no
ink/accent/bg override (confirmed via `./art scenes --check`). Per PHASE 2's
instruction, only the cold open and the close carry the Humanitarians AI
skin; the body was already valid REMOTION under the source and is not one of
"the three things" this skill changes, so it stays as authored. The two
palettes (Claude cream/terracotta vs. humanitarians cream/crimson) read as
close cousins on screen, not a jarring cut. Logged here rather than silently
reworked.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B02; the level-2/3/4 mechanisms wait until their own acts |
| Wrong guess surfaced | B00 states it directly ("can I just delete it") and the whole descent falsifies the binary framing, level by level |
| No design judgment | B14 and B21 had the source's only two verdict-flavored clauses ("not sinister, it's operational"; "beats any blanket policy") — both cut; the rest of the source narration was already factual/mechanistic |
| Both directions | B18 (training is not reversible) vs. B19 (opt-out is real but forward-only only) |
| Carry-out survives retelling | BVDT — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not naming a specific product's retention period.** The reel says "usually
  written down," never a specific number of days — the source deliberately
  keeps this generic across providers.
- **Not asserting every provider trains on conversations.** B16/B19 both hedge
  with "some providers" / "where providers train" — training-on-conversations
  is not universal, and the reel doesn't claim it is.
- **No verdict on whether any provider's retention design is good policy.**
  Explaining the mechanism (a clock you don't set) is not the same as ruling
  on whether that's the right way to run a service — that would be Teardown's
  lane, and both cut clauses were exactly that kind of ruling.

## Handoff prompt (BHTF, read aloud)

> "Open the privacy and data settings for the AI tool I use most. Find four
> things: whether it keeps conversation history, whether it has a memory
> feature and whether it's on, what retention period it states, and whether
> training on my conversations is on or off. Then tell me which of those four
> I could reverse tomorrow and which one I couldn't."

Why it's worth running: it turns the reel's four-level model into an audit of
the viewer's own account, not just a description of Claude's.

---
**GATE P — signed:** ______________________  (human)
