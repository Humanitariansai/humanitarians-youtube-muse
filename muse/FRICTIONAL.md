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

---

## 2026-10-03 — Redos: the two muse/youtube films for a general audience

**1. Date and what I was working on.**
2026-10-03. Bear's redo directive: rebuild the two films under
`muse/youtube/` for the humanitarians AI YouTube channel — general
audience (smart, pragmatic, not AI experts), explain every term, show
rather than tell. [record]

**2. I tried / expected.**
I expected two lecture-skill films in my 11-file package format. The
originals turned out to be full-toolkit-pipeline films (rich beat
schema, built artifacts), not my simplified format — so "redo" meant
adapting their act structures and attribution maps into my workflow,
not converting files. [my input]

**3. What happened (including failures and reversals).**
- Found the two films: `claude-liam-lecture-claude-making-a-film-about-muse/`
  (Bear & Claude's analysis: product, costs, business model, 12-point
  security critique, Bear's resolution; 6 acts) and
  `claude-liam-lecture-muse-making-a-film-about-muse/` (product
  explainer; 4 acts). [record]
- Noted the second film's folder has a committed
  `__pycache__/scenes.cpython-314.pyc` and `.DS_Store` files — minor
  standing-rule violations from a previous session. Left untouched;
  flagged to Bear instead of deleting someone else's history. Its
  `mp3/` holds only timings.json — no audio was committed. [record]
- Redo A ("Muse making a film about Muse" → `muse/youtube/muse-for-everyone/`):
  22 beats, 17 body, 404 s; 17 scenes, QC 17 clean · 0 warn · 0 error
  first run. [record]
- Redo B ("Claude making a film about Muse" →
  `muse/youtube/claude-on-muse-for-everyone/`): 21 beats, 16 body, 418 s;
  19 scenes, QC 19 clean · 0 warn · 0 error first run. Two pre-gate
  catches: `DashedRectangle` isn't in the QC stub (NameError — replaced
  with Rectangle); a `FadeIn` + `.animate` on one mobject in a single
  play() would fight in real Manim (split). The duration assert caught
  426 s > 420 s cap; five beats trimmed to 418 s. [record]
- Translation decisions for the general audience: "fail-safe defaults
  (Saltzer & Schroeder, 1975)" → the two-bouncers visual; "behavioral
  promise, not a technical boundary" → "a promise, not a wall"; token
  allowances cut; open-questions act cut; attribution discipline
  preserved throughout ("researchers report", "their read", "in Nik's
  experience", "the document reports"). [judgment]
- Skill choice: lecture for the product explainer (whole-product
  coverage, same as the original); deep-explainer shape for the analysis
  film (it's an argument: read → critique → resolution). [judgment]

**4. What I did.**
Built both 11-file packages, pushed all files plus folder READMEs via
the Contents API, verified all 24 files live via API reads. Originals
untouched. [record]

**5. What Claude or another person contributed.**
Bear set the redo directive, the audience rule, and the skill menu. The
original film packages (act structures, attribution map, Bear's
document via its citations) were built by a previous session and served
as the adaptation source; every narration line and visual is new.
The security-critique substance is Bear & Claude's analysis, voiced as
their opinion throughout. [record]

**6. What I understand now / still do not understand.**
I understand the redo pattern now: keep the spine and the attribution,
rewrite the words, redraw the pictures. I don't know whether Bear wants
the originals' folders cleaned of the .pyc/.DS_Store, or which film
comes next. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/muse-for-everyone/` (12 files) and
`muse/youtube/claude-on-muse-for-everyone/` (12 files) verified live;
CHECKS-REPORT.md files record the clean gates. Next step: Bear renders
on his Mac per the CLAUDE-CODE-RENDER.md files, and names the next
film. [record]
