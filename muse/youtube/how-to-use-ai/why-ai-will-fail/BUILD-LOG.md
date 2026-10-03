# BUILD-LOG.md — "AI will fail." (why-ai-will-fail)

## Decisions

1. **Skill: ai-explainer.** The film is one tight insight (the
   expert-dismissal pattern → the asymmetric bet on AI), not a multi-act
   documentary with several mechanisms — so ai-explainer, not
   deep-explainer. The source README itself recommends ai-explainer for
   "one tight insight". Channel facts applied: claude-liam, Liam "in for
   Bear" sign-in (B00) and sign-off (B13), Kokoro `am_onyx`, Teardown
   register, Claude fidelity palette, @NikBearBrown watermark bug on every
   beat, bookend spine (cold open → BLUF → body → verdict → handoff →
   title outro).
2. **Package-convention adaptation (deliberate).** The task's 12-file
   pre-render package (Manim-only `scenes.py`, no Remotion, no pantry) is
   the output contract here, so Remotion-specific laws (ClaudeComposerAsk
   cold open, BrutalistHesitantWriter B01, ClaudeTitleOutro) are honored in
   spirit — question-led cold open, one-breath overview, prompt handoff,
   title-restate outro — but rendered as Manim scenes. Recorded here, not
   silently passed.
3. **Restructure: 12 source beats → 14 film beats.** The source was a list
   with a Kore persona and remotion cards; the film adds a real overview
   (B01), splits the quote evidence across three paced beats (B02–B04),
   gives penicillin its own beat (B05), and separates mechanism (B06–B07),
   application (B08–B09), and payoff (B10) into acts.
4. **Fact-check corrections (see FACTCHECK.md).** Cut three famous but
   weakly-attributed quotes the source article presents as fact: Watson
   "five computers" (apocryphal), Gates "640K" (urban legend), Patent
   Office "everything invented" (disputed). Softened datable figures to
   orders of magnitude (cloud market, Oracle cloud revenue, penicillin
   lives saved). Framed the BMJ/penicillin claim inside what the sources
   support (the journal summarizing a study, not an editorial dismissal).
5. **Audience rewrite.** Every technical term explained in-line in ≤ one
   breath (streaming, cloud, VCR, Ethernet, penicillin, hallucinate,
   productivity statistics, snapshot vs trajectory, asymmetric bet,
   "blurry JPEG"). Show-don't-tell: the insider trap and the toy curve are
   drawn diagrams, not text cards; quotes and numbers live on screen while
   the voice judges them.
6. **No new facts invented.** All on-screen numbers come from FACTCHECK.md;
   the 2×2 matrix (B10) is labeled as the film's own synthesis.

## Gate signatures

- make_sheet.py: 14 beats, total 335.2 s (5.6 min), all assertions pass.
- py_compile: clean on make_sheet.py and scenes.py.
- static_scene_check.py: 14/14 classes clean, 0 warnings, 0 errors
  (after one fix — see below).

## Failures and fixes

- **SceneYourTurn failed static QC on first run** (1 error: "shapes never
  change — 1 distinct shape-state across 4 frames"). Cause: the beat's only
  non-text shape was the prompt card, so every snapshot had the identical
  shape set — a real instance of the repeated-animation defect the checker
  exists to catch. Fix: the handoff prompt now types line-by-line with a
  terracotta cursor bar that moves down per line (each play changes the
  shape state), and the cursor fades out as the footer appears. Re-ran:
  6 distinct states, clean. The fix also improves the real render (visible
  typing cursor).
- No other failures. No py_compile issues. No out-of-frame coordinates
  (all hand-placed inside |x| ≤ 6.3, |y| ≤ 3.4).

## Open / for Bear

- Narration audio (Kokoro am_onyx) and the Manim renders happen on Bear's
  Mac per CLAUDE-CODE-RENDER.md — nothing rendered or published from here.
- If Bear wants the Watson "five computers" anecdote back in, it must be
  framed as apocryphal ("often attributed, probably never said") — see
  FACTCHECK.md C1.
