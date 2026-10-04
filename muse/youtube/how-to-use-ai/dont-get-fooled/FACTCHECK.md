# FACTCHECK.md — Don't get fooled.

Every checkable claim in the script was verified before writing. Statistics
were avoided on purpose: the source lesson's "near zero" rate claim is
carried as the lesson's own conclusion, not as a film statistic.

## Verified (record)

1. LLMs predict the most likely next word (next-token prediction); the
   mechanism is probability, not lookup or knowledge retrieval. →
   [record] (Anthropic Prompt Engineering Tutorial · Lesson 8, via the
   mirror repo's Lesson-08 sheet: "Claude predicts the most probable
   answer, which is not the correct one"; SOURCES 1)
2. Confidence and correctness are uncorrelated for ungrounded questions;
   "a confident hallucination looks identical to a confident correct
   answer." → [record] (Lesson-08 sheet B01/B02, verbatim from the source
   beat sheet; SOURCES 1)
3. Grounding's three parts: provide the source document in the prompt;
   instruct the model to answer only from that document; instruct it to
   say "I don't know" if the answer isn't in the source. The lesson's
   conclusion: this drops the hallucination rate to near zero for
   questions answerable from the source. → [record] (Lesson-08 sheet
   B02/YTV01; the film carries "near zero" as the lesson's conclusion,
   not as its own measurement; SOURCES 1)
4. Citations extend grounding to the output side: ask for the exact
   passage, verify it appears verbatim in the source; a citation not
   verbatim in the source is a hallucinated citation — a hallucination
   you can detect. → [record] (Lesson-08 sheet B03; SOURCES 1)
5. Mata v. Avianca, S.D.N.Y., 2023: attorney Steven Schwartz used ChatGPT
   to research a brief; the brief cited six fictitious cases (including
   "Varghese v. China Southern Airlines, 925 F.3d 1339 (11th Cir. 2019)");
   opposing counsel could not locate them; Judge P. Kevin Castel imposed
   $5,000 in sanctions on Schwartz, LoDuca, and Levidow, Levidow &
   Oberman, finding bad faith. → [record] (Reuters 2023-06-22; SOURCES
   2, 3)

## Judgments (judgment)

- "It's built that way" / "perfect-sounding was the whole target" — the
  film's plain-language framing of next-token prediction; a teaching
  paraphrase, not a quote from any paper. [judgment]
- "Habit zero" (the confident tone tells you nothing) is the film's own
  organizing label for the source's confidence/correctness claim. [judgment]
- "A reader can be checked. A memory cannot." is the film's aphorism for
  why grounding works; a rhetorical compression of the lesson. [judgment]
- "The AI fills gaps rather than admitting them" / "the guessing mostly
  stops" — the film hedges the lesson's "near zero" with "mostly";
  behavior varies by model and phrasing, and no universal rate is
  claimed. [judgment]
- "Brilliant first draft. It is not a witness." is the film's metaphor
  for the cross-check habit; rhetorical, not a technical claim. [judgment]

## Illustrative (disclosed — not factual claims)

- B03's "The treaty was signed in 1847." is a made-up example line,
  framed in the narration as "Listen" — no real treaty is named or
  implied.
- M08's "SAMPLE DOCUMENT" ("The meeting is on Tuesday.") and M09's claim
  ("The new policy starts Monday.") are generic illustrative lines, shown
  as samples, making no factual claim.
- M07's "Notes on cats" document carries only ghost lines (no readable
  claims); the Peru question is asked but never answered on screen.
- M03's "The capital of France is ___" uses a well-known answer purely
  to demonstrate the selection mechanism; the film makes no claim about
  France.

## Cut or disclosed

- No model version numbers, no benchmark figures, no "X% of answers are
  hallucinations" statistics — none were in the source, none were added.
- The film does not claim grounding eliminates hallucinations, only that
  it is the strongest habit the lesson teaches; "mostly" hedges the
  lesson's "near zero."
- The mislabeled base-folder beat sheet (lesson-07 content under the
  avoiding-hallucinations folder name) is documented in SOURCES.md and
  BUILD-LOG.md; nothing from it was used.
