# BUILD-LOG — claude-for-legal--claude-liam-client-letter

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-client-letter/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `client-letter`.

**Invocation state on pickup:** this reel arrived with SCRIPT.md, CARRY-OUT.md,
QUESTION.md, beat_sheet.json, mp3/, media/, clips/, manim/, scenes.py,
render_scenes.py, TYPECHECK.md, and a compiled master already present from a
prior session — but no BUILD-LOG.md. Checked freshness per the COMPLETION LAW:
the existing master (`claude-for-legal--claude-liam-client-letter.mp4`, mtime
15:15:06) predated a manim re-render of `manim/B01.mp4` (mtime 15:21:40) and a
touch of `scenes.py`/`beat_sheet.json` at 15:21 — i.e. a fix had already been
applied to the B01 scene AFTER the previous compile, making that master STALE.
Per the law ("if a sheet fix is needed after compiling, apply it and
RECOMPILE"), did not touch beat_sheet.json further and instead re-ran
`compile.py . --force` to produce a fresh master incorporating the corrected
B01. The compile auto-backgrounded past the tool's 120s timeout; blocked on it
explicitly by polling its output file in the foreground rather than ending the
turn (per the ONE-SHOT warning), confirmed exit code 0.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), matching the
identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-case-brief` and `-build-guide` sibling redos.
The SKILL.md client-letter was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/client-letter/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what client-letter's particular
legal-clinic procedure does. This redo treats "client-letter" literally and
generically — the named example of a skill-shaped folder, using only the
well-known, generic shape of a client letter (what happened, what it means,
what happens next) as anchor flavor — and never asserts an invented
procedure from the unread SKILL.md. Logged in QUESTION.md and SCRIPT.md too.

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `case-brief` / `build-guide` sibling redos, which hit the same
source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
client-letter skill" means the model itself learned client correspondence.
Typed text: "Claude learned client letters / from the client-letter skill. /
What is a skill?", trigger "learned" → replacement "was given", ending on
the real question. Rendered `media/B00.mp4` = 11.4s (compile log), clearing
the ≥8s WRITER LAW floor with margin.

**Body beats (B01-B07):** Manim GRAPHIC scenes in this reel's own `scenes.py`.
Anchor pair: B03 plants `client-letter/` + `SKILL.md` as two plain chips; B06
returns the identical composition with `SKILL.md` accented. Close: BCRY
`WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (`folderLabel:
"@HumanitariansAI"` set explicitly), BOUT `OutroCTA` (@HumanitariansAI).

**GATE T (type_check.py): PASS** — 0 FAILs across all 11 beats (TYPECHECK.md,
run 2026-08-29T15:23).

**Compile:** `compile.py . --force` forced a clean 3840×2160 master directly
(no declared slates — all 11 beats real media, lane-check PASS, content-check
PASS, frame-check PASS). `claude-for-legal--claude-liam-client-letter.mp4`,
114.8s. One non-blocking WARNING carried through compile: GRAPHIC beats are
7/11 (63%), over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; every GRAPHIC beat is original,
locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled frames at ~1 per 8s across the full runtime
plus a fine-grained pass (1 per 2s) across the B04→B05 transition, and read
every sampled frame by hand — all legible, correct chip/box content, safe
insets, no overlapping text, 4.5:1+ contrast, the B03→B06 anchor pair
visually identical as intended, B07's paired-box layout with strike-through
reads cleanly, B00's typing correction ("learned" → "was given") visible
mid-beat, and the BOUT outro (white bg, serif title restate, SUBSCRIBE +
@HumanitariansAI) renders correctly. One apparent all-blank frame at the
coarse 8s sampling (t=56s) was re-checked at 2s granularity and resolved to
be a normal cut-point, not a rendering defect — content is present on both
sides of that instant.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −2.5 dB — comfortably clears the
−40 dB floor. Verified independently of compile.py's own GATE AUDIO PASS
report (which matched).

**Master vs. beat_sheet.json:** master mtime (15:34:37) is newer than
beat_sheet.json's last touch (15:21:48) — beat_sheet.json was NOT touched
again after this recompile, per the "never touch beat_sheet.json after
compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field), which resolves to
**"Claude Basics."** Not the bare "Claude," per the PLAYLIST LAW.

**Delivery:** wrote
`claude-for-legal--claude-liam-client-letter.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Compiled master is already genuine 3840×2160, so
`claude-for-legal--claude-liam-client-letter-4k.mp4` is a copy of the
compiled master (Remotion beats are natively 4K; Manim beats are upscaled
into the 4K canvas by the compile step itself). Ran `deliver.py --push` to
stage `DELIVERY/claude-for-legal--claude-liam-client-letter/` and commit
text artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-client-letter/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual legal-clinic client-letter
procedure is asserted anywhere in this reel.
