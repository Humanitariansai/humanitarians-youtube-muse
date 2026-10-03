---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Competitive Positioning Agent

## Purpose

Compares brands across messaging, offers, pricing signals, product features, proof points, and audience promises so a strategist can identify where a company is differentiated, overmatched, or unclear.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-competitive-positioning-agent.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Competitor list | JSON | [TODO: DATA SOURCE] Approved competitor and comparison-set list. | Yes |
| Brand evidence corpus | JSON/Markdown | [TODO: DATA SOURCE] Websites, landing pages, ads, product pages, press pages, and sales collateral. | Yes |
| Positioning rubric | JSON | [TODO: DEFINE] Define dimensions: promise, audience, price, feature, proof, tone, channel. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/comparativeanalysisagent.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-competitive-positioning-agent.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-competitive-positioning-agent.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-competitive-positioning-agent/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-competitive-positioning-agent data/verified/madison-competitive-positioning-agent -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-competitive-positioning-agent-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-competitive-positioning-agent.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-competitive-positioning-agent-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-competitive-positioning-agent.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-competitive-positioning-agent-[DATE].json && test -f reports/generated/madison-competitive-positioning-agent-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-competitive-positioning-agent-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-competitive-positioning-agent-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-competitive-positioning-agent/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-competitive-positioning-agent-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-competitive-positioning-agent/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-competitive-positioning-agent-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-competitive-positioning-agent/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-competitive-positioning-agent-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-competitive-positioning-agent-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-competitive-positioning-agent`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-competitive-positioning-agent-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-competitive-positioning-agent-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Competitive Positioning Agent` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if competitor set is unapproved because comparisons can become misleading.
- Stop if evidence lacks source references because claims cannot be audited.
- Stop if report recommends legal, pricing, or product changes without human review.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-competitive-positioning-agent --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-competitive-positioning-agent --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-competitive-positioning-agent --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-competitive-positioning-agent --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-competitive-positioning-agent --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-competitive-positioning-agent --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-competitive-positioning-agent --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-competitive-positioning-agent --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-competitive-positioning-agent --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-competitive-positioning-agent-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-competitive-positioning-agent-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-competitive-positioning-agent-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-competitive-positioning-agent-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-competitive-positioning-agent-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-competitive-positioning-agent-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-competitive-positioning-agent/` | JSON |
| Verified data | `data/verified/madison-competitive-positioning-agent/` | JSON |
| Agent log | `logs/madison-competitive-positioning-agent-[DATE].json` | JSON |
| Human report | `reports/generated/madison-competitive-positioning-agent-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-competitive-positioning-agent.md` | `test -f "recipes/madison-competitive-positioning-agent.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Compares brands across messaging, offers, pricing signals, product features, proof points, and audience promises so a strategist can identify where a company is differentiated, overmatched, or unclear.

1. Competitor gate: comparison set is approved. Test: `python3 -m json.tool data/raw/madison-competitive-positioning-agent/competitors.json`. Human capacity: [PF].
2. Evidence gate: every source has a URL or file path. Test: `rg -n "TODO:" recipes/madison-competitive-positioning-agent.md`. Human capacity: [PA].
3. Sample gate: sample mode runs without scraping unapproved sites. Test: `snickerdoodle run madison-competitive-positioning-agent --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest competitor evidence. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-competitive-positioning-agent-ingest-competitor-evidence.py`
   Input: competitor list and evidence corpus.
   Output: raw JSON fields: company, source_type, url_or_path, message_text, offer_text, product_feature, proof_point, collected_at.
   Where output goes: `data/raw/madison-competitive-positioning-agent/`.
2. Step name: Compare positioning. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-competitive-positioning-agent-compare-positioning.py`
   Input: raw evidence records and positioning rubric.
   Output: verified JSON fields: company, dimension, claim, strength_score, differentiation_flag, evidence_ref, notes.
   Where output goes: `data/verified/madison-competitive-positioning-agent/`.
3. Step name: Produce positioning report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-competitive-positioning-agent-produce-positioning-report.py`
   Input: verified positioning comparisons.
   Output: markdown sections: positioning map, competitor strengths, gaps, white-space opportunities, source evidence.
   Where output goes: `reports/generated/`.
