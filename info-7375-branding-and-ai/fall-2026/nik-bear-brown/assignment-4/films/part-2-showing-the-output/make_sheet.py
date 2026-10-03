#!/usr/bin/env python3
"""make_sheet.py — Muse shows the output (Film 2).

Builds beat_sheet.json: 15 beats, four acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm plus small pauses; body ~ 12-22s per beat.
"""
import json

BS = {
    "title": "Muse shows the output",
    "film": 2,
    "series": "Assignment 4 lecture films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "A data pipeline that only writes JSON is a pipeline nobody uses. Raw data is not an output. An output is a file a human can open, scan, and act on. Today: the gallery.",
            "screen": "Writer at desk; line on screen: raw JSON is not an output."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Output: a file built for a human. Digest: the one-page summary of everything scored. Brief: a single role card with the score, the reasons, the link, and a next step. Proof: the run report that shows the work is real.",
            "screen": "Four terms appear: output / digest / brief / proof."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "The test is simple. Could a non-technical person use this? Raw JSON fails the test. A brief card passes: the title, the fit, one sentence of why, the posting link, and what to do next. If the file can't be read by a human, it isn't output — it's exhaust.",
            "screen": "JSON block vs brief card; checkmark lands on the brief."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "The flow that produced it, end to end. Input: postings from eighteen boards plus the live Anthropic feed. Processing: the matcher scores each one. Output: the digest, the briefs, the report. Proof: the run report that ties every number back to a real run.",
            "screen": "Pipeline: Input, Processing, Output, Proof."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "First stop in the gallery: the digest. One page, dated 2026-10-03. Twenty-two PURSUE roles at the top, each with the fit score, the reasons, and the posting link. Thirty-seven NETWORK below. Three hundred twenty-five WATCH in the appendix. It exists as markdown for us and as HTML for everyone else.",
            "screen": "Digest mockup: header, first PURSUE rows."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Brief one: Developer Education Lead, Claude Platform, at Anthropic. Fit zero point nine one — the highest score in the run. Why: the title names developer education, the text names our audiences, and the company demand is the maximum. The next step is written on the card: draft the application.",
            "screen": "Anthropic brief card; why-bullets appear one by one."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Brief two: Designer Advocate, Partnerships, at Figma. Fit zero point eight four. This was one of the original target roles, and the brief shows the pairing rule working: the audience fit and the gap-close reward firing together on a real title.",
            "screen": "Figma brief card; audience names highlight."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Brief three: Learning Experiences Creator, at Replit. Fit zero point seven five. The bullseye recovered — this is the exact role we were chasing from the start, and the matcher surfaced it on its own. Each of the fifteen briefs ends the same way: with a suggested next step, not a dead end.",
            "screen": "Replit brief card; next-step line fades in."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "The proof the gallery is real: the run report. Seven hundred fourteen postings scored in three point one seconds. Zero quarantined, zero errors. Twenty-two pursue, thirty-seven network, three hundred twenty-five watch, three hundred thirty skip. Every number the digest claims is in this file.",
            "screen": "Run report table; decisions bar."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The quality check. I read every output as a non-technical user would. Three questions: can I state in one sentence why this role fits? Can I find the posting link? Is there a next step? All fifteen briefs pass all three. The HTML digest opens in a browser with nothing to install.",
            "screen": "Browser window with HTML digest; three checkboxes tick."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "And the honest gap. The scheduled delivery — approvals, the weekly digest, the email to Nik — is specified in the workflow file but not yet implemented. The outputs exist. The loop that delivers them on schedule does not. It is the clearest TODO in the assignment, and I'm not hiding it.",
            "screen": "Scheduling block greyed out, TODO stamp."
        },
        {
            "id": "B10", "scene": "M12", "dur_s": 22, "act": "4",
            "voice": "Muse",
            "line": "The loop, closed. Three thousand four hundred forty-six postings collected across eighteen boards. Seven hundred fourteen scored in one run. One digest covering fifty-nine actionable roles, fifteen full briefs for the PURSUE set, one run report as proof. From raw data to files a person can open. That is what an output is.",
            "screen": "Funnel: 3,446 -> 714 -> digest + 15 briefs + report."
        },
        {
            "id": "BVDT", "scene": "M13", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, an output is a file a human can open, and this project's flow runs input to proof. Act two, the gallery: one digest, fifteen briefs, one run report, all from real runs. Act three, the quality check passes — and the scheduled delivery is the honest gap. Act four, the loop is closed: from postings to files a person can use.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M13", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Open the HTML digest, pick one PURSUE brief, and run the three-question test: one sentence of why, one link, one next step. Then tell me: which brief would you act on first?",
            "screen": "Do-today card: open the digest, pick a brief, name your first move."
        },
        {
            "id": "BOUT", "scene": "M13", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next film: the scale tests.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    for b in BS["beats"]:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
    assert len(BS["beats"]) == 15, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 10
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
