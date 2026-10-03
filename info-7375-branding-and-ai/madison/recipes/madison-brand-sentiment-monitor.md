---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Brand Sentiment Monitor

## Purpose

Classifies brand and category coverage by sentiment and review urgency so marketing teams can see where customer trust, campaign response, or category mood is improving or deteriorating.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-brand-sentiment-monitor.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Brand query config | JSON | [TODO: DATA SOURCE] Approved brand, competitor, and category terms. | Yes |
| Article or social records | JSON | [TODO: DATA SOURCE] NewsAPI, RSS, reviews, or approved social archive. | Yes |
| Sentiment rubric | JSON | [TODO: DEFINE] Define positive, neutral, negative, mixed, and urgent criteria. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/ai-news-sentiment-agent.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-brand-sentiment-monitor.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-brand-sentiment-monitor.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-brand-sentiment-monitor/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-brand-sentiment-monitor data/verified/madison-brand-sentiment-monitor -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-brand-sentiment-monitor-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-brand-sentiment-monitor.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-brand-sentiment-monitor-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-brand-sentiment-monitor.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-brand-sentiment-monitor-[DATE].json && test -f reports/generated/madison-brand-sentiment-monitor-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-sentiment-monitor-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-brand-sentiment-monitor-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-brand-sentiment-monitor/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-sentiment-monitor-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-brand-sentiment-monitor/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-sentiment-monitor-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-brand-sentiment-monitor/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-sentiment-monitor-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-sentiment-monitor-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-sentiment-monitor`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-brand-sentiment-monitor-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-brand-sentiment-monitor-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Brand Sentiment Monitor` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if sentiment rubric is undefined because labels would be arbitrary.
- Stop if records lack source URLs because findings cannot be audited.
- Stop if sentiment output is used as investment or legal advice.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-brand-sentiment-monitor --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-brand-sentiment-monitor --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-brand-sentiment-monitor --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-brand-sentiment-monitor --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-brand-sentiment-monitor --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-brand-sentiment-monitor --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-brand-sentiment-monitor --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-brand-sentiment-monitor --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-brand-sentiment-monitor --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-brand-sentiment-monitor-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-brand-sentiment-monitor-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-brand-sentiment-monitor-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-brand-sentiment-monitor-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-brand-sentiment-monitor-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-brand-sentiment-monitor-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-brand-sentiment-monitor/` | JSON |
| Verified data | `data/verified/madison-brand-sentiment-monitor/` | JSON |
| Agent log | `logs/madison-brand-sentiment-monitor-[DATE].json` | JSON |
| Human report | `reports/generated/madison-brand-sentiment-monitor-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-brand-sentiment-monitor.md` | `test -f "recipes/madison-brand-sentiment-monitor.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Classifies brand and category coverage by sentiment and review urgency so marketing teams can see where customer trust, campaign response, or category mood is improving or deteriorating.

1. Query gate: brand terms and exclusions are approved. Test: `python3 -m json.tool data/raw/madison-brand-sentiment-monitor/query-config.json`. Human capacity: [PF].
2. Rubric gate: sentiment labels are defined before scoring. Test: `rg -n "TODO:" recipes/madison-brand-sentiment-monitor.md`. Human capacity: [IJ].
3. Sample gate: sample mode runs without email, Airtable, or dashboard writes. Test: `snickerdoodle run madison-brand-sentiment-monitor --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest sentiment records. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-brand-sentiment-monitor-ingest-sentiment-records.py`
   Input: query config and approved local or live source.
   Output: raw JSON fields: record_id, source, title, body_snippet, url, published_at, matched_brand, matched_category.
   Where output goes: `data/raw/madison-brand-sentiment-monitor/`.
2. Step name: Score brand sentiment. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-brand-sentiment-monitor-score-brand-sentiment.py`
   Input: raw records and sentiment rubric.
   Output: verified JSON fields: record_id, sentiment_label, confidence, urgency_flag, rationale, source_url, review_required.
   Where output goes: `data/verified/madison-brand-sentiment-monitor/`.
3. Step name: Produce sentiment report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-brand-sentiment-monitor-produce-sentiment-report.py`
   Input: verified sentiment records.
   Output: markdown sections: sentiment counts, urgent negative items, evidence links, campaign implications, next actions.
   Where output goes: `reports/generated/`.
