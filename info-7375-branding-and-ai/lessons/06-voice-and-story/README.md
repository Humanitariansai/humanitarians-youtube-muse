# Lesson 6 — A brand voice must survive a factual check

**Predict → Build It → Use It → Ship It → Verify**

Reading: [Chapter 10](../../chapters/10-brand-voice-and-storytelling.md). See the [reading map](../../docs/reading-map.md) for this semester's adaptations. Tools: Claude Code and Python standard library. Prerequisites: previous lessons and the running brand project. Suggested pacing: one class session plus practice; Canvas controls dates.

## Predict

Which voice choice could make the message less accurate or less useful? Predict a failure before generating copy. Record the expectation, assumptions, and a possible falsifier in PREDICTIONS.md before reviewing Claude's output. Preserve the first entry when recording later findings.

## Build It

Build a Python copy-review linter using explicit voice rules and claim IDs. Flag prohibited phrases, missing evidence references, and length constraints; keep stylistic flags separate from factual findings. Make an initial attempt before asking for a complete solution. Use learning-artifacts/06-voice-and-story/ for main.py, test_main.py, inputs, and outputs. The Python check supports the brand decision; it does not make that decision for you.

## Use It

Ask Claude to draft an introduction, a product description, and an error message from the same voice brief. Revise the copy and explain where consistency requires different expression. Record actual prompts, model identifier as displayed, date, commands, and outputs. Label fictional brands, synthetic data, simulated feedback, and mock campaigns. Claude Code is assumed; direct API calls are optional and may consume separate credits.

## Ship It

Deliver voice guide, three copy samples, linter output, and revision diff. Add README.md with exact reproduction commands, PREDICTIONS.md, CONTRIBUTIONS.md, FRICTIONAL.md, and VERIFICATION.md from the [templates](../../templates/README.md). Package a local candidate ready for review. The [Assignment map](../../assignments/fall-2026/README.md) specifies final submission.

## Verify

Test an unsupported claim in perfect brand voice and accurate copy that triggers a false stylistic flag. Human review decides context and meaning. Check the packaged candidate rather than only the development copy. Record actual results and unresolved limits. If a check fails, revise, ship, and verify again. Compare the outcome with your prediction.

### Assessments — ungraded

1. Produce the brand artifact and supporting Python mechanism.
2. Run the specified positive and failure cases and explain one result yourself.
3. Identify a case in which the code passes but the brand claim or decision remains unsupported.

<details>
<summary>Check your explanation after responding</summary>

A schema, rule, or calculation validates only its specified contract. Audience fit, factual support, creative effectiveness, and authority require their own evidence and judgment. Point to the specific remaining question in your artifact.

</details>

The book's older exercise requirements and tool stacks do not govern this semester's graded work. These Assessments are ungraded practice; use the separate 100-point Assignment briefs.

## Computational Skepticism

[Companion reading](../../docs/reading-map.md#computational-skepticism): the toolkit's checkable claims and the uncertainty chapter's calibrated wording. Name what could falsify one important brand claim, then check the supporting evidence before shipping it.
## Irreducibly Human

**AI should** draft and vary copy while checking explicit constraints.

**Human should** choose the voice, verify promises, and edit for audience and context.

Record the actual division in CONTRIBUTIONS.md: accepted, changed, rejected, or still uncertain. Do not invent audience feedback, testimonials, approvals, or creative decisions that a person did not make.

