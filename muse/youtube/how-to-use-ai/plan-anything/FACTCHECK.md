# FACTCHECK.md — "Plan anything."

Claim-by-claim audit of `beat_sheet.json` narration. Verdicts: PASS
(supported), CORRECTED (fixed during build), EXEMPT (framing/opinion, not a
factual claim), FICTIONAL (the film's own demo material, clearly not a claim
about the world). The film deliberately carries no statistics, dates, version
numbers, or current prices, so no number in it can go stale.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | "Don't ask the machine to plan everything in one go" | EXEMPT | Advice/framing of the film's question; not an empirical claim. | — |
| 2 | BDEFS | constraint / draft / itinerary definitions | EXEMPT | Operational definitions coined for this film. | — |
| 3 | B00 | "It never gets tired of revising" | EXEMPT | Characterization of the tool's affordance (iteration is cheap); the four-step loop is the film's pedagogical construct, presented as such. | — |
| 4 | B01 | "two days, a hundred and fifty dollars of spending money" | FICTIONAL | The persona's demo constraint for the worked example, not a price claim. No assertion that any trip costs this; never presented as current. | — |
| 5 | B01 | "hiking, museums, cheap eats" | FICTIONAL | The persona's demo interests. | — |
| 6 | B02 | The draft itinerary contents (day one, day two, morning hike, lunch stop, evening museum) | FICTIONAL | Illustrative draft produced for the demo arc. | — |
| 7 | B03 | "The whole plan rewrites itself in seconds" | EXEMPT | Illustrative and qualitative; "seconds" describes the demo's pacing, not a benchmark. No timing claim made. | — |
| 8 | B04 | The checklist prescription (pack / book / day before) | EXEMPT | Practice prescription, not a factual claim. | — |
| 9 | B05 | "Planning a project? Same loop" (deadline, team, draft timeline, scope slip, launch checklist) | EXEMPT | The film's framework applied to a new domain; presented as the film's pattern, not a cited method. | — |
| 10 | B06 | "A budget is a plan for money, and it runs the same loop" | EXEMPT | Same; the "first split of every dollar" is the film's framing, not financial advice. No figures given. | — |
| 11 | B07 | "AI prices and opening hours come from memory, and memory goes stale" | PASS | Qualitative and well-supported: current Claude models document a reliable knowledge cutoff (e.g. end of Jun 2026 for the current Opus), past which they "can't answer reliably" and are instructed to note information "may be outdated" (published system prompts, e.g. simonw/claude-system-prompts, prompts/claude-opus.md, `<knowledge_cutoff>`). Kept qualitative — no cutoff date is quoted in the film, so nothing dates. | — |
| 12 | B07 | "Before you book anything, check it yourself" | EXEMPT | Normative rule (the film's boundary), not a factual claim. Mandated by the film brief. | — |
| 13 | BHTF | The Your-Turn prompt will produce a draft the viewer can revise | EXEMPT | Viewer exercise; no outcome claimed. | — |

## Notes

- No dated, versioned, or price claims remain; nothing for Kokoro to misread
  as a version number (no acronyms in narration besides "AI", which Kokoro
  voices correctly — still whisper-check at audio generation per the skill).
- The sample budget is deliberately spoken as the persona's own constraint
  ("a hundred and fifty dollars of spending money") and never as a fact about
  trip costs; per the brief, no specific current prices are asserted anywhere.
- Kokoro words flagged for the whisper check at render: "day-by-day",
  "double-check", "one hundred fifty dollars".
