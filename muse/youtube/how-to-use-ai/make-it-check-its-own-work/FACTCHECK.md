# FACTCHECK.md — "Make It Check Its Own Work."

Checked 2026-10-03. Rule: no invented statistics, modest claims only.
"Self-critique reduces errors" is argued, never quantified.

| # | Claim (as the film states it) | Verdict | Basis |
|---|---|---|---|
| 1 | Asking an AI to review its own output is a documented prompting technique. | CONFIRMED | Anthropic's prompt-engineering guidance recommends a self-check ("Before you finish, verify your answer against [test criteria]"), described as catching errors reliably, especially for coding and math. Google's prompting strategies likewise document self-critique ("prompt models to review outputs against original constraints"). See SOURCES.md. [record] |
| 2 | "What's wrong with this?", "What did you assume?", "strongest objection" are standard forms of the move. | CONFIRMED | "Critique your own response" and "What are the potential flaws in this reasoning?" appear as documented power phrases in prompt-engineering guides; "steelman the opposing argument" (strongest-counterargument form) is likewise documented. See SOURCES.md. [record] |
| 3 | The demo: "which months have 28 days?" — the complete answer is all twelve. | CONFIRMED | February has 28 days (29 in leap years); every other month has 30 or 31 — so every month has at least 28 days. The film presents it as a riddle the first pass gets wrong, not as a novel finding. [record] |
| 4 | Self-critique reduces errors but does not eliminate them. | JUDGMENT, consistent with sources | The guides recommend the technique without guaranteeing correctness; the film states it as a reasoned caution (same model, same blind spots), not a measured rate. No percentage is claimed anywhere. [judgment] |
| 5 | A model can "fix" things that weren't broken during a critique pass. | JUDGMENT, consistent with sources | Over-eager revision is a known failure mode of critique loops (prompt-engineering notes warn that unfocused "make it better" prompts produce churn); the film shows it as a caution, not a measured frequency. [judgment] |
| 6 | Yes/no self-checks ("is this right?") are weaker than flaw-hunting prompts. | JUDGMENT, consistent with sources | Guides stress that vague prompts ("make it better") underperform specific ones (a concrete role and goal per revision); the film extends this to "is this right?" vs "what's wrong?" as practical advice, not a lab result. [judgment] |
| 7 | No accuracy-improvement statistic is stated. | CONFIRMED BY INSPECTION | The narration and on-screen text contain no percentages, multipliers, or study citations. [record] |
| 8 | Newest models with always-on reasoning may need less explicit self-checking. | CONTEXT, not in the film | Anthropic's Opus 5 guidance notes the model already verifies its own work and that carried-over verification instructions can add tokens/latency. Left out of the film — a general-audience how-to doesn't need the model-version nuance, and the film's claim stays true for the chatbots viewers actually use. [judgment] |

Date-sensitivity: none of the claims depend on a model version, a date, or
a drifting count. The technique is interface-agnostic (works in Claude,
ChatGPT, Gemini, and others — the film names none in the technique beats).
