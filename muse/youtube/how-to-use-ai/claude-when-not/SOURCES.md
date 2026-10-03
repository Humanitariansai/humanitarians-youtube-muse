# SOURCES.md — "Claude, When Not."

Primary source (argument and facts), read-only reference via the GitHub
Contents API, mirror repo `nikbearbrown/humanitarians-youtube-muse`:

- `claude-for-artificial-intelligence/hai-when-not/beat_sheet.json` — the
  source beat sheet (11 beats, "Claude, For Students" season finale H5).
  The argument (scaffold vs. crutch, use/don't-use lists, the hide-it test,
  predict-then-answer) is preserved; the narration is rewritten for a general
  audience and the H1–H5 season arc is dropped.
- `claude-for-artificial-intelligence/hai-when-not/PEDAGOGY.md` — the source
  evidence table and friction check (normative claims, hiding-test lineage,
  hallucination grounding). The FACTCHECK.md verdicts EXEMPT/PASS follow it.

Verification sources consulted for this film (no new empirical claims added):

- Ji, Z. et al. (2023). "Survey of Hallucination in Natural Language
  Generation." ACM Computing Surveys — standard hallucination taxonomy;
  grounds FACTCHECK #1 and #9.
- NIST AI 600-1, §2.2 "Confabulation" — "generative AI systems generate and
  confidently present erroneous or false content"; grounds the plain-language
  hallucination definition.
- OpenAI GPT-4 Technical Report (March 2023) — hallucination tabled as a
  metric (19% vs 28% for ChatGPT on internal closed-domain factuality evals);
  grounds FACTCHECK #9's "deliver it with total confidence."
- Alkaissi & McFarlane (Cureus, Feb 2023) — fabricated scientific citations in
  chatbot outputs; grounds the "invent a citation" example.
- Source PEDAGOGY.md: NACUA 2023 guidance / institutional policies (disclosure
  consensus); Bereiter & Scardamalia 1987 (drafting as learning); Josephson
  Institute / "newspaper test" tradition (hiding-test lineage).

No `mp3/` audio was downloaded from the source; narration audio will be
generated fresh (Kokoro `am_onyx`) at render time.
