#!/usr/bin/env python3
"""make_sheet.py — Muse proves it scales (Film 3).

14 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse proves it scales",
    "film": 3,
    "series": "Assignment 4 lecture films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "Every demo works on a laptop. The question that matters is: what happens at fifty times the load? We ran the test. Here's the honest answer — including the part where nothing broke.",
            "screen": "Wall with a crack; the question: will it break?"
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Scale: how the work grows with the load. Breaking point: the load where it stops working. Measured: numbers from a real run. Estimated: honest arithmetic, clearly labeled — never dressed up as a measurement.",
            "screen": "Four terms: scale / breaking point / measured / estimated."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "The test design. Three lanes: one times the real data, six hundred forty records. Ten times: six thousand four hundred. Fifty times: thirty-two thousand. Each lane runs the full pipeline — dedup, scoring, routing — timed end to end, with peak memory recorded.",
            "screen": "Three lanes: 1x, 10x, 50x."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "The method, honestly. We replicated real Anthropic records — the same shape as production data — with unique ids. Same titles, same descriptions. The timing is real; the load is synthetic. That's the caveat, stated up front.",
            "screen": "One real record card multiplies into a grid."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 24, "act": "2",
            "voice": "Muse",
            "line": "The table. Six hundred forty records: two point three seven seconds. Six thousand four hundred: twenty-three point eight seconds. Thirty-two thousand: one hundred nineteen seconds. Peak memory: fifty-two to sixty-five megabytes. Measured, not modeled.",
            "screen": "Results table with the four numbers."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "And the shape of it: a straight line. Three point seven two milliseconds per record at every scale — one x, ten x, fifty x, identical. Linear means predictable: a hundred thousand records would take about six minutes. Boring. That's the compliment.",
            "screen": "Straight line chart; label: linear, 3.72 ms/record."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "The fetch side, measured live. One pull from the Anthropic board: six hundred forty jobs, nine point two megabytes, six point two seconds, HTTP two hundred. No rate limit, no retry needed. One board is cheap; eighteen boards is the real weekly shape, and that multiplication is still untested.",
            "screen": "Fetch pipe: 640 jobs, 9.2 MB, 6.2 s, HTTP 200."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The breaking point? We didn't find it. At fifty times the load the run takes two minutes and works. What's untested is named, not hidden: n8n at scale, rate-limit behavior if we ever push the API hard, and writing a thousand brief files instead of fifteen. The honest gap is in the report.",
            "screen": "Magnifier over empty map; stamp: breaking point not found."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "Cost. The matcher makes zero API calls and zero LLM calls — it's arithmetic, not inference. Cost per hundred postings: about a third of a second of CPU, which is zero dollars. A weekly production run: effectively zero dollars a month. Estimated — but estimated from a measured zero.",
            "screen": "Price tag: $0.00; zero API calls, zero LLM calls."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 24, "act": "3",
            "voice": "Muse",
            "line": "Production readiness, judged. Scoring: ready at any realistic volume — the tests prove it. Fetching: polite and single-threaded; it wants retry and backoff per board before it's scheduled. Delivery: not ready — the scheduled approval and weekly email is specified but unimplemented. That is the one blocker.",
            "screen": "Checklist: scoring check, fetching tilde, delivery cross."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 20, "act": "4",
            "voice": "Muse",
            "line": "The verdict. Scale is boring — the numbers are linear, the memory is flat, the cost is zero. The blocker was never scale. It's delivery: the loop that puts the digest in front of a human on schedule. That is the next thing to build.",
            "screen": "Verdict card: scale is boring; delivery is the blocker."
        },
        {
            "id": "BVDT", "scene": "M12", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, the test — three lanes, one x to fifty x, real record shapes. Act two, the results — linear at three point seven two milliseconds a record, fetch at six seconds a board. Act three, no breaking point found, cost zero, and the untested territory named. Act four, the verdict: scale is boring; delivery is the blocker.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M12", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Pick a load your own project will actually see and run the same three lanes: one x, ten x, fifty x. Find your per-record cost. Then ask: is your blocker scale, or is it something else?",
            "screen": "Do-today card: run three lanes; find your per-record cost."
        },
        {
            "id": "BOUT", "scene": "M12", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next film: the professional package.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    assert len(BS["beats"]) == 14, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 9, len(acts)
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
