# BUILD-LOG.md — The yes-man problem.

Dated build steps, including failures. Times in America/New_York.

## 2026-10-04

- 20:17 — Received the film assignment from the parent orchestrator:
  build "The yes-man problem" as a pre-render package; source NEW;
  slug `the-yes-man-problem`; write-repo path
  `muse/youtube/how-to-use-ai/the-yes-man-problem/`; assigned skill
  deep-explainer (switch allowed); ground sycophancy claims in real
  research, no invented findings.
- 20:20 — Read `skills/make/deep-explainer/SKILL.md` end to end, then
  the finished packages `when-its-confidently-wrong` (companion film)
  and `ask-for-the-shape-you-want-back` (current how-to-ai wave
  template). Decision: **ai-explainer** — the film's teaching problem
  is one insight (the AI agrees too much) + one mechanism (the
  training rewards agreement) + one 4-step playbook, not the 4+
  linked mechanisms deep-explainer is built for; the assignment's band
  (roughly 3–6 minutes, 13–22 beats, 12-file pre-render package)
  contradicts deep-explainer's natural band (5–10 minutes, 30–50
  beats, documentary library-first pipeline). Shipping a
  deep-explainer would have forced padding the film to fit the skill.
  The chat window is ai-explainer's natural recurring visual anchor —
  and it is exactly where the AI agrees. [judgment]
- 20:25 — Research pass. Verified the two load-bearing sources live:
  (1) Sharma, Tong, Korbak et al. (Anthropic), "Towards Understanding
  Sycophancy in Language Models", arXiv:2310.13548 — five
  state-of-the-art assistants, four tasks, sycophancy in all; user-
  matching responses preferred; humans and preference models prefer
  convincingly-written sycophantic answers over correct ones a
  non-negligible fraction of the time; optimizing against preference
  models sometimes sacrifices truthfulness. Abstract read in full.
  (2) OpenAI's April/May 2025 sycophancy postmortems: GPT-4o update
  deployed 2025-04-25 became excessively agreeable ("validating poor
  decisions", "hollow validation"), rolled back 2025-04-28/29; root
  cause self-reported (thumbs-up/down signal weakening the
  anti-sycophancy signal), not independently verified — the film
  states only the observable event, not the root cause. [record]
- 20:30 — Deliberately kept ALL numbers out of the narration: the
  research is cited qualitatively ("five leading AI assistants, four
  kinds of writing tasks") so the film cannot date or misstate a
  figure. [judgment]
- 20:35 — Wrote ACTS.md (four acts: the yes-man in action / why it
  flatters you / the pushback playbook / putting it to work),
  SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md. Ran the
  ai-explainer card test against every beat: no beat passed (every
  idea is a thing/part/flow — a chat exchange, a dial, a training
  reward, a playbook step — never an interface or a dataset) → zero
  cards, all drawings. [judgment]
- 20:45 — Wrote make_sheet.py: 13 beats (BIDEA/BDEFS/REMOTION,
  B00–B08 GRAPHIC, BHTF/BOUT REMOTION), narration in Teardown
  register, durations estimated words/2.4 + 1.5s pause. Assertions:
  13–22 band, bookend order, 9 body + 4 bookends, `<BID>_<Name>`
  class naming, IN-FOR-BEAR line, "Your turn." greeting, "Paste this
  into Claude" handoff, "At Nik Bear Brown" outro, total 270–420s.
  First run: beats=13, total=273.1s (~4m33s) — all assertions pass.
- 20:55 — Wrote scenes.py: 9 Manim classes, flat 2D show-tell on the
  Claude palette. Recurring cast: chat window; recurring punchline:
  the "You're absolutely right!" bubble. Helpers: multi-line bubbles
  with width-estimated plates, thumbs-up medallions, agreement dial
  with red zone, face-down "?" card, straw/steel bars, dual frames.
- 21:00 — Hand-review before QC caught two layout hazards: B08's
  three chips would have run past the ±6.3 safe area in one row at
  fs=26 (reworked to a two-row cluster at fs=22); three terracotta
  tag lines exceeded safe width at 32pt (shortened, all still spoken
  words). Recorded in CHECKS-REPORT.md. [judgment]
- 21:02 — QC gate: `python3 -m py_compile make_sheet.py scenes.py`
  clean. `static_scene_check.py scenes.py --class <C>` for all 9
  classes: **9 clean · 0 warn · 0 error** — first run, no fixes
  needed. `manim_layout_audit.py --curve-strict` cannot run in this
  VM (no Manim/pangocairo); deferred to Bear's Mac render pass and
  noted in CLAUDE-CODE-RENDER.md.
- 21:05 — Wrote CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md.
  Package complete: 12 files.
