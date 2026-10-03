import os, sys
from manim import *

REEL_DIR = os.path.dirname(os.path.abspath(__file__))

CREAM  = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTE   = "#8A8070"

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


# ── B01 — Reconstruct Problem: "The Loudest Post" ────────────────────────────
class B01_ReconstructProblem(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_01.png")
        show_slide(self, img, "Slide 1 — The loudest post keeps winning the roadmap")

        # Lens label — after slide fades
        lens_lbl = mute_t("Lens — The Opening Claim", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        # (b) Brutalist recreation
        header = ink_t("THE LOUDEST POST", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        subtitle = mute_t("keeps winning the roadmap.", size=36)
        subtitle.next_to(rule, DOWN, buff=0.4)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(0.3)

        # Three columns: TIME / NOISE / RISK
        cols = [
            ("TIME", "3 hrs weekly\nscanning HN,\nDEV, GitHub."),
            ("NOISE", "Signal gets buried.\nOne viral thread\noutranks a pattern."),
            ("RISK", "Roadmaps drift.\nSmall teams bet\nwithout support."),
        ]
        xs = [-4.0, 0.0, 4.0]
        for (label_str, body_str), x in zip(cols, xs):
            lbl = terra_t(label_str, size=30)
            lbl.move_to([x, 0.2, 0])
            body = mute_t(body_str, size=24)
            body.move_to([x, -0.95, 0])
            self.play(FadeIn(lbl), run_time=0.3)
            self.play(FadeIn(body), run_time=0.3)

        self.wait(0.6)


# ── B02 — Lens 1: Evidence Taxonomy ──────────────────────────────────────────
class B02_EvidenceTaxonomy(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_02.png")
        show_slide(self, img, "Slide 4 — A signal only counts when evidence agrees")

        lens_lbl = mute_t("Lens — The IP Taxonomy", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        # INK border box — anchors the peak row for Gate T
        frame_box = Rectangle(
            width=12.2, height=4.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -0.3, 0])
        self.play(Create(frame_box), run_time=0.3)

        header = ink_t("THE EVIDENCE FRAMEWORK", size=40)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(7.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        intro = mute_t("AI explains the trend. Trust comes from sources.", size=28)
        intro.move_to([0, 1.6, 0])
        self.play(FadeIn(intro), run_time=0.4)
        self.wait(0.2)

        tiers = [
            ("DISCUSSED", "Developer debates"),
            ("EXPLAINED", "Practitioner posts"),
            ("ADOPTED",   "Repo adoption"),
            ("VERIFIED",  "Weak data labeled"),
        ]
        ys = [0.6, -0.1, -0.8, -1.5]
        for (tier, desc), y in zip(tiers, ys):
            t_lbl = terra_t(tier, size=30)
            t_lbl.move_to([-2.5, y, 0])
            t_desc = mute_t(desc, size=28)
            t_desc.move_to([2.0, y, 0])
            self.play(FadeIn(t_lbl), FadeIn(t_desc), run_time=0.25)

        self.wait(0.5)


# ── B03 — Lens 2: The Distinction ────────────────────────────────────────────
class B03_TheDistinction(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_03.png")
        show_slide(self, img, "Slide 7 — Monitors send alerts. SignalBrief recommends action.")

        lens_lbl = mute_t("Lens — The Distinction", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE DISTINCTION", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Headline claim
        claim_box = Rectangle(
            width=12.2, height=1.1,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.55, 0])
        self.play(Create(claim_box), run_time=0.3)
        claim = mute_t("Monitors send alerts. SignalBrief recommends action.", size=30)
        claim.move_to([0, 1.55, 0])
        self.play(FadeIn(claim), run_time=0.4)
        self.wait(0.3)

        # Competitor rows
        rows = [
            ("Feedly",       "Feeds, not decisions"),
            ("F5Bot",        "Keywords, not ranking"),
            ("Brand24",      "Brand alerts, not roadmap action"),
            ("SignalBrief",  "Sources, confidence, next action"),
        ]
        ys = [0.5, -0.15, -0.8, -1.5]
        for (name_str, desc_str), y in zip(rows, ys):
            highlight = name_str == "SignalBrief"
            n = terra_t(name_str, size=28) if highlight else mute_t(name_str, size=28)
            d = terra_t(desc_str, size=28) if highlight else mute_t(desc_str, size=28)
            n.move_to([-3.5, y, 0])
            d.move_to([2.2, y, 0])
            self.play(FadeIn(n), FadeIn(d), run_time=0.25)

        self.wait(0.5)


# ── B04 — Lens 3: Name Clarity ───────────────────────────────────────────────
class B04_NameClarity(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        lens_lbl = mute_t("Lens — Name Clarity", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.add(lens_lbl)

        header = ink_t("ONE NAME. ALL THE WAY THROUGH.", size=38)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(8.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)
        self.wait(0.2)

        # Two-panel comparison with INK box to anchor Gate T
        panel_box = Rectangle(
            width=12.2, height=3.6,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -0.2, 0])
        self.play(Create(panel_box), run_time=0.3)

        # Left: "In the room"
        said_lbl = mute_t("IN THE ROOM", size=26)
        said_lbl.move_to([-3.0, 1.0, 0])
        said_name = terra_t('"Signal Proof"', size=44)
        said_name.move_to([-3.0, 0.1, 0])
        self.play(FadeIn(said_lbl), FadeIn(said_name), run_time=0.4)

        # Right: "On the deck"
        deck_lbl = mute_t("ON THE DECK", size=26)
        deck_lbl.move_to([3.5, 1.0, 0])
        deck_name = terra_t('"SignalBrief"', size=44)
        deck_name.move_to([3.5, 0.1, 0])
        self.play(FadeIn(deck_lbl), FadeIn(deck_name), run_time=0.4)
        self.wait(0.3)

        # Ogilvy note
        note = mute_t("A name that can't survive a 5-minute pitch\nwon't survive a market.", size=26)
        note.move_to([0, -1.0, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.8)


# ── B05 — Lens 4: The Buried Hero ────────────────────────────────────────────
class B05_BuriedHero(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_04.png")
        show_slide(self, img, "Slide 9 — Madison already produced the first ranked brief")

        lens_lbl = mute_t("Lens — The Buried Hero", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE BURIED HERO", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # POC stats row
        stats = [("180", "public records"), ("24.25s", "stable AI batch"), ("3", "priority signals")]
        xs = [-4.0, 0.0, 4.0]
        for (num, lbl_str), x in zip(stats, xs):
            n = ink_t(num, size=54)
            n.move_to([x, 0.9, 0])
            l = mute_t(lbl_str, size=24)
            l.move_to([x, 0.15, 0])
            self.play(FadeIn(n), FadeIn(l), run_time=0.3)

        self.wait(0.3)

        # Hero reveal — the buried number
        sep = terra_rule(10.0)
        sep.move_to([0, -0.4, 0])
        self.play(Create(sep), run_time=0.3)

        hero_lbl = mute_t("THE HERO NUMBER (said aloud, never on a slide):", size=24)
        hero_lbl.move_to([0, -0.85, 0])
        self.play(FadeIn(hero_lbl), run_time=0.3)

        # INK box anchors peak row for Gate T
        hero_box = Rectangle(
            width=12.2, height=1.1,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.7, 0])
        self.play(Create(hero_box), run_time=0.3)

        hero = mute_t("3-hour scan  →  10 minutes", size=36)
        hero.move_to([0, -1.7, 0])
        self.play(Write(hero), run_time=0.6)
        self.wait(0.6)


# ── B06 — Lens 5: The Ask ─────────────────────────────────────────────────────
class B06_TheAsk(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        img = os.path.join(REEL_DIR, "pantry", "slide_05.png")
        show_slide(self, img, "Slide 10 — Help SignalBrief reach paid pilot")

        lens_lbl = mute_t("Lens — The Ask", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("THE ASK", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        headline = ink_t("Five design partners.", size=36)
        headline.move_to([0, 1.55, 0])
        self.play(FadeIn(headline), run_time=0.4)
        self.wait(0.2)

        # Two ask cards
        asks = [
            ("DESIGN PARTNERS", "5 founders to test\nthe brief each week\nand give feedback.", True),
            ("COMMUNITY ACCESS", "Intro to founder\ncommunities where\npilots can be recruited.", False),
        ]
        xs = [-3.0, 3.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=5.2, height=2.8,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.15, 0])
            t = terra_t(title_str, size=22) if highlight else mute_t(title_str, size=22)
            t.move_to([x, 0.85, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -0.25, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.3)

        sep = terra_rule(9.0)
        sep.move_to([0, -1.85, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t("What does a design partner commit to? Give the ask a job description.", size=26)
        q.move_to([0, -2.5, 0])
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)
