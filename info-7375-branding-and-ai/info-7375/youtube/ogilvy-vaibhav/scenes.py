import os, sys
from manim import *

REEL_DIR = os.path.dirname(os.path.abspath(__file__))

CREAM = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"
MUTE  = "#8A8070"

def ink_t(text, size=36, **kw):
    return Text(text, color=INK,  font="EB Garamond", font_size=size, **kw)
def terra_t(text, size=36, **kw):
    return Text(text, color=TERRA, font="EB Garamond", font_size=size, **kw)
def mute_t(text, size=36, **kw):
    return Text(text, color=MUTE,  font="EB Garamond", font_size=size, **kw)
def terra_rule(width=8.0):
    return Line(LEFT * width/2, RIGHT * width/2, color=TERRA, stroke_width=2)

def show_slide(scene, img_path, label_text, hold=3.0):
    slide = ImageMobject(img_path)
    slide.set_height(6.4)
    if slide.width > 13.0:
        slide.set_width(13.0)
    slide.move_to([0, 0.35, 0])
    border = Rectangle(
        width=slide.width + 0.12, height=slide.height + 0.12,
        color=TERRA, stroke_width=4, fill_opacity=0
    )
    border.move_to(slide)
    label = mute_t(label_text, size=24)
    label.to_edge(DOWN, buff=0.55)
    scene.play(FadeIn(slide), Create(border), run_time=0.5)
    scene.play(FadeIn(label), run_time=0.3)
    scene.wait(hold)
    scene.play(FadeOut(slide), FadeOut(border), FadeOut(label), run_time=0.5)


# ── B01 — The Tagline ────────────────────────────────────────────────────────
class B01_TheTagline(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "vaibhav_slide_01.png")
        show_slide(self, img, "Slide 1 — Olembic · Distill the signal. Silence the noise.", hold=0.5)

        lens_lbl = ink_t("Lens — The Tagline", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("OLEMBIC", size=58)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        tag = ink_t(
            "Distill the signal.\nSilence the noise.",
            size=40
        )
        tag.move_to([0, 0.7, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.5, 0])
        self.play(Create(q_box), run_time=0.3)

        q = ink_t("Which of these two lines would stop a reader?", size=36)
        q.move_to([0, -1.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B02 — The Person Priced Out ──────────────────────────────────────────────
class B02_PersonPricedOut(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "vaibhav_slide_02.png")
        show_slide(self, img, "Slide 2 — You know they're talking about you. You don't know what they're saying.")

        lens_lbl = mute_t("Lens — The Person Priced Out", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        hook_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.5, 0])
        self.play(Create(hook_box), run_time=0.3)

        hook = mute_t(
            '"You know they\'re talking about you.\nYou don\'t know what they\'re saying."',
            size=26
        )
        hook.move_to([0, 1.5, 0])
        self.play(FadeIn(hook), run_time=0.4)
        self.wait(0.2)

        stat = ink_t("$8B market", size=48)
        stat.move_to([-2.5, 0.1, 0])
        stat_lbl = mute_t("and it's failing the\npeople who need it most", size=24)
        stat_lbl.move_to([2.2, 0.1, 0])
        price = terra_t("$15,000 / yr", size=36)
        price.move_to([0, -0.85, 0])
        price_lbl = mute_t("— the entry price that prices small brands out", size=24)
        price_lbl.move_to([0, -1.4, 0])
        self.play(FadeIn(stat), FadeIn(stat_lbl), run_time=0.4)
        self.play(FadeIn(price), run_time=0.3)
        self.play(FadeIn(price_lbl), run_time=0.3)
        self.wait(0.3)

        q_box = Rectangle(
            width=12.2, height=0.9,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -2.2, 0])
        self.play(Create(q_box), run_time=0.3)
        q = mute_t("Who is that person? Name them.", size=26)
        q.move_to([0, -2.2, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)


# ── B03 — The Buried Lead ────────────────────────────────────────────────────
class B03_WorkingToday(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "vaibhav_slide_09.png")
        show_slide(self, img, "Slide 9 — Working today · Live demo on HuggingFace")

        lens_lbl = mute_t("Lens — The Buried Lead", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE BURIED LEAD", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=1.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.6, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = mute_t('"Working today."', size=40)
        line1.move_to([0, 1.0, 0])
        line2 = mute_t("Live demo on HuggingFace. 312 mentions tracked.", size=26)
        line2.move_to([0, 0.3, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.wait(0.3)

        place_note = mute_t("This fact is on Slide 9. Ogilvy would open with it.", size=28)
        place_note.move_to([0, -0.9, 0])
        self.play(FadeIn(place_note), run_time=0.4)
        self.wait(0.5)


# ── B04 — Not a Dashboard. A Narrative. ─────────────────────────────────────
class B04_NotADashboard(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "vaibhav_slide_03.png")
        show_slide(self, img, "Slide 3 — Not a dashboard. A narrative.")

        lens_lbl = mute_t("Lens — Not a Dashboard. A Narrative.", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE HIDDEN HEADLINE", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(7.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=1.6,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.5, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = mute_t("Not a dashboard.", size=40)
        line1.move_to([0, 0.95, 0])
        line2 = terra_t("A narrative.", size=40)
        line2.move_to([0, 0.2, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.wait(0.3)

        note = mute_t("Four words. The whole pitch. At the bottom of Slide 3.", size=26)
        note.move_to([0, -1.0, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B05 — The Open-Source Free Tier ─────────────────────────────────────────
class B05_OpenSourceFree(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — The Open-Source Free Tier Is the Ask", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.add(lens_lbl)

        header = ink_t("THE STRONGEST ASK IS UNSTATED", size=36)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(8.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)
        self.wait(0.2)

        info_box = Rectangle(
            width=12.2, height=2.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.5, 0])
        self.play(Create(info_box), run_time=0.3)

        tier_label = terra_t("FREE TIER: $0 / forever", size=38)
        tier_label.move_to([0, 1.05, 0])
        tier_desc = mute_t("Self-hosted · full pipeline · community support", size=28)
        tier_desc.move_to([0, 0.3, 0])
        self.play(FadeIn(tier_label), run_time=0.4)
        self.play(FadeIn(tier_desc), run_time=0.3)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.55, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t(
            "Every self-hosted install is a warm lead.\nWhy not end with 'go fork it today'?",
            size=26
        )
        q.move_to([0, -1.35, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "vaibhav_slide_10.png")
        show_slide(self, img, "Slide 10 — Fund the first briefing · $250K seed · 3 design partners · 10 intros")

        lens_lbl = mute_t("Lens — The Close", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        goal = ink_t("Fund the first briefing.", size=36)
        goal.move_to([0, 1.6, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("$250K SEED", "18 months runway.\nHire one engineer.\nShip paid tier.", True),
            ("3 DESIGN PARTNERS", "Marketing agencies\nserving SMBs.\n6-month pilot.", False),
        ]
        xs = [-3.0, 3.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=5.2, height=2.8,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.1, 0])
            t = terra_t(title_str, size=22) if highlight else mute_t(title_str, size=22)
            t.move_to([x, 0.9, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -0.25, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -1.85, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t("Investor close and developer close — same room?", size=26)
        q.move_to([0, -2.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
