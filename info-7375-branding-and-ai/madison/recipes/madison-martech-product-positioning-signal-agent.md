---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Martech Product Positioning Signal Agent

## Purpose

Tracks martech, platform, integration, and product-stack signals so marketing and product teams can understand how technology adoption affects positioning, partner strategy, and campaign claims.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-martech-product-positioning-signal-agent.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Technology watchlist | JSON | [TODO: DATA SOURCE] Approved tools, platforms, integrations, and product categories. | Yes |
| Public documentation and release feeds | RSS/API/Markdown | [TODO: DATA SOURCE] Vendor docs, release notes, integration pages, and trade news. | Yes |
| Signal rubric | JSON | [TODO: DEFINE] Define adoption, deprecation, integration, compliance, and ecosystem signals. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/tech-stack-directional-signal-agent.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-martech-product-positioning-signal-agent.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-martech-product-positioning-signal-agent.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-martech-product-positioning-signal-agent/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-martech-product-positioning-signal-agent data/verified/madison-martech-product-positioning-signal-agent -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-martech-product-positioning-signal-agent-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-martech-product-positioning-signal-agent.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-martech-product-positioning-signal-agent-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-martech-product-positioning-signal-agent.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-martech-product-positioning-signal-agent-[DATE].json && test -f reports/generated/madison-martech-product-positioning-signal-agent-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-martech-product-positioning-signal-agent-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-martech-product-positioning-signal-agent-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-martech-product-positioning-signal-agent/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-martech-product-positioning-signal-agent-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-martech-product-positioning-signal-agent/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-martech-product-positioning-signal-agent-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-martech-product-positioning-signal-agent/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-martech-product-positioning-signal-agent-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-martech-product-positioning-signal-agent-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-martech-product-positioning-signal-agent`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-martech-product-positioning-signal-agent-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-martech-product-positioning-signal-agent-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Martech Product Positioning Signal Agent` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if watchlist is undefined because signal collection would be unfocused.
- Stop if vendor claims are not cited because product positioning implications need evidence.
- Stop if report recommends integration commitments without product-owner approval.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-martech-product-positioning-signal-agent --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-martech-product-positioning-signal-agent --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-martech-product-positioning-signal-agent --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-martech-product-positioning-signal-agent --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-martech-product-positioning-signal-agent --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-martech-product-positioning-signal-agent --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-martech-product-positioning-signal-agent --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-martech-product-positioning-signal-agent --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-martech-product-positioning-signal-agent --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-martech-product-positioning-signal-agent-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-martech-product-positioning-signal-agent-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-martech-product-positioning-signal-agent-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-martech-product-positioning-signal-agent-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-martech-product-positioning-signal-agent-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-martech-product-positioning-signal-agent-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-martech-product-positioning-signal-agent/` | JSON |
| Verified data | `data/verified/madison-martech-product-positioning-signal-agent/` | JSON |
| Agent log | `logs/madison-martech-product-positioning-signal-agent-[DATE].json` | JSON |
| Human report | `reports/generated/madison-martech-product-positioning-signal-agent-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-martech-product-positioning-signal-agent.md` | `test -f "recipes/madison-martech-product-positioning-signal-agent.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Tracks martech, platform, integration, and product-stack signals so marketing and product teams can understand how technology adoption affects positioning, partner strategy, and campaign claims.

1. Watchlist gate: tools and platforms are approved. Test: `python3 -m json.tool data/raw/madison-martech-product-positioning-signal-agent/watchlist.json`. Human capacity: [PF].
2. Source gate: vendor documentation sources are allowed. Test: `rg -n "TODO:" recipes/madison-martech-product-positioning-signal-agent.md`. Human capacity: [PA].
3. Sample gate: sample mode does not call vendor APIs. Test: `snickerdoodle run madison-martech-product-positioning-signal-agent --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest martech signals. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-martech-product-positioning-signal-agent-ingest-martech-signals.py`
   Input: technology watchlist and approved feeds.
   Output: raw JSON fields: vendor, product, signal_type, source_url, title, published_at, snippet.
   Where output goes: `data/raw/madison-martech-product-positioning-signal-agent/`.
2. Step name: Score positioning impact. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-martech-product-positioning-signal-agent-score-positioning-impact.py`
   Input: raw martech signals and signal rubric.
   Output: verified JSON fields: signal_id, product, signal_type, impact_score, positioning_implication, evidence_url, flags.
   Where output goes: `data/verified/madison-martech-product-positioning-signal-agent/`.
3. Step name: Produce martech signal report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-martech-product-positioning-signal-agent-produce-martech-signal-report.py`
   Input: verified martech signals.
   Output: markdown sections: adoption signals, platform risks, partner opportunities, positioning implications.
   Where output goes: `reports/generated/`.
