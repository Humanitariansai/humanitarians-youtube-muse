# FACTCHECK.md — "Video clips for free"

Build-time verification: 2026-10-05. Free-tier numbers churn, so the film
itself never hard-codes the quota — it points viewers at vids.new. The
numbers below are the *build-time* record (what the research found), used
only in SOURCES.md and this file, not in the narration.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Google Vids is a video app that opens at vids.new | PASS | gHacks (2026-04-07): "The feature is now available through Google Vids at vids.new" | — |
| 2 | B00 | Vids gained an AI clip maker ("earlier this year") that turns a sentence into a short HD video clip | PASS | WinBuzzer (2026-04-02/03): Vids update went live April 2, 2026, adding Veo 3.1 generation inside Vids | — |
| 3 | B00/BDEFS | Veo is the AI model that turns text into video clips | PASS | Multiple: Veo 3.1 integrated in Vids (WinBuzzer, gHacks, rehandream) | — |
| 4 | B02 | Personal Google accounts get a free monthly allowance of AI video clips | PASS | WinBuzzer, gHacks, toolworthy, awesomeagents, seedancev2ai, blueheadline: 10 free generations/month | In-film: hedged to "a free monthly allowance" with the current number at vids.new (see #9) |
| 5 | B02 | The allowance refills each month | PASS | seedancev2ai: "reset automatically every 30 days" (TechRadar via seedancev2ai); gadgethacks: "resetting at 12 a.m. PT on the first day of each month" | In-film: "refills each month" (the two sources differ on the exact reset rule; the film doesn't pick one) |
| 6 | B01 | Clips are short (a few seconds), 1080p | PASS | seedancev2ai: "10 free video generations per month at 1080p resolution"; toolworthy FAQ: "Individual Veo 3.1 AI-generated clips are limited to 8 seconds each" | In-film: "a few seconds long, in high definition" — no hard numbers on screen |
| 7 | B06 | Clips can be extended (scene extension) | PASS | android.gadgethacks (2026-06-17 rollout): Vids added "longer Veo clips" and scene extension | — |
| 8 | B06 | Multiple prompts can be generated in parallel; each generation spends the budget | PASS | android.gadgethacks: parallel generation; "Monthly generation limits still shape how useful the feature [is]" | — |
| 9 | B08 | The free number has changed / is not promised to stay | PASS | gHacks: "Google has not clarified whether the 10 free generations per month will stay as a permanent free tier or if this policy might change"; toolworthy FAQ: "What happens to the free AI features after May 2026?" | In-film: no quota number anywhere; "check vids.new" is the standing instruction |
| 10 | B07 | Custom AI music and AI avatars are the paid extras, not part of the free clip allowance | PASS | toolworthy FAQ: "For higher limits and advanced AI features like custom music and customizable avatars, you need a Google Workspace plan or Google AI Pro"; WinBuzzer: Lyria 3 music + avatars in the same April update | In-film: "need a paid plan" — no prices quoted (standing rule) |
| 11 | B04/B07 | Vids ships with free stock footage and free stock music; basic editing is free | PASS | rehandream guide: Vids "select[s] matching stock footage"; toolworthy FAQ: "Basic video editing, collaboration, and sharing features are available for free" | — |
| 12 | B03 | AI video wins on shots you can't film or find in stock | EXEMPT (judgment) | Decision-framework guidance, not a factual claim; examples are illustrative | — |
| 13 | BHTF | — | EXEMPT | Viewer exercise; no factual claims | — |

No percentages, no pricing tiers, and no hard quota numbers appear in the
narration or on screen (checked by inspection of `beat_sheet.json`).
