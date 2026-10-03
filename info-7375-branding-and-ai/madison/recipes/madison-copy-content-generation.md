---
status: DRAFT
todos_open: 11
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Copy And Content Generation

## Purpose

Generates channel, persona, and A/B variant copy from the approved campaign structure. The recipe uses Madison copy agents for subject lines, pre-headers, generational messaging, SMS, ZML, and campaign development.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-copy-content-generation.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Approved campaign structure | JSON | `data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json` | Yes |
| Verified personas | JSON | `data/verified/madison-branding-marketing-pipeline/personas-verified.json` | Yes |
| Client brief | JSON | `data/raw/madison-branding-marketing-pipeline/brief.json` | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-copy-content-generation.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-copy-content-generation.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-copy-content-generation/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-copy-content-generation data/verified/madison-copy-content-generation -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-copy-content-generation-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-copy-content-generation.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-copy-content-generation-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-copy-content-generation.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-copy-content-generation-[DATE].json && test -f reports/generated/madison-copy-content-generation-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-copy-content-generation-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-copy-content-generation-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-copy-content-generation/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-copy-content-generation-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-copy-content-generation/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-copy-content-generation-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-copy-content-generation/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-copy-content-generation-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-copy-content-generation-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-copy-content-generation`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-copy-content-generation-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-copy-content-generation-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Copy And Content Generation` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if Gate G3 is missing or not approved.
- Stop if spam threshold is undefined in production; add `[TODO: DEFINE] define threshold`.
- Stop if SMS variants exceed character limits.
- Stop if duplicate subject lines are not resolved or flagged.
- Stop if generated copy violates brand safety notes or suppressions.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-copy-content-generation --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-copy-content-generation --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-copy-content-generation --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-copy-content-generation --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-copy-content-generation --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-copy-content-generation --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-copy-content-generation --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-copy-content-generation --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-copy-content-generation --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-copy-content-generation --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-copy-content-generation --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-copy-content-generation --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-copy-content-generation --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-copy-content-generation --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-copy-content-generation-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-copy-content-generation-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-copy-content-generation-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-copy-content-generation-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-copy-content-generation-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-copy-content-generation-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-copy-content-generation/` | JSON |
| Verified data | `data/verified/madison-copy-content-generation/` | JSON |
| Agent log | `logs/madison-copy-content-generation-[DATE].json` | JSON |
| Human report | `reports/generated/madison-copy-content-generation-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/raw/madison-branding-marketing-pipeline/brief.json` | `test -f "data/raw/madison-branding-marketing-pipeline/brief.json"` | Referenced source/evidence path from prior recipe text. |
| `data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json` | `test -f "data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json"` | Referenced source/evidence path from prior recipe text. |
| `data/verified/madison-branding-marketing-pipeline/personas-verified.json` | `test -f "data/verified/madison-branding-marketing-pipeline/personas-verified.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Generates channel, persona, and A/B variant copy from the approved campaign structure. The recipe uses Madison copy agents for subject lines, pre-headers, generational messaging, SMS, ZML, and campaign development.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-copy-content-generation.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-copy-content-generation --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-copy-content-generation data/verified/madison-copy-content-generation -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-copy-content-generation.md`.
   Human capacity: [EI].

1. Step name: Verify campaign approval. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: logs/gate-G3-campaign-structure.json.
   Output: approval check with gate status and reviewer_capacity.
   Where output goes: logs/gate-decisions/.
2. Step name: Generate copy variants. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-gigo-copy-generation.py`
   Input: campaign-structure-verified.json, personas-verified.json, and brief.json.
   Output: copy-variants-verified JSON fields: channel, persona_id, variant_id, subject_line, preheader, body_copy, sms_copy, spam_score, validation_flags plus email template files.
   Where output goes: data/verified/madison-branding-marketing-pipeline/.
