#!/usr/bin/env python3
"""make_sheet.py — Stop using your own Claude at work (personal-ai-at-work).

Builds beat_sheet.json: 14 beats, five acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm plus small pauses; body ~ 15-22s per beat.
Skill: lecture (BIDEA/BDEFS/BVDT/BHTF/BOUT spine; best-visual-per-beat body).
"""
import json

BS = {
    "title": "Stop using your own Claude at work.",
    "film": None,
    "series": "Humanitarians AI — Muse films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "You use your own AI chatbot at work — Claude, ChatGPT, whichever. Handy for summaries and debugging. But the things you paste in can end up training the AI company's model, kept for years. Samsung found that out the hard way. This film walks through the story, the mechanism, and the fix.",
            "screen": "Chat window sketch; a pasted 'confidential' slip slides in; arrow to a model box; 'kept for years' tag."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 25, "act": "hook",
            "voice": "Muse",
            "line": "Six terms. Personal AI: a chatbot account that belongs to you, not your company. Training: when your chats are used to improve the AI model. Retention: how long the company keeps those chats. NDA: the secrecy agreement you signed. Anonymize: stripping names and details out before you paste. Enterprise plan: a business account — by default, your data never trains the model.",
            "screen": "Six term cards appear: personal AI / training / retention / NDA / anonymize / enterprise plan."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 21, "act": "1",
            "voice": "Muse",
            "line": "April 2023. Samsung lets its semiconductor engineers use ChatGPT at work. Within twenty days, three leaks. One engineer pastes buggy source code to check it. Another pastes yield code to optimize it. A third uploads a recording of an internal meeting, for notes. All confidential. All now sitting on OpenAI's servers.",
            "screen": "Twenty-day timeline; permission marker at day zero; three leak pips: source code, yield code, meeting recording."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 15, "act": "1",
            "voice": "Muse",
            "line": "Samsung's answer: a company-wide ban on ChatGPT and the other AI tools — and disciplinary investigations into the engineers who pasted. Not for malice. For pasting. That's the ceiling on how this goes wrong.",
            "screen": "Chat window with a prohibition sign over it; 'company-wide ban' and 'disciplinary investigations' tags."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 21, "act": "2",
            "voice": "Muse",
            "line": "Here's the mechanism. On personal Claude plans — Free, Pro, Max — your chats and coding sessions can be used to improve the model. The setting is opt-out, so don't assume: open Settings, then Privacy, and check 'Help improve our AI models'. Everything you paste with that on joins the training pool.",
            "screen": "Chat bubbles flow into a model box; a settings row shows the training toggle on, about to flip off."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "And it stays there. With the setting on, Anthropic can keep those chats for up to five years. With it off, they're deleted within about thirty days. One catch: opting out only applies going forward. Data already in a training run can't be pulled back. Check the toggle before your next chat, not after.",
            "screen": "Two bars: 'setting ON: up to 5 years' (long) vs 'setting OFF: ~30 days' (short); 'opt-out starts now' tag."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 16, "act": "3",
            "voice": "Muse",
            "line": "For Claude: Settings, then Privacy, and switch off 'Help improve our AI models'. Takes ten seconds. And check it on every device you use — phone and computer — because the default may not be what you expect.",
            "screen": "Settings panel sketch; Privacy row; the training toggle knob flips to OFF; check mark lands."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 18, "act": "3",
            "voice": "Muse",
            "line": "Same idea everywhere else. ChatGPT: Settings, Data Controls, switch off 'Improve the model for everyone'. Grok: your profile settings, data controls, turn off training and sharing. Gemini: go to myactivity.google.com and switch off the Gemini activity toggle. Four apps, four toggles, two minutes.",
            "screen": "Four toggle cards: Claude / ChatGPT / Grok / Gemini, each with its path and an 'off' check."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 22, "act": "4",
            "voice": "Muse",
            "line": "Now the uncomfortable part. I'm no lawyer — talk to yours. But a lawyer could frame one paste three ways: breach of the NDA you signed, because the AI company is an outside party. Violation of data-protection law, depending where you are. Breach of your IT security policy. None of them need malicious intent.",
            "screen": "Three cards: NDA breach / data-protection law / IT policy breach; 'a paste is enough' stamp."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 19, "act": "5",
            "voice": "Muse",
            "line": "So here's the clean-room rule. Keep your personal account, but never paste client names, internal financials, source code, or meeting recordings. Anonymize first: swap real names for placeholders like CLIENT NAME, and rewrite the specifics. The AI still answers. The secrets never leave the room.",
            "screen": "A document's confidential lines get crossed out and replaced with [CLIENT NAME] / [REVENUE] / [CODE] placeholders."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 19, "act": "5",
            "voice": "Muse",
            "line": "And if you set policy for a team: get the company a business plan. Team and Enterprise accounts don't train on your data by default. Flag the exposure, show what one leak costs, and make the case. One leak costs more than a hundred plans.",
            "screen": "Personal plan card (trains by default) vs Team/Enterprise card (no training by default); 'make the case' tag."
        },
        {
            "id": "BVDT", "scene": "M12", "dur_s": 28, "act": "recap",
            "voice": "Muse",
            "line": "Let's recap. Samsung said yes to ChatGPT, and three leaks happened in twenty days. Your chats can train the model on a personal plan. Opted in, they're kept up to five years; opting out only starts now. Four apps, four toggles — flip them all. One paste can break an NDA, a law, and your IT policy. Anonymize before you paste — or get the company an enterprise plan.",
            "screen": "Six recap lines, one per movement of the film."
        },
        {
            "id": "BHTF", "scene": "M12", "dur_s": 24, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Open your chatbot's settings right now — this takes two minutes. Paste this into Claude: I use my personal Claude account at work. What data-hygiene rules should I follow so I don't violate my NDA or company policy? Give me a short checklist I can print and keep at my desk. Then actually flip the toggle.",
            "screen": "Do-today card: 1. Settings → Privacy: flip the toggle. 2. Paste the audit prompt into Claude."
        },
        {
            "id": "BOUT", "scene": "M12", "dur_s": 12, "act": "outro",
            "voice": "Muse",
            "line": "Stop using your own Claude at work. Muse, in for Bear. Thanks for watching.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    for b in BS["beats"]:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
        # ~150 wpm sanity: duration should cover the words plus a small pause
        words = len(b["line"].split())
        assert b["dur_s"] >= words / 3.2, f"{b['id']}: {b['dur_s']}s too short for {words} words"
    assert len(BS["beats"]) == 14, len(BS["beats"])
    assert 13 <= len(BS["beats"]) <= 22, "beat count outside 13-22 band"
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4", "5")]
    assert len(acts) == 9, len(acts)
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    kw = ["samsung", "train", "five years", "toggle", "nda", "enterprise"]
    missing = [k for k in kw if k not in recap["line"].lower()]
    assert not missing, f"recap misses: {missing}"
    total = sum(b["dur_s"] for b in BS["beats"])
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
