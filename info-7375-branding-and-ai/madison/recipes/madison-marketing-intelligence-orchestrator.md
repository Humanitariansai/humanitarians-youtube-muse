---
status: DRAFT
todos_open: 13
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Marketing Intelligence Orchestrator

## Purpose

Routes marketing intelligence questions to the right Madison recipe family so brand, campaign, audience, sentiment, competitive, and portfolio work can be coordinated without skipping human gates.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-marketing-intelligence-orchestrator.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| User request | Text/JSON | Chat, brief, or conductor request. | Yes |
| Available recipe registry | JSON | [TODO: DEV] Define Madison marketing recipe registry. | Yes |
| Gate state | JSON | `logs/gate-decisions/` | No |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/orchestrator.md` and `orchestrator-v2-enhanced.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-marketing-intelligence-orchestrator.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-marketing-intelligence-orchestrator.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-marketing-intelligence-orchestrator/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-marketing-intelligence-orchestrator data/verified/madison-marketing-intelligence-orchestrator -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-marketing-intelligence-orchestrator-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-marketing-intelligence-orchestrator.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-marketing-intelligence-orchestrator-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-marketing-intelligence-orchestrator.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-marketing-intelligence-orchestrator-[DATE].json && test -f reports/generated/madison-marketing-intelligence-orchestrator-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-marketing-intelligence-orchestrator-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-marketing-intelligence-orchestrator-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-marketing-intelligence-orchestrator/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-marketing-intelligence-orchestrator-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-marketing-intelligence-orchestrator/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-marketing-intelligence-orchestrator-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-marketing-intelligence-orchestrator/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-marketing-intelligence-orchestrator-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-marketing-intelligence-orchestrator-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-marketing-intelligence-orchestrator`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-marketing-intelligence-orchestrator-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-marketing-intelligence-orchestrator-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Marketing Intelligence Orchestrator` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if the request maps to no approved recipe because the orchestrator would invent workflow behavior.
- Stop if a downstream recipe has unresolved live-action gates.
- Stop if activation, email, publishing, or API writes are requested without human approval.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-marketing-intelligence-orchestrator --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-marketing-intelligence-orchestrator --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-marketing-intelligence-orchestrator --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-marketing-intelligence-orchestrator --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-marketing-intelligence-orchestrator --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-marketing-intelligence-orchestrator --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-marketing-intelligence-orchestrator --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-marketing-intelligence-orchestrator --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-marketing-intelligence-orchestrator --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-marketing-intelligence-orchestrator-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-marketing-intelligence-orchestrator-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-marketing-intelligence-orchestrator-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-marketing-intelligence-orchestrator-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-marketing-intelligence-orchestrator-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-marketing-intelligence-orchestrator-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-marketing-intelligence-orchestrator/` | JSON |
| Verified data | `data/verified/madison-marketing-intelligence-orchestrator/` | JSON |
| Agent log | `logs/madison-marketing-intelligence-orchestrator-[DATE].json` | JSON |
| Human report | `reports/generated/madison-marketing-intelligence-orchestrator-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-marketing-intelligence-orchestrator.md` | `test -f "recipes/madison-marketing-intelligence-orchestrator.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Routes marketing intelligence questions to the right Madison recipe family so brand, campaign, audience, sentiment, competitive, and portfolio work can be coordinated without skipping human gates.

1. Registry gate: available recipes and allowed routes are defined. Test: `python3 -m json.tool data/verified/madison-marketing-intelligence-orchestrator/recipe-registry.json`. Human capacity: [PF].
2. Safety gate: no downstream recipe runs in live mode unless its gates pass. Test: `rg -n "TODO:" recipes/madison-marketing-intelligence-orchestrator.md`. Human capacity: [EI].
3. Sample gate: sample mode routes only and performs no live action. Test: `snickerdoodle run madison-marketing-intelligence-orchestrator --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Classify marketing request. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-marketing-intelligence-orchestrator-classify-marketing-request.py`
   Input: user request and recipe registry.
   Output: verified JSON fields: request_type, candidate_recipes, confidence, missing_inputs, gate_requirements.
   Where output goes: `data/verified/madison-marketing-intelligence-orchestrator/`.
2. Step name: Build routing plan. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-marketing-intelligence-orchestrator-build-routing-plan.py`
   Input: classified request and gate state.
   Output: verified JSON fields: ordered_recipes, required_inputs, blocked_steps, gate_checks, sample_commands.
   Where output goes: `data/verified/madison-marketing-intelligence-orchestrator/`.
3. Step name: Produce orchestrator handoff. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-marketing-intelligence-orchestrator-produce-orchestrator-handoff.py`
   Input: routing plan.
   Output: markdown sections: request summary, recommended recipes, blocked gates, sample commands, human decisions required.
   Where output goes: `reports/generated/`.
