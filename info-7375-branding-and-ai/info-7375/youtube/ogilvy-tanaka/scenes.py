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


# ── B01 — The Morning Briefing ───────────────────────────────────────────────
class B01_MorningBriefing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.wait(3.0)

        img = os.path.join(REEL_DIR, "pantry", "tanaka_slide_01.png")
        show_slide(self, img, "Slide 1 — MentionMap · Your brand's morning briefing, powered by AI", hold=0.5)

        lens_lbl = ink_t("Lens — The Morning Briefing", size=36)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("MENTIONMAP", size=52)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        tag_box = Rectangle(
            width=12.2, height=1.4,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.9, 0])
        self.play(Create(tag_box), run_time=0.3)

        tag = ink_t(
            "Your brand's morning briefing, powered by AI.",
            size=36
        )
        tag.move_to([0, 0.9, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, 0.0, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.1, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("A ritual is not a feature — does the pitch live inside that frame?", size=24)
        q.move_to([0, -1.1, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B02 — The Person Priced Out ──────────────────────────────────────────────
class B02_PersonPricedOut(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "tanaka_slide_02.png")
        show_slide(self, img, "Slide 2 — 4.9 billion voices · $3,000/mo enterprise · $0 small teams")

        lens_lbl = mute_t("Lens — The Person Priced Out", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE PROBLEM", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        stat = terra_t("4.9B", size=80)
        stat.move_to([-2.5, 0.85, 0])
        stat_lbl = mute_t("social voices\nno signal", size=26)
        stat_lbl.move_to([1.5, 0.85, 0])
        self.play(FadeIn(stat), FadeIn(stat_lbl), run_time=0.4)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.2, 0])
        self.play(Create(sep), run_time=0.3)

        price_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.0, 0])
        self.play(Create(price_box), run_time=0.3)

        price = mute_t("Enterprise: $3,000/month  ·  Small teams: $0 (and nothing useful)", size=24)
        price.move_to([0, -1.0, 0])
        self.play(FadeIn(price), run_time=0.4)
        self.wait(0.2)

        q_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -2.05, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("The statistic is the scale — who is the person?", size=26)
        q.move_to([0, -2.05, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)


# ── B03 — Live Right Now ─────────────────────────────────────────────────────
class B03_LiveRightNow(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "tanaka_slide_09.png")
        show_slide(self, img, "Slide 9 — It's live. Right now. · All 4 features working")

        lens_lbl = mute_t("Lens — The Buried Lead", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE BURIED LEAD", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        live_box = Rectangle(
            width=12.2, height=2.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.6, 0])
        self.play(Create(live_box), run_time=0.3)

        line1 = terra_t('"It\'s live. Right now."', size=42)
        line1.move_to([0, 1.15, 0])
        line2 = mute_t("No waitlist. No account wall. No API key. All 4 features.", size=26)
        line2.move_to([0, 0.4, 0])
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.3)
        self.wait(0.3)

        place_note = mute_t("This is the most powerful fact in the pitch. It is on Slide 9.", size=26)
        place_note.move_to([0, -0.9, 0])
        self.play(FadeIn(place_note), run_time=0.4)
        self.wait(0.5)


# ── B04 — Nobody Owns This Corner ───────────────────────────────────────────
class B04_NobodyOwnsCorner(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "tanaka_slide_07.png")
        show_slide(self, img, "Slide 7 — Nobody owns this corner · Easy AND deep")

        lens_lbl = mute_t("Lens — The Competitive Claim", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE DISTINCTION", size=44)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.5)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        them_box = Rectangle(
            width=5.8, height=1.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([-3.2, 0.5, 0])
        them_label = mute_t("THEM", size=28)
        them_label.move_to([-3.2, 1.1, 0])
        them_desc = mute_t("Find mentions\nKeyword-match only", size=24)
        them_desc.move_to([-3.2, 0.3, 0])

        us_box = Rectangle(
            width=5.8, height=1.8,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([3.2, 0.5, 0])
        us_label = terra_t("US", size=28)
        us_label.move_to([3.2, 1.1, 0])
        us_desc = mute_t("Easy AND deep\nnobody owns this corner", size=24)
        us_desc.move_to([3.2, 0.3, 0])

        self.play(FadeIn(them_box), FadeIn(them_label), FadeIn(them_desc), run_time=0.4)
        self.play(FadeIn(us_box), FadeIn(us_label), FadeIn(us_desc), run_time=0.4)
        self.wait(0.3)

        note_box = Rectangle(
            width=12.2, height=1.0,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.35, 0])
        self.play(Create(note_box), run_time=0.3)

        note = mute_t("Easy compared to what? Deep in what dimension?", size=26)
        note.move_to([0, -1.35, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)


# ── B05 — Three Doors ────────────────────────────────────────────────────────
class B05_ThreeDoors(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — Three Doors", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.add(lens_lbl)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)
        self.wait(0.2)

        doors = [
            ("INVEST", "Capital for\ngrowth"),
            ("ADVISE", "Expertise\nand network"),
            ("CUSTOMER", "Use the\nproduct today"),
        ]
        xs = [-4.0, 0.0, 4.0]
        for (title_str, body_str), x in zip(doors, xs):
            box = RoundedRectangle(
                corner_radius=0.15, width=3.9, height=2.4,
                color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, 0.3, 0])
            t = mute_t(title_str, size=24)
            t.move_to([x, 0.95, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -0.1, 0])
            self.play(FadeIn(box), run_time=0.25)
            self.play(FadeIn(t), FadeIn(b), run_time=0.25)

        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -0.85, 0])
        self.play(Create(sep), run_time=0.3)

        q_box = Rectangle(
            width=12.2, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.7, 0])
        self.play(Create(q_box), run_time=0.3)

        q = mute_t("One clear ask closes a room. A menu gives permission to choose none.", size=24)
        q.move_to([0, -1.7, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.6)


# ── B06 — The Close ──────────────────────────────────────────────────────────
class B06_TheClose(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.wait(3.0)

        img = os.path.join(REEL_DIR, "pantry", "tanaka_slide_10.png")
        show_slide(self, img, "Slide 10 — $50K seed · $20K API · $20K UI/UX · $10K Product Hunt", hold=0.5)

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

        goal = ink_t('"Specific allocations. Next-step milestones."', size=36)
        goal.move_to([0, 2.05, 0])
        self.play(FadeIn(goal), run_time=0.4)
        self.wait(0.2)

        asks = [
            ("SEED", "$50K total · $20K API\n$20K UI/UX", True),
            ("LAUNCH", "$10K Product Hunt\nMarket entry · first users", False),
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

        q = ink_t("Does the reader know which door the ask is asking them to open?", size=36)
        q.move_to([0, -2.4, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
