# SHOTLIST.md — Small steps, big jobs

Scene table: scene → beat → what the viewer sees → narration beat source.
House style: show-tell — one isometric Manim drawing per beat, Claude
palette, minimal labels (1–3 words), the voice explains. Cast of objects
kept the same all film: the giant box (the whole job), step cards
(isometric pages), arrows (handoff), a mush page, check marks.

No ShowTellCard kinds are used: every beat is a thing, a part, or a flow,
so each passes the card test toward "draw it". The side-by-side beat (B06)
is two drawings next to each other, not a `tabs` card, because the claim
("everything at once" vs. "checked steps stacked") lives in the drawings,
not in switching views.

| Scene | Beat | What the viewer sees | Data source |
|-------|------|----------------------|-------------|
| — | BIDEA | Hesitant writer: types "Plan my whole kitchen renovation!" then corrects it to "Break my kitchen renovation into small steps!" | film's own premise |
| — | BDEFS | Terms card: prompt / step / context | ACTS.md term definitions |
| B00_GiantBox | B00 | One giant sealed box with terracotta tape drops in; label "the whole job" | film's own premise |
| B01_MushOut | B01 | The box slides left; a big page comes out; a messy scribble draws across it; label "mush" | film's own premise |
| B02_WhyFails | B02 | The page fades; the box opens; five labeled step cards (budget, layout, materials, timeline, your taste) tumble out in a jumble | film's own premise |
| B03_StepOne | B03 | The jumble fades; one clean step card drops center; label "step one: budget" | film's own premise |
| B04_StepTwo | B04 | The budget card stays; the layout card drops beside it; an arrow draws budget → layout; label "built on step one" | film's own premise |
| B05_Materials | B05 | The materials card drops beside the layout card; an arrow draws layout → materials; a check lands on it | film's own premise |
| B06_Timeline | B06 | The timeline card drops beside the materials card; the arrow chain completes; checks land on every card | film's own premise |
| B07_SideBySide | B07 | Left: the mush page returns with label "one giant prompt"; right: the four checked cards stack neatly with label "small steps" | film's own premise |
| B08_OneJob | B08 | One big card lands on the stack: "one job per prompt"; a check drops on it | film's own premise |
| — | BHTF | Claude composer: the viewer's first step-one prompt, typed in full; two checks | film's own call to action |
| — | BOUT | Spoken outro: title + "At Nik Bear Brown" | film identity constants |

Every on-screen word is read aloud in its beat. Scene classes are literal
`class BNN_Name(Scene):` so run.sh finds them.
