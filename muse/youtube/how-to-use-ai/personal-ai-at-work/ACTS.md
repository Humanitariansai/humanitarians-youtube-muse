# ACTS.md — Stop using your own Claude at work.

A cautionary how-to for the humanitarians channel "how to use AI" series: why
your personal AI chatbot is the wrong place for work secrets, and exactly how
to protect yourself.

**Exact title:** Stop using your own Claude at work.

**Core promise:** By the end, the viewer can state what happened at Samsung in
April 2023, explain in plain words why a personal chatbot account puts work
data at risk (training + retention), flip the training toggle in Claude,
ChatGPT, Grok and Gemini, name the three legal framings a lawyer could use,
and follow the clean-room rule when they keep using a personal account.

**Skill:** lecture. The source is one whole document; the spine is the lecture
spine (BIDEA hesitant writer → BDEFS key terms → acts → BVDT recap → BHTF
your-turn → BOUT). cc-explainer was auditioned and rejected (this film is not
about a terminal session); deep-explainer's parent laws apply through
lecture's lineage, but lecture's BDEFS beat is what the audience rule needs —
every technical term is defined up front, in plain language.

**Structure:** Five acts.

- Act 1 — The Samsung story (2 beats): permission → three leaks in twenty
  days (source code, yield code, meeting recording) → company-wide ban and
  disciplinary investigations.
- Act 2 — The mechanism (2 beats): why personal plans are the exposure
  (chats can improve the model; the setting is opt-out); retention (up to
  five years opted in, ~30 days opted out; opt-out only applies going
  forward).
- Act 3 — The fix (2 beats): Claude's toggle path (Settings → Privacy);
  the same move in ChatGPT, Grok, Gemini.
- Act 4 — The legal reality (1 beat): three framings — NDA breach, data
  protection law, IT security policy; none needs malicious intent.
- Act 5 — The clean-room habit (2 beats): anonymize before you paste (shown,
  not told); if you set policy, get the company an enterprise plan.

**Tone:** plain-spoken and a little urgent; Teardown register throughout —
short sentences, no jargon left unexplained. The film is a warning with a
fix, not a lecture on AI ethics.

**What this film is not:** not legal advice (said on screen and in the
narration — "I'm no lawyer, talk to yours"); not an enterprise sales pitch;
not a claim that personal AI should never be used at work — the clean-room
rule keeps the personal account usable. No model names are quoted except as
needed for toggle paths; the toggle locations are dated UI that may move.

**Source facts:**
- Samsung, April 2023: semiconductor engineers authorized to use ChatGPT;
  three leaks in ~20 days (semiconductor measurement-DB source code pasted
  for bug-checking; device-yield program code pasted for "code
  optimization"; internal meeting recording pasted for minutes). Samsung
  capped uploads, then banned ChatGPT and other external AI tools
  company-wide, and opened disciplinary investigations. (press: The
  Economist Korea via Mashable; TechSpot; TechTimes)
- Personal Claude plans (Free, Pro, Max): chats and coding sessions can be
  used to improve the model; the "Help improve our AI models" toggle is
  Settings → Privacy, opt-out. Opted in: up to 5 years retention in training
  pipelines; opted out: ~30-day deletion. Opting out applies going forward;
  data already in a training run can't be pulled back. (Anthropic Consumer
  Terms / Privacy Center via 2026 guides)
- ChatGPT: Settings → Data Controls → off "Improve the model for everyone".
  (OpenAI Data Controls FAQ)
- Grok: profile settings → privacy/data controls → turn off training and
  data sharing. (X privacy settings; Grok data-sharing toggle)
- Gemini: myactivity.google.com → Gemini activity ("Keep Activity") toggle
  off; even off, ~72-hour service retention; human-reviewed chats kept up to
  3 years. (Google Gemini Apps Help)
- Enterprise/Team plans (Anthropic, OpenAI): no training on your data by
  default. (Anthropic plan comparison; OpenAI Enterprise privacy)
