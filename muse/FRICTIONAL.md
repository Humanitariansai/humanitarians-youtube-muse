# FRICTIONAL.md — muse/ film collection

Build log for the humanitarians-channel Muse film series. One entry per
film (and per substantive build), seven fields each. Values labeled
[record] / [judgment] / [my input].

---

## 2026-10-03 — Film 1: "Register for Muse with a privacy.com card"

**1. Date and what I was working on.**
2026-10-03. First film of the humanitarians-channel Muse series: a
pre-render package (script, Manim visuals, docs) for "Register for Muse
with a privacy.com card", built to FILM-BUILDER-HANDOFF.md spec and pushed
to `muse/register-muse-privacy-card/`. [record]

**2. I tried / expected.**
I expected to follow the handoff's §13 order cleanly: token → toolkit →
study the four finished films → build. I expected the brutlist.art clone
and the GitHub helpers to exist or be trivial. [my input]

**3. What happened (including failures and reversals).**
- The `~/workspace/skills/github/bin/` helpers did not exist; I wrote
  gh-put-file.py, gh-mkdir.py, gh-delete.py from the handoff spec. [record]
- The `custom.github` credential was not provisioned; Bear completed the
  secure form later the same day (token "muse-vm", fine-grained, Contents
  read+write, never expires). [record]
- `git clone` of brutalist.art failed twice (interrupted mid-checkout,
  empty tree). Fixed with `--depth 1 --filter=blob:none --sparse`,
  checking out only `skills/make` and `runtime/qc`. [record]
- make_sheet.py failed its own recap-coverage assertion on the first run:
  the check counted lowercase "act " but the line uses "Act two"/"Act
  three". Fixed to case-insensitive; the line was correct. [record]
- Pre-gate review of the QC stub caught four latent bugs before the
  checker ran: shapes introduced only via `.animate()` (M01 card, M05/M08
  coins, M12 gauge fill) never enter the stub's scene graph; M13's
  text-removal hack used a stub-only `_text` attribute; M13 recap lines
  were wider than the 16:9 frame at real-Manin text metrics. All fixed
  before the first checker run. [record]
- Static QC then passed first try: 13 clean · 0 warn · 0 error. [record]
- Placement: this is a channel film, not course work, so I created a new
  top-level `muse/` collection (`muse/register-muse-privacy-card/`)
  following the repo's `codex/` precedent, and flagged the choice to
  Bear. [judgment]

**4. What I did.**
Built the full 11-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 15 beats, 10 body, 296 s — scenes.py with 13 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER),
pushed all files plus the folder README via the Contents API, and
verified all 12 files live via API read. [record]

**5. What Claude or another person contributed.**
Bear set the topic, the channel/persona lock (humanitarians channel,
Liam), the film-identity constants, and every core fact of the film:
the Meta-account signup fork, the $1 hold released in ~1 week, and the
privacy.com $10-limit workaround — all from his own signup experience.
He provisioned the GitHub token and shared four setup screenshots,
which I audited for tokens/PII (clean). The lecture skill, QC checker,
and film-package pattern came from the brutalist.art toolkit and the
four finished assignment-4 films. I wrote every file; the AI contribution
is the drafting, the QC pre-review, and the research verification
against privacy.com and Muse docs. [record]

**6. What I understand now / still do not understand.**
I understand the full pre-render pipeline now: research → ACTS/SHOTLIST/
FACTCHECK → make_sheet → scenes → QC gate → docs → push → verify.
I still do not know whether Bear wants the `muse/` collection placement
to stand, or the next film's topic. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/register-muse-privacy-card/` on Humanitariansai/humanitarians-
youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear
renders narration (Kokoro am_onyx) and the review cut on his Mac per
CLAUDE-CODE-RENDER.md, and tells me the next film's topic. [record]
