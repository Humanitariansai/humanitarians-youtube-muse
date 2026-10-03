# Claude, Chronology — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet — see
QUESTION.md for the source-fidelity note: unlike sibling redos in this
family, this source's narration was genuinely written, not left as unfilled
placeholders). Register: **Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone building a case chronology assumes the job is just sorting every date the file mentions. It isn't — the real question is which dates actually weigh on the case, once duplicates are gone." | BrutalistHesitantWriter — types "Just sort\nevery date?", corrects "sort" → "weigh" |
| B01 | 1 stakes / 2 wrong guess | A legal matter draws its facts from a stack of documents — emails, invoices, deposition transcripts — each one mentioning dates on its own. Ask what happened, and the easy move is to pull every date out and lay them in order. But two different documents often describe the exact same event, on the exact same day, in different words — and a plain list of every mention counts it twice. | A sorted date list fed by three source chips (EMAIL / INVOICE / DEPOSITION); two cards land on the same day, worded differently, sitting side by side — visibly duplicated |
| B02 | 3 mechanism / **4 anchor planted** | Chronology building extracts every dated event from the declared sources, then collapses duplicates — however many documents name the same event, it becomes one entry. Watch one event: a late payment. An email flags it. An invoice restates it. A deposition describes it again, in different words, same day. | THE ANCHOR — three source cards (EMAIL / INVOICE / DEPOSITION), same date stamped on each, collapsing into one card: "LATE PAYMENT — ONE ENTRY" |
| B03 | **4 anchor payoff / 5 both directions** | One entry, not three — that part doesn't change. What does change is the tag on it: for a matter built on breach of contract, that payment is central, tagged high. For a different matter, built on a different theory, that same payment barely registers, tagged low. A low tag doesn't mean the event is wrong, or missing — it means this matter's theory doesn't turn on it. And one entry instead of three doesn't mean only one document mentioned it — it means every mention pointed at the same day. | THE ANCHOR RETURNS — the collapsed card splits into two tagged copies: "BREACH-OF-CONTRACT MATTER: HIGH" (terracotta) and "A DIFFERENT MATTER: LOW" (dimmed) |
| **BCRY** | **6 carry-out** | A chronology isn't every date in order — it's each event named once, no matter how many documents mention it, and weighed by what this case is trying to prove. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Paste in the documents your matter draws from — emails, invoices, transcripts, whatever's been produced. Then ask: pull every dated event, collapse anything that's really the same event into one entry, and flag which ones actually matter to how this case is argued. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Chronology. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the multi-document, mentions-dates-on-its-own fact; the extraction/dedup mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (sort every date); the B02→B03 anchor falsifies it directly — a plain sorted list prints the late payment three times, chronology building prints it once |
| Exactly one inference flag | none needed — the account states only what the source's own (genuinely written) description already asserts: extraction, de-dup, and significance-by-matter-theory; see QUESTION.md |
| One anchor, planted early, paid off late | B02 → B03 (a late-payment event named in three source documents, collapsed to one entry, tagged differently by two different matter theories) |
| Both directions | B03 — a low-significance tag isn't a wrong or missing event, it means this matter's theory doesn't turn on it; one entry instead of three doesn't mean only one document mentioned it, it means every mention pointed at the same day |
| No design judgment | B01–B03 state what chronology building does and why a plain date list can't answer the same question, never a verdict on any specific skill's or drafter's design choices |

## Deliberately not claimed

- **Not that every duplicate is obvious.** The reel doesn't claim de-dup is
  trivial or automatic in every case — it states the ordinary shape: the
  same event named across sources collapses to one entry.
- **Not a specific Claude product feature.** The account describes the
  generic mechanics the source's own description names (declared-source
  extraction, de-dup, matter-theory significance tagging), not any
  particular tool's UI or output format — see QUESTION.md.
- **No accusation that anyone drafted carelessly.** Reading only a plain
  sorted date list is presented as an ordinary, understandable shortcut,
  not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "Paste in the documents this matter draws from — emails, invoices,
> transcripts, whatever's been produced. Pull every dated event, collapse
> anything that's really the same event into one entry, and flag which
> ones actually matter to how this case is argued."

Why it's worth running: the exercise surfaces the same distinction the reel
is built around — a document that looks like a flat pile of dates turns
into a small set of events, each one weighed against what the case actually
needs to show.

---
**GATE P — signed:** register carried Teardown → Plain per QUESTION.md;
source facts genuinely written, so no reconstruction gap exists (unlike
sibling redos in this family).
