# FACTCHECK.md — "Claude, On the Job."

Claim-by-claim audit of `beat_sheet.json` narration. Verdicts: PASS
(supported), CORRECTED (fixed during build), EXEMPT (framing/opinion, not a
factual claim). The film deliberately carries no hard statistics, dates, or
version numbers, so every remaining claim is qualitative.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | "Everyone asks whether AI will take their job" | EXEMPT | Rhetorical framing of the film's question; not a survey claim. | — |
| 2 | BDEFS | "A hallucination: a confident made-up answer that sounds right and isn't" | PASS | Ji, Lee, Frieske et al., "Survey of Hallucination in Natural Language Generation," *ACM Computing Surveys* 55(12), Art. 248, 2023 — "generated content that is nonsensical or unfaithful to the provided source content." DOI 10.1145/3571730. | — |
| 3 | BDEFS | "An audit: reading the output line by line before you sign off" | EXEMPT | Operational definition coined for this film. | — |
| 4 | B00 | "a four-tier map of work. The machine owns the bottom. You own the top." | PASS (framing) | The four-tier framework is the source series' own pedagogical construct (see source PEDAGOGY.md: "a pedagogical construct, not a citation"). Presented as the film's map, not a cited theory. | — |
| 5 | B01 | "Tier one is recall: facts, syntax, finding things. The machine is superhuman here, right now." | PASS | Consensus across model evaluations 2024–2026 (source PEDAGOGY.md evidence table); "superhuman" is interpretive but uncontested for recall/retrieval-style tasks. Kept qualitative — no benchmark cited, none implied. | — |
| 6 | B01 | "No one memorizes or searches faster than it." | PASS | Rhetorical; consistent with the consensus in #5. No literal timing claim. | — |
| 7 | B02 | "Tier two is synthesis: drafts, summaries, spotting patterns... contested space" | PASS (framing) | Interpretive mapping onto the series' tier construct; "contested" is the film's characterization. | — |
| 8 | B03 | "Only a person knows what matters here" (re: whether output is right, good, serves the goal) | PASS (interpretive) | Consistent with human-factors literature on evaluation and judgment as human-advantage tasks; framed as the film's argument, not an empirical result. | — |
| 9 | B04 | "Tier four... deciding which problem is worth solving, and whether to trust the answer at all" | PASS (framing) | The series' own Tier-4 definition; presented as the film's construct. | — |
| 10 | B04 | "Yours today, and for a long while" | EXEMPT | Forward-looking judgment, explicitly hedged; the source episode treats "irreducible" the same way. | — |
| 11 | B05 | "what is actually scarce is conducting" | PASS (interpretive) | Direction-of-travel claim consistent with employer-survey trend data (WEF Future of Jobs Report 2023; BCG AI at Work survey 2023, per source PEDAGOGY.md); no precise figures quoted, so no overclaim. | — |
| 12 | B06 | "One real task a day... Read every line. Name one thing it got wrong" | EXEMPT | Practice prescription, not a factual claim. | — |
| 13 | B06 | Implies daily audit practice builds judgment ("One rep of judgment, every day") | PASS | Grounded in human-factors research on appropriate trust / automation complacency: Parasuraman & Riley, "Humans and automation: Use, misuse, disuse, abuse," *Human Factors* 39(2), 1997 — overreliance (misuse) comes from uncritical reliance without monitoring; monitoring practice is the documented countermeasure. | — |
| 14 | B07 | "Your name on it means your judgment owns it" | EXEMPT | Normative rule (the film's boundary), not a factual claim. | — |
| 15 | B08 | "fire a vendor" is the human-alone decision; the others are AI-assistable | EXEMPT | Worked example illustrating the tier map; the source episode's own verdict. | — |
| 16 | BHTF | The Your-Turn prompt will produce a self-audit | EXEMPT | Viewer exercise; no outcome claimed. | — |

## Notes

- "Distrust-calibration" (the source's term) was not used in the final
  narration: it is a series neologism that would need its own definition beat
  for a general audience. The idea survives as "knowing when to trust the
  output and when to override it" — no, in the final script it survives as the
  daily loop's "name one thing it got wrong," which IS the calibration
  practice, shown rather than named. [judgment]
- No dated or version-sensitive claims remain; no Kokoro pronunciation traps
  (no acronyms, no version numbers in narration).
- Kokoro check worth doing at render: "four-tier" (hyphenated compound) and
  "AI-assistable"? — "AI-assistable" was cut; final narration contains
  "four-tier", "superhuman", "irreducible" — whisper-check these at audio
  generation per the skill's traps.
