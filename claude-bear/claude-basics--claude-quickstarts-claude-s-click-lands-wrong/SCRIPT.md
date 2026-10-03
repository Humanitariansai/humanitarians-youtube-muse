# Why Claude's Click Lands in the Wrong Spot — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`claude-basics/claude-quickstarts-claude-s-click-lands-wrong`, Teardown
register, unbuilt `ai-explainer` scaffold — 0/8 beats filled). Register:
**Plain**. 8 beats, matching the source's beat count exactly. Carry-out
derived from the source's mechanism beat (CARRY-OUT.md, GATE C) — already a
factual rule, not a design judgment, so it needed only a register label,
not a rewrite.*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Act | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer cold open | "People assume Claude's click is just random guessing. It isn't. It's scaling — Claude sees a smaller image than your screen. So why does Claude's click land in the wrong spot?" | Writer types "Claude's click is just random guessing."; "guessing" hesitates and corrects to "scaling"; lands on "Why does Claude's click land in the wrong spot?" |
| B01 | 1 the question | If Claude returns coordinates for a 1456 by 819 image, how do you translate them onto a 1920 by 1080 screen without the click landing wrong? | Manim: two labeled rectangles (SENT 1456×819 / SCREEN 1920×1080), a question mark bridging them |
| B02 | **4 ANCHOR PLANTED** | Say your screen is 1920 by 1080, but the API only sends Claude a 1456 by 819 view. Claude says click 700, 410. Sent raw, that misses — the coordinates belong to the smaller image, not your screen. | THE ANCHOR — small SENT rectangle with a dot at (700,410); a large SCREEN rectangle with the same raw dot landing off the button |
| B03 | 3 mechanism | Multiply Claude's coordinates by the ratio original over sent, per axis. That's the inverse of the resize — it maps the smaller image's pixels back onto your real screen. | Formula card: x′ = x·(screen_w / sent_w), y′ = y·(screen_h / sent_h) |
| B04 | **4 ANCHOR PAYOFF** | Back to 700, 410: scale by 1920 over 1456 and 1080 over 819, and you get 960, 540 — dead center on the button. The same math holds at any resolution: sent at 1456 by 819, a 2560 by 1440 screen still gets a perfect hit. | THE ANCHOR RETURNS — same SENT/SCREEN composition as B02, the scaled dot now landing on the button; a second, smaller resolution pair confirming the ratio generalizes |
| **BCRY** | **6 carry-out** | Multiply Claude's coordinates by original over sent, per axis — that inverse ratio is what turns a smaller image's pixels back into your real screen's pixels. | the sentence, alone, serif, large |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. My computer-use app sends Claude a 1456 by 819 view of a 1920 by 1080 screen. Claude returns click coordinates in the view's coordinate space. Show me the two-line scaling formula I need before passing those coordinates to the OS input driver, and explain what happens if I skip it on a Retina display with a device pixel ratio of two. Liam, in for Bear. | `ClaudeComposerAsk` — "Your turn." |
| BOUT | outro | Why Claude's click lands in the wrong spot — and the one ratio that fixes it. Liam, in for Bear. | `OutroCTA` — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, `ai-explainer` scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why Claude's click lands in the wrong spot — and the one ratio that fixes it" | unchanged |
| Facts | resize the API sends (1456×819) vs. the real screen (1920×1080); scale by original÷sent per axis; the (700,410)→(960,540) worked case; the (728,409)→(1280,720) confirming case at a different resolution | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) — never built (0/8 filled) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` text-card cold open, itself the (700,410)→(960,540) worked case | `BrutalistHesitantWriter` (WRITER LAW) — "guessing" → "scaling"; the worked case moved to B02/B04 as the anchor pair |
| Register | Teardown (metadata; narration itself was pure arithmetic, no judgment language) | Plain — no design-judgment clauses existed to cut; only the framing (question→tension→mechanism→payoff) was reshaped into the anchor-pair spine |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | source's YOURTURN/OUTRO used `ClaudeComposerAsk` / `ClaudeTitleOutro`, `@NikBearBrown` | `ClaudeComposerAsk` (unchanged pattern) / `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Body B01–B04 | source's B01 (question) / B02 (tension, no visual) / B03 (mechanism) / B04 (second worked example) / B05 (mechanism recap) — `FormBCard`, now a banned component | rebuilt as Manim GRAPHIC scenes (`scenes.py`) — same facts, same order, B05's verbatim recap promoted to BCRY as the carry-out |

**Component note:** the source's body beats used `FormBCard`, which
`./art scenes --check FormBCard` confirms is now retired ("SlateCard
composition deleted 2026-08-26 — banned card form, never to return"). This is
not a NO-GENAI/NO-PANTRY substitution (FormBCard was never AI-video, pantry,
or human-drop) — it's a retired-component swap, so the body was rebuilt as
custom Manim scenes carrying the identical facts and sequence, per the
standard GRAPHIC beat pipeline (`scenes.py` + `render_scenes.py`).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the mechanism waits until B03 |
| Wrong guess surfaced and falsified by a case | B00 states it directly ("just random guessing") and B02's concrete miss, then B03's mechanism, falsifies it — it's not guessing, it's a fixed, computable ratio |
| No design judgment | source narration was already pure arithmetic/mechanism; no verdict language existed to remove |
| One running anchor, planted and paid off | B02 plants (700,410) sent raw → misses; B04 pays it off, scaled → (960,540), dead center |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not naming a specific resize algorithm.** The source doesn't specify how
  the vision API downscales the image, so the reel doesn't invent one.
- **Not a claim about every computer-use framework.** The ratio generalizes
  mathematically, but the reel demonstrates it on the one input/output pair
  the source gives, plus the source's own second resolution as confirmation.
- **No verdict on the API's design.** Explaining why the coordinates need
  scaling is not the same as ruling on whether sending a downscaled
  screenshot is the right way to build a vision API — that's Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "My computer-use app sends Claude a 1456 by 819 view of a 1920 by 1080
> screen. Claude returns click coordinates in the view's coordinate space.
> Show me the two-line scaling formula I need before passing those
> coordinates to the OS input driver, and explain what happens if I skip it
> on a Retina display with a device pixel ratio of two."

Why it's worth running: it forces the viewer to apply the ratio to a case
the reel never solves for them — a Retina display, where a second scaling
factor stacks on top of the first.

---
**GATE P — signed:** ______________________  (human)
