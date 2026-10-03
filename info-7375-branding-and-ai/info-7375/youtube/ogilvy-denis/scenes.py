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


# ── B01 — The DC Specificity ─────────────────────────────────────────────────
class B01_DCSpecificity(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_01.png")
        show_slide(self, img, "Slide 1 — Madison · DC job-market intel", hold=0.5)

        lens_lbl = ink_t("Lens — The DC Specificity", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("MADISON", size=60)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        tag = ink_t(
            "AI job-market intelligence\nfor the DC metro area.",
            size=36
        )
        tag.move_to([0, 0.7, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(0.3)

        q_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.3, 0])
        self.play(Create(q_box), run_time=0.3)

        q = ink_t("What does a DC analyst get\nthat no one else can?", size=36)
        q.move_to([0, -1.3, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B02 — Two Costs, One Story ───────────────────────────────────────────────
class B02_TwoCosts(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_02.png")
        show_slide(self, img, "Slide 2 — You can't tell if you're competitive — until it's too late")

        lens_lbl = mute_t("Lens — Two Costs, One Story", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        hook_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.5, 0])
        self.play(Create(hook_box), run_time=0.3)

        hook = mute_t('"You can\'t tell if you\'re competitive — until it\'s too late."', size=26)
        hook.move_to([0, 1.5, 0])
        self.play(FadeIn(hook), run_time=0.4)
        self.wait(0.2)

        cost1 = ink_t("HOURS WASTED", size=36)
        cost1.move_to([-3.0, 0.4, 0])
        cost1_lbl = mute_t("applying to jobs\nyou'll never land", size=22)
        cost1_lbl.move_to([-3.0, -0.25, 0])

        cost2 = terra_t("CONFIDENCE LOST", size=36)
        cost2.move_to([3.0, 0.4, 0])
        cost2_lbl = mute_t("not applying to jobs\nyou were qualified for", size=22)
        cost2_lbl.move_to([3.0, -0.25, 0])

        self.play(FadeIn(cost1), FadeIn(cost1_lbl), run_time=0.3)
        self.play(FadeIn(cost2), FadeIn(cost2_lbl), run_time=0.3)
        self.wait(0.2)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.85, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.55, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("Two people, one slide — which one carries the story?", size=26)
        q.move_to([0, -1.55, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)


# ── B03 — AI Arguing Your Resume ─────────────────────────────────────────────
class B03_AIArguing(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_04.png")
        show_slide(self, img, "Slide 4 — AI arguing about your resume — so you don't have to guess")

        lens_lbl = mute_t("Lens — Name the Mechanism", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE MECHANISM", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        q_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.5, 0])
        self.play(Create(q_box), run_time=0.3)

        line0 = mute_t('"AI arguing your resume\n— so you don\'t have to guess."', size=30)
        line0.move_to([0, 1.5, 0])
        self.play(FadeIn(line0), run_time=0.4)
        self.wait(0.2)

        agents = [
            ("Harsh\nHiring Manager", "finds every reason\nto reject you"),
            ("Advocate", "makes the strongest\ncase for you"),
            ("Judge", "delivers one\nhonest verdict"),
        ]
        xs = [-4.0, 0.0, 4.0]
        for (title_str, body_str), x in zip(agents, xs):
            box = RoundedRectangle(
                corner_radius=0.15, width=3.9, height=2.4,
                color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.1, 0])
            t = terra_t(title_str, size=22)
            t.move_to([x, 0.7, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -0.35, 0])
            self.play(FadeIn(box), run_time=0.25)
            self.play(FadeIn(t), FadeIn(b), run_time=0.25)

        self.wait(0.5)


# ── B04 — Multi-Agent Judgment ───────────────────────────────────────────────
class B04_MultiAgentJudgment(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_06.png")
        show_slide(self, img, "Slide 6 — Competition · Real multi-agent judgment, not keywords", hold=0.5)

        lens_lbl = ink_t("Lens — The Competitive Claim", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE DISTINCTION", size=44)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        them_box = Rectangle(
            width=5.8, height=1.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.2, 0.5, 0])
        them_label = ink_t("THEM", size=36)
        them_label.move_to([-3.2, 1.1, 0])
        them_desc = mute_t("Keyword-matching\nATS scanners", size=24)
        them_desc.move_to([-3.2, 0.3, 0])

        us_box = Rectangle(
            width=5.8, height=1.8,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.2, 0.5, 0])
        us_label = terra_t("US", size=28)
        us_label.move_to([3.2, 1.1, 0])
        us_desc = mute_t("Real multi-agent\njudgment, not keywords", size=24)
        us_desc.move_to([3.2, 0.3, 0])

        self.play(FadeIn(them_box), FadeIn(them_label), FadeIn(them_desc), run_time=0.4)
        self.play(FadeIn(us_box), FadeIn(us_label), FadeIn(us_desc), run_time=0.4)
        self.wait(0.3)

        note_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.4, 0])
        self.play(Create(note_box), run_time=0.3)

        note = ink_t("Five words. Where does the claim live in the pitch?", size=36)
        note.move_to([0, -1.4, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


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

        tier_label = terra_t("FREE TIER · LIVE DEMO", size=38)
        tier_label.move_to([0, 1.05, 0])
        tier_desc = mute_t("Run your resume against any DC job posting · right now", size=26)
        tier_desc.move_to([0, 0.3, 0])
        self.play(FadeIn(tier_label), run_time=0.4)
        self.play(FadeIn(tier_desc), run_time=0.3)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.55, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t(
            "The product is live. The free tier exists.\nWhy not end with 'go run your resume today'?",
            size=24
        )
        q.move_to([0, -1.35, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — Help Us Close the Loop ────────────────────────────────────────────
class B06_CloseTheLoop(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_09.png")
        show_slide(self, img, "Slide 9 — Help us close the loop · Funding · DC data access · Hiring feedback")

        lens_lbl = mute_t("Lens — The Close", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        goal = ink_t("Help us close the loop.", size=34)
        goal.move_to([0, 1.5, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("DATA PIPELINE", "Funding to expand\nDC-metro job\npostings coverage.", True),
            ("HIRING FEEDBACK", "Feedback from\nreal hiring managers\nto close the loop.", False),
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

        q = mute_t("Close the loop implies it's open — does the audience know they're holding it?", size=23)
        q.move_to([0, -2.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
