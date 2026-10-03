"""
Manim scenes for correlation-vs-causation-signals
B01_CorrelationAlone   — two lines moving together, question mark over the gap
B02_MechanismRequired  — correlation alone vs. correlation + mechanism
B03_SpuriousExample    — the real Vigen example, two unrelated lines correlating
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


class B01_CorrelationAlone(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Two Lines Moving Together", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        # two roughly-parallel wavy lines, drawn as simple polylines
        line_a_pts = [[-4.5, -0.5, 0], [-3.0, 0.3, 0], [-1.5, -0.2, 0], [0.0, 0.6, 0], [1.5, 0.1, 0], [3.0, 0.8, 0], [4.5, 0.4, 0]]
        line_b_pts = [[-4.5, -1.3, 0], [-3.0, -0.5, 0], [-1.5, -1.0, 0], [0.0, -0.2, 0], [1.5, -0.7, 0], [3.0, 0.0, 0], [4.5, -0.4, 0]]

        line_a = VMobject(color=PALETTE["teal"], stroke_width=4).set_points_as_corners(line_a_pts)
        line_b = VMobject(color=PALETTE["crimson"], stroke_width=4).set_points_as_corners(line_b_pts)

        label_a = Text("Variable A", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to([4.5, 0.9, 0])
        label_b = Text("Variable B", color=PALETTE["crimson"], font_size=16, font=BODY_FONT).move_to([4.5, -0.9, 0])

        self.play(Create(line_a), Write(label_a), run_time=1.4)
        self.wait(0.3)
        self.play(Create(line_b), Write(label_b), run_time=1.4)
        self.wait(0.8)

        question = Text(
            "why?", color=PALETTE["gold"], font_size=28, font=BODY_FONT
        ).move_to([0, -2.4, 0])
        self.play(Write(question), run_time=0.8)
        self.play(Indicate(question, scale_factor=1.2), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "moving together is not the same as one causing the other",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_MechanismRequired(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Correlation Alone vs. Correlation + Mechanism", color=PALETTE["ink"], font_size=20, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        left_box = RoundedRectangle(
            corner_radius=0.12, width=5.0, height=3.6,
            fill_color=PALETTE["crimson"], fill_opacity=0.06,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([-3.2, -0.2, 0])
        left_title = Text("Correlation Alone", color=PALETTE["crimson"], font_size=17, font=BODY_FONT).move_to(
            [-3.2, 1.4, 0]
        )
        left_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            for t in ["A and B move together", "No known mechanism", "No ruled-out third factor"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([-3.2, -0.3, 0])

        right_box = RoundedRectangle(
            corner_radius=0.12, width=5.0, height=3.6,
            fill_color=PALETTE["teal"], fill_opacity=0.06,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([3.2, -0.2, 0])
        right_title = Text("Correlation + Mechanism", color=PALETTE["teal"], font_size=17, font=BODY_FONT).move_to(
            [3.2, 1.4, 0]
        )
        right_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            for t in ["A and B move together", "A real reason A moves B", "Third factors checked and ruled out"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([3.2, -0.3, 0])

        self.play(Create(left_box), Write(left_title), run_time=0.8)
        self.play(Write(left_items), run_time=1.2)
        self.wait(0.8)
        self.play(Create(right_box), Write(right_title), run_time=0.8)
        self.play(Write(right_items), run_time=1.2)
        self.wait(0.8)

        self.play(Indicate(right_box, scale_factor=1.02), run_time=1.0)
        self.wait(1.5)


class B03_SpuriousExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "A Real, Documented Example", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        line_a_pts = [[-4.5, -0.3, 0], [-3.0, 0.5, 0], [-1.5, 0.0, 0], [0.0, 0.8, 0], [1.5, 0.3, 0], [3.0, 1.0, 0], [4.5, 0.5, 0]]
        line_b_pts = [[-4.5, -1.0, 0], [-3.0, -0.2, 0], [-1.5, -0.7, 0], [0.0, 0.1, 0], [1.5, -0.4, 0], [3.0, 0.3, 0], [4.5, -0.2, 0]]

        line_a = VMobject(color=PALETTE["slate"], stroke_width=4).set_points_as_corners(line_a_pts)
        line_b = VMobject(color=PALETTE["gold"], stroke_width=4).set_points_as_corners(line_b_pts)

        label_a = Text("Nicolas Cage films per year", color=PALETTE["slate"], font_size=14, font=BODY_FONT).move_to([0, 1.7, 0])
        label_b = Text("Swimming pool drownings per year", color=PALETTE["gold"], font_size=14, font=BODY_FONT).move_to([0, -1.6, 0])

        self.play(Create(line_a), Write(label_a), run_time=1.4)
        self.wait(0.3)
        self.play(Create(line_b), Write(label_b), run_time=1.4)
        self.wait(0.8)

        source = Text(
            "Tyler Vigen, Spurious Correlations (~1999-2009)",
            color=PALETTE["ink"], font_size=13, font=BODY_FONT
        ).to_edge(DOWN, buff=1.0)
        self.play(Write(source), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "real correlation — no plausible causal link",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
