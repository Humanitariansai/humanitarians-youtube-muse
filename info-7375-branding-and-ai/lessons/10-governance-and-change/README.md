# Lesson 10 — Make brand rules usable at the decision point

**Predict → Build It → Use It → Ship It → Verify**

Reading: [Chapter 14](../../chapters/14-brand-management-governance-and-rebranding.md). See the [reading map](../../docs/reading-map.md) for this semester's adaptations. Tools: Claude Code and Python standard library. Prerequisites: previous lessons and the running brand project. Suggested pacing: one class session plus practice; Canvas controls dates.

## Predict

Which small change will create unintended drift across your existing assets? Record the expectation, assumptions, and a possible falsifier in PREDICTIONS.md before reviewing Claude's output. Preserve the first entry when recording later findings.

## Build It

Build a Python asset manifest with versioned references to tokens, voice rules, claims, and owners. Mark dependent assets for review when a referenced rule changes. Make an initial attempt before asking for a complete solution. Use learning-artifacts/10-governance-and-change/ for main.py, test_main.py, inputs, and outputs. The Python check supports the brand decision; it does not make that decision for you.

## Use It

Ask Claude to propose a refresh and explain why it is needed. Apply one approved classroom change and inspect the impact on earlier work. Record actual prompts, model identifier as displayed, date, commands, and outputs. Label fictional brands, synthetic data, simulated feedback, and mock campaigns. Claude Code is assumed; direct API calls are optional and may consume separate credits.

## Ship It

Deliver versioned brand guidelines, asset dependencies, change record, and updated specimen. Add README.md with exact reproduction commands, PREDICTIONS.md, CONTRIBUTIONS.md, FRICTIONAL.md, and VERIFICATION.md from the [templates](../../templates/README.md). Package a local candidate ready for review. The [Assignment map](../../assignments/fall-2026/README.md) specifies final submission.

## Verify

Test a changed token affecting two assets, an unchanged asset, and an unknown version. A passing manifest does not prove the change is strategically wise. Check the packaged candidate rather than only the development copy. Record actual results and unresolved limits. If a check fails, revise, ship, and verify again. Compare the outcome with your prediction.

### Assessments — ungraded

1. Produce the brand artifact and supporting Python mechanism.
2. Run the specified positive and failure cases and explain one result yourself.
3. Identify a case in which the code passes but the brand claim or decision remains unsupported.

<details>
<summary>Check your explanation after responding</summary>

A schema, rule, or calculation validates only its specified contract. Audience fit, factual support, creative effectiveness, and authority require their own evidence and judgment. Point to the specific remaining question in your artifact.

</details>

The book's older exercise requirements and tool stacks do not govern this semester's graded work. These Assessments are ungraded practice; use the separate 100-point Assignment briefs.

## Conducting AI

[Companion reading](../../docs/reading-map.md#conducting-ai): explicit handoffs. State what passes to the next person or tool, what it is trusted to mean, and the evidence or approval required. Apply the condition to the current asset.
## Irreducibly Human

**AI should** identify dependencies and draft consistent revisions.

**Human should** decide whether to refresh or rebrand and approve the tradeoff.

Record the actual division in CONTRIBUTIONS.md: accepted, changed, rejected, or still uncertain. Do not invent audience feedback, testimonials, approvals, or creative decisions that a person did not make.

