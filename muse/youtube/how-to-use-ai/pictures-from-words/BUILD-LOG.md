# BUILD-LOG.md — Pictures from Words

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:45 — Received subagent task: build film 19 of 24 ("Pictures from
  words"), NEW from scratch, reference-only the rohan-v fellows film
  (how-it-works) — mine teaches how-to-use. Assigned skill ai-explainer;
  12-file package to `muse/youtube/how-to-use-ai/pictures-from-words/`.
- 21:46 — Read `skills/make/ai-explainer/SKILL.md` end to end. Skill
  decision: KEEP ai-explainer (the film explains one AI capability to a
  smart non-expert — exactly the skill's lane) and apply its content laws
  (SHOW-DON'T-TELL, DOUBLE-CHECK, REBUILD — every "result" is a drawn
  Manim placeholder, never a lifted or generated image). The skill's
  Claude-brand Remotion bookends do NOT apply: this is a series film with
  a locked identity (Liam / claude-liam / am_onyx / @NikBearBrown) and
  the series' established lean Manim package shape from film 1 — switching
  the whole series to Remotion mid-run would break Bear's review pattern.
  [judgment]
- 21:50 — Studied film 1's package
  (`~/workspace/film-builds/register-muse-privacy-card/`) end to end:
  copied its package shape, beat-sheet schema, Manim house palette and
  safe-area conventions, and the CHECKS-REPORT honesty pattern. Note: its
  folder had 11 files locally; README.md is the 12th per this film's spec.
- 21:52 — Read the mirror repo's rohan-v film FACTCHECK via Contents API
  (local mirror lacks the fellows/ tree). Took only the mechanism
  one-liner facts (noise → denoise steps; Midjourney "Seeds" docs quote);
  the film teaches use, not mechanism. Nothing quoted on screen.
- 21:55 — Factcheck research (web, 2026-10-03): prompt formula
  subject+style+setting+lighting+mood verified across DALL-E guides and
  the community S-S-C-D-C method; text-in-image misspellings verified
  (PetaPixel 2024-03, TechCrunch 2024-03, quoting UCL's Peter Bentley and
  DAIR's Asmelash Teka Hadgu); hands/fingers as a historically hard case
  verified (arXiv 2408.15461 context); AI-label disclosure norm verified
  (TikTok/YouTube/X/Meta labels, C2PA, EU AI Act Art. 50). All recorded
  in FACTCHECK.md with [record]/[judgment] labels; version-specific
  claims cut so the film doesn't rot.
- 22:00 — Read muse/QUEUE.md via Contents API: confirmed film 19's slot
  and skill, and film 20's title ("What never to paste into AI") for the
  outro teaser.
- 22:02 — Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md,
  PROMPTS.md. Decision: 3 acts (the ladder / the recipe + uses / the
  honest limits), 14 beats, 282 s (~4m42s) — inside the 4.5–7 min band.
- 22:05 — Wrote make_sheet.py; first run clean: beats=14 body=9
  total=282s. beat_sheet.json generated.
- 22:10 — Wrote scenes.py (M01–M12). Pre-gate self-review caught three
  issues before running the checker: the M08 garden icon used throwaway
  mobjects for placement (replaced with explicit coords); M04's prompt
  card second line was too wide at real-Manin metrics (re-split to three
  lines); M05's tweaks were designed as Transforms to explicit targets
  from the start (no animate-only introductions). M12 recap lines capped
  at 48 chars / font 16 for the 10.6-wide plates.
- 22:12 — Gate: `python3 -m py_compile` clean; static_scene_check.py per
  class: 12 clean · 0 warn · 0 error on the first full run.
- Next: push the 12 files via gh-put-file.py; verify each via Contents
  API; file the seven-field FRICTIONAL.md entry (do NOT write
  muse/FRICTIONAL.md — that is the parent's job; I report the entry text).
