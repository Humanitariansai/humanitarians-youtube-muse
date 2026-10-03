---
status: DRAFT
todos_open: 10
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Audience Definition

## Purpose

Defines and validates the campaign audience from `brief.json`. The Audience Builder Agent translates the natural-language audience description into executable Boolean logic and behavioral criteria for Madison ZMP, while GIGO checks segment size, suppression overlap, and geography/propensity-score fit.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-audience-definition.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Client brief | JSON | `data/raw/madison-branding-marketing-pipeline/brief.json` | Yes |
| Madison Data Cloud propensity scores | Query result | Madison Data Cloud | Yes |
| SuperGraph profiles | Query result | Madison SuperGraph | Yes |
| Suppression rules | JSON array | `brief.json` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-audience-definition.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-audience-definition.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-audience-definition/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-audience-definition data/verified/madison-audience-definition -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-audience-definition-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-audience-definition.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-audience-definition-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-audience-definition.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-audience-definition-[DATE].json && test -f reports/generated/madison-audience-definition-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-audience-definition-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-audience-definition-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-audience-definition/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-audience-definition-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-audience-definition/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-audience-definition-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-audience-definition/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-audience-definition-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-audience-definition-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-audience-definition`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-audience-definition-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-audience-definition-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Audience Definition` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if `brief.json` is missing or invalid.
- Stop if audience description is missing.
- Stop if verified segment size is below 1,000 profiles.
- Stop if suppression rules cannot be applied.
- Stop if U.S.-only retail scores are being treated as valid for a non-U.S. client without human approval.
- Stop if Gate G1 is not approved.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-audience-definition --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-audience-definition --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-audience-definition --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-audience-definition --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-audience-definition --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-audience-definition --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-audience-definition --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-audience-definition --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-audience-definition --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-audience-definition --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-audience-definition --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-audience-definition --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-audience-definition --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-audience-definition --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-audience-definition-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-audience-definition-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-audience-definition-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-audience-definition-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-audience-definition-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-audience-definition-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-audience-definition/` | JSON |
| Verified data | `data/verified/madison-audience-definition/` | JSON |
| Agent log | `logs/madison-audience-definition-[DATE].json` | JSON |
| Human report | `reports/generated/madison-audience-definition-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/raw/madison-branding-marketing-pipeline/brief.json` | `test -f "data/raw/madison-branding-marketing-pipeline/brief.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Defines and validates the campaign audience from `brief.json`. The Audience Builder Agent translates the natural-language audience description into executable Boolean logic and behavioral criteria for Madison ZMP, while GIGO checks segment size, suppression overlap, and geography/propensity-score fit.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-audience-definition.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-audience-definition --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-audience-definition data/verified/madison-audience-definition -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-audience-definition.md`.
   Human capacity: [EI].

1. Step name: Load brief. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-audience-definition-load-brief.py`
   Input: data/raw/madison-branding-marketing-pipeline/brief.json.
   Output: brief readiness fields: brand, objective, audience_description, channels, suppressions, geography_flags.
   Where output goes: logs/.
2. Step name: Query audience explorer. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-ingest-audience-explorer.py`
   Input: approved brief parameters.
   Output: audience-raw JSON fields: segment_id, query_logic, profile_count, propensity_score_metadata, suppression_overlap.
   Where output goes: data/raw/madison-branding-marketing-pipeline/.
3. Step name: Validate audience. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-gigo-audience-validation.py`
   Input: audience-raw.json, brief.json, suppression rules.
   Output: audience-verified JSON fields: segment_id, criteria, segment_size, suppressions_applied, geography_flags, score_provenance, validation_flags.
   Where output goes: data/verified/madison-branding-marketing-pipeline/.
4. Step name: Gate G1 review. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: audience-verified.json.
   Output: gate decision with decision, reviewer_capacity, note, approved_at.
   Where output goes: logs/gate-G1-audience.json.
