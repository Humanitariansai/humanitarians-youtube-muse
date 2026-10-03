#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Muse making a film about Muse".

LECTURE, channel claude-liam (Liam, in for Bear · Kokoro am_onyx · @NikBearBrown).
The film about Muse, made by Muse. Source: ~/docs/muse.md (primary),
~/docs/client-surfaces.md, ~/docs/data-handling.md. Every claim doc-grounded
(see FACTCHECK.md); prices, tier names, and model version numbers are never
claimed.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "claude-liam-lecture-muse-making-a-film-about-muse"
TITLE = "Muse making a film about Muse"


def beat(bid, act, narration, cls, image, show, claim=None):
    return {
        "beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "GRAPHIC", "source": "own",
            "visual_intent": image, "show": show,
            "manim": {"class": cls},
            "motion_claim": claim or image,
        },
        "qc": {
            "sparse_by_design": True,
            "sparse_reason": "lecture style: one drawn scene on a cream stage per beat, minimal labels, voice carries the explanation.",
        },
    }


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {
        "beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": show,
                 "remotion": {"pattern": pattern, "props": props}},
    }
    b.update(extra)
    return b


B = [
    # ── ACT I — what Muse is ──────────────────────────────────────────────
    beat("B01", "what it is",
         "Muse is a personal AI agent. Everyone gets their own — you get an agent, and it runs on its own dedicated computer, which stays with you between conversations.",
         "M01_OwnAgent",
         "One user mark and one computer mark; a pairing link draws between them and holds.",
         [{"at": 0.1, "event": "user mark and computer mark"},
          {"at": 0.4, "event": "pairing link draws"}],
         claim="The drawn 1:1 link is the claim: one agent, one computer, yours."),
    beat("B02", "what it is",
         "And it's strictly personal. Every conversation is between you and your own agent. No group chats, no shared rooms. One to one.",
         "M02_StrictlyPersonal",
         "Two nodes joined by one link; a third node reaches in and its link is crossed out in terracotta.",
         [{"at": 0.1, "event": "two nodes, one link"},
          {"at": 0.5, "event": "third node rejected"}],
         claim="The rejected third connection teaches 'no group chats' in motion."),
    beat("B03", "what it is",
         "Under the hood, it's powered by Muse Spark — from Meta's Muse model family.",
         "M03_MuseSpark",
         "A lineage tree builds downward: Meta, then the Muse model family, then Muse Spark, then Muse.",
         [{"at": 0.1, "event": "Meta node"},
          {"at": 0.35, "event": "family branches"},
          {"at": 0.6, "event": "Muse Spark lands"},
          {"at": 0.8, "event": "Muse at the root"}],
         claim="The growing tree is the lineage."),
    beat("B04", "what it is",
         "Muse went live on September 8th, 2026, and it's available in the US and Canada.",
         "M04_LaunchDate",
         "A timeline; a tick lands on September 8, 2026; 'US' and 'Canada' labels fade in beneath.",
         [{"at": 0.2, "event": "timeline"},
          {"at": 0.45, "event": "tick lands on the date"},
          {"at": 0.7, "event": "US + Canada labels"}],
         claim="The tick landing on the date is the launch event."),
    # ── ACT II — what it does ─────────────────────────────────────────────
    beat("B05", "what it does",
         "Chat is the front door. Every surface opens on a conversation — you talk, it answers, and the thread stays yours.",
         "M05_ChatFrontDoor",
         "Chat bubbles converge from four surface marks into the agent mark at center.",
         [{"at": 0.1, "event": "surface marks"},
          {"at": 0.4, "event": "bubbles converge"}],
         claim="The converging bubbles show every surface leading to the same agent."),
    beat("B06", "what it does",
         "It remembers. Your conversations, your preferences, your files — they carry from one chat to the next, so you never start over.",
         "M06_ItRemembers",
         "Chat one deposits a memory chip into a store; chat two retrieves the same chip.",
         [{"at": 0.15, "event": "chat one deposits the chip"},
          {"at": 0.55, "event": "chat two retrieves it"}],
         claim="Deposit then retrieve, in motion, is memory across chats."),
    beat("B07", "what it does",
         "It uses tools. Skills and connectors plug it into mail, calendar, shopping, media, and your paired devices — it can act, not just answer.",
         "M07_UsesTools",
         "Hub-and-spoke: the agent at center, tool nodes around; links light up one by one.",
         [{"at": 0.1, "event": "agent hub, tool nodes"},
          {"at": 0.4, "event": "links light up in turn"}],
         claim="The lighting links show it reaching out and using the tools."),
    beat("B08", "what it does",
         "It builds things. Artifacts — documents, web pages, apps — that you keep, and keep using.",
         "M08_BuildsThings",
         "Parts assemble into a document, then a page, then an app icon — each labeled once.",
         [{"at": 0.15, "event": "document assembles"},
          {"at": 0.45, "event": "page assembles"},
          {"at": 0.7, "event": "app assembles"}],
         claim="Assembly in motion is the making."),
    beat("B09", "what it does",
         "It keeps your stuff. Files you hand it land in your Library — organized, and findable.",
         "M09_KeepsYourStuff",
         "File marks flow into a Library shelf that fills, row by row.",
         [{"at": 0.15, "event": "files arrive"},
          {"at": 0.5, "event": "shelf fills"}],
         claim="The filling shelf is accumulation made visible."),
    beat("B10", "what it does",
         "And it works while you're away. Scheduled checks, Feed posts, Ideas, Goals — the work goes on when you're not watching.",
         "M10_WorksWhileAway",
         "A clock sweeps while task cards complete along a timeline; the user mark is absent.",
         [{"at": 0.15, "event": "clock starts, user mark leaves"},
          {"at": 0.45, "event": "task cards complete"}],
         claim="Time passing with work happening, and no user present."),
    # ── ACT III — where you reach it ──────────────────────────────────────
    beat("B11", "where you reach it",
         "On the web, at muse.ai — the full app in your browser: chat, feed, ideas, goals, library.",
         "M11_WebApp",
         "A browser-window skin labeled muse.ai; chat lines type themselves inside.",
         [{"at": 0.15, "event": "browser window"},
          {"at": 0.45, "event": "chat lines type"}],
         claim="The typing lines show the app alive in the browser."),
    beat("B12", "where you reach it",
         "On your phone — native iPhone and Android apps, with the same tabs and the same agent.",
         "M12_MobileApps",
         "Two phone marks; chat lines animate in on both, in sync.",
         [{"at": 0.15, "event": "two phones"},
          {"at": 0.45, "event": "chat lines on both"}],
         claim="Synced lines on both phones: the same agent, everywhere."),
    beat("B13", "where you reach it",
         "On your Mac — a chat app that also pairs your Mac as one of its devices, so it can work with what's there.",
         "M13_MacApp",
         "A desktop mark; a pairing link draws to the agent and pulses.",
         [{"at": 0.15, "event": "desktop mark"},
          {"at": 0.45, "event": "pairing link draws and pulses"}],
         claim="The drawn, pulsing link is the pairing."),
    beat("B14", "where you reach it",
         "And over WhatsApp — Muse as a messaging channel. The same agent, in the chat app you already use.",
         "M14_WhatsApp",
         "A phone mark; message bubbles exchange between the phone and the agent.",
         [{"at": 0.15, "event": "phone mark"},
          {"at": 0.45, "event": "bubbles exchange"}],
         claim="The exchange is the channel working."),
    # ── ACT IV — how it's paid for ────────────────────────────────────────
    beat("B15", "how it's paid for",
         "It's free to start. Free access comes with a usage limit — enough to put it to work.",
         "M15_FreeTier",
         "A meter fills and stops dead at a limit line.",
         [{"at": 0.2, "event": "meter fills"},
          {"at": 0.6, "event": "stops at the limit"}],
         claim="The meter stopping IS the usage limit."),
    beat("B16", "how it's paid for",
         "And there's a paid monthly subscription for more usage, whenever you need it.",
         "M16_Subscription",
         "The same meter; the cap lifts higher and the meter fills past the old line.",
         [{"at": 0.2, "event": "cap lifts"},
          {"at": 0.55, "event": "meter fills higher"}],
         claim="The same meter, a higher cap — the rhyme teaches the difference."),
    beat("B17", "how it's paid for",
         "You subscribe at muse.ai, or through the Apple App Store and Google Play. It renews monthly, unless you cancel.",
         "M17_WhereToSubscribe",
         "Three purchase marks; a circular monthly arrow turns above them.",
         [{"at": 0.15, "event": "three purchase marks"},
          {"at": 0.5, "event": "monthly arrow turns"}],
         claim="The turning arrow is the renewing subscription."),
]

OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. You've heard the name Muse. But what is it — just another chatbot? No. It's something more specific. Let me show you what it does, and how it's paid for.",
        "BrutalistHesitantWriter",
        {"text": "What is Muse —\njust another chatbot?",
         "triggerWords": "just another chatbot",
         "replacementWords": "a personal agent",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
         "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'What is Muse —'"},
         {"at": 0.5, "event": "backspaces 'just another chatbot' → 'a personal agent' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive chatbot framing and corrects it to the real one: a personal agent.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    ),
    remotion(
        "BDEFS", "terms",
        "Four terms. Agent: a program that works for you on its own. Memory: what it keeps about you between chats. Skill: one built-in thing it knows how to do. Artifact: a document, page, or app it builds for you.",
        "ClaudeDefinitions",
        {"title": "Terms In This Lecture",
         "terms": [
             {"term": "agent", "meaning": "a program that works for you on its own"},
             {"term": "memory", "meaning": "what it keeps about you between chats"},
             {"term": "skill", "meaning": "one built-in thing it knows how to do"},
             {"term": "artifact", "meaning": "a document, page, or app it builds for you"},
         ],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'agent' lands"},
         {"at": 0.4, "event": "'memory' lands"},
         {"at": 0.62, "event": "'skill' lands"},
         {"at": 0.8, "event": "'artifact' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: four prerequisites, one line each."},
    ),
]

YT_PROMPT = ("Remember one preference about me: I take my coffee black. Then, in a brand-new chat, "
             "tell me what you remember about my coffee. When I ask you to forget it, forget it.")

B = OPEN + B + [
    remotion(
        "BVDT", "recap",
        "Let's recap with Claude. Muse is your own personal AI agent, on its own computer. "
        "It talks, remembers, uses tools, builds things, and works while you're away. "
        "You reach it on the web, your phone, your Mac, or WhatsApp. "
        "It's free with a usage limit — or a monthly subscription for more.",
        "ClaudeVerdictArtifact",
        {"artifactTitle": "What is Muse",
         "artifactHeading": "Recap",
         "brandLabel": "@NikBearBrown",
         "artifactLines": [
             "Muse is your own personal AI agent, on its own computer.",
             "It talks, remembers, uses tools, builds things, and works while you're away.",
             "You reach it on the web, your phone, your Mac, or WhatsApp.",
             "It's free with a usage limit — or a monthly subscription for more.",
         ]},
        [{"at": 0.1, "event": "line 1 lands"},
         {"at": 0.35, "event": "line 2 lands"},
         {"at": 0.6, "event": "line 3 lands"},
         {"at": 0.8, "event": "line 4 lands"}],
    ),
    remotion(
        "BHTF", "your turn",
        "Your turn. Paste this into Muse: " + YT_PROMPT + " Then check two things yourself. "
        "Does it recall the preference correctly in the new chat? And does it offer to forget it when you ask?",
        "ClaudeComposerAsk",
        {"greeting": "Your turn.", "topic": "MUSE · YOUR TURN",
         "segment": "Test Its Memory", "command": YT_PROMPT,
         "runningText": "paste this into Muse…",
         "output": ["Check: it recalls the preference correctly in the new chat.",
                    "Check: it offers to forget it when you ask."],
         "folderLabel": "@NikBearBrown", "modelLabel": "Muse Spark", "effortLabel": "Low"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.8, "event": "two check lines land"}],
    ),
    {
        "beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
        "narration_text": f"{TITLE}. At Nik Bear Brown.",
        "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {"title": TITLE, "slug": SLUG,
                          "handle": "@NikBearBrown", "subline": ""},
            },
        },
        "kind": "outro_voice", "tail_silence_s": 1.0,
    },
]

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "topic": "MUSE · WHAT IT IS",
        "skill": "lecture", "style_preset": "lecture",
        "channel": "claude-liam", "persona": "Liam (in for Bear)",
        "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
        "clock": "narration", "palette": "claude", "register": "Teardown",
        "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
        "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
        "audience": "anyone who has heard the name Muse and wants the plain version",
        "source_doc": "~/docs/muse.md (primary); ~/docs/client-surfaces.md; ~/docs/data-handling.md",
        "playlist": "Muse", "chapter_number": 0,
        "tags": ["Muse", "Meta", "personal AI agent", "Muse Spark", "Nik Bear Brown"],
    },
    "beats": B,
}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b["estimated_duration_s"] for b in B)), "s")
