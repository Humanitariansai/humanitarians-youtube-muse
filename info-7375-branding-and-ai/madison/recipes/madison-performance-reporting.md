---
status: DRAFT
todos_open: 12
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Performance Reporting

## Purpose

Generates post-launch performance reporting after a campaign has been live for a defined window. The Analytics - Insights Studio Agent queries cross-channel performance data and produces comparative trend breakdowns.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-performance-reporting.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Launch approval | JSON | `logs/gate-G5-launch.json` | Yes |
| Campaign ID | String | `[TODO: DATA SOURCE] campaign tracking source` | Yes |
| Reporting window | Date range | `[TODO: DEFINE] define window` | Yes |
| Insights Studio data | Query result | Madison Insights Studio | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-performance-reporting.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-performance-reporting.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-performance-reporting/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-performance-reporting data/verified/madison-performance-reporting -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-performance-reporting-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-performance-reporting.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-performance-reporting-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-performance-reporting.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-performance-reporting-[DATE].json && test -f reports/generated/madison-performance-reporting-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-performance-reporting-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-performance-reporting-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-performance-reporting/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-performance-reporting-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-performance-reporting/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-performance-reporting-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-performance-reporting/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-performance-reporting-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-performance-reporting-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-performance-reporting`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-performance-reporting-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-performance-reporting-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Performance Reporting` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if campaign ID is missing or ambiguous.
- Stop if reporting window is undefined.
- Stop if Insights Studio access is not approved.
- Stop if report omits the limitation about propensity-score outcome tracking.
- Stop if the tool attempts to mutate campaign state.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-performance-reporting --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-performance-reporting --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-performance-reporting --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-performance-reporting --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-performance-reporting --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-performance-reporting --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-performance-reporting --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-performance-reporting --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-performance-reporting --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-performance-reporting --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-performance-reporting --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-performance-reporting --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-performance-reporting --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-performance-reporting --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-performance-reporting-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-performance-reporting-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-performance-reporting-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-performance-reporting-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-performance-reporting-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-performance-reporting-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-performance-reporting/` | JSON |
| Verified data | `data/verified/madison-performance-reporting/` | JSON |
| Agent log | `logs/madison-performance-reporting-[DATE].json` | JSON |
| Human report | `reports/generated/madison-performance-reporting-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-performance-reporting.md` | `test -f "recipes/madison-performance-reporting.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Generates post-launch performance reporting after a campaign has been live for a defined window. The Analytics - Insights Studio Agent queries cross-channel performance data and produces comparative trend breakdowns.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-performance-reporting.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-performance-reporting --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-performance-reporting data/verified/madison-performance-reporting -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-performance-reporting.md`.
   Human capacity: [EI].

1. Step name: Verify launch record. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: logs/gate-G5-launch.json and campaign ID.
   Output: reporting readiness fields: campaign_id, reporting_window, launch_approval_status.
   Where output goes: logs/gate-decisions/.
2. Step name: Generate performance report. Labor: AI with Human review.
   Script called: `scripts/tools/madison-tool-performance-report.py`
   Input: campaign ID, reporting window, Insights Studio data.
   Output: markdown report sections plus JSON log fields: campaign_id, window_start, window_end, channel_metrics, trend_breakdown, propensity_score_limitation.
   Where output goes: reports/generated/.
