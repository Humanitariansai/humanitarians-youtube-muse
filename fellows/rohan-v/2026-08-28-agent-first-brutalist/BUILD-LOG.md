# BUILD-LOG — "Your Weekly Video, Handled."

Session date: 2026-08-28 · Toolkit: `brutalist.art` (fresh clone) · Cost: $0.00

## Phase 0 — install

`./setup --install` run to a green readiness table. Every core feature verified
live: Kokoro synth + decode, Manim, Remotion node deps, Pillow compile path,
bundled fonts. LaTeX left uninstalled — required only for Manim equation beats,
and this reel has none.

**Windows note:** `python3` resolves to the Microsoft Store stub unless the real
Python directory precedes `WindowsApps` on `PATH`. Prepended for every command in
this session; without it the readiness table reports false misses.

## Phase 1 — library-first (GATE L)

`./art scenes "…"` run per intended beat before any authoring.

**Reused from the library:** `ClaudeComposerAsk` (B00, B11), `ClaudeTitleOutro`
(B12), `OctoMark` from `GitHubRepoHero`, and the `claude` / `github` token sets.

**Genuine misses → built, not slated:** ten components. Each was a real gap —
nothing in the library covers the weekly-submission requirement, a Claude desktop
permission dialog, a fork-vs-branch git-graph, or a Drive upload. Registered
under the `hai-weekly-submission` folder in `Root.tsx` so the next fellow finds
them. **Slates used: zero.**

## Phase 2 — still-frame QC before any audio spend

All ten components rendered as stills and inspected. Defects found and fixed
*before* committing to audio:

| Defect | Scenes | Fix |
|---|---|---|
| Spark line descenders crossed the y=1026 title-safe line | 8 | Pinned to `bottom: height * 0.058` |
| `⎇` glyph absent from the UI font — rendered as `⌐` | 2 | Replaced with an inline SVG git-branch icon |
| Cards taller than their content, ~40% dead space | Recap | Restructured as a stretch-flex row that sizes to content |
| Dashed tick lines crossing label text | AudioClock | Opaque plate behind the label |
| Underfilled canvas, large empty band | Formats, DriveUpload | Enlarged frames; added a Drive drop-zone |
| URL block colliding with the Drive status bar | DriveUpload | Tightened row padding, moved the URL down |

## Phase 3 — audio is the clock

`generate_audio_kokoro.py`, voice `af_bella`, 13 beats, **254.0s total**.
Composition durations were then set *from* the measured mp3 lengths — not the
reverse. No timing was adjusted by hand at any point.

## Phase 4 — render

Two genuine cross-platform defects in the toolkit surfaced and were fixed:

| # | Defect | Fix | Impact |
|---|---|---|---|
| 1 | `remotion_scenes.py` invoked bare `npx`; on Windows npm ships `npx.cmd`, so `subprocess.run` raised `FileNotFoundError` | Resolve via `shutil.which`, falling back to `npx.cmd` | Rendering was **impossible** on Windows before this |
| 2 | `--concurrency=1` hardcoded, leaving 11 of 12 threads idle | `ART_CONCURRENCY` env override | 0.5 fps → 3.8 fps at 4K, a **7.6×** speedup. Full reel: ~4 hours → ~30 minutes |

All 13 beats rendered at `--scale=2` (true 3840×2160), each freeze-extended to
its exact measured beat length.

## Phase 5 — compile

`compile.py --height 2160`: **13/13 slots filled, all VIDEO, zero slates.**
Output 253.9s.

Advisory warning logged and accepted: motion histogram shows `illustrate` at
9/13 (69%) against a ~40% guideline. That cap governs *pantry* stills, which are
Ken-Burns-animated photographs. Every beat here is a purpose-built animated
Remotion composition, so the lane label is misleading — the reel contains no
still imagery at all.

## Phase 6 — GATE V, and the defect it did not catch

`final_frame_check.py`: 26 frames sampled, **BLOCKER 0, MAJOR 4**.

| Finding | Verdict |
|---|---|
| B07 low-contrast, separation 0.17 | **False positive.** The metric compares mean ink luminance against the background, which assumes dark ink on a light ground. B07 is GitHub's own dark surface: the "ink" average is dragged down by large dark panel fills (`#0d1117`, `#161b22`) sitting near the `#010409` background, while the actual text is `#f0f6fc` on near-black — far above any contrast requirement. Confirmed legible by inspection. |
| B12 underfill, 11% of safe area | **By design.** B12 is the shared `ClaudeTitleOutro`, a poster-style centred title card. Its negative space is the house outro convention and is inherited unchanged by every claude-brand reel. |

**The defect the gate missed, found by looking at the contact sheet:**

Every em-dash in a beat's *props* rendered as `â€"` — mojibake, burned into the
video. `remotion_scenes.py` read `beat_sheet.json` with `Path.read_text()`, which
uses the locale codec (cp1252 on Windows) rather than UTF-8.

Root cause proven by differential read: text coming from a component's own `.tsx`
source rendered correctly (esbuild reads UTF-8), while the identical character
coming through `props` did not. That split is what localised the bug to the
Python read rather than to the font, the renderer, or the beat sheet — the sheet
itself was verified clean at the byte level (`e2 80 94`).

Fix applied in `remotion_scenes.py` and `compile.py` (`encoding="utf-8"` on every
`read_text`/`write_text` handling a beat sheet or manifest). Note that the props are serialised with
`json.dump`, whose `ensure_ascii=True` default escapes non-ASCII — so the *write*
side was never at fault; only the read.

**A second defect, found while fixing the first:** three HTML entities
(`&rsquo;`, `&ldquo;`, `&rdquo;`) had been authored into `beat_sheet.json`. React
escapes entities in text nodes, so these would have rendered as the literal
string `machine&rsquo;s` on screen. Replaced with real Unicode characters and the
JSON re-validated before writing.

Both fixes together put **nine** beats out of date — B00, B01, B02, B04, B05,
B08, B09, B10, B11 — all re-rendered with `--force` and the reel recompiled.

This is exactly why the house rule is to verify by **looking at frames**, never
by the probe or the gate alone. Neither defect was caught by any automated check
in the pipeline: the mp4 probed clean, every gate passed, and the reel was the
correct length with correct audio. Both were only visible in a frame.

## Status

Built · compiled · QC'd · **not published**. There is no publishing machinery in
this toolkit by design; the master stays in this folder pending human review.
