#!/usr/bin/env python3
"""make_sheet.py — Muse packages it (Film 4).

13 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse packages it",
    "film": 4,
    "series": "Assignment 4 lecture films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "A project isn't finished when it works. It's finished when you can hand it to someone else. The professional test is simple: would you show this to a client? Today: the package.",
            "screen": "Wrapped package; the question: would you show this to a client?"
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Package: everything a stranger needs to understand the work. Executive summary: one page — problem, solution, results, value. Architecture: how it fits together, including how it fails. Demo: the walkthrough that proves it live.",
            "screen": "Four terms: package / executive summary / architecture / demo."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "First, the executive summary. One page. The problem: three thousand four hundred forty-six postings is a pile, not a job search. The solution: five weighted dimensions, two implementations, one spec. The results: seven hundred fourteen scored in three seconds, twenty-two to pursue. The value: a weekly firehose becomes a twenty-two-item action list.",
            "screen": "Summary page: problem, solution, results, value."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "Second, the architecture. Sources to fetch to normalize to score to route to outputs — one left-to-right flow. The intelligence is labeled: the scoring box carries its weights and the pairing rule. The delivery lane is drawn dashed, because it's specified but not built. The diagram doesn't flatter the project; it describes it.",
            "screen": "Architecture flow, left to right."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "A professional diagram shows how it fails. Three failure paths, in red: malformed records go to quarantine — logged, never dropped. A failed fetch falls back to the last good pull, flagged in the report. Scoring exceptions land in quarantine too. Failure is a feature of the design, not an accident.",
            "screen": "Failure paths glow red: quarantine, cached fallback."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Integration points. The system is two implementations of one specification: the Python script and the n8n workflow score identically. The n8n side owns scheduling and delivery; the Python side owns batch scoring and the brief files. One spec, two runtimes — pick the one your team operates.",
            "screen": "Two nodes: n8n workflow, Python script — one spec."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 24, "act": "2",
            "voice": "Muse",
            "line": "The demo walkthrough. Step one: show the digest — one page, twenty-two pursue roles. Step two: open a brief — the score, the reasons, the link, the next step. Step three: open the run report — every number traced. Step four: open the architecture — and point at the dashed lane, the part not built yet. A demo that shows the gap is a demo you can trust.",
            "screen": "Four numbered demo steps."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The pitch, in numbers. Three point seven two milliseconds a record, linear to thirty-two thousand. Zero dollars a month to operate — zero API calls, zero LLM calls. Fifteen briefs a non-technical user can open and use. One diagram a client can read. That is the package.",
            "screen": "Pitch card with the verdict numbers."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "And the one thing the package doesn't hide: scheduled delivery — the approval gate, the weekly digest, the email — is specified but unimplemented. It's the single blocker before this is a production service, and it's written on the card in plain text. Professionals disclose the gap.",
            "screen": "Single TODO card: scheduled delivery — the blocker."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 30, "act": "4",
            "voice": "Muse",
            "line": "Finally, the evaluation this whole series promised. Scripting: strong — the matcher, the tests, the tooling all run. Agents: useful for research and fetching, supervised throughout. Analysis: the strongest suit — the pairing rule and the vocabulary audit came from measurement. Repo-based work: solid, with one real failure owned and fixed — the push script bug. Film production: the packages are complete and gated, but the renders are yours — judge the films when they're cut.",
            "screen": "Five graded dimensions appear one by one."
        },
        {
            "id": "BVDT", "scene": "M11", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, the package — a one-page summary and an honest architecture diagram. Act two, the story it tells — failure paths, two implementations of one spec, and a demo plan that shows the gap. Act three, the pitch — linear, zero-cost, client-ready, with the blocker disclosed. Act four, the evaluation — graded, with the failure owned.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M11", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Take a project of yours and apply the client test: one-page summary, one architecture diagram with the failure paths drawn in, one demo plan. What's the gap you'd have to disclose?",
            "screen": "Do-today card: package one of your projects; name the gap."
        },
        {
            "id": "BOUT", "scene": "M11", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching the series.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    assert len(BS["beats"]) == 13, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 8, len(acts)
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
