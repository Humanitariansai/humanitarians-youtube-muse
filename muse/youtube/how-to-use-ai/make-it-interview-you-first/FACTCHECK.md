# FACTCHECK.md — Make It Interview You First

Checked 2026-10-03. This is an advice film, not a reporting film: claims are
kept modest, behavioral, and explicitly framed as craft guidance. Verdicts:
PASS, CORRECTED, EXEMPT (framing / craft advice / persona mechanics, no
factual load).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Typing a one-line request ("plan my trip") into Claude returns a generic, thin answer | EXEMPT | Craft framing of the film's thesis (a vague brief yields a vague answer); consistent with Anthropic's prompting guidance to provide context | Labeled as the film's working model, not a measured result |
| 2 | B01 | Telling Claude "ask me 5 questions first" makes it ask clarifying questions before starting | PASS | Observed, reproducible Claude behavior: an explicit instruction to ask clarifying questions before starting is followed in the Claude.ai chat interface | Kept modest: "stops guessing and starts asking" is what the instruction does |
| 3 | B02 | The five questions (budget, dates, who, pace, must-see) are things Claude would otherwise have to guess | EXEMPT | Original worked example; the claim is definitional (these details aren't in the one-line ask, so they must come from guessing or asking) | — |
| 4 | B03 | Answering takes about thirty seconds and builds the brief | EXEMPT | Practice estimate for five short answers; "thirty seconds" is illustrative pacing, not a measured figure | — |
| 5 | B04 | With the brief, the plan reflects the answers (slow mornings, free sights, fish market day two) | EXEMPT | Stated as what the technique is for, not a guaranteed outcome; no quality numbers attached | — |
| 6 | B05 | For a difficult email, three questions (who, what went wrong, tone) aim the draft | EXEMPT | Second worked example; consistent with the film's thesis | — |
| 7 | B06 | Questions that wouldn't change the answer cost time; ask for answer-changing questions | EXEMPT | Craft advice; the Your-Turn check ("did every answer change something") makes it self-testing | — |
| 8 | B07 | Skip the interview for plain facts ("what time is it in Tokyo") | EXEMPT | Judgment guidance, framed as a rule of thumb | — |
| 9 | BHTF | The paste-in prompt (up to five questions, one at a time, waiting for each reply) makes Claude interview the viewer | EXEMPT | Instructional prompt, not a factual claim; behavior described is the intended use | — |
| 10 | BIDEA | Greeting "Hallo" is voiced cleanly by Kokoro am_onyx | PASS | show-tell skill notes: "Hallo" is in the clean-greetings list (2026-09-27); whisper-check at render | — |

## Notes

- No statistics are cited anywhere in the film — deliberately. This is
  technique advice; attaching numbers would be invented precision.
- The interview questions and trip answers are an original worked example
  (Tokyo trip: tight budget, November, two adults and a kid, slow pace, the
  fish market), not a transcript of a real session.
- No plan/price/product claims are made, so nothing about Claude's 2026
  lineup can go stale.
- "Prompt", "interview", "brief" definitions in BDEFS are simplified for a
  general audience; they are directionally correct, not technical definitions.
