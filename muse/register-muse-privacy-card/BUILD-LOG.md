# BUILD-LOG.md — Register for Muse with a privacy.com card

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 15:34 — Received FILM-BUILDER-HANDOFF.md from Bear: build lecture films as
  pre-render packages on Humanitariansai/humanitarians-youtube-muse; never
  render or publish; push everything to GitHub immediately.
- 15:34–15:43 — Onboarding with Bear (name: Bear; assistant name: Muse).
- 15:44 — Setup: `~/workspace/skills/github/bin/` did not exist, so I wrote
  gh-put-file.py, gh-mkdir.py, gh-delete.py per the handoff spec (surrogate
  auth via dynamic_credentials, api.github.com only). py_compile clean.
- 15:44 — `custom.github` credential not provisioned; created the secure
  connector request (api_key, bearer_header, api.github.com) and got the
  capture link for Bear.
- 15:45 — First `git clone` of brutalist.art was interrupted twice
  mid-checkout (empty working tree, then aborted). Fixed with
  `--depth 1 --filter=blob:none --sparse`, checking out only
  `skills/make` + `runtime/qc`. Lesson: sparse-checkout the toolkit; the
  full clone is slow and fragile here.
- 15:47 — Bear's briefs arrived: always films for the humanitarians AI
  YouTube channel (https://www.youtube.com/@humanitariansai), always the
  Liam persona; I do everything except final renders and voice; primarily
  use the lecture skill; first film = register/set up for Muse with a
  privacy.com card; key facts (Meta account → probably no card; no account
  → $1 hold refunded in ~1 week; privacy.com $10-limit card works).
- 15:50 — Read `skills/make/lecture/SKILL.md` end to end (spine, BEST-BEAT
  LAW, SHOW-THE-THING LAW, channel outro table). Noted the tension: the
  skill's outro table wants claude-hai for HumanitariansAI, but Bear's
  handoff fixes film identity to channel claude-liam / Liam / am_onyx /
  "Muse, in for Bear" — Bear's direct instruction wins.
- 15:52 — Sparse-cloned the mirror repo; read part-2-showing-the-output
  end to end (ACTS → FACTCHECK → beat_sheet.json → scenes.py), plus
  make_sheet.py, CHECKS-REPORT.md, PROMPTS.md, CLAUDE-CODE-RENDER.md.
  This film copies that package structure exactly (11 files + README).
- 15:55 — Read the course-layer AGENTS.md (house rules). Its "every
  human-facing Markdown opens with an Executive summary" rule targets
  course lessons; the four finished, gated film packages carry no
  executive summaries, so this film follows the film-package pattern.
  [judgment]
- 15:58 — Research: verified privacy.com spend-limit mechanics against
  support.privacy.com (per-card limits, auto-decline, cap-not-preload,
  merchant lock, pause/close, free tier, US-only, KYC signup); verified
  Muse product facts against docs/muse.md; confirmed $1 authorization
  holds are standard card-verification practice.
- 16:05 — Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md. Decision: 3 acts
  (the fork / the privacy.com card / finish setup), 15 beats, 296 s
  (~4m56s) — inside the 4.5–7 min band.
- 16:10 — Wrote make_sheet.py. First run FAILED on my own assertion:
  the recap-coverage check was case-sensitive and the line uses "Act
  two"/"Act three". Fixed the assertion (case-insensitive), re-ran:
  beats=15 body=10 total=296s. Logged because the failure was mine, not
  the script's logic.
- 16:15 — Wrote scenes.py (M01–M13). Pre-flight review of the QC stub
  caught four real bugs before running the gate: shapes that were only
  ever `.animate()`d (M01 card, M05/M08 coins, M12 gauge fill) are never
  added to the stub's scene graph, so they would be invisible to the
  checker; M13's text-removal hack used a `_text` attribute that only
  exists in the stub, not real Manim. Fixed by explicit FadeIn adds and
  a collected-mobs FadeOut. Also shortened M13 recap lines to fit the
  plate at real-Manin text widths.
- 16:20 — Gate: `python3 -m py_compile` clean; static_scene_check.py per
  class: 13 clean · 0 warn · 0 error on the first full run.
- Placement decision: this is a channel film, not course work, so it goes
  in a new top-level `muse/` collection —
  `muse/register-muse-privacy-card/` — following the repo's `codex/`
  precedent. Flagged to Bear; reversible.
- Reel name: `muse-register-privacy-card` (the part-N-<slug> convention
  was for the course series).
- Next: push the 11 files via gh-put-file.py once Bear completes the
  GitHub token form; verify via Contents API; log FRICTIONAL.md.
