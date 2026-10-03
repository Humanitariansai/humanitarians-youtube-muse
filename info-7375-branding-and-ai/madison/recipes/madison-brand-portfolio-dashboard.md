---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Brand Portfolio Dashboard

## Purpose

Tracks multiple brands, products, or campaigns as a portfolio so leadership can compare reputation, sentiment, momentum, risk, and readiness across the whole marketing estate.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-brand-portfolio-dashboard.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Brand portfolio list | JSON | [TODO: DATA SOURCE] Approved brands, products, campaigns, or business units. | Yes |
| Portfolio metrics | JSON/CSV | [TODO: DATA SOURCE] Reputation, sentiment, campaign, traffic, sales, or service metrics. | Yes |
| Dashboard metric schema | JSON | [TODO: DEV] Define metric names, formulas, source priority, and rollup rules. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/portfolio-dashboard.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-brand-portfolio-dashboard.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-brand-portfolio-dashboard.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-brand-portfolio-dashboard/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-brand-portfolio-dashboard data/verified/madison-brand-portfolio-dashboard -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-brand-portfolio-dashboard-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-brand-portfolio-dashboard.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-brand-portfolio-dashboard-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-brand-portfolio-dashboard.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-brand-portfolio-dashboard-[DATE].json && test -f reports/generated/madison-brand-portfolio-dashboard-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-portfolio-dashboard-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-brand-portfolio-dashboard-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-brand-portfolio-dashboard/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-portfolio-dashboard-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-brand-portfolio-dashboard/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-portfolio-dashboard-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-brand-portfolio-dashboard/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-portfolio-dashboard-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-portfolio-dashboard-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-portfolio-dashboard`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-brand-portfolio-dashboard-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-brand-portfolio-dashboard-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Brand Portfolio Dashboard` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if metric formulas are undefined because scores would be misleading.
- Stop if portfolio items are not approved because dashboard scope would be unstable.
- Stop if dashboard output is used to allocate budget without human review.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-brand-portfolio-dashboard --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-brand-portfolio-dashboard --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-brand-portfolio-dashboard --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-brand-portfolio-dashboard --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-brand-portfolio-dashboard --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-brand-portfolio-dashboard --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-brand-portfolio-dashboard --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-brand-portfolio-dashboard --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-brand-portfolio-dashboard --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-brand-portfolio-dashboard-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-brand-portfolio-dashboard-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-brand-portfolio-dashboard-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-brand-portfolio-dashboard-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-brand-portfolio-dashboard-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-brand-portfolio-dashboard-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-brand-portfolio-dashboard/` | JSON |
| Verified data | `data/verified/madison-brand-portfolio-dashboard/` | JSON |
| Agent log | `logs/madison-brand-portfolio-dashboard-[DATE].json` | JSON |
| Human report | `reports/generated/madison-brand-portfolio-dashboard-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-brand-portfolio-dashboard.md` | `test -f "recipes/madison-brand-portfolio-dashboard.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Tracks multiple brands, products, or campaigns as a portfolio so leadership can compare reputation, sentiment, momentum, risk, and readiness across the whole marketing estate.

1. Portfolio gate: brands and campaigns are approved. Test: `python3 -m json.tool data/raw/madison-brand-portfolio-dashboard/portfolio-list.json`. Human capacity: [PF].
2. Metric gate: metric schema defines formulas and source priority. Test: `rg -n "TODO:" recipes/madison-brand-portfolio-dashboard.md`. Human capacity: [PA].
3. Sample gate: sample mode produces local dashboard JSON only. Test: `snickerdoodle run madison-brand-portfolio-dashboard --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest portfolio metrics. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-brand-portfolio-dashboard-ingest-portfolio-metrics.py`
   Input: portfolio list and approved metric sources.
   Output: raw JSON fields: portfolio_item, metric_name, metric_value, source, period_start, period_end, source_url_or_path.
   Where output goes: `data/raw/madison-brand-portfolio-dashboard/`.
2. Step name: Build portfolio dashboard data. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-brand-portfolio-dashboard-build-portfolio-dashboard-data.py`
   Input: raw portfolio metrics and metric schema.
   Output: verified JSON fields: portfolio_item, health_score, sentiment_score, momentum_score, risk_score, missing_metrics, flags.
   Where output goes: `data/verified/madison-brand-portfolio-dashboard/`.
3. Step name: Produce portfolio dashboard report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-brand-portfolio-dashboard-produce-portfolio-dashboard-report.py`
   Input: verified dashboard data.
   Output: markdown sections: portfolio summary, winners, risks, missing data, leadership decisions.
   Where output goes: `reports/generated/`.
