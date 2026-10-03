# NEU course conversion template

**Predict → Build It → Use It → Ship It → Verify**

Use this as the reusable conversion contract for a book becoming an NEU course. Start with the book's actual claims and exercises, choose a concrete artifact per lesson, and cross-reference specific companion passages only when they add something to that artifact.

## Predict

The learner records an expectation before seeing the output or a reference solution: result, confidence, assumptions, and an observation that would change the prediction. Keep the first record; add a dated revision after learning. A wrong honest prediction is useful evidence, not a grading penalty.

## Build It

Implement the smallest mechanism in Python. Begin with an understandable input/output contract, a worked example, and failure boundaries. Claude Code may explain syntax, challenge a plan, or assist implementation, but the learner makes an initial attempt and must explain the resulting mechanism. Standard-library implementations precede frameworks. Credit borrowed code and AI assistance.

## Use It

Apply the mechanism to a domain question with Claude Code. Freeze evaluation inputs and record commands, outputs, assumptions, and revisions. Distinguish fixtures, simulations, actual Claude interactions, and direct API calls. API credits are not required for the core sequence.

## Ship It

Package a candidate artifact another person can inspect: README, code, tests, inputs or retrieval instructions, evidence, original predictions, human/AI contribution record, and Frictional log. A candidate can be shipped locally for inspection; this stage does not require deployment or an unverified public release.

## Verify

Check the packaged candidate against its acceptance criteria using independent calculations, source inspection, final-state checks, or reproduction. Record what was checked, by whom or what, what failed, and what remains uncertain. If it fails, revise and repeat Ship It → Verify. The final Canvas/GitHub submission identifies the checked revision. Agreement between models alone is not an independent check.

## Course and book boundary

Keep narrative reading in chapters/ and activity instructions in lessons/. Each lesson names its exact source file and reading selection. Put NEU access, grading, submission rules, and optional Brutalist preparation in prerequisites/. Assessments are ungraded; Assignments occur every ten days and use 60/10/10/20 scoring. Never import another book's old points or video requirements.

Append Anthropics, Conducting AI, Branding and AI, or Irreducibly Human only where relevant. Name the specific contribution and apply it to the current artifact. Irreducibly Human must explicitly say **AI should** and **Human should** with concrete tasks. A book's philosophical thesis is an argument to examine, not proof of a universal technical limit.

For a new conversion: inventory the source, select readings explicitly, write the lesson and assignment maps, create concrete exercise contracts and verification cases, adapt the term prerequisites, validate links and points, and record unresolved official logistics. Preserve earlier editions and student records.

