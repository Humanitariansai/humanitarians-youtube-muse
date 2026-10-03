# BUILD-LOG — why-invisible-change-can-flip-models-mind

- **Reel**: `why-invisible-change-can-flip-models-mind`
- **Topic**: Computational Skepticism for AI — Candidate 04: Why an Invisible Change Can Flip a Model's Mind
- **Book Chapter**: Chapter 4 (`04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`)
- **Date**: 2026-08-29
- **Register**: Plain (Explaining the linear accumulation mechanism $\Delta f = \epsilon \|w\|_1$ and FGSM without Teardown judgment)
- **Voice / Engine**: Kokoro `am_onyx` (free local neural TTS)
- **Total Duration**: 178.6s (02:58)
- **Canvas / Resolution**: 3840×2160 (4K clean master)
- **Beats**: 15 beats (15/15 filled, 0 slates)
  - `B00`: Remotion `BrutalistHesitantWriter` (10.35s) — Types naive "random noise" question, hesitates, corrects to "accumulated linear math"
  - `B01`: Manim `B01Scene` (13.61s) — Clean Panda image vs faint $\epsilon = 0.007$ perturbation budget
  - `B02`: Manim `B02Scene` (12.39s) — Goodfellow 2014 panda-to-gibbon (57.7% panda -> 99.3% gibbon)
  - `B03`: Manim `B03Scene` (11.43s) — The core question: why doesn't tiny noise average out to zero?
  - `B04`: Manim `B04Scene` (11.88s) — The linear scoring mechanism $f(x) = w^T x = \sum w_i x_i$
  - `B05`: Manim `B05Scene` (12.29s) — Random vs Coordinated noise ($\mathbb{E} \approx 0$ vs deliberate alignment)
  - `B06`: Manim `B06Scene` (15.49s) — Fast Gradient Sign Method: $\eta = \epsilon \operatorname{sign}(w)$ aligns every coordinate
  - `B07`: Manim `B07Scene` (13.99s) — Kinetic accumulation demo: $\Delta f = \epsilon \|w\|_1 = \epsilon \sum |w_i|$
  - `B08`: Manim `B08Scene` (11.90s) — Numerical scale calculation: $d = 100{,}000$, $\epsilon = 1/255$, $\Delta f = 196$
  - `B09`: Manim `B09Scene` (14.29s) — The linear hypothesis: high-dimensional linearity creates fragility
  - `B10`: Manim `B10Scene` (8.51s) — Both directions: clean accuracy vs worst-case coordinate alignment
  - `B11`: Manim `B11Scene` (9.13s) — Summary: invisible to human eyes, massive in accumulated sum
  - `BCRY`: Remotion `WantQuote` (7.87s) — Carry-out sentence
  - `BHTF`: Remotion `ClaudeComposerAsk` (19.65s) — Paste-ready verification prompt for practitioners
  - `BOUT`: Remotion `OutroCTA` (4.86s + 1.0s tail) — Channel outro with @HumanitariansAI skin

## Verification Gates
- **Audio Check**: PASS (mean volume: -23.9 dB, max volume: -3.0 dB)
- **Gate T (Typecheck)**: PASS (All text runs $\ge 28\text{px}$, WCAG 4.5:1 contrast `#3D3929` on `#FAF9F5`, `#D97757` terracotta accent)
- **Gate V (Visual Inspection)**: PASS (4K frames inspected at key moments: clean layout, no collisions, elegant mathematics)
- **No-GenAI / No-Pantry Law**: PASS (100% Manim + Remotion, 0 AI video, 0 stock assets)
- **Output Artifacts**:
  - `why-invisible-change-can-flip-models-mind.mp4` (4K Master)
  - `why-invisible-change-can-flip-models-mind-4k.mp4` (4K Fellow-facing master)
  - `why-invisible-change-can-flip-models-mind.md` (YouTube metadata & description)
  - `beat_sheet.json` (Structured beat sheet)
  - `SCRIPT.md` (Narration script)
  - `QUESTION.md` (Asker question)
  - `CARRY-OUT.md` (Carry-out line)
