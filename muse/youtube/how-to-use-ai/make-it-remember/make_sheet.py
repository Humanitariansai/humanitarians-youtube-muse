#!/usr/bin/env python3
"""make_sheet.py — Make it remember (and forget) (Humanitarians AI YouTube film, #24 of 24).

Builds beat_sheet.json: 13 beats, show-tell spine (hesitant writer -> terms
-> the notebook -> what to store -> what never to store -> where it lives ->
fix one note -> pause vs reset -> incognito -> memory is not the chat ->
memory is not the archive -> your turn -> outro).
Skill: show-tell. Persona: Liam, in for Bear. TTS: Kokoro am_onyx.
Register: Teardown. Channel: claude-liam. Watermark: @NikBearBrown.

Skill note (recorded in BUILD-LOG.md): the assignment named cc-explainer,
but cc-explainer's TERMINAL-FIRST / REAL-SESSION laws cannot be satisfied —
there is no Claude Code terminal session to reconstruct, no `claude` CLI in
this VM, and no credential authorized by the task to run one. The topic
(memory features for a general audience) is the direct sibling of
set-it-up-once (custom instructions), which shipped as show-tell. So this
film is built as show-tell.

Source: NEW — built from scratch (no mirror source). Facts verified
2026-10-04: Claude memory (Settings -> Memory -> Topics), pause vs reset,
sensitive-topics opt-in, never-stored categories, incognito chats, chat
search as a separate feature (see FACTCHECK.md). Product details are the
minimum needed; UI paths are kept shallow so the film doesn't rot.

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~150 wpm narration => words/2.5 + small pause, rounded.
"""
import json

SLUG = "make-it-remember"
TITLE = "Make it remember (and forget)"


def manim(beat_id, cls, show_events, sparse_reason=None):
    shot = {"type": "MANIM", "manim": {"class": cls},
            "show": [{"at": at, "event": ev} for at, ev in show_events]}
    if sparse_reason:
        shot["qc"] = {"sparse_by_design": True, "sparse_reason": sparse_reason}
    return shot


B = [
    {
        "beat_id": "BIDEA", "act": "the question", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": ("Hallo. This is Liam, in for Bear. You open a fresh "
                           "chat, and the AI doesn't know a thing about you. "
                           "Except — that's not quite true anymore. It keeps "
                           "notes, saved from your chats. The question isn't "
                           "whether it remembers. It's: what should be on those "
                           "notes, what should never be there, and how do you check?"),
        "estimated_duration_s": 23, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.0, "event": "types 'How do I make Claude remember me between chats?'"},
                {"at": 0.6, "event": "backspaces 'remember me' -> 'remember what matters, forget what doesn't' on the spoken correction"}],
            "remotion": {
                "pattern": "BrutalistHesitantWriter",
                "props": {
                    "text": "How do I make\nClaude remember me\nbetween chats?",
                    "triggerWords": "remember me",
                    "replacementWords": "remember what matters, forget what doesn't",
                    "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
                    "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
                    "seed": "make-it-remember", "banner": ""}}},
        "lead_silence_s": 0.8,
        "motion_claim": ("The writer types the naive 'make Claude remember me' "
                         "question and corrects it to the real one: remember "
                         "what matters, forget what doesn't."),
        "qc": {"sparse_by_design": True,
               "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    },
    {
        "beat_id": "BDEFS", "act": "terms", "lane": "bookend",
        "proof_gate": "CARD",
        "narration_text": ("Three terms. Memory: notes the AI saves from your "
                           "chats and reads in new ones. Topics: the list of "
                           "notes — you can read, edit, or delete each one. "
                           "And incognito: a chat that leaves no trace in memory."),
        "estimated_duration_s": 15, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.12, "event": "'memory' lands"},
                {"at": 0.5, "event": "'topics' lands"},
                {"at": 0.78, "event": "'incognito' lands"}],
            "remotion": {
                "pattern": "ClaudeDefinitions",
                "props": {
                    "title": "Terms In This Film",
                    "terms": [
                        {"term": "memory",
                         "meaning": "notes the AI saves from your chats and reads in new ones"},
                        {"term": "topics",
                         "meaning": "the list of notes — read, edit, or delete each one"},
                        {"term": "incognito",
                         "meaning": "a chat that leaves no trace in memory"}],
                    "folderLabel": "@NikBearBrown"}}},
        "qc": {"sparse_by_design": True,
               "sparse_reason": "TERMS card: three prerequisites, one line each."},
    },
    {
        "beat_id": "B00", "act": "the notes", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Here is what memory actually is. You chat, and as "
                           "you talk, Claude takes notes. Mention your café's "
                           "move to Lisbon — that lands in the notebook. Open "
                           "a new chat next week, and the notebook opens on the "
                           "first page."),
        "estimated_duration_s": 16, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B00", "B00_TheNotebook", [
            (0.05, "chat window fades in left; the open notebook fades in right, labelled 'memory'"),
            (0.35, "user bubble 'moving my café to Lisbon' lands in the window"),
            (0.55, "a 'café in Lisbon' note card drops into the notebook"),
            (0.80, "the old window leaves; a 'new chat' window arrives; a kraft cable draws notebook → window")],
            "show-tell body beat: one window, one note, one notebook"),
        "motion_claim": "The spoken fact becomes a card in the notebook, then the notebook feeds a new chat.",
    },
    {
        "beat_id": "B01", "act": "the notes", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("What belongs there? Three kinds of notes, all "
                           "recurring. What you're working on. How you like "
                           "things done. And the details that keep coming up — "
                           "your manager's name, the headcount for the event. "
                           "The test: would a future chat thank you for this?"),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B01", "B01_KeepWorthy", [
            (0.05, "the notebook fades in, labelled 'memory'"),
            (0.30, "'café in Lisbon' card lands: what you're working on"),
            (0.50, "'bullet points' card lands: how you like things done"),
            (0.70, "'Ana: short updates' card lands: the recurring details"),
            (0.88, "an ink check and a 'the test' label land beside the notebook")],
            "show-tell body beat: three keep-worthy cards, one test"),
        "motion_claim": "Three example notes drop into the notebook; the check marks the keeper test.",
    },
    {
        "beat_id": "B02", "act": "the red lines", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("And what never goes in? Secrets, full stop. "
                           "Passwords, card numbers, door codes — never in a "
                           "chat that becomes memory. And the sensitive stuff: "
                           "health, beliefs, politics. Claude leaves those out "
                           "by default, and only saves them if you explicitly "
                           "switch it on. Even then, some things are never "
                           "saved at all: ID numbers, criminal history, "
                           "immigration status."),
        "estimated_duration_s": 23, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B02", "B02_NeverIn", [
            (0.05, "the notebook fades in, labelled 'memory'"),
            (0.25, "'passwords', 'card numbers', 'door codes' cards land"),
            (0.45, "a terracotta X crosses each of the three cards"),
            (0.65, "a dim 'health · beliefs · politics' pill lands left, 'off by default'"),
            (0.85, "a dim 'never stored: ID numbers' pill lands right, 'even with opt-in'")],
            "show-tell body beat: three banned cards, two guarded pills"),
        "motion_claim": "The banned cards are crossed out; the guarded pills carry the defaults.",
    },
    {
        "beat_id": "B03", "act": "the red lines", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("So where does the notebook live? Settings, then "
                           "Memory, then Topics. The whole list, open. Read "
                           "each card. If a note looks wrong — outdated, or "
                           "something you'd never have said — that's where you fix it."),
        "estimated_duration_s": 14, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B03", "B03_WhereItLives", [
            (0.05, "settings panel fades in, labelled 'settings'"),
            (0.30, "'Settings', 'Memory', 'Topics' pills land in the panel in order"),
            (0.60, "the cursor lands on the 'Topics' pill"),
            (0.75, "the open notebook fades in right with two cards, labelled 'memory'")],
            "show-tell body beat: one panel, three words, the open notebook"),
        "motion_claim": "The cursor picks 'Topics'; the notebook opens on the whole list.",
    },
    {
        "beat_id": "B04", "act": "the red lines", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("One note is wrong — your company moved offices. "
                           "Lift the card, rewrite the line, set it back. From "
                           "here on, every chat gets it right. And the stale "
                           "one? Delete it. Outdated notes don't age well; "
                           "they argue with the new ones."),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B04", "B04_FixOne", [
            (0.05, "the notebook fades in with 'old office' and 'old menu' cards"),
            (0.30, "the pencil lands; the 'old office' card lifts out and rewrites to 'new office'"),
            (0.60, "the fixed card sets back in; an ink check and 'fixed' label land"),
            (0.82, "a terracotta X crosses 'old menu'; the stale card leaves")],
            "show-tell body beat: one note fixed, one deleted"),
        "motion_claim": "The wrong card lifts, rewrites, and sets back; the stale card is deleted.",
    },
    {
        "beat_id": "B05", "act": "the controls", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("The two big levers. Pause: the notebook stays on "
                           "the shelf. Claude stops reading it and stops "
                           "adding to it. Reset: the notebook empties — every "
                           "topic, gone. That one is permanent. So: pause to "
                           "take a break, reset only when you mean it."),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B05", "B05_TwoLevers", [
            (0.05, "the notebook fades in with two cards; 'Pause' and 'Reset' pills land"),
            (0.30, "the cursor lands on 'Pause'; the notebook slides onto a shelf line, 'paused' label"),
            (0.60, "the cursor moves to 'Reset'; the cards leave the notebook, 'gone — for good' label"),
            (0.85, "an ink check lands on the 'Pause' pill")],
            "show-tell body beat: two levers, two different endings"),
        "motion_claim": "Pause shelves the notebook; Reset empties it for good.",
    },
    {
        "beat_id": "B06", "act": "the controls", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("And for the one-off question: incognito. A chat "
                           "that leaves no trace in memory — nothing saved, "
                           "nothing used. The gift you're price-checking, the "
                           "awkward question for a friend. Ask it, close it, gone."),
        "estimated_duration_s": 13, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B06", "B06_Incognito", [
            (0.05, "an 'incognito' chat window fades in left; the notebook fades in right, closed"),
            (0.35, "user bubble 'a gift for Ana?' lands in the window"),
            (0.65, "a note card rises toward the notebook, meets a terracotta X, and leaves")],
            "show-tell body beat: the note that never lands"),
        "motion_claim": "The incognito note rises, is turned away, and is gone.",
    },
    {
        "beat_id": "B07", "act": "the controls", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Two things memory is not. First: deleting the chat "
                           "doesn't delete the note. The chat is the "
                           "conversation; the note lives in the notebook, "
                           "apart. Trash the chat all you want — the note "
                           "stays until you delete it."),
        "estimated_duration_s": 15, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B07", "B07_ChatDelete", [
            (0.05, "chat window labelled 'the chat' left; notebook labelled 'the notebook' right with a 'deadline: Friday' card"),
            (0.40, "a terracotta X crosses the chat window; the window and bubble leave"),
            (0.70, "an ink check and a 'stays' label land on the notebook's card")],
            "show-tell body beat: the chat leaves, the note stays"),
        "motion_claim": "The chat is deleted; the note card stays in the notebook.",
    },
    {
        "beat_id": "B08", "act": "the controls", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Second: memory isn't your archive. Searching your "
                           "old chats is a separate feature, with its own "
                           "setting. The notes get loaded into new chats "
                           "automatically; the archive you search. Two doors "
                           "into your past — and you can close either one."),
        "estimated_duration_s": 16, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B08", "B08_NotArchive", [
            (0.05, "the notebook labelled 'memory' fades in left; a dark archive cabinet labelled 'archive' fades in right; a small 'new chat' window fades in top center"),
            (0.40, "a kraft cable draws from the notebook to the new chat window"),
            (0.65, "a 'search it yourself' label lands under the archive"),
            (0.85, "a 'memory: on' pill and an 'archive: on' pill land under their boxes")],
            "show-tell body beat: two doors, two switches"),
        "motion_claim": "The notebook feeds new chats automatically; the archive waits to be searched.",
    },
    {
        "beat_id": "BHTF", "act": "your turn", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": ("Your turn. In your next chat, paste this: Remember "
                           "this about me: I like my answers short and "
                           "practical. Now tell me what's in your memory. "
                           "Then check it. Open Settings, then Memory, then "
                           "Topics — and find the new note. Ask: what do you "
                           "remember about me? And compare. If a note looks "
                           "wrong, edit it. That's the whole habit: check the "
                           "notebook."),
        "estimated_duration_s": 25, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.0, "event": "Composer opens — 'Your turn.'"},
                {"at": 0.1, "event": "the prompt types in full"},
                {"at": 0.8, "event": "two check lines land"}],
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "AI · YOUR TURN",
                    "segment": "Make It Remember (And Forget)",
                    "command": ("Remember this about me: I like my answers "
                                "short and practical. Now tell me what's in "
                                "your memory."),
                    "runningText": "paste this into your next chat…",
                    "output": [
                        "Check: open Settings, then Memory, then Topics — find the new note.",
                        "Check: ask 'what do you remember about me?' and compare."],
                    "folderLabel": "@NikBearBrown"}}},
    },
    {
        "beat_id": "BOUT", "act": "outro", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": "Make it remember (and forget). At Nik Bear Brown.",
        "estimated_duration_s": 5, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [{"at": 0.0, "event": "title restates; handle"}],
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Make it remember (and forget)",
                    "slug": "make-it-remember",
                    "handle": "@NikBearBrown",
                    "subline": "What to store, what never to store, how to delete it."}}},
        "kind": "outro_voice",
        "tail_silence_s": 1.0,
    },
]

METADATA = {
    "slug": SLUG, "title": TITLE, "topic": "AI · MEMORY",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "watermark": "@NikBearBrown",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the "
                              "hesitant writer + terms card, no verdict card; "
                              "Your Turn is the composer; spoken outro stays."),
    "audience": ("smart general audience — pragmatic, not necessarily AI "
                 "experts; every term explained"),
    "source_doc": "NEW — built from scratch 2026-10-04 (no mirror source); "
                  "facts verified 2026-10-04, see FACTCHECK.md",
    "playlist": "How to use AI", "chapter_number": 24,
    "tags": ["memory", "Claude memory", "privacy", "settings",
             "how to use AI", "Nik Bear Brown"],
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in B]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05",
                   "B06", "B07", "B08", "BHTF", "BOUT"], ids
    assert len(B) == 13, len(B)
    assert sum(1 for b in B if b["lane"] == "manim") == 9, "expected 9 manim body beats"
    assert sum(1 for b in B if b["lane"] == "bookend") == 4, "expected 4 bookends"
    total = sum(b["estimated_duration_s"] for b in B)
    assert 200 <= total <= 320, f"total duration {total}s outside 200-320s band"
    for b in B:
        assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
        assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", \
            f"{b['beat_id']}: voice/engine"
        assert b["shot"]["show"], f"{b['beat_id']}: no show block"
        if b["lane"] == "manim":
            cls = b["shot"]["manim"]["class"]
            assert cls.startswith(b["beat_id"] + "_"), \
                f"{b['beat_id']}: class {cls} must start with beat id"
    # IN-FOR-BEAR law
    assert "Liam, in for Bear" in B[0]["narration_text"], "name the voice"
    # BIDEA trigger contract: trigger appears verbatim in text; neither ends in punctuation
    _tp = B[0]["shot"]["remotion"]["props"]
    assert _tp["triggerWords"] in _tp["text"].replace("\n", " "), \
        "triggerWords not verbatim in text"
    assert _tp["triggerWords"][-1] not in ".?!" and \
        _tp["replacementWords"][-1] not in ".?!", \
        "trigger/replacement must not end in punctuation"
    # BDEFS term-length contract (ClaudeDefinitions truncates past ~17 chars)
    for t in B[1]["shot"]["remotion"]["props"]["terms"]:
        assert len(t["term"]) <= 17, f"BDEFS term too long: {t['term']!r}"
    # BHTF prompt contract: the command is read in full in the narration
    _htf = next(b for b in B if b["beat_id"] == "BHTF")
    assert _htf["shot"]["remotion"]["props"]["command"] in \
        _htf["narration_text"], "BHTF prompt not read in full"
    # BOUT outro contract
    _out = next(b for b in B if b["beat_id"] == "BOUT")
    assert _out["kind"] == "outro_voice" and _out["tail_silence_s"] == 1.0, \
        "BOUT must be outro_voice with 1.0s tail"
    sheet = {"metadata": METADATA, "beats": B}
    with open("beat_sheet.json", "w") as f:
        json.dump(sheet, f, indent=2, ensure_ascii=False)
    print(f"beats={len(B)} manim=9 bookends=4 total={total}s "
          f"(~{total//60}m{total%60:02d}s)")
