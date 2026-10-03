# BUILD-LOG.md — "How to outsource everything to AI & get dumb"

## 2026-10-03 — pre-render package build

**Skill choice: show-tell** (not ai-explainer). The source suggested show-tell or
ai-explainer. ai-explainer is the Claude-app-skin brand for product/feature explainers;
this film is a behavioral concept (cognitive offloading) for a general audience, and the
job's rewrite rules demand drawn demonstrations over cards. Show-tell's "one image per
beat, the voice explains" is the exact fit. [judgment]

**Rewrite for the general audience.** The source was written for the Kore persona
(af_kore, Pragmatist register, hai channel) with Remotion text cards and mixed/technical
framing. Rewritten for Liam ("Liam, in for Bear"), Kokoro am_onyx, Teardown register,
claude-liam channel, watermark @NikBearBrown. Every technical term is explained in plain
words (BDEFS: brain rot, outsource, constraints); the five-step method is shown as
physical actions (card, pencil, pages) rather than described. [record]

**Structure kept from the source:** the paste-and-hope pattern, the GPS analogy, the one
line (outsource work, not understanding), the five-step method, "two extra minutes", the
Your Turn draft+constraints prompt. The Chief of Staff scenario survives as the B06
strategy-doc example (the ninety-day rollout plan). [record]

**Evidence beats added (B07, B08).** The source argued from analogy alone. Added two
fact-checked evidence beats: UCL 2017 satnav study (Nature Communications) and the MIT
Media Lab 2025 "Your Brain on ChatGPT" preprint (arXiv:2506.08872). Both numbers are
attributed aloud and captioned on screen per show-tell law 8; the preprint status is
stated in the narration ("suggestive, not settled"). The 83% figure and the 11%
comparison come via secondary summaries — the 11% is flagged in FACTCHECK.md as
verify-against-primary before final render. [judgment]

**Kokoro pronunciation calls.** "UCL" never spoken (acronym risk) — narration says "In
London, researchers…", the on-screen caption carries "UCL, 2017". "MIT" and "ChatGPT"
kept (voice cleanly in practice). Numbers spoken as words ("eighty-three percent").
Greeting "Hallo" (known-clean). [judgment]

**Drawing decisions.** One cast the whole film: worker + glowing brain, dark AI box with
terracotta spark, iso pages, pencil. Terracotta rationed: spark, brain dots, one ring
dot (B02's ring drawn in ink per the curve rule). Gauges use BAR1/ghost greys, never
terracotta bars. B06 and B08 skip the sparse waiver (they fill the frame); all other
body beats carry it. [record]

**QC.** `python3 -m py_compile` clean on make_sheet.py and scenes.py. Static checker:
10/10 scene classes clean, 0 warnings, 0 errors, first run — no fixes needed. (Full
record in CHECKS-REPORT.md.) [record]

**Not done (by design).** Pre-render package only: no audio generated, no Manim render,
no assembly, no publish. Render instructions for Bear's Mac in CLAUDE-CODE-RENDER.md.
