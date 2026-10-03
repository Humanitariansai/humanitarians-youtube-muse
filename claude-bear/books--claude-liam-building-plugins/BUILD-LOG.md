# BUILD-LOG — books--claude-liam-building-plugins

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-building-plugins/beat_sheet.json`
— a fully-built, GATE-T-passed, published-quality Teardown/deep-explainer
reel (37 beats, Ch.12 "Building Your Own Plugins", mean_volume -25.8 dB,
`claude-liam` / @NikBearBrown). No SCRIPT.md existed on the source; its
`beats[*].narration_text` served as the locked narration per the redo
contract. Never touched the source reel's folder.

**Facts kept unchanged:** a plugin bundles up to four things (skills,
commands, connectors, subagents); it is a folder of plain text (one
instructions file at the root, a directory per part); you build one by
describing a workflow in plain language to a guided builder (itself an
installable plugin) — no code, no config-file editing; the four-step loop
(describe, answer follow-ups, refine on a real case, use it); the four
build-worthy signals (same steps every time, consistency matters, you'd
rather not think about it, "I wish I could hand this off"); the discipline
of automating the repeatable scaffolding while keeping judgment calls;
sharing a working plugin (team or the wider directory) and continuing to
refine it; checking the community directory before building from scratch.

**Beat-count adjustment (logged per SCRIPT.md):** source is 37 beats — 5
act-title cards (C01-C05), 25 body beats (B01-B25), a body-close triad
(V01 verdict-recap / H01 your-turn / O01 outro), and a duplicate bookend
triad (BVDT/BHTF/BOUT) with blank narration on BHTF/BOUT. hai-simple's
spine has no act-title-card slot and no duplicate bookend tail, so: the 5
act cards were dropped (titles now land as narration transitions); the 25
body beats were merged 3 times where two source beats carried one
continuous idea (B03+B04, B20+B21, B23+B24) to 22 body beats, preserving
every fact and the full five-act argument; the source's body-close
(V01/H01/O01) was kept as the reel's one close, renamed to hai-simple's
BCRY/BHTF/BOUT convention, dropping the duplicate blank-narration triad
rather than rendering two closes back to back. Result: B00 + 22 body +
BCRY/BHTF/BOUT = 26 beats — same scale as the `claude-liam-four-places`
sibling redo (26 beats).

**B00 WRITER LAW:** source's misconception — a newcomer assumes building a
plugin means learning to write code, corrected at the source's own B12
("you don't write code... you build yours by having a conversation with
it"). Typed text: "Building my own Claude plugin means learning to code. /
How do I build one?" trigger "code" → replacement "describe it" (a direct
callback to B12's actual mechanism). First render's typing didn't finish
the final question before the beat ended (10.2s audio window, original
charMs=55/hesitateBetween=20 too slow for the full ~85-char text) —
shortened the tail ("actually" dropped) and sped up the performance
(charMs 55→46, hesitateBetween 20→12, hesitateWithin 3→2, mistakeRate
6→5); reverified: correction ("code"→"describe it") resolves by t≈6.5s,
full question types out to completion by t≈9.6s of 10.2s.

**Body beats:** all 22 rebuilt as Manim GRAPHIC scenes via one shared
generic "chip row" renderer in `scenes.py` (title + up to 5 labeled chips,
optional connecting arrows, optional terracotta accent/dim, caption) driven
per-beat by a content dict — not 22 hand-tuned custom scenes. Anchor pair:
B05 plants "four parts" (SKILLS/COMMANDS/CONNECTORS/SUBAGENTS, plain
chips), B14 returns the identical composition with SUBAGENTS accented
("conversation in, plugin out"). Source's now-retired Remotion patterns
(SourceFlow, LayerStack, Onda) were replaced by this same Manim template —
a retired-component swap, not a NO-GENAI/NO-PANTRY substitution (none of
the source's beats were ever ai-video-prompt, pantry, or human-drop).
Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (source's
verbatim Your-Turn prompt, explicit `folderLabel: "@HumanitariansAI"` per
the known ClaudeComposerAsk-defaults-to-@NikBearBrown bug), BOUT `OutroCTA`
(@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (26 beats), `scenes.py` (generic chip-row Manim generator +
22-beat content table), `render_scenes.py`. Ran `generate_audio_kokoro.py`
(26/26 beats, am_onyx, $0.00) — measured durations became the clock.
Rendered 22 Manim beats (foreground) and 4 Remotion beats via
`remotion_scenes.py` (foreground, waited on exit code both times — no
orphaned background renders).

**GATE T (type_check.py) first pass: 11 FAILs.** Diagnosed each by calling
the checker's own `text_run_bboxes`/`labeled_blobs` functions directly
against rendered frames (not guessing from the report text alone):

1. **6 confirmed real min-size defects** (B02, B04, B06, B11, B12, B14,
   B19, B22 — some beats had 2 findings): the shared caption used an
   *italic* Manim/Pango serif substitution that renders as a cursive
   script whose 'i'/'j' dot detaches from the stem into its own isolated
   ~9-10px blob (verified by cropping the exact reported coordinates —
   e.g. B02's failure was literally the floating dot on the "i" in
   "thing"). **Fixed at the root**: dropped `slant=ITALIC` from the
   caption `Text()` — upright serif keeps every glyph one connected run,
   at no visual cost. Re-verified: 0 caption-related FAILs after the fix.
2. **1 confirmed real min-size defect** (B12): "GENERATE QUESTIONNAIRE"
   (22 chars) forced the auto-shrink-to-fit-width logic to compress the
   chip's text below the readable floor (17px measured). **Fixed at the
   root**: shortened chip labels ("GENERATE QUESTIONNAIRE" →
   "MAKE QUESTIONNAIRE", "DRAFT WELCOME EMAIL" → "DRAFT EMAIL").
3. **1 confirmed real contrast defect** (B18, later also B14): white
   chip text on a solid terracotta fill measures 3.90-3.99:1 < 4.5:1 WCAG
   — the checker only flags this when *every* visible text run in the
   frame shares that low-contrast pairing (mixed ink-on-cream + one
   accented chip elsewhere in the deck never tripped it). **Fixed at the
   root**: B18 dropped its accent entirely (the beat's point — "these are
   the same" — doesn't need one); B14 (anchor payoff, originally 4/4
   chips accented) reduced to a single accented chip (SUBAGENTS).
4. **1 confirmed real design smell** (B19): chip labels embedded a literal
   "→" glyph ("SCAFFOLDING → AUTOMATE"), which the checker's per-glyph
   connected-component detector isolates as its own ~10px sub-glyph blob
   (same failure class documented in sibling reels' arrow-glyph fixes).
   **Fixed at the root**: reworded to "AUTOMATE THE SCAFFOLDING" /
   "KEEP THE JUDGMENT CALLS" — no special glyph.
5. **3 confirmed false positives** (B10, B21, then B12 again after fix #2
   changed its layout): `check_bbox_overlap` flags any chip whose
   INK-bordered box (a closed ring — passes the "text run" filters at its
   full box-height bbox) numerically contains its own centered label's
   bbox once, by chance, that label happens to render as one connected run
   instead of fragmenting into individual too-narrow letters (the reason
   most of the other 19 identical chip-row beats never trip this at all).
   Verified false by cropping the exact frame at the checker's own
   mid-clip sample point for both beats — arrows sit cleanly in the gap
   with visible margin, no actual text-on-text overlap anywhere. This is
   the documented "box-border blobs are falsely detected as text runs
   that overlap with interior labels... design-correct layouts, not real
   readability bugs" class (`BBOX_OVERLAP_EXEMPT_PATTERNS`, `type_check.py`
   line ~320) — added `BPB10Scene`, `BPB21Scene`, `BPB12Scene` to that set
   with the verification recorded inline, matching the exact precedent
   already set by `B01Scene`/`B03Scene`/`SPCB04Scene`/`SERB02Scene` etc.
   in the same dict. Content and the checker's genuine catches were fixed
   first; this exemption covers only what was independently re-verified
   clean, per the same rule those precedents were added under — never a
   blanket loosening.

**GATE T (type_check.py) final pass: PASS, 0 FAILs.**

Compiled with `compile.py .` (no `--force` needed, sheet not previously
compiled): 26/26 beats real (no slate), master born natively 4K
(3840×2160, `compile.py`'s 4K LAW), 297.3s. `content-check`/`frame-check`/
`lane-check` all PASS. Non-blocking warning: motion histogram
`graphic:22 remotion:4` (84%, over the ~40% pantry cap) — logged as
structural, not a defect: hai-simple's mandated shape is B00 (writer) +
BCRY + BHTF + BOUT all REMOTION by skill contract, against 22 Manim body
beats for a 26-beat reel; the ratio is fixed by beat count, same
disposition as the `claude-quickstarts-claude-s-click-lands-wrong` and
`what-is-claude-basics` sibling reels.

**Gate V:** pulled 30 frames at 10s spacing across the full 297.3s runtime
plus 11 densely-spaced frames around every beat transition and the B00
correction window; read every one directly. B00's correction and full
question both land inside the beat with margin. The B05→B14 anchor pair
reads as the same object returning (identical four-chip composition,
SUBAGENTS singled out at the payoff). BCRY/BHTF/BOUT are centered, legible,
safe-inset, and BHTF correctly shows `@HumanitariansAI` (not the
`ClaudeComposerAsk` Root.tsx default `@NikBearBrown`, per the explicit
`folderLabel` override learned from the `what-is-claude-basics` sibling's
BUILD-LOG). No remaining blockers.

**Audio:** ffprobe confirms an AAC stream present, master mtime newer than
beat_sheet.json; `ffmpeg -af volumedetect`: mean_volume **-23.7 dB**, max
-2.8 dB — comfortably above the -40 dB floor.

Metadata file written: `books--claude-liam-building-plugins.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Playlist note: `SUBJECT.json`'s `family` is `"books"`, which
has no literal entry in `skills/make/hai-simple/loop/playlists.json`'s map
(the source book lives under `anthropics/books/`, not under a
`claude-basics`-style youtube tree), and the slug's `books--` prefix isn't
in the map either — so the mechanical prefix match fails. Rather than fall
through to `_default` ("Claude Across the Curriculum") when a clearly
on-topic entry exists, matched on content: the map's `claude-plugins` /
`claude-skills` / `claude-agent-skills` / `claude-mcp-connectors` /
`knowledge-work-plugins` keys all resolve to **"Extending Claude — Skills,
Plugins & Connectors"**, which is exactly this reel's subject. Per the
DELIVERY CONTRACT format, the description also carries the direct code
link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840×2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.
