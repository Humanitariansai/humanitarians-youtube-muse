#!/usr/bin/env python3
"""make_sheet.py — What never to paste into AI (what-never-to-paste-into-ai).

Builds beat_sheet.json: 14 beats, three acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm plus small pauses; body ~ 18-25s per beat.
Skill: lecture (BIDEA/BDEFS/BVDT/BHTF/BOUT spine; best-visual-per-beat body).
cc-explainer was assigned and rejected: this film has no terminal session;
the lecture BDEFS beat is what the audience rule needs. See BUILD-LOG.md.
"""
import json

BS = {
    "title": "What never to paste into AI",
    "film": None,
    "series": "Humanitarians AI — Muse films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 25, "act": "hook",
            "voice": "Muse",
            "line": "This is Liam, in for Bear. You paste things into an AI chatbot the way you'd talk to a friend — private, easy, gone when you're done. Except it isn't gone. Think of it as a postcard instead: everyone who handles it along the way can read it. This film is the postcard test — what never to paste into AI.",
            "screen": "Chat bubble slides into a postcard frame; 'like a postcard' tag."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 24, "act": "hook",
            "voice": "Muse",
            "line": "Six terms. The postcard test: would you write it on a postcard? Training: when your chats are used to improve the AI model. Retention: how long the company keeps your chats. Redaction: blacking bits out. Anonymize: swapping real names for fakes. Credential: anything that logs you in — passwords, keys, codes.",
            "screen": "Six term cards appear: postcard test / training / retention / redaction / anonymize / credential."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 25, "act": "1",
            "voice": "Muse",
            "line": "Here's the why. When you paste text into a chatbot, it leaves your phone and lands on the AI company's servers. Depending on the product and its settings, what you pasted can be stored, read by staff checking for abuse or improving the model, or used to train future versions of it. Not will — can. That's the whole reason for the rule.",
            "screen": "Phone → arrow → company server; three plates light up: stored / reviewed by staff / may train the model."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "The settings matter. On a personal plan, find the training toggle and switch it off yourself. On a business plan, your data normally never trains the model. Defaults differ by product — and they change — so check yours. But no toggle covers everything. That's why the never-list exists.",
            "screen": "Personal-plan card with a training toggle flipping off; business-plan card: 'no training by default'."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 23, "act": "2",
            "voice": "Muse",
            "line": "First: passwords and credentials. Passwords, API keys, the export from your password manager. Whoever sees a credential owns the account — and for this purpose, the AI counts as whoever. Never paste one. If you need login help, describe the problem: 'my two-factor code stopped arriving' beats the code itself.",
            "screen": "Fake credential lines get crossed out: 'pa55word-EXAMPLE', 'sk-fake-0000'; ban sign lands."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "Second: full money numbers. Bank account numbers, card numbers — the digits that move money. A balance is a fact; an account number is a key. Paste 'I have about two grand in checking' if the question needs it. Never the sixteen digits.",
            "screen": "Test card number '4111 1111 1111 1111' and 'routing: 000000000' crossed out; 'keys, not facts' tag."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 18, "act": "2",
            "voice": "Muse",
            "line": "Third: other people's private stuff. Your kid's name and school. Someone's medical details. A friend's message they never wrote to the AI company. You can take risks with your own information. You can't consent for anyone else.",
            "screen": "Three figures: kid's name + school / medical details / a friend's message; 'you can't consent for them' tag."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Fourth: work-confidential material you don't own. Client data, unreleased numbers, internal code. There's a whole film on the work version of this rule — the short version is: if the secret isn't yours, the paste isn't yours to make. Ask before you paste, or don't paste.",
            "screen": "Confidential slips feed into a locked box; 'not yours to paste' tag."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 25, "act": "3",
            "voice": "Muse",
            "line": "Now the good news: you can still get help. Redact first. Black out the account number, the password, the name — edit it in a notes app before you paste, or use the chat's own edit. The AI answers just as well, because it never needed the secret. It needed the shape of the problem.",
            "screen": "Sensitive lines on a document get covered by black redaction bars; 'the AI answers anyway' tag."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 25, "act": "3",
            "voice": "Muse",
            "line": "Or anonymize. Swap the real names for placeholders: 'my client — call them Client X.' 'A revenue figure — call it R.' The AI doesn't know your client from Client X, and the answer comes back the same. And when in doubt, describe instead of paste: summarize the document, don't upload the document.",
            "screen": "Real labels crossed out, replaced by [CLIENT X] / [R]; 'summarize, don't upload' tag."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "Last: make it a reflex. Before you hit enter on anything sensitive, ask the postcard question: would I write this on a postcard and hand it to a stranger? If yes, type away. If no — redact, anonymize, or describe. Three seconds of pause, and the rule runs itself.",
            "screen": "A postcard with a question mark; 'the 3-second pause' tag."
        },
        {
            "id": "BVDT", "scene": "M12", "dur_s": 28, "act": "recap",
            "voice": "Muse",
            "line": "Let's recap. A chat is a postcard, not a diary: pasted text can be stored, reviewed, or used for training. Never paste passwords or credentials. Never paste full money numbers. Never paste other people's private details — you can't consent for them. Never paste work secrets you don't own. Redact, anonymize, or describe — and ask the postcard question before you hit enter.",
            "screen": "Six recap lines, one per movement of the film."
        },
        {
            "id": "BHTF", "scene": "M12", "dur_s": 26, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Open your chatbot and paste this: 'Act as my privacy coach. I handle school forms for my kids, client invoices, and medical bills. Ask me five questions, then give me a personal never-paste checklist I can keep by my desk.' Then check one thing: is training still turned on in your settings?",
            "screen": "Do-today card: 1. Paste the privacy-coach prompt. 2. Check whether training is still on."
        },
        {
            "id": "BOUT", "scene": "M12", "dur_s": 12, "act": "outro",
            "voice": "Muse",
            "line": "What never to paste into AI. Muse, in for Bear. Thanks for watching.",
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
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3")]
    assert len(acts) == 9, len(acts)
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    kw = ["postcard", "password", "money", "consent", "redact"]
    missing = [k for k in kw if k not in recap["line"].lower()]
    assert not missing, f"recap misses: {missing}"
    total = sum(b["dur_s"] for b in BS["beats"])
    assert 240 <= total <= 360, f"total {total}s outside 4-6 min band"
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
