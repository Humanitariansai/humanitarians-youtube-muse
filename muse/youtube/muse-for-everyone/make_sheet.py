#!/usr/bin/env python3
"""make_sheet.py — "Muse making a film about Muse" (general-audience redo).

Builds beat_sheet.json: 22 beats, four acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm plus small pauses; body ~ 14-20s per beat.
"""
import json

BS = {
    "title": "Muse making a film about Muse",
    "film": "muse-for-everyone",
    "series": "Humanitarians AI — Muse films (general-audience redos)",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "Hallo. This is Liam, in for Bear. So — Muse. Just another chatbot? No. A personal agent. This film about Muse was made by Muse, and I'll show you what that means, in plain words.",
            "screen": "Writer types 'just another chatbot', strikes it, types 'a personal agent'."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Agent: a program that works for you on its own. Memory: what it keeps about you between chats. Skill: one built-in thing it knows how to do. Artifact: a document, page, or app it builds for you.",
            "screen": "Four terms appear: agent / memory / skill / artifact."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "First: what it is. Muse is a personal AI agent. Everyone gets their own — you get an agent, and it runs on its own dedicated computer, which stays with you between conversations. One person, one agent, one computer.",
            "screen": "User mark, agent mark, computer mark; 1:1 pairing link draws."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 18, "act": "1",
            "voice": "Muse",
            "line": "And it's strictly personal. Every conversation is between you and your agent. No group chats, no shared spaces, no strangers reading along. It's yours the way your phone is yours.",
            "screen": "One chat window, one user; a second window is crossed out."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 16, "act": "1",
            "voice": "Muse",
            "line": "Under the hood it runs on Muse Spark — Meta's family of AI models, the engine behind the agent. Built by Meta, made for regular people.",
            "screen": "'Muse Spark' engine label glows inside the computer mark."
        },
        {
            "id": "B04", "scene": "M05", "dur_s": 16, "act": "1",
            "voice": "Muse",
            "line": "It launched on September 8th, 2026, in the United States and Canada. That's the basics — now what it actually does for you.",
            "screen": "Calendar flips to Sept 8 2026; US + Canada pins drop."
        },
        {
            "id": "B05", "scene": "M06", "dur_s": 18, "act": "2",
            "voice": "Muse",
            "line": "It talks with you. Chat is the front door — you just write what you want, the way you'd text a helpful friend. That works the same on every surface.",
            "screen": "Chat bubbles appear one by one, alternating sides."
        },
        {
            "id": "B06", "scene": "M07", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "It remembers. Tell it you like your news summaries short, and next week it still knows. Your conversations, your preferences, your files — they carry over between chats.",
            "screen": "Notebook opens; preference slips file in; week-page flips, slips stay."
        },
        {
            "id": "B07", "scene": "M08", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "It uses tools. With your approval, it can read your email, manage your calendar, look up products, even work with paired devices. Think of these as plug-ins you switch on.",
            "screen": "Plug icons (mail, calendar, cart, phone) light up one by one."
        },
        {
            "id": "B08", "scene": "M09", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "It builds things. Ask for a trip plan and you get a document. Ask for a webpage and you get a page. These are called artifacts — things you keep, not just chat replies.",
            "screen": "Blank page; document lines draw in; page lifts into a 'kept' tray."
        },
        {
            "id": "B09", "scene": "M10", "dur_s": 18, "act": "2",
            "voice": "Muse",
            "line": "It keeps your stuff. Everything it makes for you lands in one place — your files, and a Library tab where they collect. Nothing vanishes when the chat ends.",
            "screen": "Shelves; files slide on; 'Library' label."
        },
        {
            "id": "B10", "scene": "M11", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "And it works while you're away. It can run scheduled checks, remind you of things, write you briefing posts, track your goals. Your agent has its own computer — it doesn't sleep when you do.",
            "screen": "Clock face; night falls; task checkmarks tick while the user sleeps."
        },
        {
            "id": "B11", "scene": "M12", "dur_s": 16, "act": "3",
            "voice": "Muse",
            "line": "Where do you reach it? Start on the web, at muse.ai. That's the front door most people use.",
            "screen": "Browser window draws; 'muse.ai' types into the address bar."
        },
        {
            "id": "B12", "scene": "M13", "dur_s": 16, "act": "3",
            "voice": "Muse",
            "line": "Or the phone apps — iPhone and Android. Same agent, same memory, in your pocket.",
            "screen": "Phone draws; the same chat bubbles appear inside it."
        },
        {
            "id": "B13", "scene": "M14", "dur_s": 16, "act": "3",
            "voice": "Muse",
            "line": "There's a Mac app too, which pairs your Mac as one of its devices.",
            "screen": "Laptop draws beside the phone."
        },
        {
            "id": "B14", "scene": "M14", "dur_s": 16, "act": "3",
            "voice": "Muse",
            "line": "And if you live in WhatsApp, your agent can meet you there as well.",
            "screen": "WhatsApp message bubble pops with checkmarks."
        },
        {
            "id": "B15", "scene": "M15", "dur_s": 18, "act": "4",
            "voice": "Muse",
            "line": "How is it paid for? There's free access with a usage limit — enough to actually use it, not just a demo.",
            "screen": "Gauge fills to the 'free' mark and stops."
        },
        {
            "id": "B16", "scene": "M15", "dur_s": 18, "act": "4",
            "voice": "Muse",
            "line": "And an optional paid monthly subscription if you want more usage. Same agent, same features — you're paying for volume, not unlocking a better brain.",
            "screen": "Second gauge fills past the free mark: 'paid monthly'."
        },
        {
            "id": "B17", "scene": "M16", "dur_s": 18, "act": "4",
            "voice": "Muse",
            "line": "You sign up at muse.ai or through the Apple App Store or Google Play. Subscriptions renew monthly, and you can cancel anytime.",
            "screen": "Signup flow: muse.ai → app store badges → monthly cycle arrow."
        },
        {
            "id": "BVDT", "scene": "M17", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, Muse is your own personal AI agent on its own computer — strictly yours. Act two, it talks, remembers, uses tools, builds things, keeps your files, and works while you're away. Act three, you reach it on the web, your phone, your Mac, or WhatsApp. Act four, free with a limit, or paid monthly for more.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M17", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Ask Muse to remember one preference — say, how you take your news summaries. Then open a new chat and ask what it remembers. Two checks: it recalls it right, and it offers to forget it if you ask.",
            "screen": "Do-today card: remember one preference; new chat; check recall."
        },
        {
            "id": "BOUT", "scene": "M17", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching.",
            "screen": "Title card: 'Muse making a film about Muse' + @NikBearBrown."
        }
    ]
}

if __name__ == "__main__":
    for b in BS["beats"]:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
    assert len(BS["beats"]) == 22, len(BS["beats"])
    assert 13 <= len(BS["beats"]) <= 22, "beat count outside 13-22 band"
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 17, len(acts)
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    assert recap["line"].lower().count("act ") >= 4, "recap must cover each act"
    total = sum(b["dur_s"] for b in BS["beats"])
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
