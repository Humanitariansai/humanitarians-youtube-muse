# FACTCHECK.md — How to Use Claude

Checked 2026-10-03 against primary sources where they exist. Verdicts: PASS,
CORRECTED, EXEMPT (framing / craft advice / persona mechanics, no factual load).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Claude is a chat window in your browser; you type at the bottom, the answer appears above | PASS | claude.ai web app (first-hand product knowledge; Anthropic docs describe the chat interface) | — |
| 2 | B01 | A model is an AI program trained on a huge library of writing, so it can answer questions well | PASS | Plain-language paraphrase of LLM training on large text corpora (Anthropic research pages; standard field knowledge) | — |
| 3 | B02 | Using Claude with zero context yields generic answers | EXEMPT | Craft framing of the film's thesis; consistent with Anthropic's own prompting guidance to provide context | Labeled as the film's working model, not a measured result |
| 4 | B03 | More context → closer first draft, fewer revision rounds | EXEMPT | Practice guidance; Anthropic docs ("prompt engineering" guidance) advise giving Claude relevant context and examples | Kept as advice, no numbers attached |
| 5 | B04 | In Claude, open a Project for a piece of work; drop in style, constraints, an example; every chat inside inherits the context | PASS | Anthropic support: "What are projects?" — Projects hold custom instructions plus a knowledge base; every conversation in the project inherits that context. https://support.anthropic.com/en/articles/9517075-what-are-projects | — |
| 6 | B05 | Artifacts: when the answer should be a finished piece (document, chart, small program), Claude builds it in a panel beside the chat | PASS | Anthropic Artifacts: dedicated panel beside the conversation rendering documents, code, SVG, Mermaid, HTML. https://instapods.com/blog/what-are-claude-artifacts/ ; https://medium.com/@tuanhadev/what-are-claude-artifacts-and-how-do-i-use-them-090e0d3a2559 | — |
| 7 | B06 | Hand Claude something long and it maps the structure before you say what to change | EXEMPT | Observed capability claim, no numbers or guarantees; phrased as what to try, not what is guaranteed | — |
| 8 | B07 | Rough draft + a voice example → hits the tone on the first pass | EXEMPT | Practice claim, no numbers; "first pass" is the film's phrasing for "close on the first try" | — |
| 9 | B08 | When Claude doesn't know something, it can still answer confidently | PASS | Hallucination/confabulation in LLMs is well documented; Anthropic's own usage guidance advises verifying important outputs | — |
| 10 | B08 | On-screen example: "The Eiffel Tower is 330 metres tall." | PASS | 330 m including the 2022 DAB+ antenna (previously 324 m) — widely reported measurement | — |
| 11 | BHTF | The paste-in prompt makes Claude ask the viewer for needed context | EXEMPT | Instructional prompt, not a factual claim; behavior described is the intended use | — |
| 12 | BIDEA | Greeting "Hallo" is voiced cleanly by Kokoro am_onyx | PASS | show-tell skill notes: "Hallo" is in the clean-greetings list (2026-09-27); whisper-check at render | — |

## Notes

- No plan/price claims are made (no "free tier", no dollar figures), so nothing
  about Claude's 2026 plan lineup can go stale.
- The Sept 2026 Projects redesign added agentic features; the film describes
  only the stable core (custom instructions + knowledge base, inherited per
  chat), which the redesign keeps.
- "Model", "prompt", "context" definitions in BDEFS are simplified for a
  general audience; they are directionally correct, not technical definitions.
