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
    label = mute_t(label_text, size=26)
    label.to_edge(DOWN, buff=0.55)
    scene.play(FadeIn(slide), Create(border), run_time=0.5)
    scene.play(FadeIn(label), run_time=0.3)
    scene.wait(hold)
    scene.play(FadeOut(slide), FadeOut(border), FadeOut(label), run_time=0.5)


# ── B01 — The Tagline ────────────────────────────────────────────────────────
class B01_TheTagline(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "xinchen_slide_01.png")
        show_slide(self, img, "Slide 1 — Marketing Intelligence Brief · Turning Marketing Information Into Client-Ready Insights")

        lens_lbl = mute_t("Lens — The Tagline", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("MARKETING INTELLIGENCE", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(9.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        tag = mute_t(
            "Turning Marketing Information\nInto Client-Ready Insights.",
            size=34
        )
        tag.move_to([0, 0.75, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(0.3)

        q_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.3, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("Slide 7 has the real headline. Why is it on Slide 7?", size=26)
        q.move_to([0, -1.3, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B02 — The Consultant in the Room ────────────────────────────────────────
class B02_ConsultantInRoom(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "xinchen_slide_02.png")
        show_slide(self, img, "Slide 2 — 135 articles from 5 sources — more than any consultant can review manually")

        lens_lbl = mute_t("Lens — The Consultant in the Room", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        stat = ink_t("135", size=80)
        stat.move_to([-2.5, 0.8, 0])
        stat_lbl = mute_t("marketing articles\nfrom 5 sources\nin one workflow run", size=24)
        stat_lbl.move_to([2.5, 0.8, 0])
        self.play(FadeIn(stat), FadeIn(stat_lbl), run_time=0.4)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.2, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.2, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t(
            "Who is the consultant who walked into the client meeting\nwith the wrong information?",
            size=24
        )
        q.move_to([0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B03 — The Working Prototype ──────────────────────────────────────────────
class B03_WorkingPrototype(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "xinchen_slide_09.png")
        show_slide(self, img, "Slide 9 — Functional Working Prototype · Validated with 3 technology consultants")

        lens_lbl = mute_t("Lens — The Buried Lead", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE BURIED LEAD", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=2.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.5, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = mute_t('"Functional Working Prototype."', size=36)
        line1.move_to([0, 1.0, 0])
        line2 = mute_t("Tested with 3 consultants. Strong SaaS potential.", size=26)
        line2.move_to([0, 0.2, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.wait(0.3)

        place_note = mute_t("This is the most powerful fact in the pitch. It is on Slide 9.", size=26)
        place_note.move_to([0, -0.9, 0])
        self.play(FadeIn(place_note), run_time=0.4)
        self.wait(0.5)


# ── B04 — Competitors Find. We Prepare. ─────────────────────────────────────
class B04_CompetitorsFindWePrepare(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "xinchen_slide_07.png")
        show_slide(self, img, "Slide 7 — Competitors Find Information. We Prepare It for Client Conversations.")

        lens_lbl = mute_t("Lens — The Hidden Headline", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE HEADLINE", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=2.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.6, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = mute_t("Competitors find information.", size=34)
        line1.move_to([0, 1.2, 0])
        line2 = terra_t("We prepare it for client conversations.", size=34)
        line2.move_to([0, 0.4, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.wait(0.3)

        note = mute_t("Nine words. The whole pitch. On Slide 7.", size=26)
        note.move_to([0, -1.05, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B05 — Honest Signals ─────────────────────────────────────────────────────
class B05_HonestSignals(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — Honest Signals", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.add(lens_lbl)

        header = ink_t("THE HONEST SIGNAL", size=42)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(7.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)
        self.wait(0.2)

        info_box = Rectangle(
            width=12.2, height=2.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.6, 0])
        self.play(Create(info_box), run_time=0.3)

        label = mute_t('"PROPOSED — NOT CURRENT REVENUE"', size=30)
        label.move_to([0, 1.1, 0])
        sublabel = mute_t('"These figures are illustrative only."', size=26)
        sublabel.move_to([0, 0.4, 0])
        self.play(FadeIn(label), run_time=0.4)
        self.play(FadeIn(sublabel), run_time=0.3)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.45, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.25, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("Ogilvy approved honesty. Does this read as integrity\nor as hedging the ask?", size=24)
        q.move_to([0, -1.25, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "xinchen_slide_10.png")
        show_slide(self, img, "Slide 10 — Help us turn a working prototype into a stronger consulting product")

        lens_lbl = mute_t("Lens — The Close", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        goal = mute_t('"Help us turn a working prototype into a stronger consulting product."', size=26)
        goal.move_to([0, 1.55, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("PILOT PARTICIPANTS", "Technology consultants\nwilling to test the product\nwith real topics.", True),
            ("PRODUCT GUIDANCE", "Feedback on recommendations,\nworkflow clarity, and\nconsulting usefulness.", False),
        ]
        xs = [-3.0, 3.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=5.2, height=3.0,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.2, 0])
            t = terra_t(title_str, size=21) if highlight else mute_t(title_str, size=21)
            t.move_to([x, 0.85, 0])
            b = mute_t(body_str, size=19)
            b.move_to([x, -0.4, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -1.95, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t("Does the audience know they're the pilot participant?", size=25)
        q.move_to([0, -2.55, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
