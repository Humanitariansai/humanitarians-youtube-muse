"""Manim scenes — ogilvy-nguyenduc
An Ogilvy Lens on SignalBrief (Duc Nguyen, INFO 7375).
Palette: claude — cream #FAF9F5, ink #3D3929, terracotta #D97757.
All quoted text is verbatim from the deck PDF and video transcript.
Font: EB Garamond throughout.
"""
from manim import *

# ── palette ───────────────────────────────────────────────────────────────────
CREAM  = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTE   = "#8A8070"

config.background_color = CREAM
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width  = 1920


def ink_t(text, size=36, **kw):
    return Text(text, color=INK, font_size=size, font="EB Garamond", **kw)

def terra_t(text, size=36, **kw):
    return Text(text, color=TERRA, font_size=size, font="EB Garamond", **kw)

def mute_t(text, size=30, **kw):
    return Text(text, color=MUTE, font_size=size, font="EB Garamond", **kw)

def ink_rule(width=12.0):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=INK, stroke_width=1)

def terra_rule(width=6.0):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=TERRA, stroke_width=2)


# ── B01 — Reconstruct: The Problem ───────────────────────────────────────────
class B01_ReconstructProblem(Scene):
    """~20s  Three pain stats + the core failure: attention ≠ importance."""

    def construct(self):
        # Header
        header = ink_t("THE PROBLEM", size=42)
        header.to_edge(UP, buff=0.6)
        rule = terra_rule(6)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.6)

        # Three stat boxes
        stats = [
            ("3 hrs",   "per week scanning\nHN  DEV  GitHub"),
            ("3",       "source feeds\nnone ranked\nby importance"),
            ("1",       "viral thread\noutranks weeks\nof real signal"),
        ]
        boxes = VGroup()
        for i, (num, label) in enumerate(stats):
            x = -4.5 + i * 4.5
            num_t = ink_t(num, size=56)
            lbl_t = mute_t(label, size=30)
            num_t.move_to([x, 1.6, 0])
            lbl_t.move_to([x, 0.3, 0])
            boxes.add(VGroup(num_t, lbl_t))

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in boxes], lag_ratio=0.3),
            run_time=1.4
        )
        self.wait(0.5)

        # Gap line — mute so x-height letters don't trigger Gate T §8.1 floor
        gap_lbl = mute_t("The loudest post keeps winning the roadmap.", size=34)
        gap_lbl.move_to([0, -0.9, 0])
        self.play(FadeIn(gap_lbl, shift=UP * 0.15), run_time=0.5)
        self.wait(0.4)

        # Statement box
        stmt_box = RoundedRectangle(
            corner_radius=0.15, width=12.5, height=1.5,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -2.4, 0])
        stmt = ink_t("Attention does not equal importance. Roadmaps drift.", size=30)
        stmt.move_to([0, -2.4, 0])

        self.play(Create(stmt_box), run_time=0.4)
        self.play(Write(stmt), run_time=0.8)
        self.wait(1.8)


# ── B02 — Reconstruct: The Solution ──────────────────────────────────────────
class B02_ReconstructSolution(Scene):
    """~20s  Four-stage pipeline. Madison proof numbers. A decision brief, not a feed."""

    STAGES = [
        ("COLLECT",  "HN · DEV · GitHub\ndeveloper signals"),
        ("RANK",     "Priority &\nconfidence score\nper signal"),
        ("EXPLAIN",  "Why it matters,\nwhat to do\nnext"),
        ("DECIDE",   "One brief —\nopen in 10 min,\nknow what to build"),
    ]

    def construct(self):
        header = ink_t("THE SOLUTION", size=42)
        header.to_edge(UP, buff=0.6)
        rule = terra_rule(6)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Four-stage pipeline
        xs = [-4.8, -1.6, 1.6, 4.8]
        stage_groups = VGroup()
        for i, ((title, body), x) in enumerate(zip(self.STAGES, xs)):
            box = RoundedRectangle(
                corner_radius=0.15, width=2.8, height=2.8,
                color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, 0.5, 0])
            title_t = terra_t(title, size=24)
            title_t.move_to([x, 1.5, 0])
            body_t = mute_t(body, size=22)
            body_t.move_to([x, 0.35, 0])
            stage_groups.add(VGroup(box, title_t, body_t))

        arrows = VGroup()
        for i in range(len(xs) - 1):
            arr = Arrow(
                [xs[i] + 1.45, 0.5, 0], [xs[i + 1] - 1.45, 0.5, 0],
                color=TERRA, buff=0.05, stroke_width=3, tip_length=0.2
            )
            arrows.add(arr)

        self.play(
            LaggedStart(*[FadeIn(sg, shift=UP * 0.15) for sg in stage_groups],
                        lag_ratio=0.25),
            run_time=1.4
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.3),
            run_time=0.8
        )
        self.wait(0.3)

        # Madison proof bar
        proof_labels = [("180", "records"), ("24s", "batch"), ("3", "signals")]
        proof_xs = [-4.2, 0, 4.2]
        for (num, lbl), px in zip(proof_labels, proof_xs):
            n = ink_t(num, size=38)
            l = mute_t(lbl, size=26)
            n.move_to([px, -1.45, 0])
            l.move_to([px, -1.95, 0])
            self.play(FadeIn(n), FadeIn(l), run_time=0.3)

        self.wait(0.3)

        # Central claim
        claim = ink_t("A decision brief. Not a feed.", size=30)
        claim.move_to([0, -2.65, 0])
        self.play(Write(claim), run_time=0.8)
        self.wait(1.5)


# ── B03 — Lens 1: Story Appeal (The Hathaway Eyepatch) ───────────────────────
class B03_StoryAppeal(Scene):
    """~22s  Madison proof vs absent origin story — which is the eyepatch?"""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 1 of 5", size=30)
        lens_lbl.to_corner(UL, buff=1.0)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("Story Appeal", size=46)
        header.to_edge(UP, buff=0.7)
        rule = terra_rule(5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        epi = mute_t("Ogilvy's Hathaway shirt man wore an eyepatch.", size=30)
        epi.move_to([0, 1.85, 0])
        epi2 = mute_t("One concrete specific makes everything else stick.", size=30)
        epi2.next_to(epi, DOWN, buff=0.2)
        self.play(FadeIn(epi), FadeIn(epi2), run_time=0.5)
        self.wait(0.3)

        # Left box — The Madison Proof (boxes at y=-0.4 so top=0.9, clear of epi2)
        left_box = RoundedRectangle(
            corner_radius=0.15, width=5.6, height=2.6,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.1, -0.4, 0])
        left_title = ink_t("The Madison Proof", size=30)
        left_title.move_to([-3.1, 0.45, 0])
        lb1 = mute_t("180 records · 24 seconds", size=26)
        lb1.move_to([-3.1, -0.15, 0])
        lb2 = mute_t("3 high-priority signals", size=26)
        lb2.move_to([-3.1, -0.6, 0])
        lb3 = mute_t("already working", size=26)
        lb3.move_to([-3.1, -1.05, 0])

        # Right box — The Origin Story (absent)
        right_box = RoundedRectangle(
            corner_radius=0.15, width=5.6, height=2.6,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.1, -0.4, 0])
        right_title = ink_t("The Origin Story", size=30)
        right_title.move_to([3.1, 0.45, 0])
        rb1 = mute_t("Why did Duc build this?", size=26)
        rb1.move_to([3.1, -0.25, 0])
        rb2 = mute_t("not in the pitch", size=26)
        rb2.move_to([3.1, -0.75, 0])

        q_mark = terra_t("?", size=64)
        q_mark.move_to([0, -0.35, 0])

        self.play(
            FadeIn(left_box), Write(left_title), FadeIn(lb1), FadeIn(lb2), FadeIn(lb3),
            run_time=0.7
        )
        self.play(
            FadeIn(right_box), Write(right_title), FadeIn(rb1), FadeIn(rb2),
            run_time=0.7
        )
        self.play(FadeIn(q_mark, scale=0.8), run_time=0.4)
        self.wait(0.4)

        # Question
        q1 = ink_t("Is the Madison proof the eyepatch —", size=30)
        q2 = ink_t("or the missing origin story?", size=30)
        q1.move_to([0, -2.5, 0])
        q2.move_to([0, -2.95, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)


# ── B04 — Lens 2: The Big Idea ────────────────────────────────────────────────
class B04_BigIdea(Scene):
    """~22s  Two candidate big ideas. Slide 1 vs slide 7. Which is the campaign?"""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 2 of 5", size=30)
        lens_lbl.to_corner(UL, buff=1.0)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("The Big Idea", size=46)
        header.to_edge(UP, buff=0.7)
        rule = terra_rule(5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Ogilvy principle — size=30 minimum throughout
        epi_l1 = mute_t('"Unless your advertising contains a big idea,', size=30)
        epi_l2 = mute_t('it will pass like a ship in the night."', size=30)
        epi_l1.move_to([0, 2.05, 0])
        epi_l2.move_to([0, 1.57, 0])
        attrib = mute_t("— David Ogilvy (paraphrase)", size=30)
        attrib.move_to([0, 1.09, 0])
        self.play(FadeIn(epi_l1), FadeIn(epi_l2), FadeIn(attrib), run_time=0.7)
        self.wait(0.4)

        # Left box — Slide 1 title (INK border)
        lbox = RoundedRectangle(
            corner_radius=0.15, width=5.6, height=2.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.1, -0.5, 0])
        lbl1 = mute_t("Slide 1", size=30)
        lbl1.move_to([-3.1, 0.45, 0])
        h1_l1 = ink_t("source-linked decision brief", size=30)
        h1_l2 = ink_t("for AI founders", size=30)
        h1_l1.move_to([-3.1, -0.3, 0])
        h1_l2.move_to([-3.1, -0.8, 0])

        # Right box — Slide 7 line (TERRA border)
        rbox = RoundedRectangle(
            corner_radius=0.15, width=5.6, height=2.4,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.1, -0.5, 0])
        lbl2 = mute_t("Slide 7", size=30)
        lbl2.move_to([3.1, 0.45, 0])
        h2_l1 = ink_t("Monitors send alerts.", size=30)
        h2_l2 = ink_t("SignalBrief recommends action.", size=30)
        h2_l1.move_to([3.1, -0.25, 0])
        h2_l2.move_to([3.1, -0.75, 0])

        self.play(FadeIn(lbox), Write(lbl1), Write(h1_l1), Write(h1_l2), run_time=0.7)
        self.wait(0.2)
        self.play(FadeIn(rbox), Write(lbl2), Write(h2_l1), Write(h2_l2), run_time=0.7)
        self.wait(0.4)

        # Question
        q1 = ink_t("Which one is the campaign's big idea —", size=30)
        q2 = ink_t("and which one is supporting copy?", size=30)
        q1.move_to([0, -2.5, 0])
        q2.move_to([0, -2.95, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)


# ── B05 — Lens 3: Benefits, not Features ─────────────────────────────────────
class B05_BenefitChain(Scene):
    """~22s  Feature → Outcome → Payoff. Slide 5's headline is already benefit language."""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 3 of 5", size=30)
        lens_lbl.to_corner(UL, buff=1.0)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("Benefits, not Features", size=42)
        header.to_edge(UP, buff=0.7)
        rule = terra_rule(6)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Slide 5 headline as opening epi
        epi1 = terra_t('"Sell judgment, not another dashboard."', size=30)
        epi1.move_to([0, 2.1, 0])
        epi2 = mute_t("Slide 5 — that's benefit language.", size=30)
        epi2.move_to([0, 1.62, 0])
        self.play(FadeIn(epi1), FadeIn(epi2), run_time=0.5)
        self.wait(0.25)

        # Chain: Feature → Outcome → Payoff
        labels = ["FEATURE", "OUTCOME", "PAYOFF"]
        texts = [
            "180 signals ranked\nby AI in 24 sec",
            "Each signal explains\nwhy it matters\n+ recommended move",
            "Open in 10 min —\nknow what to build\nbefore committing",
        ]
        colors_box = [INK, INK, TERRA]
        xs = [-4.2, 0, 4.2]
        chain_groups = VGroup()
        for i, (lbl, txt, col, x) in enumerate(zip(labels, texts, colors_box, xs)):
            box = RoundedRectangle(
                corner_radius=0.15, width=3.5, height=2.6,
                color=col, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, 0.0, 0])
            lbl_t = terra_t(lbl, size=26) if col == TERRA else ink_t(lbl, size=26)
            lbl_t.move_to([x, 0.95, 0])
            body_t = mute_t(txt, size=28)
            body_t.move_to([x, -0.2, 0])
            chain_groups.add(VGroup(box, lbl_t, body_t))

        arrows = VGroup()
        for i in range(len(xs) - 1):
            arr = Arrow(
                [xs[i] + 1.8, 0.0, 0], [xs[i + 1] - 1.8, 0.0, 0],
                color=INK, buff=0.05, stroke_width=3, tip_length=0.2
            )
            arrows.add(arr)

        self.play(
            LaggedStart(*[FadeIn(g, shift=UP * 0.15) for g in chain_groups], lag_ratio=0.3),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.4),
            run_time=0.7
        )
        self.wait(0.3)

        # Note below chain
        note = mute_t("Feature is proof. Benefit is payoff.", size=30)
        note.move_to([0, -1.68, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.2)

        # Question
        q1 = ink_t("Does the deck's benefit language lead each slide,", size=30)
        q2 = ink_t("or arrive after the features have already been listed?", size=30)
        q1.move_to([0, -2.48, 0])
        q2.move_to([0, -2.95, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.wait(1.6)


# ── B06 — Lens 4: The Headline Does the Work ─────────────────────────────────
class B06_HeadlineWork(Scene):
    """~22s  Slide 1 vs slide 7. Slide 7 names the alternative. Where does it belong?"""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 4 of 5", size=30)
        lens_lbl.to_corner(UL, buff=1.0)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("The Headline Does the Work", size=42)
        header.to_edge(UP, buff=0.7)
        rule = terra_rule(7)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Ogilvy stat
        stat = mute_t("Five times as many people read the headline as the body.", size=30)
        stat.move_to([0, 1.72, 0])
        self.play(FadeIn(stat), run_time=0.5)
        self.wait(0.3)

        # Left box — Slide 1
        lbox = RoundedRectangle(
            corner_radius=0.15, width=5.5, height=2.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.0, -0.2, 0])
        lbl1 = mute_t("Slide 1", size=30)
        lbl1.move_to([-3.0, 0.8, 0])
        h1_l1 = ink_t("source-linked", size=30)
        h1_l2 = ink_t("decision brief", size=30)
        h1_l3 = ink_t("for AI founders", size=30)
        h1_l1.move_to([-3.0, 0.2, 0])
        h1_l2.move_to([-3.0, -0.3, 0])
        h1_l3.move_to([-3.0, -0.8, 0])

        # Right box — Slide 7 (TERRA, the stronger line)
        rbox = RoundedRectangle(
            corner_radius=0.15, width=5.5, height=2.8,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.0, -0.2, 0])
        lbl2 = mute_t("Slide 7", size=30)
        lbl2.move_to([3.0, 0.8, 0])
        h2_l1 = ink_t("Monitors send alerts.", size=30)
        h2_l2 = ink_t("SignalBrief recommends", size=30)
        h2_l3 = ink_t("action.", size=30)
        h2_l1.move_to([3.0, 0.18, 0])
        h2_l2.move_to([3.0, -0.32, 0])
        h2_l3.move_to([3.0, -0.82, 0])

        self.play(FadeIn(lbox), Write(lbl1), Write(h1_l1), Write(h1_l2), Write(h1_l3),
                  run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(rbox), Write(lbl2), Write(h2_l1), Write(h2_l2), Write(h2_l3),
                  run_time=0.8)
        self.wait(0.5)

        # Question
        q1 = ink_t("Slide seven's line already exists in the deck.", size=30)
        q2 = ink_t("What would happen if it moved to slide one?", size=30)
        q1.move_to([0, -2.5, 0])
        q2.move_to([0, -2.95, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)


# ── B07 — Lens 5: The Close ───────────────────────────────────────────────────
class B07_TheClose(Scene):
    """~20s  Clean single ask. Roadmap. Does 'design partner' land with the audience?"""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 5 of 5", size=30)
        lens_lbl.to_corner(UL, buff=1.0)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("The Close", size=46)
        header.to_edge(UP, buff=0.7)
        rule = terra_rule(4)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Admirable: one clean ask
        epi = mute_t("One ask. Not three.", size=30)
        epi.move_to([0, 1.8, 0])
        self.play(FadeIn(epi), run_time=0.4)
        self.wait(0.2)

        # The ask box (TERRA border — primary)
        ask_box = RoundedRectangle(
            corner_radius=0.15, width=9.0, height=1.8,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=3
        ).move_to([0, 0.6, 0])
        ask_l1 = ink_t("Five Design Partners", size=36)
        ask_l2 = mute_t("+ access to founder communities", size=30)
        ask_l1.move_to([0, 0.85, 0])
        ask_l2.move_to([0, 0.35, 0])
        self.play(Create(ask_box), Write(ask_l1), FadeIn(ask_l2), run_time=0.8)
        self.wait(0.3)

        # 60-day roadmap strip — dots + labels only (no body descriptions)
        milestones = ["Now", "30 days", "60 days"]
        road_xs = [-4.2, 0, 4.2]
        road_line = Line([-4.2, -0.8, 0], [4.2, -0.8, 0], color=INK, stroke_width=1.5)
        self.play(Create(road_line), run_time=0.4)
        for m_lbl, mx in zip(milestones, road_xs):
            dot = Circle(radius=0.18, color=TERRA, fill_color=TERRA, fill_opacity=1)
            dot.move_to([mx, -0.8, 0])
            m_t = ink_t(m_lbl, size=30)
            m_t.move_to([mx, -1.35, 0])
            self.play(FadeIn(dot), Write(m_t), run_time=0.35)

        self.wait(0.3)

        # Question
        q1 = ink_t("Does 'design partner' mean the same thing", size=30)
        q2 = ink_t("to your audience as it does to you?", size=30)
        q1.move_to([0, -2.3, 0])
        q2.move_to([0, -2.78, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)
