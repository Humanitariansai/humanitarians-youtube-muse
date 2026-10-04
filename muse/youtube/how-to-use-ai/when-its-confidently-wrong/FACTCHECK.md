# FACTCHECK.md — When it's confidently wrong.

Every claim in the script was checked before writing. Unverifiable claims
were cut; hedges ("often", "half the battle") are kept where the claim
is advice or a tendency rather than a measurement. No invented
statistics anywhere in the script.

## Verified (record)

1. LLMs generate text by repeatedly predicting the next token: the
   model outputs a probability distribution over possible next tokens,
   one is sampled, it is appended to the input, and the loop repeats.
   → [record] (oqxo/inference-engineering-handbook "How LLMs Generate
   Text"; ckvermaai deep-learning notes "LLM Generation")
2. The film's mechanism phrasing — "writes by picking the most likely
   next word, one after another" — matches the documented autoregressive
   next-token sampling mechanism. → [record] (same sources)
3. "No fact-checker inside, no honesty meter" is plain-language for: the
   generation loop has no separate truth-verification step; fluency and
   accuracy come from the same sampling process. → [record]
   (mechanism sources; failure-mode survey lists hallucination as
   "probabilistic generation without truth guarantee")
4. LLMs are systematically overconfident and tend to escalate confidence
   when challenged rather than revise: in 60 three-round policy debates,
   ten state-of-the-art models began at 72.9% average self-rated
   confidence (rational baseline 50%) and rose to 83% by the final round;
   61.7% of debates had both sides at ≥75%. → [record]
   (marginalrevolution.com, summarizing the debate-calibration study)
5. UC Irvine's Steyvers names the "calibration gap" — a disconnect
   between what LLMs know and what people think they know; LLMs do not
   automatically supply language indicating their level of confidence,
   and responses "can oftentimes appear confidently wrong." → [record]
   (news.uci.edu, 2025-01-22)
6. Benchmarks and training reward confident guessing over abstention:
   "like students facing hard exam questions, large language models
   sometimes guess when uncertain, producing plausible yet incorrect
   statements instead of admitting uncertainty"; binary scoring gives no
   credit for "I'm not sure," teaching confident guessing over honest
   hedging. → [record] (temperature2.com, summarizing Kalai et al.)
7. The narration hedges the double-down claim ("the most consistent
   reply to 'I was right' is 'I'm still right'") as a consequence of the
   continuation mechanism, not as a universal behavioral law — some
   models in some framings apologize and flip; the film's advice covers
   both by restarting rather than relying on the argument. → [record]
8. The Riverside Library exchange (the March 2019 claim, the archive
   page, the 2021 sale, the "it moved" resolution) is authored
   illustrative dialogue, not a real transcript — and is presented in
   the film as a staged example ("Picture this", "Watch the whole
   playbook in one pass"), never as a fact about a real library. →
   [record]

## Judgments (judgment)

- The four-step playbook (restart; ask for sources and check one;
  narrow the question; verify elsewhere) is the film's own recovery
  advice — standard, defensible practice, not research findings.
  [judgment]
- "Half the battle is won right here" is rhetorical, not a measured
  proportion. [judgment]
- "Knowing when to leave is a skill, not a defeat" is the film's
  thesis line, argued from the mechanism, not an empirical claim.
  [judgment]
- "Confidence is fluency, not knowledge" is the film's one-line
  framing of the mechanism — plain-language teaching, not a technical
  definition of model confidence. [judgment]
- The worked example's resolution ("the library never closed; it
  moved") is part of the staged illustration, not a claim about any
  real library. [judgment]

## Definitions (exempt — not factual claims)

- hallucination ("a confident wrong answer"), model ("the engine inside
  the AI"), double down ("when you challenge it and it insists it's
  right"), fluency ("how smoothly the words flow") — plain-language
  definitions authored for the film's general audience.

## Cut or disclosed

- No specific AI product is shown or recommended; the chat is a drawn
  window, never a screenshot of a real interface.
- No model version numbers, no dates that drift — the film names no
  model at all.
- The debate-study statistics appear in this file only, not in the
  script — the film itself carries no numbers that could date it.
- No claim that arguing never works; the film hedges the mechanism and
  the playbook covers the flip case by restarting.
