#!/usr/bin/env python3
"""make_sheet.py — Register for Muse with a privacy.com card (Film 1).

Builds beat_sheet.json: 15 beats, three acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm plus small pauses; body ~ 16-24s per beat.
"""
import json

BS = {
    "title": "Register for Muse with a privacy.com card",
    "film": 1,
    "series": "Humanitarians AI — Muse films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "You want to try Muse, Meta's personal AI agent. But signup asks for a credit card, and you don't want your real card on yet another form. Here's the workaround: a virtual card with a ten-dollar limit. This film shows you the whole path.",
            "screen": "Signup form sketch; card field circled; $10-limit virtual card slides in."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Muse: Meta's personal AI agent, free to start. Meta account: your Instagram or Facebook login — it changes the signup. Authorization hold: a one-dollar card check, not a charge, released in about a week. Virtual card: a privacy.com card number with its own spending limit.",
            "screen": "Four terms appear: Muse / Meta account / authorization hold / virtual card."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "First, what you're signing up for. Muse is Meta's personal AI agent — your own agent on its own computer. It launched in September 2026 for the US and Canada. Free to start, with a usage limit, and paid monthly plans if you want more. Use it on the web at muse.ai, or the phone and Mac apps.",
            "screen": "Three panels grow: muse.ai window, phone, Mac; US + Canada tag."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 18, "act": "1",
            "voice": "Muse",
            "line": "Now the fork. If you already have an Instagram, Facebook, or other Meta account, sign in with it. Meta already knows you, so it probably won't ask for a credit card at all. That's the easy path — most people take it.",
            "screen": "Fork diagram; YES path (have Meta account) gets the checkmark."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "No Meta account? Then signup asks for a card. It places a one-dollar authorization hold — a card validity check, not a charge — and releases it in about a week. Standard practice. But if you'd rather not hand over your real card, here's the workaround.",
            "screen": "$1 coin drops on a card; 'hold, not a charge'; release timeline fills."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "privacy.com makes virtual debit cards — real card numbers that draw from your bank, each with its own spending limit. There's a free tier. One catch: it's US-only. If you're in the US, this is the workaround.",
            "screen": "Virtual card mockup; US-only tag; free tier tag."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Step one: make a privacy.com account. Link your bank account or debit card as the funding source and verify your identity — that's the KYC check. Step two: hit New Card, name it something like Muse signup, and you get a fresh sixteen-digit number, expiry, and CVV.",
            "screen": "Two-step flow: account card (bank link + ID check) → new card with fresh number."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "Step three: set the limit. Click Spend Limit on the card, type ten dollars, and pick per-transaction or total. Anything over ten dollars is declined automatically. The one-dollar hold clears easily inside a ten-dollar limit — and nothing bigger can ever go through.",
            "screen": "Limit slider animates to $10; $1 coin fits under the limit bar."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "Step four: use it at Muse signup. Enter the virtual card number, expiry, and CVV where it asks for a card. The one-dollar hold goes through, signup completes. After that, pause or close the card — it locks to the first merchant anyway, so it can't be used anywhere else.",
            "screen": "Card details fly into the signup form; hold clears; pause icon lands."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 18, "act": "3",
            "voice": "Muse",
            "line": "Card accepted — now setup. Muse asks your name, then what to call your agent. Pick something you'll like saying. This is your personal agent, not a shared chatbot: every conversation is between you and it.",
            "screen": "Two name fields type in; 'personal, not shared' bubble."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "Then it offers to connect your apps — Gmail and Google Calendar. This is optional, and it's what makes the agent useful: it can read your inbox and manage your schedule, with your approval. Connect now, or skip and do it later.",
            "screen": "Gmail and Calendar connect cards; toggles flip on; 'optional' tag."
        },
        {
            "id": "B10", "scene": "M12", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "And you're in. Free access with a usage limit gets you started; paid monthly plans add more. Your agent has its own computer, so it can keep working while you're away. The whole signup cost you one virtual card — your real card number never touched the form.",
            "screen": "Agent at its own computer; usage-limit gauge; 'real card never touched the form' stamp."
        },
        {
            "id": "BVDT", "scene": "M13", "dur_s": 24, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, the signup fork — a Meta account probably skips the card; without one, expect a one-dollar hold, released in about a week. Act two, the workaround — a privacy.com virtual card with a ten-dollar limit clears the hold and caps your exposure. Act three, setup — name yourself, name your agent, connect your apps, and you're in.",
            "screen": "Three recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M13", "dur_s": 18, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Today: open privacy.com, create the card, set the ten-dollar limit. Then go to muse.ai and register. Tell me what you named your agent.",
            "screen": "Do-today card: 1. privacy.com → new card → $10 limit. 2. muse.ai → register."
        },
        {
            "id": "BOUT", "scene": "M13", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next film: connecting Gmail without the mess.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    for b in BS["beats"]:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
    assert len(BS["beats"]) == 15, len(BS["beats"])
    assert 13 <= len(BS["beats"]) <= 22, "beat count outside 13-22 band"
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3")]
    assert len(acts) == 10, len(acts)
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    assert recap["line"].lower().count("act ") >= 3, "recap must cover each act"
    total = sum(b["dur_s"] for b in BS["beats"])
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
