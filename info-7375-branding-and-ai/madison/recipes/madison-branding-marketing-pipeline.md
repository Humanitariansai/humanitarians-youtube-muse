---
status: DRAFT
todos_open: 11
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Branding Marketing Pipeline

## Purpose

Draft Snickerdoodle recipe for a Madison branding and marketing pipeline. The first defined step ingests a client brief and converts it into structured JSON that later audience, channel, creative, budget, compliance, and reporting steps can use.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-branding-marketing-pipeline.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Client brief | PDF, document, or JSON | `[TODO: DATA SOURCE] intake location` | Yes |
| Channel list | Structured field or extracted text | Client brief | Yes |
| Audience description | Structured field or extracted text | Client brief | Yes |
| Suppression rules | Structured field or extracted text | Client brief | No |
| Brand safety constraints | Structured field or extracted text | Client brief | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-branding-marketing-pipeline.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-branding-marketing-pipeline.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-branding-marketing-pipeline/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-branding-marketing-pipeline data/verified/madison-branding-marketing-pipeline -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-branding-marketing-pipeline-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-branding-marketing-pipeline.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-branding-marketing-pipeline-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-branding-marketing-pipeline.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-branding-marketing-pipeline-[DATE].json && test -f reports/generated/madison-branding-marketing-pipeline-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-branding-marketing-pipeline-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-branding-marketing-pipeline-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-branding-marketing-pipeline/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-branding-marketing-pipeline-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-branding-marketing-pipeline/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-branding-marketing-pipeline-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-branding-marketing-pipeline/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-branding-marketing-pipeline-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-branding-marketing-pipeline-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-branding-marketing-pipeline`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-branding-marketing-pipeline-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-branding-marketing-pipeline-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Branding Marketing Pipeline` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if the client brief is missing or cannot be read.
- Stop if `objective`, `channels`, or `audience_description` is missing.
- Stop if the extracted text is garbled or materially incomplete.
- Stop if suppressions or brand safety constraints are present in the source but missing from `brief.json`.
- Stop if the brief contains credentials, private tokens, or unapproved personal data that would be copied into outputs.
- Stop if any downstream live campaign action is requested before human approval.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-branding-marketing-pipeline --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-branding-marketing-pipeline --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-branding-marketing-pipeline --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-branding-marketing-pipeline --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-branding-marketing-pipeline --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-branding-marketing-pipeline --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-branding-marketing-pipeline --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-branding-marketing-pipeline --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-branding-marketing-pipeline --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-branding-marketing-pipeline-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-branding-marketing-pipeline-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-branding-marketing-pipeline-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-branding-marketing-pipeline-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-branding-marketing-pipeline-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-branding-marketing-pipeline-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-branding-marketing-pipeline/` | JSON |
| Verified data | `data/verified/madison-branding-marketing-pipeline/` | JSON |
| Agent log | `logs/madison-branding-marketing-pipeline-[DATE].json` | JSON |
| Human report | `reports/generated/madison-branding-marketing-pipeline-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-branding-marketing-pipeline.md` | `test -f "recipes/madison-branding-marketing-pipeline.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Draft Snickerdoodle recipe for a Madison branding and marketing pipeline. The first defined step ingests a client brief and converts it into structured JSON that later audience, channel, creative, budget, compliance, and reporting steps can use.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-branding-marketing-pipeline.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-branding-marketing-pipeline --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-branding-marketing-pipeline data/verified/madison-branding-marketing-pipeline -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-branding-marketing-pipeline.md`.
   Human capacity: [EI].

1. Step name: Verify brief provenance. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: approved intake file.
   Output: provenance entry with source_file, source_checksum, and approval status.
   Where output goes: logs/gate-decisions/.
2. Step name: Ingest Client Brief. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-ingest-client-brief.py`
   Input: PDF, document, or structured JSON intake form.
   Output: brief JSON fields: brand, objective, audience_description, channels, budget_range, timeline, suppressions, brand_safety_notes.
   Where output goes: data/raw/madison-branding-marketing-pipeline/.
3. Step name: Produce ingest report. Labor: AI with Human review.
   Script called: `scripts/tools/madison-branding-marketing-pipeline-produce-ingest-report.py`
   Input: brief.json and run log.
   Output: markdown sections: brief summary, missing fields, suppressions, brand safety constraints, next-step readiness.
   Where output goes: reports/generated/.
