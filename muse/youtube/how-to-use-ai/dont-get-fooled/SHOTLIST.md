# SHOTLIST.md — Don't get fooled.

Scene table: scene → beat → what the viewer sees → data source.
House style: Manim, 16:9, safe area ±6.3 x / ±3.4 y, ai-explainer Claude
palette (STAGE #F2F0E9, INK #3D3929, TERRA #D97757, DIM #8B8F96,
GHOST #D9D4C7, CARD #FAF9F5). Every on-screen word is read aloud in its
beat. Every scene carries the @NikBearBrown watermark bug (lower-right).
The Claude-style composer card (spark, serif header, typed lines) is the
recurring cast object at the bookends.

| Scene | Beat | What the viewer sees | Data source |
|-------|------|----------------------|-------------|
| M01 | B00 | Composer window: spark + "Olá, Liam" header; ask "Why does the AI sound so sure when it's wrong?" types in; "thinking…" runs; two output lines answer | film's hook (ask → result) |
| M02 | B01 | Paper card; "AI lies to you because it's badly trained." writes; terracotta strike crosses "badly trained"; "AI guesses the most likely words, not the truth." writes in | film's BLUF correction |
| M03 | B02 | Sentence stem "The capital of France is ___."; three candidate next-words with probability bars (Paris tall/terracotta, Lyon, Nice short/ghost); ring + arrow select Paris; caption "most likely ≠ always right" | next-token sampling mechanism (SOURCES 1) |
| M04 | B03 | Two identical answer cards, "Definitely." headers, "The treaty was signed in 1847."; terracotta X stamps left ("made up"); ink check lands right ("true"); rule plate "confident ≠ proof" | film's habit zero; example line is illustrative |
| M05 | B04 | Legal brief card "BRIEF — filed in court"; real citation "Varghese v. China Southern Airlines, 925 F.3d 1339 (11th Cir. 2019)" + two rows "citation 2/3 of 6 — invented"; terracotta "NOT A REAL CASE" stamps; "$5,000 fine" plate; caption "nobody checked, because nobody doubted" | Mata v. Avianca (SOURCES 2, 3) |
| M06 | B05 | Chat frame; source document card slides in with ghost lines; "Answer only from this text." types in; answer card emerges tethered to the document (terracotta line); tag "a reader can be checked" | grounding steps 1–2 (SOURCES 1) |
| M07 | B06 | Question card "What is the capital of Peru?"; document "Notes on cats" (ghost lines); terracotta gap opens between them; answer card writes "I don't know — it's not in the text."; ring circles "I don't know" | grounding step 3 (SOURCES 1) |
| M08 | B07 | Answer card quotes "The meeting is on Tuesday."; magnifier carries the quote to SAMPLE DOCUMENT; word-for-word match ticks (ink check); second quote "The meeting is on Friday." fails — terracotta X, "hallucinated citation" | citation audit (SOURCES 1); sample-doc lines are illustrative |
| M09 | B08 | Claim card "The new policy starts Monday." center; source cards A and B land left/right; ink checks land on each; badge "confident tone ≠ proof" drops | film's habit three; claim line is illustrative |
| M10 | B09 | Three numbered sentence cards stack: "Paste the source. Answer only from this text." / "If the answer isn't in the text, say you don't know." / "Quote the exact sentence — and check it." (terracotta edge); checks land on each | the three grounding sentences (SOURCES 1) |
| M11 | BVDT | Three recap lines reveal with dot bullets: "It guesses words, not truth." / "Ground it: paste the source; answer only from it; allow 'I don't know'." / "Audit it: quote the passage; check the quote; cross-check what matters." | — (recap) |
| M12 | BHTF | Composer card; "Your turn." header; the three-line prompt types in with terracotta underlines; "paste into Claude" tag lands | — (call to action) |
| M13 | BOUT | Title "Don't get fooled" writes in serif; terracotta rule draws; terracotta period drops; @NikBearBrown handle fades in | film identity constants |

Why drawings, no cards: no beat passes the show-tell card test — every
idea here is a thing, a flow, or a comparison (the predictor, the two
answers, the brief, the tether, the audit), never an interface or a
dataset. The composer appears only where the interface is the subject:
cold open and handoff. Zero lifted images; no real product UI.
