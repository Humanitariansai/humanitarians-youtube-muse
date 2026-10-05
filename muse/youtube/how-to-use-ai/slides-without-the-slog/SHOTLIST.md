# SHOTLIST.md — Slides without the slog

Scene table: scene → beat → what the viewer sees → narration beat source.
House style: show-tell — one isometric Manim drawing per beat, Claude
palette, minimal labels (1–3 words), the voice explains. Cast of objects
kept the same all film: the messy notes page (rough input), the slide
card (white card, ink headline bar, ghost text lines), the wall card (a
slide drowned in dense text lines), the outline card (numbered
one-line-per-slide rows), the notes card (speaker notes), ink arrows
(the flow from notes to deck), deep-kraft sight lines (the room looking
at the slide), terracotta checks (approvals) and flag dots (problems).

No ShowTellCard kinds are used: every beat is a thing, a part, or a
flow, so each passes the card test toward "draw it". The side-by-side
beat (B07) is two drawings next to each other, not a `tabs` card,
because the claim ("eighteen slides of walls of text" vs. "a deck
people can actually read") lives in the drawings, not in switching
views. The outline card's slide rows, the notes card's lines, and the
rule card's three lines are the documents' own content written on the
card — the idea in each beat is the document itself, so a drawing of the
bare card would say less, not more. [judgment]

| Scene | Beat | What the viewer sees | Data source |
|-------|------|----------------------|-------------|
| — | BIDEA | Hesitant writer: types "Make my notes into a slide deck." then corrects it to "Turn my notes into a slide deck, one move at a time." | film's own premise |
| — | BDEFS | Terms card: outline / slide / polish | ACTS.md term definitions |
| B00_Goal | B00 | A messy notes page drops in; an arrow draws to three clean slide cards in a row; label "the goal"; a terracotta check | film's own premise |
| B01_Walls | B01 | One big wall-of-text slide lands; two more stacked behind it; label "all at once"; terracotta dots flag the walls of text | film's own premise |
| B02_WhyRead | B02 | The wall slide on stage; three audience dots land; their deep-kraft sight lines draw to the slide, not the speaker; label "walls get read" | film's own premise |
| B03_Outline | B03 | The outline card lands; its five slide rows draw in; a terracotta check stamps approval; label "move one: outline" | film's own premise |
| B04_OneSlide | B04 | The outline card slides left while slide one drops in; an arrow draws card → slide; label "move two: one slide"; a check lands on the slide | film's own premise |
| B05_Polish | B05 | A full slide; its text lines lift out and fade one by one; a notes card appears below and catches them (label "notes"); label "the polish: cut"; a check | film's own premise |
| B06_BackRow | B06 | The slide shrinks toward the back of the room; a check stamps it; label "the back-row test" | film's own premise |
| B07_SideBySide | B07 | Left: two wall-of-text cards with label "one giant prompt". Right: a neat four-page stack with a check and label "outline, slides, polish" | film's own premise |
| B08_Habit | B08 | One big card lands with its three rows ("outline first" / "one slide per prompt" / "polish last"); a check drops on it | film's own premise |
| — | BHTF | Claude composer: the viewer's first deck-outline prompt, typed in full; two checks | film's own call to action |
| — | BOUT | Spoken outro: title + "At Nik Bear Brown" | film identity constants |

Every on-screen word is read aloud in its beat ("notes" is spoken inside
"speaker notes"). Scene classes are literal `class BNN_Name(Scene):` so
run.sh finds them.
