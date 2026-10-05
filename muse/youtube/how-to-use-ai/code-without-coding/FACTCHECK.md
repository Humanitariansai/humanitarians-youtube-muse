# FACTCHECK — Code without coding

Checked 2026-10-04 against the sources in SOURCES.md. One quantitative claim
(the Y Combinator figure) — attributed aloud in the narration ("Y
Combinator … says") and captioned on screen ("per Y Combinator"), per the
show-tell thin-numbers law. No other statistics, quotations, or studies are
claimed; the three mistakes and the two safety rules are craft guidance,
phrased as rules of thumb, not findings.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BDEFS | "code: the written instructions a computer follows" | PASS | Standard definition; matches common references (e.g. MDN "code" glosses, Codecademy). Simplified for a general audience, not a contested claim. | — |
| 2 | BDEFS/B01 | An AI coding tool takes a plain-language description and writes the code. | PASS | Observable product behavior of Claude Code, Claude's coding features, and peers (public docs and demos, 2025–2026). Described generically, no product-specific feature asserted. | — |
| 3 | BDEFS | "bug: a mistake in the code that makes it do the wrong thing — or nothing at all" | PASS | Standard definition, simplified. | — |
| 4 | B08 | A quarter of Y Combinator's Winter 2025 batch shipped products on codebases that were 95% AI-written. | PASS (attributed) | TechCrunch, Mar 2025, reporting YC managing partner Jared Friedman and CEO Garry Tan in the YC YouTube video "Vibe Coding is the Future". Spoken aloud as "Y Combinator … says" and captioned "per Y Combinator". | — |
| 5 | B08 | Y Combinator is "the startup school behind Airbnb and Stripe". | PASS | Both are YC alumni — widely documented (YC's own site, company histories). | — |
| 6 | B02 | Safe first builds: things you can check by looking (a page, a quiz, a tracker). | EXEMPT (craft guidance) | Author's judgment, phrased as a safety rule, not a factual claim. | — |
| 7 | B03 | Keep first builds personal; passwords/payments/other people's data are not a first project. | EXEMPT (craft guidance) | Standard security posture; matches Anthropic's guidance not to put sensitive information in prompts (see SOURCES.md). Phrased as a rule of thumb. | — |
| 8 | B04 | "thousands of lines you can't check" | EXEMPT (rhetorical, not a stat) | Deliberately non-numeric ("thousands", not a figure); illustrates the failure mode, not a measured claim. | — |
| 9 | B05 | Never paste passwords, keys, or private info into an AI; once it's in, you can't take it back. | PASS (guidance, sourced) | Anthropic's Privacy Policy / consumer terms advise against sharing sensitive information in prompts; prompts may be used for safety/training per policy. The "can't take it back" phrasing reflects that submitted content leaves the user's control. | — |
| 10 | B06 | Always click every button yourself; if you can't check it, don't ship it. | EXEMPT (craft guidance) | Author's judgment; the YC partners themselves stress judgment over blind trust (Diana Hu: "to do good vibe coding, you need taste and knowledge to decide what's good and bad" — same video). | — |
| 11 | B07 | When it breaks, describe the problem back to the tool in plain words; it fixes the code. | PASS (product behavior) | Standard iterative behavior of AI coding tools (describe → regenerate/fix), described generically. | — |
| 12 | BHTF | The viewer exercise (build one small page; two self-checks). | EXEMPT (exercise) | No claim made; the viewer generates the evidence themselves. | — |

No [VERIFY] items remain. No invented statistics, people, quotations, or
historical details. Kokoro-sensitive wording checked: "twenty twenty-five"
and "ninety-five percent" are spelled out; no acronyms or version numbers are
spoken; "AI" is voiced correctly per the skill's whisper-check guidance.
