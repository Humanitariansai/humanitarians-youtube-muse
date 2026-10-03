# SOURCES.md — "AI will fail." (why-ai-will-fail)

## Primary source (the argument)

- Ruben Hassid, "AI will fail.", How to AI (Substack), https://ruben.substack.com/p/why-ai-will-fail
  — the list of confident expert predictions (1830–2024) and the closing
  argument ("The early version of the future is usually embarrassing. Then
  it becomes the present. History doesn't repeat itself. But the people
  betting against it do."). The film keeps the argument and the
  best-documented cases; it drops the article's closing workshop sales
  pitch and all weakly-attributed quotes (see FACTCHECK.md C1–C7).

## Mirror-repo source (read-only reference)

- `nikbearbrown/humanitarians-youtube-muse:claude-for-artificial-intelligence/why-ai-will-fail/`
  (`beat_sheet.json` — 12 beats, Kore persona, remotion cards; `README.md`
  with the brutalist rebuild guide). The film is a from-scratch rewrite for
  the humanitarians AI channel audience, not a port: new persona (Liam),
  new register (Teardown), new visuals (Manim), restructured beats.

## Verification sources (per FACTCHECK.md)

- Ken Olsen 1977: Cengage "Entrepreneurship Module" (1977 DEC statement);
  Elon University, "Imagining the Internet" expert-predictions archive,
  https://www.elon.edu/u/imagining/expert_predictions/the-trends-that-will-shape-our-future-4/
- Robert Metcalfe 1995/1997: Elon University archive (Dec 1995 InfoWorld
  column, direct quote), https://www.elon.edu/u/imagining/?p=16109 ;
  Reuters 1997-04-11, "Sage who warned of Net's collapse eats his words."
- Steve Ballmer 2007: Wikipedia "Steve Ballmer" (USA Today interview
  2007-04-30); MacRumors 2007-04-30 ("Ballmer on iPhone Marketshare").
- Paul Krugman 1998: Red Herring 1998 ("fax machine" quote); roundup at
  https://everything-everywhere.com/the-worlds-worst-predictions/
- Jim Keyes 2008: Fast Company, "Blockbuster Bankruptcy: A Decade of
  Decline" (2008 interview); TechCrunch 2011-04-06 ("Snoozing and Losing").
- Larry Ellison 2008: Oracle OpenWorld Sept 2008 speech via WSJ/CNET/eWeek
  ("Oracle CEO Larry Ellison Spits on Cloud Computing Hype"); Wikiquote
  "Larry Ellison"; NetworkWorld ("Once a basher, now a believer").
- Jack Valenti 1982: Wikiquote "Jack Valenti" (House Judiciary testimony,
  12 April 1982); Wikipedia "Jack Valenti" (home-video revenue history).
- BMJ 1941 / penicillin: Wikipedia "Alexander Fleming" (BMJ 1941 report);
  "History of penicillin" (fuller study context).
- Robert Solow 1987: "You can see the computer age everywhere but in the
  productivity statistics" (NY Times Book Review, 1987-07-12) — the
  productivity paradox.
- Daron Acemoglu: NBER Working Paper 32487, "The Simple Macroeconomics of
  AI" (TFP ≤0.66% over 10 years); MIT News 2024-12-06 ("What do we know
  about the economics of AI?"); MIT Technology Review 2025-02-25.
- Ted Chiang: "ChatGPT Is a Blurry JPEG of the Web", The New Yorker,
  2023-02-09.
- Watson "five computers" apocrypha: IEEE Computer Society bibliography
  ("probably apocryphal"); https://deprogrammaticaipsum.com/five-computers/

## Toolkit & brand references

- Skill: `~/workspace/brutalist.art/skills/make/ai-explainer/SKILL.md`
  (extends `explainer`; Claude-brand fidelity, Teardown register,
  IN-FOR-BEAR LAW, bookend spine, SHOW-DON'T-TELL / DOUBLE-CHECK /
  REBUILD / FILL-THE-CANVAS laws).
- Static QC: `~/workspace/brutalist.art/runtime/qc/static_scene_check.py`.
- Palette tokens: claude cream `#F2F0E9`, ink `#3D3929`, terracotta `#D97757`
  (per ai-explainer brand facts).

## Seeds & determinism

- No generative randomness in the package. `make_sheet.py` is
  deterministic; scene layouts are hand-placed coordinates. Re-running
  `make_sheet.py` reproduces `beat_sheet.json` byte-for-byte.

## Credits

- Argument and quote list: Ruben Hassid ("How to AI").
- Verification: web research 2026-10-03 (see FACTCHECK.md).
- Package: Muse (film-package builder), for Bear / Humanitarians AI.
- Channel: https://www.youtube.com/@humanitariansai — watermark @NikBearBrown.
