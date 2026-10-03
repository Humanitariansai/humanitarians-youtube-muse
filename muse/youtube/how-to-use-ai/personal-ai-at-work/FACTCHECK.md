# FACTCHECK.md — Stop using your own Claude at work.

Every checkable claim was verified against press and vendor docs on
2026-10-03, before the script was written. Dated UI paths are presented as
they were on that date.

## Verified (record)

1. April 2023: Samsung authorized ChatGPT use for semiconductor-division
   engineers; within ~20 days, three leaks — an employee pasted
   confidential source code (semiconductor measurement-DB software) to check
   errors; another pasted device-yield program code asking for "code
   optimization"; a third submitted a recording of a confidential meeting to
   be converted into notes. → The Economist Korea via Mashable; TechSpot;
   Communications Today [record]
2. Samsung first limited ChatGPT uploads (≈1024 bytes per person), then
   banned ChatGPT company-wide (extended to Bard/Bing), and opened
   disciplinary investigations into the employees. → TechTimes; memeburn
   (citing TechCrunch) [record]
3. Personal Claude plans (Free, Pro, Max): "Help improve our AI models"
   toggle at Settings → Privacy; Anthropic's plan comparison describes
   model training as opt-out on consumer plans, none by default on Team and
   Enterprise. → Anthropic docs via theaicareerlab (Sep 2026),
   c-ai.chat (Sep 2026) [record]
4. Opted in: Anthropic may keep chats in training pipelines up to 5 years,
   de-identified. Opted out: standard ~30-day deletion; deleted conversations
   leave back-end storage within 30 days. → same sources [record]
5. Opting out stops future training use; data already in a completed or
   in-progress training run can't be pulled back. → Engadget (Sep 2026);
   theaicareerlab [record]
6. ChatGPT: Settings → Data Controls → turn off "Improve the model for
   everyone". → OpenAI Data Controls FAQ via autoprintshop (Sep 2026),
   theaicareerlab [record]
7. Grok/X: Settings and privacy → Privacy and safety → Grok → turn off
   "Allow your posts as well as your interactions, inputs, and results with
   Grok to be used for training and fine-tuning"; conversation history can
   be deleted. → Fast Company; makeuseof; thewindowsclub [record]
8. Gemini: toggle at myactivity.google.com ("Gemini Apps Activity", renamed
   "Keep Activity" in Aug 2025); on by default; auto-delete 3/18/36 months;
   even with it off, ~72-hour service retention; human-reviewed chats kept
   up to 3 years. → Google Gemini Apps Help; redact.dev; Engadget [record]
9. Anthropic Team/Enterprise and OpenAI Business/Enterprise/Edu do not use
   your data for model training by default. → Anthropic plan comparison;
   OpenAI Enterprise privacy via autoprintshop [record]

## Judgments (judgment)

- "All now sitting on OpenAI's servers" is a simplification of "OpenAI may
  retain inputs for training / 30-day safety retention"; the point is the
  data left Samsung's control. [judgment]
- The narration says Anthropic "can keep those chats for up to five years"
  with the setting on; exact default state of a new account is not stated by
  Anthropic, so the film says "the setting is opt-out — don't assume" and
  tells the viewer to check rather than claiming what the default is.
  [judgment]
- The three legal framings (NDA breach / data-protection law / IT policy
  breach) are framings a lawyer could use, not verdicts; the film and the
  M09 scene carry "I'm no lawyer" / "not legal advice". [judgment]
- "One leak costs more than a hundred plans" is rhetoric, not arithmetic.
  [judgment]

## Cut or disclosed

- The source beat sheet's line "the not a lawyer — he's clear about that"
  was garbled and the referenced guide could not be identified; the
  attribution was dropped and replaced with Liam's own "I'm no lawyer — talk
  to yours". The source's "All three have precedent" was softened: the film
  asserts exposure, not specific case law.
- The source's "one additional guide covers" (garbled) was dropped; the
  going-forward-only caveat is stated from Anthropic's terms instead.
- Grok's path is given loosely ("profile settings, data controls") because
  the exact path differs between the X app and the standalone Grok app and
  changes often; the setting name to find ("training and fine-tuning" data
  sharing) is stated.
- The film does not mention Samsung's later (2026) ChatGPT Enterprise
  deployment — it would date the film and doesn't change the lesson.
- Toggle paths are dated UI: the film works even if paths move, because the
  action ("find the training toggle and switch it off") survives the UI.
