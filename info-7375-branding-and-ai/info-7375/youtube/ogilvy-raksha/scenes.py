"""Manim scenes — ogilvy-raksha
An Ogilvy Lens on Threadline (Raksha Krishna Moorthy, INFO 7375).
Palette: claude — cream #FAF9F5, ink #3D3929, terracotta #D97757.
All quoted text is verbatim from the deck PDF and video transcript.
Font: EB Garamond throughout.
"""
import os
from manim import *

# ── palette ───────────────────────────────────────────────────────────────────
CREAM  = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTE   = "#8A8070"

config.background_color = CREAM
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width  = 1920


def ink_t(text, size=36, **kw):
    return Text(text, color=INK, font_size=size, font="EB Garamond", **kw)

def terra_t(text, size=36, **kw):
    return Text(text, color=TERRA, font_size=size, font="EB Garamond", **kw)

def mute_t(text, size=30, **kw):
    return Text(text, color=MUTE, font_size=size, font="EB Garamond", **kw)

def terra_rule(width=6.0):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=TERRA, stroke_width=2)


def show_slide(scene, img_path, label_text, hold=3.0):
    """(a) Show the real PDF slide full-frame with TERRA border + label, then fade out."""
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


# ── B01 — Reconstruct: Slide 1 — The Title ───────────────────────────────────
class B01_ReconstructTitle(Scene):
    """~20s  Show real Slide 1, then Brutalist rebuild: title + origin story."""

    def construct(self):
        REEL_DIR = os.path.dirname(os.path.abspath(__file__))

        # (a) Real slide
        show_slide(self, f"{REEL_DIR}/pantry/slide_01.png",
                   "Slide 1 — Threadline · Adaptive Fashion Market Intelligence",
                   hold=3.0)

        # (b) Brutalist recreation
        title = ink_t("THREADLINE", size=64)
        title.move_to([0, 2.0, 0])
        rule = terra_rule(7.0)
        rule.next_to(title, DOWN, buff=0.18)
        sub = ink_t("Adaptive Fashion Market Intelligence", size=36)
        sub.next_to(rule, DOWN, buff=0.28)

        origin = mute_t(
            "While interning at a cancer detection startup,\n"
            "I kept noticing gaps beyond treatment —\n"
            "people couldn't find clothing that worked for their bodies.",
            size=28
        )
        origin.move_to([0, -1.1, 0])

        byline = mute_t("Raksha Krishna Moorthy · Northeastern University", size=26)
        byline.to_edge(DOWN, buff=0.4)

        self.play(Write(title), run_time=0.7)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(origin), run_time=0.7)
        self.play(FadeIn(byline), run_time=0.4)
        self.wait(3.5)


# ── B02 — Reconstruct: Slide 2 — The Problem ─────────────────────────────────
class B02_ReconstructProblem(Scene):
    """~35s  Show real Slide 2, then Brutalist rebuild: stats + Reddit quote."""

    def construct(self):
        REEL_DIR = os.path.dirname(os.path.abspath(__file__))

        # (a) Real slide
        show_slide(self, f"{REEL_DIR}/pantry/slide_02.png",
                   "Slide 2 — The Problem",
                   hold=3.5)

        # (b) Brutalist recreation
        header = ink_t("THE PROBLEM", size=42)
        header.to_edge(UP, buff=0.6)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Market claim
        claim = mute_t("A $15-20B market. No brand is listening.", size=32)
        claim.move_to([0, 2.0, 0])
        self.play(FadeIn(claim), run_time=0.5)
        self.wait(0.3)

        # Three stats
        stats = [
            ("35M",    "US consumers\nneed adaptive clothing"),
            ("168K",   "surgeries annually —\nchanges what someone\ncan wear"),
            ("$20K+",  "one brand focus group,\nsix weeks"),
        ]
        xs = [-4.4, 0.0, 4.4]
        for (num, lbl), x in zip(stats, xs):
            n = ink_t(num, size=52)
            l = mute_t(lbl, size=28)
            n.move_to([x, 0.8, 0])
            l.move_to([x, -0.1, 0])
            self.play(FadeIn(n, shift=UP * 0.15), FadeIn(l), run_time=0.4)
        self.wait(0.3)

        # Reddit quote block
        q_rule = terra_rule(11.0)
        q_rule.move_to([0, -1.35, 0])
        self.play(Create(q_rule), run_time=0.3)

        q1 = mute_t(
            '"Help me. I cannot make one more Amazon return.',
            size=30
        )
        q1.move_to([0, -1.85, 0])
        q2 = mute_t(
            "I'm weeks out from surgery and I'm looking for something that actually works.\"",
            size=30
        )
        q2.move_to([0, -2.28, 0])
        src = mute_t("r/breastcancer, verified post, May 2026", size=26)
        src.move_to([0, -2.75, 0])

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(src), run_time=0.3)
        self.wait(5.0)


# ── B03 — Lens 1: The Big Idea — Where Does It Live? ─────────────────────────
class B03_BigIdea(Scene):
    """~30s  Show real Slide 7, then rebuild: the differentiator line, then the question."""

    def construct(self):
        REEL_DIR = os.path.dirname(os.path.abspath(__file__))

        # (a) Real slide — lens label appears AFTER slide fades out
        show_slide(self, f"{REEL_DIR}/pantry/slide_07.png",
                   "Slide 7 — Competition · Where the Big Idea Lives",
                   hold=3.5)

        # Lens label shown during reconstruction, not during slide display
        lens_lbl = mute_t("Ogilvy lens 1 of 4", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        # (b) Brutalist recreation
        header = ink_t("THE BIG IDEA", size=42)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # The differentiator — split into punchier lines
        line1 = ink_t("Our competitors sell clothing.", size=38)
        line1.move_to([0, 1.6, 0])
        self.play(FadeIn(line1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)

        line2 = terra_t("Threadline sells the intelligence", size=36)
        line2.move_to([0, 0.9, 0])
        self.play(FadeIn(line2, shift=UP * 0.15), run_time=0.5)

        line3 = mute_t(
            "that tells any brand — including them —\nwhat to build next.",
            size=30
        )
        line3.move_to([0, 0.2, 0])
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(0.5)

        # Separator
        sep = terra_rule(8.0)
        sep.move_to([0, -0.85, 0])
        self.play(Create(sep), run_time=0.3)

        # Location note
        loc = mute_t("This line lives on Slide 7.", size=30)
        loc.move_to([0, -1.4, 0])
        self.play(FadeIn(loc), run_time=0.4)
        self.wait(0.3)

        # The question
        q = mute_t("What if it led?", size=36)
        q.move_to([0, -2.15, 0])
        self.play(Write(q), run_time=0.7)
        self.wait(3.0)


# ── B04 — Lens 2: Story Appeal — The Reddit Quote ────────────────────────────
class B04_StoryAppeal(Scene):
    """~35s  The verified Reddit quote as the Hathaway eyepatch moment."""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 2 of 4", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = ink_t("Story Appeal", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Ogilvy principle line
        epi = mute_t(
            "One concrete, specific detail makes everything else credible.",
            size=30
        )
        epi.move_to([0, 1.9, 0])
        self.play(FadeIn(epi), run_time=0.4)
        self.wait(0.5)

        # Full-frame display quote — the eyepatch moment
        q_box = Rectangle(
            width=12.2, height=2.8,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 0.3, 0])
        self.play(Create(q_box), run_time=0.4)

        q1 = terra_t('"Help me. I cannot make one more Amazon return.', size=34)
        q1.move_to([0, 0.85, 0])
        q2 = mute_t(
            "I'm weeks out from surgery and I'm looking for\nsomething that actually works.\"",
            size=30
        )
        q2.move_to([0, 0.05, 0])
        src = mute_t("r/breastcancer, verified post, May 2026", size=26)
        src.next_to(q_box, DOWN, buff=0.2)

        self.play(Write(q1), run_time=0.7)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(src), run_time=0.3)
        self.wait(1.0)

        # The question
        sep = terra_rule(8.0)
        sep.move_to([0, -2.0, 0])
        self.play(Create(sep), run_time=0.3)

        loc = mute_t(
            "Lives on Slide 2, in a bullet list, beside the market figures.",
            size=30
        )
        loc.move_to([0, -2.55, 0])
        self.play(FadeIn(loc), run_time=0.4)
        self.wait(0.5)

        q_end = mute_t("What if it was the first thing in the pitch?", size=32)
        q_end.move_to([0, -3.15, 0])
        self.play(Write(q_end), run_time=0.7)
        self.wait(4.0)


# ── B05 — Lens 3: Where's the Source? ────────────────────────────────────────
class B05_Sources(Scene):
    """~30s  Three market numbers, then provenance tags animate in beside each."""

    def construct(self):
        lens_lbl = mute_t("Ogilvy lens 3 of 4", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        header = terra_t("Where's the Source?", size=46)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(6.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Three rows: number | label — then source tag fades in
        items = [
            ("$15-20B", "adaptive clothing market", "[IBIS / Grand View]"),
            ("35M",     "US consumers",             "[CDC disability data]"),
            ("168K",    "surgeries annually",        "[ACS / NCI]"),
        ]
        ys = [1.4, 0.2, -1.0]

        # Phase 1 — show numbers and labels only
        rows = []
        for (num, lbl, _src), y in zip(items, ys):
            n = ink_t(num, size=42)
            n.move_to([-3.5, y, 0])
            l = mute_t(lbl, size=26)
            l.move_to([0.8, y, 0])
            self.play(FadeIn(n), FadeIn(l), run_time=0.35)
            rows.append((n, l))
        self.wait(1.0)

        # Phase 2 — source tags appear beside each row (no special chars for kerning)
        src_tags = [
            "[IBIS, Grand View]",
            "[CDC disability data]",
            "[ACS, NCI]",
        ]
        for src, y in zip(src_tags, ys):
            s = terra_t(src, size=22)
            s.move_to([4.8, y, 0])
            self.play(FadeIn(s, shift=LEFT * 0.2), run_time=0.45)
        self.wait(0.8)

        # Question
        sep = terra_rule(9.0)
        sep.move_to([0, -2.1, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t("Which version asks the audience for less?", size=32)
        q.move_to([0, -2.75, 0])
        self.play(Write(q), run_time=0.7)
        self.wait(4.5)


# ── B06 — Lens 4: The Close — One Ask or Three? ──────────────────────────────
class B06_TheClose(Scene):
    """~32s  Show real Slide 10, then rebuild: three asks, pilot partner highlighted."""

    def construct(self):
        REEL_DIR = os.path.dirname(os.path.abspath(__file__))

        # (a) Real slide — lens label appears AFTER slide fades out
        show_slide(self, f"{REEL_DIR}/pantry/slide_10.png",
                   "Slide 10 — The Ask",
                   hold=3.5)

        # Lens label shown during reconstruction, not during slide display
        lens_lbl = mute_t("Ogilvy lens 4 of 4", size=28)
        lens_lbl.to_corner(UL, buff=1.2)
        self.play(FadeIn(lens_lbl), run_time=0.3)

        # (b) Brutalist recreation
        header = ink_t("THE ASK", size=42)
        header.to_edge(UP, buff=0.65)
        rule = terra_rule(5.0)
        rule.next_to(header, DOWN, buff=0.12)
        self.play(Write(header), Create(rule), run_time=0.5)

        # Headline
        headline = ink_t("Stop guessing. Start knowing.", size=34)
        headline.move_to([0, 1.85, 0])
        self.play(FadeIn(headline), run_time=0.5)
        self.wait(0.3)

        # Three ask cards
        asks = [
            ("A PILOT PARTNER", "One brand or hospital\nto test on a real\ndecision — 60 days.", True),
            ("TECHNICAL HELP", "A developer to automate\nthe system fully.\nPartly manual now.", False),
            ("AN INTRO", "Someone in adaptive\nfashion, healthcare,\nor retail.", False),
        ]
        xs = [-4.0, 0.0, 4.0]
        for (title_str, body_str, highlight), x in zip(asks, xs):
            box_color = TERRA if highlight else INK
            box = RoundedRectangle(
                corner_radius=0.15, width=3.9, height=3.0,
                color=box_color, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, -0.2, 0])
            t = terra_t(title_str, size=22) if highlight else mute_t(title_str, size=22)
            t.move_to([x, 0.85, 0])
            b = mute_t(body_str, size=20)
            b.move_to([x, -0.35, 0])
            self.play(FadeIn(box), run_time=0.3)
            self.play(FadeIn(t), FadeIn(b), run_time=0.3)

        self.wait(0.5)

        # Question
        sep = terra_rule(9.0)
        sep.move_to([0, -2.15, 0])
        self.play(Create(sep), run_time=0.3)

        q = mute_t("Which one does this audience walk away wanting to do?", size=30)
        q.move_to([0, -2.75, 0])
        self.play(Write(q), run_time=0.7)
        self.wait(4.5)
