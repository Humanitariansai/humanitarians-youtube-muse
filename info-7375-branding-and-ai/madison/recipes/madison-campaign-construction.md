---
status: DRAFT
todos_open: 12
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Campaign Construction

## Purpose

Builds the campaign skeleton from the approved brief and personas. The Campaign Builder Agent and Experience Builder and Insights Agent define channel mix, A/B test structure, send schedule, and journey branches.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-campaign-construction.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Client brief | JSON | `data/raw/madison-branding-marketing-pipeline/brief.json` | Yes |
| Verified personas | JSON | `data/verified/madison-branding-marketing-pipeline/personas-verified.json` | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-campaign-construction.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-campaign-construction.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-campaign-construction/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-campaign-construction data/verified/madison-campaign-construction -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-campaign-construction-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-campaign-construction.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-campaign-construction-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-campaign-construction.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-campaign-construction-[DATE].json && test -f reports/generated/madison-campaign-construction-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-campaign-construction-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-campaign-construction-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-campaign-construction/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-campaign-construction-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-campaign-construction/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-campaign-construction-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-campaign-construction/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-campaign-construction-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-campaign-construction-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-campaign-construction`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-campaign-construction-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-campaign-construction-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Campaign Construction` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if Gate G2 is missing or not approved.
- Stop if requested channels are missing from the campaign structure.
- Stop if campaign branches cannot be mapped to personas or segments.
- Stop if CTV is included and budget threshold evidence is missing; add `[TODO: DEFINE] confirm Madison CTV minimums`.
- Stop if Gate G3 is not approved.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-campaign-construction --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-campaign-construction --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-campaign-construction --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-campaign-construction --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-campaign-construction --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-campaign-construction --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-campaign-construction --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-campaign-construction --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-campaign-construction --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-campaign-construction --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-campaign-construction --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-campaign-construction --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-campaign-construction --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-campaign-construction --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-campaign-construction-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-campaign-construction-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-campaign-construction-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-campaign-construction-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-campaign-construction-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-campaign-construction-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-campaign-construction/` | JSON |
| Verified data | `data/verified/madison-campaign-construction/` | JSON |
| Agent log | `logs/madison-campaign-construction-[DATE].json` | JSON |
| Human report | `reports/generated/madison-campaign-construction-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/raw/madison-branding-marketing-pipeline/brief.json` | `test -f "data/raw/madison-branding-marketing-pipeline/brief.json"` | Referenced source/evidence path from prior recipe text. |
| `data/verified/madison-branding-marketing-pipeline/personas-verified.json` | `test -f "data/verified/madison-branding-marketing-pipeline/personas-verified.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Builds the campaign skeleton from the approved brief and personas. The Campaign Builder Agent and Experience Builder and Insights Agent define channel mix, A/B test structure, send schedule, and journey branches.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-campaign-construction.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-campaign-construction --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-campaign-construction data/verified/madison-campaign-construction -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-campaign-construction.md`.
   Human capacity: [EI].

1. Step name: Verify persona approval. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: logs/gate-G2-personas.json.
   Output: approval check with gate status and reviewer_capacity.
   Where output goes: logs/gate-decisions/.
2. Step name: Build campaign structure. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-gigo-campaign-structure.py`
   Input: brief.json and personas-verified.json.
   Output: campaign-structure-verified JSON fields: channel_mix, ab_tests, send_schedule, journey_branches, budget_flags, ctv_threshold_status.
   Where output goes: data/verified/madison-branding-marketing-pipeline/.
3. Step name: Gate G3 review. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: campaign-structure-verified.json.
   Output: gate decision with structure changes, channel approvals, and approval status.
   Where output goes: logs/gate-G3-campaign-structure.json.
