---
status: DRAFT
todos_open: 11
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Pre-Launch Simulation

## Purpose

Runs a read-only pre-launch forecast for the approved campaign before budget commitment. The Simulator, using the Athena Agentic App, models expected outcomes such as open rate, CTR, conversion, and revenue.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-pre-launch-simulation.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| QA gate | JSON | `logs/gate-G4-qa.json` | Yes |
| Campaign package | JSON/files | Verified campaign, copy, and QA outputs | Yes |
| Propensity score metadata | JSON | Madison score metadata | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-pre-launch-simulation.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-pre-launch-simulation.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-pre-launch-simulation/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-pre-launch-simulation data/verified/madison-pre-launch-simulation -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-pre-launch-simulation-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-pre-launch-simulation.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-pre-launch-simulation-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-pre-launch-simulation.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-pre-launch-simulation-[DATE].json && test -f reports/generated/madison-pre-launch-simulation-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-pre-launch-simulation-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-pre-launch-simulation-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-pre-launch-simulation/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-pre-launch-simulation-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-pre-launch-simulation/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-pre-launch-simulation-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-pre-launch-simulation/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-pre-launch-simulation-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-pre-launch-simulation-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-pre-launch-simulation`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-pre-launch-simulation-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-pre-launch-simulation-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Pre-Launch Simulation` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if Gate G4 is missing or not approved.
- Stop if the simulator tool attempts live activation, budget commitment, or production mutation.
- Stop if score age is unknown in production without `[TODO: DEFINE] confirm score refresh date`.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-pre-launch-simulation --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-pre-launch-simulation --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-pre-launch-simulation --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-pre-launch-simulation --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-pre-launch-simulation --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-pre-launch-simulation --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-pre-launch-simulation --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-pre-launch-simulation --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-pre-launch-simulation --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-pre-launch-simulation --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-pre-launch-simulation --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-pre-launch-simulation --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-pre-launch-simulation --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-pre-launch-simulation --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-pre-launch-simulation-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-pre-launch-simulation-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-pre-launch-simulation-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-pre-launch-simulation-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-pre-launch-simulation-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-pre-launch-simulation-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-pre-launch-simulation/` | JSON |
| Verified data | `data/verified/madison-pre-launch-simulation/` | JSON |
| Agent log | `logs/madison-pre-launch-simulation-[DATE].json` | JSON |
| Human report | `reports/generated/madison-pre-launch-simulation-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-pre-launch-simulation.md` | `test -f "recipes/madison-pre-launch-simulation.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Runs a read-only pre-launch forecast for the approved campaign before budget commitment. The Simulator, using the Athena Agentic App, models expected outcomes such as open rate, CTR, conversion, and revenue.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-pre-launch-simulation.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-pre-launch-simulation --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-pre-launch-simulation data/verified/madison-pre-launch-simulation -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-pre-launch-simulation.md`.
   Human capacity: [EI].

1. Step name: Verify QA approval. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: logs/gate-G4-qa.json.
   Output: approval check with gate status and reviewer_capacity.
   Where output goes: logs/gate-decisions/.
2. Step name: Run simulator forecast. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-tool-simulator-forecast.py`
   Input: approved campaign package and score metadata.
   Output: forecast JSON fields: open_rate_estimate, ctr_estimate, conversion_estimate, revenue_estimate, score_age_days, staleness_warning, assumptions.
   Where output goes: logs/.
