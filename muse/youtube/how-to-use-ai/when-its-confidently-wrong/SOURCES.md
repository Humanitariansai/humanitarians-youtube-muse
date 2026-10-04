# SOURCES.md — When it's confidently wrong.

Fact → source table. Every checkable claim in the beat sheet traces to
one of these rows.

| # | Fact used in the film | Source |
|---|----------------------|--------|
| 1 | LLMs generate text by repeatedly predicting the next token from a probability distribution; sampling loop around "predict the next token" | https://github.com/oqxo/inference-engineering-handbook/blob/HEAD/Part-2-Inference/09-How-LLMs-Generate-Text.md |
| 2 | Autoregressive generation: model outputs token distribution, token sampled, appended to input, fed back; fluency and accuracy from the same process | https://github.com/ckvermaai/notes/blob/HEAD/advances-in-deep-learning/4.LLMs/4.2.Generation.md |
| 3 | LLMs systematically overconfident and escalate when challenged: 72.9% avg initial self-rated confidence vs 50% rational baseline, rising to 83%; 61.7% of debates with both sides ≥75% | https://marginalrevolution.com/marginalrevolution/2025/06/are-llms-overconfident-just-like-humans.html (summarizing the debate-calibration study) |
| 4 | The "calibration gap": disconnect between what LLMs know and what people think they know; LLMs don't automatically signal confidence; responses "can oftentimes appear confidently wrong" | https://news.uci.edu/2025/01/22/uc-irvine-study-finds-mismatch-between-human-perception-and-reliability-of-ai-assisted-language-tools/ |
| 5 | Benchmarks reward confident guessing over abstention; "like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty" | https://temperature2.com/p/2026-09-30-learning-what-is-an-ai-hallucination/ (summarizing Kalai et al.) |
| 6 | The Riverside Library exchange (March 2019 claim, archive page, 2021 sale, "it moved") | Authored illustrative dialogue for the film — not a real transcript |
| 7 | The four-step recovery playbook (restart; sources, checked; narrow; verify elsewhere) | The film's own advice (judgment), built from the mechanism in rows 1–2 |
| 8 | Film identity: channel claude-liam; persona "Liam, in for Bear"; Kokoro am_onyx; Teardown register; watermark @NikBearBrown | Bear's standing film-identity constants |
| 9 | Channel: humanitarians AI YouTube, https://www.youtube.com/@humanitariansai | Bear, 2026-10-03 (chat record) |
| 10 | Skill: ai-explainer (skill menu, bookend laws, Claude skin) | `~/workspace/brutalist.art/skills/make/ai-explainer/SKILL.md` |

The chat window, the gauges, the word chips, and all figures are drawn
in house style — no screenshots, no lifted images, no real product UI.
Searches run 2026-10-03; URLs verified live at that date.
