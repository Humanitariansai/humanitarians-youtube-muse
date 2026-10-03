# Migrating to Opus 4.5 — Narration Script (redo, GATE P)

*Skill: `hai-simple`. Register: **Plain**. 14 beats ≈ 2:50.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion), Kokoro `am_onyx`. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asked how to upgrade their code to Opus 4.5. Not upgrade — migrate: the string changes, but nothing about how Claude behaves gets touched unless you ask. So — how do you migrate to Opus 4.5?" | writer types "upgrade", corrects to "migrate" |
| NB01 | 1 stakes | Say your code calls Claude on Sonnet 4.0, Sonnet 4.5, or Opus 4.1, and it's time to move it to Opus 4.5. | chips: SONNET 4.0 · SONNET 4.5 · OPUS 4.1 → OPUS 4.5 |
| NB02 | 2 wrong guess | The natural guess: migrating swaps the model string and quietly smooths over anything that behaves differently on the new one. | chips: NEW MODEL STRING → SMOOTHED-OVER BEHAVIOR |
| NB03 | **2 break it** | It doesn't. The skill touches exactly four things — a model string, a beta header, one parameter, and a summary — and not one word of your prompts. | chips: MODEL STRING · BETA HEADER · EFFORT PARAM · A SUMMARY |
| NB04 | **3 mechanism / anchor planted** | Take the line that calls the model. Right now it names Sonnet 4.5, and it's carrying a header for a beta context window. | THE ANCHOR — code card, before |
| NB05 | 3 mechanism | The skill searches your whole codebase for calls like it first, then updates every one it finds — using the right string for whichever platform you're on: Anthropic's own API, AWS Bedrock, Google Vertex AI, or Azure AI Foundry. | chips: ANTHROPIC API · AWS BEDROCK · GOOGLE VERTEX · AZURE AI FOUNDRY |
| NB06 | 3 mechanism | Along the way it drops that beta header if the new model doesn't support it yet, and sets an effort parameter to high. | chips: REMOVE BETA HEADER → SET EFFORT: HIGH |
| NB07 | 3 mechanism | One model never moves in this pass: Haiku. Sonnet and Opus calls migrate; Haiku calls stay exactly as they are. | chips: SONNET → MIGRATES · OPUS → MIGRATES · HAIKU → UNTOUCHED |
| NB08 | **4 anchor payoff** | Back to that same line: it now names Opus 4.5, the beta header is gone, and effort is set to high — one call, four small edits, nothing else touched. | THE ANCHOR RETURNS — code card, after, same frame as NB04 |
| NB09 | **5 direction A** | If your code only ever called Sonnet or Opus, that's the whole job: it searches, swaps, and tells you exactly what it changed. | chips: SEARCH → SWAP → SUMMARIZE |
| NB10 | **5 direction B** | But if Opus 4.5 actually behaves differently once it's running — say it starts firing tools too eagerly — the skill won't touch your prompt for that on its own. Report the specific behavior, and only then does it make a targeted adjustment. | chips: BEHAVIOR CHANGES → YOU REPORT IT → THEN IT ADJUSTS |
| **BCRY** | **6 carry-out** | Migrating to Opus 4.5 only touches the model string, a header, and one parameter — it never changes your prompts unless you ask it to. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Open Claude Code in a project that calls a Claude Sonnet or Opus model, and paste this: Search this codebase for Claude model strings and migrate them to Opus 4.5 — Anthropic API, AWS Bedrock, Google Vertex AI, or Azure AI Foundry, whichever you use. Remove any one-million-token-context beta header you find, add an effort parameter, and summarize every change. Watch two things: does it leave every Haiku string untouched, and does it change so much as one word of your prompts without asking first? | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Migrating to Opus 4.5. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | NB01; mechanism waits until NB04 |
| Wrong guess surfaced *and falsified by a case* | NB02 states the read (migration also smooths over behavior); NB03 breaks it with the closed, concrete list of exactly four things the skill touches |
| Inference flag | N/A — this reel describes a defined skill's documented behavior throughout, not an inference from evidence; nothing here is a leap requiring a flag |
| One anchor, planted early, paid off late | NB04 → NB08 (the same model-call line, before and after migration) |
| Both failure directions | NB09 (clean case: only Sonnet/Opus strings, done in one pass) and NB10 (behavior differs post-migration: opt-in only, never fixed by default) |
| No design judgment | Facts are stated as the skill's documented scope and behavior, never ranked as well- or poorly-designed — the source's Teardown "gaps" section (Azure source table incomplete, vague triggers, no rollback guidance) is dropped entirely, per WRITER LAW/redo register rule |

## Beat-count note (redo)

Source (`claude-liam-claude-opus-4-5-migration`, Teardown) ran 7 beats: B00
(`ClaudeComposerAsk` cold open) + B01 (platform matrix + six-step workflow,
one long beat) + B02 (five behavioral-adjustment triggers, one long beat) +
B05 (teardown "gets right" / "bites" verdict) + BVDT (verdict artifact) +
BHTF (handoff) + BOUT (outro). Facts carried over unchanged: the four target
platforms and their exact model strings, the three source models (Sonnet
4.0, Sonnet 4.5, Opus 4.1), the explicit Haiku exclusion, the six-step
workflow (search → update strings → remove beta header → add effort → summarize
→ offer to help with prompt adjustments), the beta header name
(`context-1m-2025-08-07`), the opt-in-only discipline for prompt adjustments,
and the tool-overtriggering example used to illustrate a behavioral
difference.

Per hai-simple's one-idea-per-beat rule, B01 and B02's two dense multi-fact
beats were split into 10 single-idea Plain beats (NB01–NB10), and B05/BVDT's
Teardown verdict (what the skill "gets right" vs. "where it bites") was
dropped entirely and replaced by this register's own required shape: a
wrong-guess beat (NB02) broken by a case (NB03), one anchor planted and paid
off (NB04/NB08), and a both-directions pair (NB09/NB10) built from the
source's own opt-in-only rule rather than a design verdict. The five
behavioral-adjustment triggers (tool overtriggering, over-engineering, code
exploration, frontend design, thinking sensitivity) are represented by their
governing rule — opt-in only, apply if reported — at NB10, rather than
listed individually; naming all five as a bullet list would read as Teardown
inventory, not Plain mechanism. Net: 14 beats total (B00 + 10 body +
BCRY/BHTF/BOUT), the full body argument preserved, no fact dropped, judgment
removed.

## Deliberately not claimed

- **No source-string table for Azure AI Foundry.** The source's platform
  matrix pairs Azure with a target string but no corresponding source
  strings to replace (a gap the source's own Teardown flagged). NB05 lists
  Azure among the four platforms without asserting it has a source table —
  consistent with the source data, not a new claim.
- **No specific reproduction detail for "tool overtriggering."** The source
  calls the behavioral triggers "vague and not reproducible without
  testing." NB10 names the trigger as an illustrative example ("fires tools
  too eagerly") without claiming a precise, checkable symptom.
- **No claim that migration is risk-free.** The source notes there's no
  rollback guidance; this reel doesn't claim otherwise — it simply never
  raises rollback, staying inside what it does claim (the four things
  touched).

## Handoff prompt (BHTF, read aloud)

> "Search this codebase for Claude model strings and migrate them to Opus
> 4.5 — Anthropic API, AWS Bedrock, Google Vertex AI, or Azure AI Foundry,
> whichever you use. Remove any one-million-token-context beta header you
> find, add an effort parameter, and summarize every change."

Why it's worth running: it's the exact one-shot job the skill claims to do,
on the viewer's own codebase, with two concrete things to watch for — Haiku
strings left alone, and no unrequested prompt changes.

---
**GATE P — signed:** ______________________  (human — N/A, unattended redo build)
