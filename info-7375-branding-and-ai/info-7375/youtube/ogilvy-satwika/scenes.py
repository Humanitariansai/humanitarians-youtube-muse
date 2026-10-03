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


# ── B01 — The Headline ───────────────────────────────────────────────────────
class B01_TheHeadline(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "satwika_slide_01.png")
        show_slide(self, img, "Slide 1 — Behavrix · Human Risk Intelligence Platform")

        lens_lbl = mute_t("Lens — The Headline", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE HEADLINE", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        stat_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.1, 0])
        self.play(Create(stat_box), run_time=0.3)

        stat = mute_t('"80% of breaches are caused by people — not firewalls."', size=28)
        stat.move_to([0, 1.1, 0])
        self.play(FadeIn(stat), run_time=0.4)
        self.wait(0.2)

        sep = terra_rule(9.0)
        sep.move_to([0, 0.2, 0])
        self.play(Create(sep), run_time=0.3)

        tag_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -0.75, 0])
        self.play(Create(tag_box), run_time=0.3)

        tag = mute_t('"We make human behavioral risk visible."', size=28)
        tag.move_to([0, -0.75, 0])
        self.play(FadeIn(tag), run_time=0.4)
        self.wait(0.2)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.85, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("Visible is passive. Can the tagline make the number land harder?", size=24)
        q.move_to([0, -1.85, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)


# ── B02 — Six Weeks ──────────────────────────────────────────────────────────
class B02_SixWeeks(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "satwika_slide_02.png")
        show_slide(self, img, "Slide 2 — $9.5T annual cybercrime · $25K per vendor assessment · 6 weeks")

        lens_lbl = mute_t("Lens — What Gets Breached in Six Weeks", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        stats = [
            ("$9.5T", "annual\ncybercrime"),
            ("$25,000", "one consulting\nengagement"),
            ("6 WEEKS", "one vendor\nassessment"),
        ]
        xs = [-4.0, 0.0, 4.0]
        for (num, lbl), x in zip(stats, xs):
            n = terra_t(num, size=44)
            n.move_to([x, 0.9, 0])
            l = mute_t(lbl, size=22)
            l.move_to([x, 0.15, 0])
            self.play(FadeIn(n), FadeIn(l), run_time=0.4)

        self.wait(0.2)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.6, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.4, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("What gets breached in those six weeks?", size=28)
        q.move_to([0, -1.4, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)


# ── B03 — Try It Live ────────────────────────────────────────────────────────
class B03_TryItLive(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "satwika_slide_01.png")
        show_slide(self, img, "Slide 1 — 'Try Behavrix Live' CTA on the title slide")

        lens_lbl = mute_t("Lens — Live Product on Slide 1", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE RIGHT CALL", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        cta_box = Rectangle(
            width=10.0, height=1.6,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=3
        ).move_to([0, 0.9, 0])
        self.play(Create(cta_box), run_time=0.3)

        cta_label = terra_t("TRY BEHAVRIX LIVE", size=42)
        cta_label.move_to([0, 0.9, 0])
        self.play(FadeIn(cta_label), run_time=0.4)
        self.wait(0.2)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.1, 0])
        self.play(Create(sep), run_time=0.3)

        info_box = Rectangle(
            width=12.2, height=2.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.4, 0])
        self.play(Create(info_box), run_time=0.3)

        note = mute_t("Most products bury the live demo on Slide 9. This one leads.", size=26)
        note.move_to([0, -1.0, 0])
        self.play(FadeIn(note), run_time=0.4)

        q = mute_t("Does the audience know they can click it right now?", size=26)
        q.move_to([0, -1.8, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B04 — Price Comparison ───────────────────────────────────────────────────
class B04_PriceComparison(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "satwika_slide_03.png")
        show_slide(self, img, "Slide 3 — Behavrix vs Alternatives · 90 sec, $0.002 vs 6 weeks, $25,000")

        lens_lbl = mute_t("Lens — The Price Comparison", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE CLAIM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        them_box = Rectangle(
            width=5.8, height=2.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.2, 0.55, 0])
        them_label = mute_t("CONSULTING", size=28)
        them_label.move_to([-3.2, 1.25, 0])
        them_desc = mute_t("$25,000\n6 weeks", size=26)
        them_desc.move_to([-3.2, 0.3, 0])

        us_box = Rectangle(
            width=5.8, height=2.0,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.2, 0.55, 0])
        us_label = terra_t("BEHAVRIX", size=28)
        us_label.move_to([3.2, 1.25, 0])
        us_desc = mute_t("$0.002\n90 seconds", size=26)
        us_desc.move_to([3.2, 0.3, 0])

        self.play(FadeIn(them_box), FadeIn(them_label), FadeIn(them_desc), run_time=0.4)
        self.play(FadeIn(us_box), FadeIn(us_label), FadeIn(us_desc), run_time=0.4)
        self.wait(0.3)

        note_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.35, 0])
        self.play(Create(note_box), run_time=0.3)

        note = mute_t("Three specifics: time, price, headcount. This slide earns its place.", size=24)
        note.move_to([0, -1.35, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B05 — Are You In ─────────────────────────────────────────────────────────
class B05_AreYouIn(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — The Close Earns Its Question", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.add(lens_lbl)

        header = ink_t("THE CLOSE", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)
        self.wait(0.2)

        ask_box = Rectangle(
            width=12.2, height=2.4,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=3
        ).move_to([0, 0.6, 0])
        self.play(Create(ask_box), run_time=0.3)

        line1 = mute_t("The human risk gap is real.", size=34)
        line1.move_to([0, 1.15, 0])
        line2 = mute_t("The product is live.", size=34)
        line2.move_to([0, 0.55, 0])
        line3 = terra_t("Are you in?", size=40)
        line3.move_to([0, -0.1, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.75, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.55, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("Directness lands when the pitch has built to it. This one has.", size=24)
        q.move_to([0, -1.55, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.wait(3.0)

        img = os.path.join(REEL_DIR, "pantry", "satwika_slide_10.png")
        show_slide(self, img, "Slide 10 — $150K seed · 15% equity · Advisory board seat", hold=0.5)

        lens_lbl = ink_t("Lens — The Close", size=36)
        lens_lbl.to_corner(UL, buff=0.65)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        goal_box = Rectangle(
            width=12.2, height=0.9,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 2.05, 0])
        self.play(Create(goal_box), run_time=0.3)

        goal = ink_t('"Specific allocations. Ninety-day milestones."', size=36)
        goal.move_to([0, 2.05, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("SEED ASK", "$150K seed · 15% equity\nAdvisory board seat", True),
            ("ALLOCATIONS", "$60K eng · $40K data\n$30K GTM · $20K ops", False),
        ]
        xs = [-3.0, 3.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=5.2, height=2.8,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, 0.0, 0])
            t = terra_t(title_str, size=36) if highlight else ink_t(title_str, size=36)
            t.move_to([x, 0.8, 0])
            b = ink_t(body_str, size=36)
            b.move_to([x, -0.25, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -1.65, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -2.4, 0])
        self.play(Create(q_box), run_time=0.3)

        q = ink_t("A close that gives the reader everything they need to act.", size=36)
        q.move_to([0, -2.4, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
