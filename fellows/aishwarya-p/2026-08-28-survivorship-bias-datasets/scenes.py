"""
Manim scenes for survivorship-bias-datasets
B01_SurvivorsOnly    — companies fading out, leaving only survivors visible
B02_PointInTimeList  — today's list vs. point-in-time list, side by side
B03_CitedStudies     — the three real cited studies and their found ranges
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


class B01_SurvivorsOnly(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Today's Dataset, Built Backward", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        companies = ["Company A", "Company B", "Company C", "Company D", "Company E", "Company F"]
        positions = [
            [-3.0, 1.0, 0], [0.0, 1.0, 0], [3.0, 1.0, 0],
            [-3.0, -0.4, 0], [0.0, -0.4, 0], [3.0, -0.4, 0],
        ]
        cards = VGroup()
        for name, pos in zip(companies, positions):
            card = RoundedRectangle(
                corner_radius=0.1, width=2.1, height=1.0,
                fill_color=PALETTE["sage"], fill_opacity=0.15,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            ).move_to(pos)
            label = Text(name, color=PALETTE["ink"], font_size=14, font=BODY_FONT).move_to(card.get_center())
            group = VGroup(card, label)
            cards.add(group)

        self.play(*[Create(c[0]) for c in cards], *[Write(c[1]) for c in cards], run_time=1.4)
        self.wait(1.0)

        # mark two as failed, then fade them out
        failed = [cards[1], cards[4]]
        for f in failed:
            x = Text("X", color=PALETTE["crimson"], font_size=30, font=BODY_FONT).move_to(f.get_center())
            self.play(Write(x), run_time=0.6)
            self.wait(0.3)
            self.play(FadeOut(f), FadeOut(x), run_time=0.8)
            self.wait(0.3)

        remaining = VGroup(*[c for c in cards if c not in failed])
        self.play(Indicate(remaining, scale_factor=1.03), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "delisted or bankrupt companies quietly disappear",
            color=PALETTE["crimson"], font_size=17, font=BODY_FONT
        ).shift(DOWN * 2.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(2.0)


class B02_PointInTimeList(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Today's List vs. Point-in-Time List", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        left_box = RoundedRectangle(
            corner_radius=0.12, width=5.0, height=3.6,
            fill_color=PALETTE["crimson"], fill_opacity=0.06,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).shift(LEFT * 3.2)
        left_title = Text("Today's List", color=PALETTE["crimson"], font_size=18, font=BODY_FONT).move_to(
            left_box.get_top() + DOWN * 0.4
        )
        left_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            for t in ["Company A", "Company C", "Company D", "Company F"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(left_box.get_center() + DOWN * 0.1)

        right_box = RoundedRectangle(
            corner_radius=0.12, width=5.0, height=3.6,
            fill_color=PALETTE["teal"], fill_opacity=0.06,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).shift(RIGHT * 3.2)
        right_title = Text("Point-in-Time List", color=PALETTE["teal"], font_size=18, font=BODY_FONT).move_to(
            right_box.get_top() + DOWN * 0.4
        )
        right_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            for t in ["Company A", "Company B (delisted)", "Company C", "Company D",
                      "Company E (bankrupt)", "Company F"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(right_box.get_center() + DOWN * 0.1)

        self.play(Create(left_box), Write(left_title), run_time=0.8)
        self.play(Write(left_items), run_time=1.2)
        self.wait(0.8)
        self.play(Create(right_box), Write(right_title), run_time=0.8)
        self.play(Write(right_items), run_time=1.4)
        self.wait(0.8)

        self.play(Indicate(right_box, scale_factor=1.02), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "built forward from history, not backward from survivors",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).shift(DOWN * 3.1)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_CitedStudies(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "The Range Across Real Studies", color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        studies = [
            ("Grinblatt & Titman (1989)", "0.1-0.4 pts/yr", "mutual funds"),
            ("Kothari, Shanken & Sloan (1995)", "9-10 points", "equity data"),
            ("Amin & Kat (2001)", "~2 pts/yr", "hedge fund peer indices"),
        ]

        rows = VGroup()
        for name, effect, domain in studies:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=9.5, height=1.1,
                fill_color=PALETTE["slate"], fill_opacity=0.06,
                stroke_color=PALETTE["slate"], stroke_width=1.3
            )
            name_label = Text(name, color=PALETTE["slate"], font_size=15, font=BODY_FONT)
            effect_label = Text(effect, color=PALETTE["crimson"], font_size=15, font=BODY_FONT)
            domain_label = Text(domain, color=PALETTE["ink"], font_size=13, font=BODY_FONT)
            text_group = VGroup(name_label, effect_label, domain_label).arrange(
                RIGHT, buff=0.5
            ).move_to(row_box.get_center())
            rows.add(VGroup(row_box, text_group))

        rows.arrange(DOWN, buff=0.35).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=1.1)
            self.wait(0.5)

        self.wait(0.5)
        bottom = Text(
            "the size varies — the direction never does",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).shift(DOWN * 3.1)
        self.play(Write(bottom), run_time=1.2)
        self.wait(2.0)
