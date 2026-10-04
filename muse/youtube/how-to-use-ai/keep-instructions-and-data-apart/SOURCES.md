# SOURCES.md — Keep instructions and data apart

## Refactor source (mirror repo, read-only)
- `nikbearbrown/humanitarians-youtube-muse`
  `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-04-separating-data/`
  (beat_sheet.json, README.md, description.txt, scenes.py).
  This is the closest match to the assigned base-name path
  `claude/claude-for-education/prompt-tutorial-lesson-04-separating-data`,
  which 404s on the Contents API (the folder exists only with the
  `claude-liam-` prefix). The source supplied the argument and facts —
  instructions vs data, the injected "ignore previous instructions" line,
  XML tags as hard separators, indexed document tags, consistency over tag
  names — not the script, which was rewritten for a general audience.

## Independent verification (web, 2026-10-03)
- Anthropic prompt-engineering tutorial, Chapter 4 "Separating Data from
  Instructions": XML tags are the recommended way to separate data from
  instructions; Claude was trained to recognize XML tags; no "magic" tag
  names; consistency of tag names. Verified via multiple independent
  summaries of the official tutorial, e.g.
  https://github.com/rexleimo/rex-skills/blob/HEAD/anthropic-1p-prompt-optimizer/references/anthropic-1p-cheatsheet.md
  and
  https://github.com/ilyaivanchikov/mendbot/blob/HEAD/docs/prompt-engineering-best-practices.md
- OWASP Top 10 for LLM Applications: prompt injection ranked LLM01 in the
  2025 edition and held at LLM01 in the August 2026 refresh.
  https://www.infosecurity-magazine.com/news-features/owasp-top-10-llm-means-future-ai/
  and https://hackerdna.com/blog/owasp-llm-top-10
- Mechanism gloss ("same channel" for instructions and data):
  https://temperature2.com/p/2026-09-24-did-you-know-indirect-prompt-injection/

## Assets
- No third-party images, footage, or audio used. All visuals are authored
  Manim fragments (`scenes.py`) and Remotion patterns (`ClaudeComposerAsk`,
  `BrutalistHesitantWriter`, `ClaudeTitleOutro`) in the Claude fidelity
  palette. Logo bug: channel handle `@NikBearBrown` rendered as a wordmark
  (no logo file required).
