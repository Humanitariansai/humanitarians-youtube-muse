---
status: DRAFT
todos_open: 14
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# intelligence-agent

## Purpose

The intelligence-agent monitors brand, competitor, Reddit, and regulatory signals for Apple and adjacent technology brands. It normalizes source items, deduplicates them against prior state, applies local sentiment and compliance-risk analysis, computes drift and anomaly metrics, builds knowledge graph and competitor summaries, and emits local report contracts in place of live Google Sheets writes or webhook responses.

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
| Original n8n workflow JSON | JSON | data/madison-main/n8n-workflows/originals/intelligence-agent/workflow.json | Yes |
| Brand config | JSON array | `scripts/tools/intelligence-agent-config.py` | Yes |
| Apple press items | RSS/JSON rows | `scripts/ingest/intelligence-agent-get-news.py` | Yes |
| Google News items | RSS/JSON rows | `scripts/ingest/intelligence-agent-get-news.py` | Yes |
| Reddit posts | JSON rows | `scripts/ingest/intelligence-agent-get-reddit.py` | Yes |
| Regulatory items | RSS/JSON rows | `scripts/ingest/intelligence-agent-get-regulatory.py` | Yes |
| Prior processed links/articles | JSON rows | `scripts/ingest/intelligence-agent-get-prior-state.py` | Yes |
| Human-cleared analysis scope | Text/JSON | Conductor gate | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/intelligence-agent.md" && rg -n "\[TODO: DEFINE]" "recipes/intelligence-agent.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/intelligence-agent/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/intelligence-agent data/verified/intelligence-agent -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/intelligence-agent-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/intelligence-agent.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/intelligence-agent-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/intelligence-agent.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/intelligence-agent-[DATE].json && test -f reports/generated/intelligence-agent-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/intelligence-agent-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/intelligence-agent-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/intelligence-agent/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/intelligence-agent-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/intelligence-agent/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/intelligence-agent-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/intelligence-agent/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/intelligence-agent-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/intelligence-agent-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `intelligence-agent`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/intelligence-agent-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/intelligence-agent-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `intelligence-agent` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if the original JSON is missing.
- Stop if live ingest is requested before sample ingest passes.
- Stop if source items cannot be normalized to title/link/source/fullText rows.
- Stop if dedupe cannot access prior-state data or a human-approved fallback.
- Stop if live OpenAI sentiment is requested without human clearance.
- Stop if regulatory risk is used as final compliance advice without human review.
- Stop if alert payloads would post live without explicit clearance.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run intelligence-agent --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run intelligence-agent --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run intelligence-agent --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run intelligence-agent --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run intelligence-agent --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run intelligence-agent --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run intelligence-agent --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run intelligence-agent --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate intelligence-agent --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate intelligence-agent --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate intelligence-agent --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate intelligence-agent --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate intelligence-agent --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate intelligence-agent --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/intelligence-agent-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/intelligence-agent-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/intelligence-agent-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/intelligence-agent-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/intelligence-agent-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/intelligence-agent-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/intelligence-agent/` | JSON |
| Verified data | `data/verified/intelligence-agent/` | JSON |
| Agent log | `logs/intelligence-agent-[DATE].json` | JSON |
| Human report | `reports/generated/intelligence-agent-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/madison-main/n8n-workflows/originals/intelligence-agent/workflow.json` | `test -f "data/madison-main/n8n-workflows/originals/intelligence-agent/workflow.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

The intelligence-agent monitors brand, competitor, Reddit, and regulatory signals for Apple and adjacent technology brands. It normalizes source items, deduplicates them against prior state, applies local sentiment and compliance-risk analysis, computes drift and anomaly metrics, builds knowledge graph and competitor summaries, and emits local report contracts in place of live Google Sheets writes or webhook responses.

1. Source identity gate: Original workflow JSON exists and is the intended source. Test: `test -f "data/madison-main/n8n-workflows/originals/intelligence-agent/workflow.json"`.
   Human capacity: [PF].
2. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/intelligence-agent.md`.
   Human capacity: [PA].
3. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run intelligence-agent --mode dialogic --sample`.
   Human capacity: [TO].
4. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/intelligence-agent data/verified/intelligence-agent -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
5. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/intelligence-agent.md`.
   Human capacity: [EI].

1. Step name: Verify provenance and source intent. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: data/madison-main/n8n-workflows/originals/intelligence-agent/workflow.json.
   Output: provenance fields: workflow_path, exists, parsed_ok, title_matches_pipeline, source_inventory_checked.
   Where output goes: logs/gate-decisions/.
2. Step name: Map workflow or specification to scripts. Labor: AI with Human gate.
   Script called: `scripts/gigo/intelligence-agent-map-workflow-or-specification-to-scripts.py`
   Input: recipe inputs and provenance evidence.
   Output: implementation map fields: steps, script_paths, missing_specs, typed_todos.
   Where output goes: data/verified/.
3. Step name: Produce human report. Labor: AI with Human review.
   Script called: `scripts/tools/intelligence-agent-produce-human-report.py`
   Input: agent log plus raw and verified outputs.
   Output: markdown report sections: run summary, source inventory, inputs used, validation results, flags, typed TODOs, decision recommendation.
   Where output goes: reports/generated/.
