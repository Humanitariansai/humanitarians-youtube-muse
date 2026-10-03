# Lesson 5 — Build a repeatable visual system

**Predict → Build It → Use It → Ship It → Verify**

Reading: [Chapter 9](../../chapters/09-visual-identity-systems.md). See the [reading map](../../docs/reading-map.md) for this semester's adaptations. Tools: Claude Code and Python standard library. Prerequisites: previous lessons and the running brand project. Suggested pacing: one class session plus practice; Canvas controls dates.

## Predict

Which palette, type, and spacing choices will communicate your strategy consistently? Predict a readability problem. Record the expectation, assumptions, and a possible falsifier in PREDICTIONS.md before reviewing Claude's output. Preserve the first entry when recording later findings.

## Build It

Build a Python script that reads JSON design tokens and produces an SVG identity specimen with colors, text hierarchy, and spacing examples. Validate hex colors, positive sizes, and missing required tokens. Make an initial attempt before asking for a complete solution. Use learning-artifacts/05-visual-identity/ for main.py, test_main.py, inputs, and outputs. The Python check supports the brand decision; it does not make that decision for you.

## Use It

Ask Claude Code to help implement the specimen from your creative brief. Compare two design directions and choose based on stated audience and strategy criteria. Record actual prompts, model identifier as displayed, date, commands, and outputs. Label fictional brands, synthetic data, simulated feedback, and mock campaigns. Claude Code is assumed; direct API calls are optional and may consume separate credits.

## Ship It

Deliver creative brief, tokens.json, generator, SVG specimen, and design rationale. Add README.md with exact reproduction commands, PREDICTIONS.md, CONTRIBUTIONS.md, FRICTIONAL.md, and VERIFICATION.md from the [templates](../../templates/README.md). Package a local candidate ready for review. The [Assignment map](../../assignments/fall-2026/README.md) specifies final submission.

## Verify

Inspect the rendered specimen for clipping, legibility, and consistency; test malformed colors and zero sizes. Document accessibility checks actually performed without claiming a complete accessibility certification. Check the packaged candidate rather than only the development copy. Record actual results and unresolved limits. If a check fails, revise, ship, and verify again. Compare the outcome with your prediction.

### Assessments — ungraded

1. Produce the brand artifact and supporting Python mechanism.
2. Run the specified positive and failure cases and explain one result yourself.
3. Identify a case in which the code passes but the brand claim or decision remains unsupported.

<details>
<summary>Check your explanation after responding</summary>

A schema, rule, or calculation validates only its specified contract. Audience fit, factual support, creative effectiveness, and authority require their own evidence and judgment. Point to the specific remaining question in your artifact.

</details>

The book's older exercise requirements and tool stacks do not govern this semester's graded work. These Assessments are ungraded practice; use the separate 100-point Assignment briefs.

## Irreducibly Human

**AI should** generate code and design alternatives within the brief.

**Human should** set creative direction, inspect the rendered work, and decide which system serves the audience.

Record the actual division in CONTRIBUTIONS.md: accepted, changed, rejected, or still uncertain. Do not invent audience feedback, testimonials, approvals, or creative decisions that a person did not make.

