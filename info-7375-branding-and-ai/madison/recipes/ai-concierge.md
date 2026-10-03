---
status: DRAFT
todos_open: 14
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# ai-concierge

## Purpose

The ai-concierge workflow answers customer questions for a cafe-style service experience: it handles greetings, FAQ lookup, inventory-aware recommendations, order status checks, and booking/order support. For a marketing or experience lead, the workflow is a bounded customer-facing assistant that can use approved operational data while keeping staff escalation clear for cancellations, unavailable items, and uncertain answers.

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
| Original n8n workflow JSON | JSON | data/madison-main/n8n-workflows/originals/archives/cicerone/ai-concierge.json | Yes |
| Customer message | Text | Chat trigger | Yes |
| Customer name | Text | Conversation state | No |
| Inventory sheet | Tabular rows | Google Sheets export via `scripts/ingest/ai-concierge-get-inventory.py` | Yes |
| FAQ sheet | Tabular rows | Google Sheets export via `scripts/ingest/ai-concierge-get-faq.py` | Yes |
| Orders sheet | Tabular rows | Google Sheets export via `scripts/ingest/ai-concierge-get-orders.py` | Yes |
| Brand/service rules | Text | Original workflow system message | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/ai-concierge.md" && rg -n "\[TODO: DEFINE]" "recipes/ai-concierge.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/ai-concierge/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/ai-concierge data/verified/ai-concierge -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/ai-concierge-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/ai-concierge.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/ai-concierge-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/ai-concierge.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/ai-concierge-[DATE].json && test -f reports/generated/ai-concierge-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/ai-concierge-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/ai-concierge-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/ai-concierge/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/ai-concierge-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/ai-concierge/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/ai-concierge-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/ai-concierge/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/ai-concierge-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/ai-concierge-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `ai-concierge`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/ai-concierge-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/ai-concierge-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `ai-concierge` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if the original JSON is missing or differs from the provenance path.
- Stop if live ingest is requested without a spreadsheet id or required access.
- Stop if inventory, FAQ, or order data cannot be parsed as JSON arrays of objects.
- Stop if a user asks for cancellation that policy says staff must handle.
- Stop if the requested item is unavailable and no available alternatives are present in inventory.
- Stop if the response would claim a booking/order is confirmed before a human-approved write path exists.
- Stop if a customer-facing message contains unverified policy, price, allergen, availability, or booking information.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run ai-concierge --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run ai-concierge --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run ai-concierge --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run ai-concierge --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run ai-concierge --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run ai-concierge --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run ai-concierge --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run ai-concierge --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate ai-concierge --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate ai-concierge --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate ai-concierge --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate ai-concierge --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate ai-concierge --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate ai-concierge --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/ai-concierge-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/ai-concierge-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/ai-concierge-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/ai-concierge-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/ai-concierge-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/ai-concierge-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/ai-concierge/` | JSON |
| Verified data | `data/verified/ai-concierge/` | JSON |
| Agent log | `logs/ai-concierge-[DATE].json` | JSON |
| Human report | `reports/generated/ai-concierge-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/madison-main/n8n-workflows/originals/archives/cicerone/ai-concierge.json` | `test -f "data/madison-main/n8n-workflows/originals/archives/cicerone/ai-concierge.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

The ai-concierge workflow answers customer questions for a cafe-style service experience: it handles greetings, FAQ lookup, inventory-aware recommendations, order status checks, and booking/order support. For a marketing or experience lead, the workflow is a bounded customer-facing assistant that can use approved operational data while keeping staff escalation clear for cancellations, unavailable items, and uncertain answers.

1. Source identity gate: Original workflow JSON exists and is the intended source. Test: `test -f "data/madison-main/n8n-workflows/originals/archives/cicerone/ai-concierge.json"`.
   Human capacity: [PF].
2. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/ai-concierge.md`.
   Human capacity: [PA].
3. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run ai-concierge --mode dialogic --sample`.
   Human capacity: [TO].
4. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/ai-concierge data/verified/ai-concierge -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
5. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/ai-concierge.md`.
   Human capacity: [EI].

1. Step name: Verify provenance and source intent. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: data/madison-main/n8n-workflows/originals/archives/cicerone/ai-concierge.json.
   Output: provenance fields: workflow_path, exists, parsed_ok, title_matches_pipeline, source_inventory_checked.
   Where output goes: logs/gate-decisions/.
2. Step name: Map workflow or specification to scripts. Labor: AI with Human gate.
   Script called: `scripts/gigo/ai-concierge-map-workflow-or-specification-to-scripts.py`
   Input: recipe inputs and provenance evidence.
   Output: implementation map fields: steps, script_paths, missing_specs, typed_todos.
   Where output goes: data/verified/.
3. Step name: Produce human report. Labor: AI with Human review.
   Script called: `scripts/tools/ai-concierge-produce-human-report.py`
   Input: agent log plus raw and verified outputs.
   Output: markdown report sections: run summary, source inventory, inputs used, validation results, flags, typed TODOs, decision recommendation.
   Where output goes: reports/generated/.
