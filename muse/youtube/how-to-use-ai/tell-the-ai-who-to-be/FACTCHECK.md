# FACTCHECK — Tell the AI who to be

Checked 2026-10-03 against the refactor source (Anthropic Prompt Engineering
Interactive Tutorial, Lesson 03: Role Prompting, via the mirror-repo beat sheet
and description) plus general prompt-engineering references. No statistics,
quotations, or studies are claimed anywhere in this film — the one quantitative
idea ("four axes") is the tutorial's own framing, kept as such.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | A "role prompt" is a line at the start of a prompt like "act as a chef" that gives the AI a job to act as. | PASS | Anthropic prompt-engineering tutorial Lesson 03 (source lesson); standard industry usage. | — |
| 2 | B01–B03 | A role calibrates "register": vocabulary complexity, assumed reader knowledge, tone formality, explanation depth. | PASS | Source lesson's four-axis register framing; description.txt of the source folder. Kept as the tutorial's framing, not presented as a research finding. | — |
| 3 | B01 | The AI doesn't "become" the role or believe it; the role is an instruction that steers output style. | EXEMPT (interpretive framing) | Broadly accepted characterization of LLM role prompting; no factual claim about internals beyond "it steers the output". | — |
| 4 | B03 | Pediatric oncologist talking to a child vs pathologist at grand rounds give different answers to the same question. | EXEMPT (illustrative example from source) | Source lesson's own canonical example, kept verbatim in structure. Presented as a thought experiment ("the classic experiment"), not a measured result. | — |
| 5 | B04 | Role vs persona: "you are an expert tax attorney" (functional) vs "you are Marcus, a sardonic 1970s tax attorney who uses nautical metaphors" (character/voice). Both valid. | EXEMPT (illustrative example from source) | Source lesson's own role/persona pair, kept. Labeled in narration as tools, not findings. | — |
| 6 | B05 | Test: use a role when it changes what counts as a good answer; skip it for register-agnostic tasks (extracting a date, doing a sum). | PASS (heuristic, attributed) | Source lesson's decision rule, presented as a rule of thumb ("Use this test"), not a measured claim. | — |
| 7 | B06 | Specific roles with an audience beat vague ones ("genius"). | EXEMPT (craft advice) | Author's judgment; phrased as a tip, not a factual claim. | — |
| 8 | BHTF | The viewer exercise (ask one question under two roles and compare). | EXEMPT (exercise) | No claim made; the viewer generates the evidence themselves. | — |

No [VERIFY] items remain. No invented statistics, people, quotations, or
historical details. Kokoro-sensitive wording checked: "1970s" is spelled out
as "nineteen-seventies" in the narration; no acronyms or version numbers are
spoken.
