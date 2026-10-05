# SHOTLIST.md — The long game

Scene table: scene → beat → what the viewer sees → narration beat source.
House style: show-tell — one isometric Manim drawing per beat, Claude
palette, minimal labels (1–3 words), the voice explains. Cast of objects
kept the same all film: the page stack (the finished document), the
outline card (the skeleton, with its section rows), section pages, ink
arrows (the handoff), the terracotta scan line (the stitching
read-through), terracotta checks (approvals) and flag dots (problems).

No ShowTellCard kinds are used: every beat is a thing, a part, or a flow,
so each passes the card test toward "draw it". The side-by-side beat (B07)
is two drawings next to each other, not a `tabs` card, because the claim
("twenty pages that fall apart" vs. "a document that holds together")
lives in the drawings, not in switching views. The outline card's section
rows and the rule card's three lines are the documents' own content
written on the card — the idea in each beat is the document itself, so a
drawing of the bare card would say less, not more. [judgment]

| Scene | Beat | What the viewer sees | Data source |
|-------|------|----------------------|-------------|
| — | BIDEA | Hesitant writer: types "Write our twenty-page grant proposal." then corrects it to "Help me outline our grant proposal first." | film's own premise |
| — | BDEFS | Terms card: outline / section / stitch | ACTS.md term definitions |
| B00_Stack | B00 | A tall stack of pages drops in; a title line draws on the top page; label "the goal" | film's own premise |
| B01_AllAtOnce | B01 | The neat stack bursts into five scattered pages; label "all at once"; terracotta dots flag the repeated pair and the contradicted page | film's own premise |
| B02_Drift | B02 | Three pages in a row, numbered 3, 9, 14; label "it drifts"; repeat dots on page 9, a changed-fact dot on page 14; a staple draws across them | film's own premise |
| B03_Outline | B03 | The drift pages fade; the outline card lands; its four section rows draw in; a terracotta check stamps approval; label "move one: outline" | film's own premise |
| B04_SectionOne | B04 | The outline card slides left; the section-one page drops in; an arrow draws card → page; label "move two: sections"; a check lands on the page | film's own premise |
| B05_Handoff | B05 | Section two drops below section one; arrows draw outline → section two and section one → section two; check and label "move three: the handoff" | film's own premise |
| B06_Stitching | B06 | Three numbered sections line up; a terracotta scan line sweeps down them; the repeated line lifts out and fades; label "the stitching" | film's own premise |
| B07_SideBySide | B07 | Left: the scattered pages return with label "one giant prompt". Right: a neat checked stack with label "the long game" | film's own premise |
| B08_Habit | B08 | One big card lands with its three rows ("outline first" / "one section per prompt" / "stitch at the end"); a check drops on it | film's own premise |
| — | BHTF | Claude composer: the viewer's first outline prompt, typed in full; two checks | film's own call to action |
| — | BOUT | Spoken outro: title + "At Nik Bear Brown" | film identity constants |

Every on-screen word is read aloud in its beat. Scene classes are literal
`class BNN_Name(Scene):` so run.sh finds them.
