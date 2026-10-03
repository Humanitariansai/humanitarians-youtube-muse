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


# ── B01 — The Smoke Detector ─────────────────────────────────────────────────
class B01_TheSmokeMeter(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.wait(1.5)

        img = os.path.join(REEL_DIR, "pantry", "kanishk_slide_01.png")
        show_slide(self, img, "Slide 1 — Accessibility Monitor", hold=0.5)

        lens_lbl = ink_t("Lens — The Smoke Detector", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("ACCESSIBILITY MONITOR", size=46)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        tag_plate = Rectangle(
            width=13.0, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=1
        ).move_to([0, 0.7, 0])
        self.play(FadeIn(tag_plate), run_time=0.2)
        tag = ink_t(
            "The smoke detector\nfor your website's accessibility.",
            size=38
        )
        tag.move_to([0, 0.7, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.5, 0])
        self.play(Create(q_box), run_time=0.3)

        q = ink_t("What burns down when the smoke alarm fails?", size=36)
        q.move_to([0, -1.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B02 — The Person Behind the Number ──────────────────────────────────────
class B02_PersonBehindNumber(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "kanishk_slide_02.png")
        show_slide(self, img, "Slide 2 — Small teams pass an audit once — then silently break it on the next deploy")

        lens_lbl = mute_t("Lens — The Person Behind the Number", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        stat1 = ink_t("96%", size=64)
        stat1.move_to([-3.8, 0.9, 0])
        lbl1 = mute_t("fail WCAG", size=24)
        lbl1.move_to([-3.8, 0.2, 0])

        stat2 = ink_t("4,000+", size=54)
        stat2.move_to([0.0, 0.9, 0])
        lbl2 = mute_t("ADA lawsuits/year", size=24)
        lbl2.move_to([0.0, 0.2, 0])

        stat3 = ink_t("1 in 4", size=54)
        stat3.move_to([3.8, 0.9, 0])
        lbl3 = mute_t("adults has disability", size=24)
        lbl3.move_to([3.8, 0.2, 0])

        self.play(FadeIn(stat1), FadeIn(lbl1), run_time=0.3)
        self.play(FadeIn(stat2), FadeIn(lbl2), run_time=0.3)
        self.play(FadeIn(stat3), FadeIn(lbl3), run_time=0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.35, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.35, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t(
            "Who is the blind user who finds broken alt-text\n3 days after the deploy?",
            size=26
        )
        q.move_to([0, -1.35, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B03 — The Buried Lead ────────────────────────────────────────────────────
class B03_LivePipeline(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "kanishk_slide_09.png")
        show_slide(self, img, "Slide 9 — A working, accountable pipeline — not a slide-ware idea")

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

        line1 = mute_t('"A working, accountable pipeline', size=32)
        line1.move_to([0, 0.85, 0])
        line2 = mute_t('— not a slide-ware idea."', size=32)
        line2.move_to([0, 0.2, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.wait(0.3)

        place_note = mute_t("This line is on Slide 9. The pipeline runs today.", size=28)
        place_note.move_to([0, -0.95, 0])
        self.play(FadeIn(place_note), run_time=0.4)
        self.wait(0.5)


# ── B04 — The Headline ───────────────────────────────────────────────────────
class B04_TheHeadline(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "kanishk_slide_07.png")
        show_slide(self, img, "Slide 7 — Everyone audits a moment in time. No one guards the diff for small teams.")

        lens_lbl = mute_t("Lens — The Headline on Slide 7", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE HEADLINE", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=2.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.55, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = mute_t("Everyone audits a moment in time.", size=30)
        line1.move_to([0, 1.0, 0])
        line2 = terra_t("No one guards the diff for small teams.", size=30)
        line2.move_to([0, 0.25, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.wait(0.3)

        note = mute_t("Nine words. The whole pitch. Why is it on Slide 7?", size=26)
        note.move_to([0, -1.05, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B05 — Free Is the Most Powerful Word ────────────────────────────────────
class B05_FreeIsTheMostPowerfulWord(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — Free Is the Most Powerful Word", size=28)
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

        tier_label = terra_t("FREE TIER: $0", size=40)
        tier_label.move_to([0, 1.05, 0])
        tier_desc = mute_t("First accessibility scan · no setup required", size=28)
        tier_desc.move_to([0, 0.3, 0])
        self.play(FadeIn(tier_label), run_time=0.4)
        self.play(FadeIn(tier_desc), run_time=0.3)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.55, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t(
            "The product is live. The free tier exists.\nWhy not end with 'run your first diff today'?",
            size=26
        )
        q.move_to([0, -1.35, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "kanishk_slide_10.png")
        show_slide(self, img, "Slide 10 — Design partners · Technical help · Seed support")

        lens_lbl = mute_t("Lens — The Close", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=2.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.3, 0])
        self.play(Create(q_box), run_time=0.3)

        close_line1 = mute_t('"Accessibility burns down in the dark —', size=27)
        close_line1.move_to([0, 1.75, 0])
        close_line2 = mute_t('no one smells the smoke until someone is harmed."', size=27)
        close_line2.move_to([0, 1.1, 0])
        self.play(FadeIn(close_line1), run_time=0.4)
        self.play(FadeIn(close_line2), run_time=0.3)
        self.wait(0.3)

        asks = [
            ("DESIGN PARTNERS", "3–5 agencies to validate\nthe diff workflow\nin real deploys.", True),
            ("TECHNICAL HELP", "Pipeline + infrastructure\nto scale from prototype\nto MVP.", False),
        ]
        xs = [-3.0, 3.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=5.2, height=2.8,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.9, 0])
            t = terra_t(title_str, size=22) if highlight else mute_t(title_str, size=22)
            t.move_to([x, -0.05, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -1.1, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.5)
