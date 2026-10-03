# FACTCHECK.md — Claude, Your Quizmaster

Every factual claim in the script was checked on 2026-10-03 before
writing. No statistics, quotations, people, or results were invented.

| # | Beat | Claim | Verdict | Source | Fix |
|---|------|-------|---------|--------|-----|
| 1 | BDEFS | Retrieval practice = pulling an answer out of memory instead of re-reading it | PASS | Standard definition, consistent with Roediger & Karpicke 2006 usage | — |
| 2 | B01 | Quizzing builds memory, not just checks it (the testing effect) | PASS | Roediger, H. L. & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255 | — |
| 3 | B01 | A week later: quizzers kept ~61%, re-readers ~40% | PASS | Roediger & Karpicke (2006), Experiment 2: STTT 61% vs SSSS 40% at 1 week; SAGE abstract confirms the crossover (5-min restudy advantage reverses by 2 days / 1 week) | Spoken as "about forty / about sixty percent", on-screen "61% vs 40%", tagged "memory researchers" |
| 4 | B01 | Re-reading feels productive because you recognize the words; restudiers were more confident yet retained less | PASS | Roediger & Karpicke (2006): repeated studying increased students' confidence in their ability to remember while producing substantially lower delayed retention; Karpicke et al. (2009) on students' lack of metacognitive awareness of the testing effect | Kept qualitative ("feels productive because you recognize them") — no invented mechanism |
| 5 | B02 | Even a wrong guess helps: failed attempts still boost what you learn next | PASS | Kornell, Hays & Bjork (2009). Unsuccessful retrieval attempts enhance subsequent learning. *JEP: Learning, Memory, and Cognition*; Richland, Kornell & Kao (2009). The pretesting effect. *JEP: Applied*, 15(3), 243–257 | "Boost" kept qualitative; no effect size quoted |
| 6 | B03 | Memory fades over time; that is the system working, not a flaw | PASS | Ebbinghaus, H. (1885). *Memory: A Contribution to Experimental Psychology* (forgetting curve) | Plain-language framing of the forgetting curve; no percentages quoted (popular "70% in 24 hours" style figures deliberately avoided — they come from savings scores for nonsense syllables, not recall of real material) |
| 7 | B03 | Spaced reviews — today, tomorrow, next week, next month — extend retention; each review lands as the memory fades | PASS | Cepeda, Pashler, Vul, Wixted & Rohrer (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132, 354–380 (317 experiments, 839 assessments); Dunlosky et al. (2013) rates distributed practice "high utility" | The 1-1-7-30 day cadence is an illustrative expanding schedule, not a quoted optimal interval — the narration never claims optimality |
| 8 | B04 | Explaining a concept back surfaces gaps: what is right, incomplete, missed; the hesitation tells you what to study next | PASS | Chi, Bassok, Lewis, Reimann & Glaser (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13(2), 145–182 (self-explaining students detect comprehension failures and learn more); Bielaczyc & Recker (1991) — students can be taught to self-explain | "Claude marks what is right/incomplete/missed" is the film's prescribed use of the tool, not a product claim about Claude's grading accuracy |
| 9 | BHTF | Claude can quiz you one question at a time and produce a spaced review schedule | EXEMPT | Prescribed user action, not a factual claim — the prompt is a handoff the viewer runs themselves; no guarantee of output quality is made on screen or in narration | Framed as "paste this in", never "Claude will correctly…" |
| 10 | B05 | "Claude does not know your industry's edge" — the tool handles repetition, you bring judgment about what matters | EXEMPT | Editorial judgment; a caution against over-delegation, not a verifiable product claim | — |
| 11 | — | Film identity: channel claude-liam; persona "Liam, in for Bear"; Kokoro am_onyx; Teardown register; watermark @NikBearBrown | PASS | Film-builder brief | — |

## Judgments (judgment)

- The 1-1-7-30 cadence (today / tomorrow / next week / next month) is my
  illustrative expanding schedule, consistent with Cepeda et al.'s finding
  that wider spacing suits longer retention intervals; it is not quoted as
  the optimal schedule. [judgment]
- "The struggle is the learning" is the film's one-line principle —
  my compression of the desirable-difficulties literature (Bjork & Bjork),
  not a quoted result. [judgment]
- The four-move stack (quiz / predict-first / space / explain-back) is my
  structure for the source beat sheet's argument; the source's mid-career
  beat and verdict map onto Act 2 and BVDT. [judgment]
- School examples (photosynthesis, Keynesian economics, the third
  amendment) from the source were cut; the film's examples are work life,
  because the audience is a general audience, not students. [judgment]

## Cut or disclosed

- No retention percentages are promised to the viewer; 61/40 is a lab
  result on prose passages, labeled "memory researchers" on screen and
  "in the lab study" in narration.
- "Wrong guesses count" is qualified: the attempt primes you to catch
  the answer when it arrives — the narration never says errors alone
  teach.
- The film does not claim quizzing replaces first learning the material;
  ACTS.md states you quiz what you have already met.
- The BHTF prompt is presented as a starting point the viewer runs and
  judges themselves, not as a certified workflow.
