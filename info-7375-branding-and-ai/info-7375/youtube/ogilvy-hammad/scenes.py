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


# ── B01 — The Buried Badge ───────────────────────────────────────────────────
class B01_LiveMVP(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_01.png")
        show_slide(self, img, "Slide 1 — SentinelGRC · AI-Powered Compliance Intelligence · LIVE MVP badge top-left")

        lens_lbl = mute_t("Lens — The Buried Badge", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("SENTINELGRC", size=54)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        badge_box = Rectangle(
            width=12.2, height=1.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.8, 0])
        self.play(Create(badge_box), run_time=0.3)

        badge_label = mute_t("[ LIVE MVP ]", size=26)
        badge_label.move_to([0, 1.3, 0])
        badge_q = mute_t("Why is your most powerful fact a version tag?", size=28)
        badge_q.move_to([0, 0.5, 0])
        self.play(FadeIn(badge_label), run_time=0.3)
        self.play(FadeIn(badge_q), run_time=0.4)
        self.wait(0.3)

        note = mute_t('"Live MVP" is the headline. Everything else is the subhead.', size=24)
        note.move_to([0, -0.7, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B02 — The 0 Time ─────────────────────────────────────────────────────────
class B02_ZeroTime(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_02.png")
        show_slide(self, img, "Slide 2 — Every Monday Morning, GRC Analysts Face This", hold=0.5)

        lens_lbl = ink_t("Lens — The Human Cost", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        stat1 = ink_t("2–3 HRS", size=52)
        stat1.move_to([-4.0, 0.9, 0])
        lbl1 = ink_t("manual CISA review", size=36)
        lbl1.move_to([-4.0, 0.2, 0])

        stat2 = ink_t("$200K", size=52)
        stat2.move_to([0.0, 0.9, 0])
        lbl2 = ink_t("enterprise entry price", size=36)
        lbl2.move_to([0.0, 0.2, 0])

        stat3 = terra_t("0 TIME", size=52)
        stat3.move_to([4.0, 0.9, 0])
        lbl3 = ink_t("no time to react", size=36)
        lbl3.move_to([4.0, 0.15, 0])

        self.play(FadeIn(stat1), FadeIn(lbl1), run_time=0.3)
        self.play(FadeIn(stat2), FadeIn(lbl2), run_time=0.3)
        self.play(FadeIn(stat3), FadeIn(lbl3), run_time=0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.45, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.25, 0])
        self.play(Create(q_box), run_time=0.3)

        q = ink_t("2–3 hrs is the input.\n0 time — the cost to the person.", size=36)
        q.move_to([0, -1.25, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B03 — Live on HuggingFace ────────────────────────────────────────────────
class B03_LiveOnHuggingFace(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.wait(3.0)

        img = os.path.join(REEL_DIR, "pantry", "slide_09.png")
        show_slide(self, img, "Slide 9 — Sentinel GRC Ops · Live on HuggingFace today", hold=0.5)

        lens_lbl = ink_t("Lens — The Buried Lead", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE BURIED LEAD", size=44)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=2.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.1, 0])
        self.play(Create(q_box), run_time=0.3)

        line1 = terra_t("Live on HuggingFace today.", size=36)
        line1.move_to([0, 0.9, 0])
        line2 = ink_t("No setup · Real output.", size=36)
        line2.move_to([0, 0.1, 0])
        line3 = ink_t("This product is live. It is on Slide 9.", size=36)
        line3.move_to([0, -0.65, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.play(FadeIn(line3), run_time=0.3)
        self.wait(0.5)


# ── B04 — We Own the White Space ─────────────────────────────────────────────
class B04_WhiteSpace(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_07.png")
        show_slide(self, img, "Slide 7 — We Own the White Space · Enterprise price vs compliance intelligence")

        lens_lbl = mute_t("Lens — The Competition Claim", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE DISTINCTION", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        claim_box = Rectangle(
            width=12.2, height=2.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.7, 0])
        self.play(Create(claim_box), run_time=0.3)

        line1 = mute_t("Enterprise vendors can't hit our price point.", size=28)
        line1.move_to([0, 1.25, 0])
        line2 = mute_t("Automation tools don't have the compliance intelligence.", size=28)
        line2.move_to([0, 0.6, 0])
        line3 = terra_t("We have both.", size=30)
        line3.move_to([0, 0.0, 0])
        self.play(FadeIn(line1), run_time=0.3)
        self.play(FadeIn(line2), run_time=0.3)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(0.5)

        note = mute_t("Specifics always outperform generalities. This slide earns its place.", size=24)
        note.move_to([0, -1.1, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.4)


# ── B05 — Free and Live ──────────────────────────────────────────────────────
class B05_FreeAndLive(Scene):
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

        tier_label = terra_t("FREE TIER · LIVE MVP", size=38)
        tier_label.move_to([0, 1.05, 0])
        tier_desc = mute_t("Zero setup · run CISA analysis now · no cost", size=28)
        tier_desc.move_to([0, 0.3, 0])
        self.play(FadeIn(tier_label), run_time=0.4)
        self.play(FadeIn(tier_desc), run_time=0.3)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.55, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t(
            "The product is live. The free tier exists.\nWhy not end with 'go run your first analysis today'?",
            size=24
        )
        q.move_to([0, -1.35, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_10.png")
        show_slide(self, img, "Slide 10 — Let's Build This Together · Co-op or $150K seed")

        lens_lbl = mute_t("Lens — The Close", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        goal = ink_t("Let's Build This Together", size=34)
        goal.move_to([0, 1.5, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("CO-OP / INTERNSHIP", "Pilot SentinelGRC\nwith Northeastern\npartnership.", True),
            ("$150K SEED", "Onboard first\n10 customers\nin 6 months.", False),
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

        q = mute_t("Student and investor — do they need separate rooms?", size=26)
        q.move_to([0, -2.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
