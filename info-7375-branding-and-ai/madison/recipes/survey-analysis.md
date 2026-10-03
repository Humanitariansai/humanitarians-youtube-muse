---
status: DRAFT
todos_open: 14
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# survey-analysis

## Purpose

The survey-analysis workflow ingests survey responses, validates and cleans rows, prepares analysis and segmentation prompts, derives sentiment distribution and NPS, and prepares Slack, MySQL, and Grafana output contracts. This recipe preserves the imported workflow while replacing live OpenAI, Slack, MySQL, and Grafana side effects with local, auditable artifacts unless a human explicitly clears live execution.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Original workflow sources | [TODO: DEV] Parse original workflow node types. | [TODO: DATA SOURCE] Extract source URLs or paths from original workflow JSON. | Confirm source is allowed, current, and rate-safe before live fetch. |

| Node Name | Node Type | Classification |
|---|---|---|
| Original workflow node map | [TODO: DEV] Parse original n8n JSON. | [TODO: DEFINE] Classify parsed nodes as ingest, gigo, tool, conductor, or report. |
## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Original n8n workflow JSON | JSON | data/madison-main/n8n-workflows/originals/survey-analysis/workflow.json | Yes |
| Survey CSV | CSV rows | Published Google Sheet export, local CSV, or sample rows | Yes |
| Survey row | JSON object | Webhook payload or CSV extraction | Yes |
| Respondent fields | Text/number | `respondent_id`, `age`, `gender`, `q1_satisfaction`, `q2_easeofuse`, `q3_recommend` | Yes |
| Grafana datasource UID | Text | Grafana API or approved env var | Only for live dashboard update |
| Slack destination | Text | `#survey-analysis` in original workflow | Only for live Slack send |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/survey-analysis.md" && rg -n "\[TODO: DEFINE]" "recipes/survey-analysis.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/survey-analysis/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/survey-analysis data/verified/survey-analysis -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/survey-analysis-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/survey-analysis.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/survey-analysis-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/survey-analysis.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/survey-analysis-[DATE].json && test -f reports/generated/survey-analysis-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/survey-analysis-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/survey-analysis-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/survey-analysis/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/survey-analysis-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/survey-analysis/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/survey-analysis-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/survey-analysis/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/survey-analysis-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/survey-analysis-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `survey-analysis`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/survey-analysis-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/survey-analysis-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `survey-analysis` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if the original JSON is missing.
- Stop if live ingest is requested before sample ingest passes.
- Stop if required survey columns are missing or cannot be normalized.
- Stop if live model calls, Slack sends, MySQL inserts, or Grafana updates are requested without explicit clearance.
- Stop if output contracts would expose credentials, bearer tokens, webhook IDs, or raw PII beyond the approved fields.
- Stop if the NPS or sentiment summary cannot be reproduced from clean rows.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run survey-analysis --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run survey-analysis --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run survey-analysis --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run survey-analysis --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run survey-analysis --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run survey-analysis --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run survey-analysis --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run survey-analysis --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate survey-analysis --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate survey-analysis --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate survey-analysis --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate survey-analysis --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate survey-analysis --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate survey-analysis --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/survey-analysis-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/survey-analysis-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/survey-analysis-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/survey-analysis-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/survey-analysis-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/survey-analysis-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/survey-analysis/` | JSON |
| Verified data | `data/verified/survey-analysis/` | JSON |
| Agent log | `logs/survey-analysis-[DATE].json` | JSON |
| Human report | `reports/generated/survey-analysis-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/madison-main/n8n-workflows/originals/survey-analysis/workflow.json` | `test -f "data/madison-main/n8n-workflows/originals/survey-analysis/workflow.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

The survey-analysis workflow ingests survey responses, validates and cleans rows, prepares analysis and segmentation prompts, derives sentiment distribution and NPS, and prepares Slack, MySQL, and Grafana output contracts. This recipe preserves the imported workflow while replacing live OpenAI, Slack, MySQL, and Grafana side effects with local, auditable artifacts unless a human explicitly clears live execution.

1. Source identity gate: Original workflow JSON exists and is the intended source. Test: `test -f "data/madison-main/n8n-workflows/originals/survey-analysis/workflow.json"`.
   Human capacity: [PF].
2. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/survey-analysis.md`.
   Human capacity: [PA].
3. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run survey-analysis --mode dialogic --sample`.
   Human capacity: [TO].
4. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/survey-analysis data/verified/survey-analysis -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
5. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/survey-analysis.md`.
   Human capacity: [EI].

1. Step name: Verify provenance and source intent. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: data/madison-main/n8n-workflows/originals/survey-analysis/workflow.json.
   Output: provenance fields: workflow_path, exists, parsed_ok, title_matches_pipeline, source_inventory_checked.
   Where output goes: logs/gate-decisions/.
2. Step name: Map workflow or specification to scripts. Labor: AI with Human gate.
   Script called: `scripts/gigo/survey-analysis-map-workflow-or-specification-to-scripts.py`
   Input: recipe inputs and provenance evidence.
   Output: implementation map fields: steps, script_paths, missing_specs, typed_todos.
   Where output goes: data/verified/.
3. Step name: Produce human report. Labor: AI with Human review.
   Script called: `scripts/tools/survey-analysis-produce-human-report.py`
   Input: agent log plus raw and verified outputs.
   Output: markdown report sections: run summary, source inventory, inputs used, validation results, flags, typed TODOs, decision recommendation.
   Where output goes: reports/generated/.
