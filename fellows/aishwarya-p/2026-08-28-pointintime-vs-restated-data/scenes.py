"""
Manim scenes for pointintime-vs-restated-data
B01_RestatedNumber      — a number changing from original to restated
B02_PointInTimeRecord   — how point-in-time data preserves both entries
B03_CompustatExample    — the real Compustat Point-In-Time database
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


class B01_RestatedNumber(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "The Number Changes After the Fact", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        label = Text("Q1 Earnings", color=PALETTE["ink"], font_size=18, font=BODY_FONT).move_to([0, 1.6, 0])
        self.play(Write(label), run_time=0.8)

        original = Text("$310 million", color=PALETTE["teal"], font_size=36, font=BODY_FONT).move_to([0, 0.6, 0])
        original_tag = Text("as reported at the time", color=PALETTE["teal"], font_size=14, font=BODY_FONT).move_to([0, 0.0, 0])
        self.play(Write(original), Write(original_tag), run_time=1.2)
        self.wait(1.0)

        arrow = Arrow([0, -0.4, 0], [0, -1.0, 0], color=PALETTE["ink"], stroke_width=3)
        self.play(Create(arrow), run_time=0.6)

        restated = Text("$340 million", color=PALETTE["crimson"], font_size=36, font=BODY_FONT).move_to([0, -1.8, 0])
        restated_tag = Text("as reported today", color=PALETTE["crimson"], font_size=14, font=BODY_FONT).move_to([0, -2.4, 0])
        self.play(Write(restated), Write(restated_tag), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the model trained on today's number wasn't there on the actual date",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_PointInTimeRecord(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "What Point-in-Time Data Preserves", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        row1_box = RoundedRectangle(
            corner_radius=0.1, width=9.0, height=1.2,
            fill_color=PALETTE["teal"], fill_opacity=0.06,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        row1_text = Text(
            "Q1 Report Date: $310 million (recorded as-of that date)",
            color=PALETTE["teal"], font_size=16, font=BODY_FONT
        ).move_to(row1_box.get_center())

        row2_box = RoundedRectangle(
            corner_radius=0.1, width=9.0, height=1.2,
            fill_color=PALETTE["crimson"], fill_opacity=0.06,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.6, 0])
        row2_text = Text(
            "Later Restatement: $340 million (a separate, dated entry)",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).move_to(row2_box.get_center())

        self.play(Create(row1_box), Write(row1_text), run_time=1.2)
        self.wait(0.8)
        self.play(Create(row2_box), Write(row2_text), run_time=1.2)
        self.wait(0.8)

        self.play(Indicate(row1_box, scale_factor=1.02), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "both entries exist — neither one overwrites the other",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_CompustatExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "A Real Product Built for This", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.12, width=8.0, height=3.4,
            fill_color=PALETTE["slate"], fill_opacity=0.06,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        name = Text("Compustat Point-In-Time Database", color=PALETTE["slate"], font_size=20, font=BODY_FONT).move_to(
            box.get_top() + DOWN * 0.6
        )
        items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            for t in [
                "Tracks original figures and later restatements separately",
                "Reconstructs what was known at any past month-end",
                "Built to avoid survivorship and look-ahead bias",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(box.get_center() + DOWN * 0.3)

        self.play(Create(box), Write(name), run_time=1.0)
        self.wait(0.5)
        self.play(Write(items), run_time=1.8)
        self.wait(1.0)

        self.play(Indicate(box, scale_factor=1.02), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "a dedicated product exists because the problem is routine",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
