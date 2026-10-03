"""
Manim scenes for patent-agent-video2-splitting-claims
B01_HowItSplits    — the regex logic, numbered claims -> classified claims
B02_FirstRealTest  — the real 20/20 result on US-11791319-B2
B03_StressTest     — three more real patents, 44 more claims
B04_TheHonestCatch — the false-positive flag, traced by hand
"""
from manim import *

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

BODY_FONT = "Menlo"


class B01_HowItSplits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "How the Split Works", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        raw_box = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.4,
            fill_color=PALETTE["slate"], fill_opacity=0.06,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.6, 0])
        raw_text = Text(
            '"1. A semiconductor system... 2. The system of claim 1..."',
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).move_to(raw_box.get_center())

        self.play(Create(raw_box), Write(raw_text), run_time=1.2)
        self.wait(0.8)

        arrow = Arrow([0, 0.8, 0], [0, 0.2, 0], color=PALETTE["ink"], stroke_width=3)
        self.play(Create(arrow), run_time=0.6)

        card1 = RoundedRectangle(
            corner_radius=0.1, width=3.9, height=1.3,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([-2.2, -1.2, 0])
        card1_text = Text(
            "Claim 1\nno 'claim N' found\n→ INDEPENDENT",
            color=PALETTE["teal"], font_size=14, font=BODY_FONT, line_spacing=1.2
        ).move_to(card1.get_center())

        card2 = RoundedRectangle(
            corner_radius=0.1, width=3.9, height=1.3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([2.2, -1.2, 0])
        card2_text = Text(
            "Claim 2\n'claim 1' found\n→ DEPENDENT on 1",
            color=PALETTE["crimson"], font_size=14, font=BODY_FONT, line_spacing=1.2
        ).move_to(card2.get_center())

        self.play(Create(card1), Write(card1_text), run_time=1.0)
        self.wait(0.4)
        self.play(Create(card2), Write(card2_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "split on numbering, classify by reference",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.5)


class B02_FirstRealTest(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "The First Real Test", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        patent_label = Text(
            "US-11791319-B2", color=PALETTE["slate"], font_size=20, font=BODY_FONT
        ).move_to([0, 1.8, 0])
        self.play(Write(patent_label), run_time=0.8)
        self.wait(0.5)

        stat1 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([-3.0, 0.2, 0])
        stat1_text = Text("20\nclaims", color=PALETTE["ink"], font_size=20, font=BODY_FONT, line_spacing=1.2).move_to(stat1.get_center())

        stat2 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.4,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.2, 0])
        stat2_text = Text("3\nindependent", color=PALETTE["teal"], font_size=18, font=BODY_FONT, line_spacing=1.2).move_to(stat2.get_center())

        stat3 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.4,
            fill_color=PALETTE["crimson"], fill_opacity=0.1,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([3.0, 0.2, 0])
        stat3_text = Text("17\ndependent", color=PALETTE["crimson"], font_size=18, font=BODY_FONT, line_spacing=1.2).move_to(stat3.get_center())

        self.play(Create(stat1), Write(stat1_text), run_time=0.8)
        self.play(Create(stat2), Write(stat2_text), run_time=0.8)
        self.play(Create(stat3), Write(stat3_text), run_time=0.8)
        self.wait(0.8)

        self.play(Indicate(VGroup(stat1, stat2, stat3), scale_factor=1.03), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "20 out of 20, verified by hand against the raw text",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_StressTest(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Stress-Testing Against More Patents", color=PALETTE["ink"], font_size=20, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        patents = [
            ("US-10822628-B2", "7 claims"),
            ("US-11197952-B2", "17 claims"),
            ("US-10265458-B2", "20 claims"),
        ]

        rows = VGroup()
        for name, count in patents:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=7.5, height=1.0,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            name_label = Text(name, color=PALETTE["ink"], font_size=16, font=BODY_FONT)
            count_label = Text(count, color=PALETTE["teal"], font_size=16, font=BODY_FONT)
            text_group = VGroup(name_label, count_label).arrange(RIGHT, buff=1.0).move_to(row_box.get_center())
            rows.add(VGroup(row_box, text_group))

        rows.arrange(DOWN, buff=0.3).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=1.0)
            self.wait(0.4)

        self.wait(0.5)
        bottom = Text(
            "44 more claims — every one held up",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_TheHonestCatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "The Honest Catch", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        flag = Text(
            "Claim 5 flagged: POSSIBLE MULTI-DEPENDENCY",
            color=PALETTE["gold"], font_size=17, font=BODY_FONT
        ).move_to([0, 1.6, 0])
        self.play(Write(flag), run_time=1.0)
        self.wait(1.0)

        real_box = RoundedRectangle(
            corner_radius=0.12, width=8.5, height=1.6,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        real_text = Text(
            '"The port of claim 3, wherein... bumps or projections..."',
            color=PALETTE["teal"], font_size=15, font=BODY_FONT
        ).move_to(real_box.get_center())

        self.play(Create(real_box), Write(real_text), run_time=1.2)
        self.wait(1.0)

        self.play(real_box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)
        self.play(Indicate(real_box, scale_factor=1.02), run_time=1.0)
        self.wait(0.5)

        verdict = Text(
            "the 'or' was about projections, not the dependency",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).move_to([0, -1.6, 0])
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the parsing was right — the flag was too eager",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
