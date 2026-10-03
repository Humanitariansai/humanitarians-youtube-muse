# Claude, Finding It — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-cowork-plugins/claude-liam-enterprise-search`).*
*Register: **Plain**. 8 beats. Source was a 36-beat, ~330s deep-explainer
(register: Teardown) covering six acts — the buried answer, content vs.
filename, context injection, five workflows, access boundaries, and habits.
Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude would search everywhere in the company. It only reaches what you can already open. So — can Claude find what your company already wrote down, using just your own access?" | Writer types "My company already wrote this down. Can Claude search everywhere for it?"; "everywhere" hesitates and corrects to "only what I can see" |
| B01 | 1 stakes / 2 wrong guess — ANCHOR PLANTED | In any company that's been running a while, the answer already exists — it's in a colleague's doc, a slide deck, a chat thread. You just can't reach it. So the natural next thought is: I already searched, it isn't there. But normal search only matches the file's name, not what's inside it. Call a document "Q3 notes" when it actually holds the reason you switched payment processors, and searching "payment processor" finds nothing — the name and the content have nothing to do with each other. | THE ANCHOR — a file labeled "Q3 notes" sits dark; the query "payment processor" sweeps every filename and misses by a mile |
| B02 | 3 mechanism | Enterprise search fixes exactly that: it reads the words inside your documents, not the label on the folder. It searches your drive, your wiki, your shared folders, and your chat all at once, so you don't have to remember where you put something — only roughly what it was about. And you just ask, in plain language, the way you'd ask a person: no boolean operators, no query syntax. | the same "Q3 notes" file opens; the query lands on a sentence deep inside it; several source streams flow into one simultaneous search |
| B03 | 3 mechanism | It goes one step further than finding the file — it can pull that content straight into the conversation. Ask "how did we decide on Stripe over PayPal, and why," and if anyone wrote that down, even casually in a meeting note, Claude retrieves the actual reasoning and answers from it. That's the difference between generic advice and grounded advice: without it, Claude reasons from best practices; with it, Claude reasons from your own decisions. | a found document slides into an active conversation and becomes part of the context; two answer-arrows — one generic, drifting wide, one grounded, landing on target |
| B04 | 5 both directions — ANCHOR PAYOFF | Here's the part to be clear about. It searches only what you can already see — your own credentials, your own permissions, nothing new. So finding that Q3-notes file doesn't mean Claude reached anywhere new; you could always have opened it yourself. And not finding something doesn't mean it isn't written down somewhere — it might just not be connected or indexed yet. Which is also why it does nothing until you point it at your sources; the first index takes a while, and after that, searches are fast. | THE ANCHOR RETURNS — the same "Q3 notes" file, now inside a boundary ring labeled "your existing access"; the search wavefront stops hard at the ring |
| **BCRY** | **6 carry-out** | Enterprise search doesn't give Claude new access — it gives you faster reach over what you can already see, because it reads what's actually written, not just what it's named. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Help me set up enterprise search for my team. First, ask me which tools our documents actually live in — drive, wiki, shared folders, chat. Then tell me the three questions I should try first to prove it works, and one decision I should start documenting this week so it's searchable later. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Finding It. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`books`/`claude-cowork-plugins`, Teardown metadata) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "My company already wrote this down somewhere. Can Claude just find it?" (B00 cold-open command) | unchanged |
| Facts | buried answer; filename vs. content ("Q3 notes" / payment processor); reads content across drive/wiki/folders/chat at once; pulls content into context (Stripe/PayPal example); five workflows (memory, client context, policy, meeting prep, no-contradictions); bounded strictly by existing access; connect-then-index; habits compound | unchanged |
| Beat count | 36 beats across 6 acts (COLD OPEN + 6× SegmentCard/act pairs + verdict + Your Turn + outro, plus 3 unfilled BOOKEND slates BVDT/BHTF/BOUT) | 8 (B00 writer + 4 body + BCRY + BHTF + BOUT) — the six acts compressed to one idea per body beat: buried-answer+wrong-guess (Act I+II), mechanism/reads-content (Act II), grounded-not-generic (Act III), bounded-access+both-directions (Act V). Acts IV (five workflows) and VI (habits) are referenced in the carry-out and Your Turn rather than given their own beats, to fit the Plain-register 2–3 minute runtime. |
| B00 | `ClaudeComposerAsk` cold open stating the answer directly ("Yes — across every source you've connected, bounded strictly by your own access"), no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — reframed to state the wrong guess the body falsifies: assuming "search everywhere" means beyond your own access |
| Register | Teardown (metadata `register: "Teardown"`) | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | source H01's team-setup prompt | same prompt, carried to BHTF near-verbatim |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot for the
content this reel keeps — B03/B05/B09/B13/B14/B17/B20/B23 used
`pantry_note`/doodle stills in the source's fuller cut, but none of that
illustrative padding is load-bearing for the compressed argument, so it is
dropped rather than substituted; every beat this reel keeps was already a
GRAPHIC (Manim) or REMOTION shape in the source (NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00, covered by WRITER LAW anyway).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B02 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (already searched, it's not there / search reaches everywhere); B01's anchor is the falsifying case (filename "Q3 notes" hides a payment-processor decision from a filename search) |
| One anchor, planted early, paid off late | B01 plants the Q3-notes/payment-processor document; B04 pays it off (the same document, now shown inside the access boundary) |
| Both directions | B04 — a hit doesn't mean Claude reached somewhere new (you could always have opened it); a miss doesn't mean the fact isn't written down anywhere (it might not be connected/indexed yet) |
| No design judgment | B02–B03 describe why the mechanism works; nothing rules on whether enterprise search is the right tool to adopt |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not "everywhere."** Only sources you've connected, and only content you
  could already open yourself (B04's both-directions clause).
- **Not instant.** First-time indexing takes a while; after that, searches
  are fast (B04).
- **Not a substitute for documenting.** The payoff compounds only if
  decisions get written down as they're made (referenced in the Your Turn
  handoff).

## Handoff prompt (BHTF, read aloud)

> "Help me set up enterprise search for my team. First, ask me which tools
> our documents actually live in — drive, wiki, shared folders, chat. Then
> tell me the three questions I should try first to prove it works, and one
> decision I should start documenting this week so it's searchable later."

Why it's worth running: it turns the reel's explanation into an actual setup
plan for the viewer's own sources, and forces the concrete first step —
naming where the documents already live — that most people skip.

---
**GATE P — signed:** ______________________  (human)
