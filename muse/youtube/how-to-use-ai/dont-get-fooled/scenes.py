"""scenes.py — Don't get fooled. (Humanitarians AI YouTube film)

13 Manim scenes, M01-M13, one per beat. Skill: ai-explainer.
House conventions: 16:9, safe-area coords (x within +-6.3, y within +-3.4),
ai-explainer Claude palette (cream stage, warm ink, terracotta accent), one
idea per beat, every on-screen word read aloud in its beat. Every scene
carries the @NikBearBrown watermark bug (lower-right). Text lines are kept
short enough to sit inside their cards at real Manim text metrics.

Each scene adds at least one new non-text shape per play() so the static
QC gate sees evolving shape states; explicit FadeIn/Create before any
.animate() motion.
"""
import numpy as np
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = "#F2F0E9"

# ---- ai-explainer Claude palette ----
STAGE = "#F2F0E9"
INK = "#3D3929"
TERRA = "#D97757"
DIM = "#8B8F96"
GHOST = "#D9D4C7"
CARD = "#FAF9F5"
SERIF = "EB Garamond"

# manim exposes BOLD/NORMAL; the QC stub does not. Same string values either way.
BOLD = "BOLD"
NORMAL = "NORMAL"


def T(s, size=32, color=INK, bold=False):
    return Text(s, font=SERIF, font_size=size, color=color,
                weight=BOLD if bold else NORMAL)


def bug():
    """Channel watermark bug, lower-right, inside the safe area."""
    return Text("@NikBearBrown", font_size=16, color=INK,
                fill_opacity=0.45).move_to(np.array([5.35, -3.05, 0.0]))


def card(w, h, pos, fill=CARD, edge=INK, sw=3, rad=0.18):
    return RoundedRectangle(corner_radius=rad, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=edge, stroke_width=sw).move_to(pos)


def check_mark(pos, scale=1.0, color=TERRA):
    g = VGroup(
        Line(np.array([0, 0, 0]), np.array([0.5, -0.3, 0]),
             color=color, stroke_width=12),
        Line(np.array([0.5, -0.3, 0]), np.array([1.3, 0.4, 0]),
             color=color, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def x_mark(pos, scale=1.0, color=TERRA):
    g = VGroup(
        Line(np.array([-0.45, 0.45, 0]), np.array([0.45, -0.45, 0]),
             color=color, stroke_width=12),
        Line(np.array([-0.45, -0.45, 0]), np.array([0.45, 0.45, 0]),
             color=color, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def bullet(pos, color=TERRA, r=0.11):
    return Circle(radius=r, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to(pos)


def ghost_line(pos, w):
    return Rectangle(width=w, height=0.14, fill_color=GHOST,
                     fill_opacity=1, stroke_width=0).move_to(pos)


def plate_tag(text, pos, fs=28, color=INK, bg=CARD):
    plate = RoundedRectangle(corner_radius=0.14, width=len(text) * 0.19 + 0.8,
                             height=0.72, fill_color=bg, fill_opacity=1,
                             stroke_color=color, stroke_width=3).move_to(pos)
    t = T(text, size=fs, color=color).move_to(pos)
    return VGroup(plate, t)


class M01_ColdOpen(Scene):
    def construct(self):
        self.add(bug())
        window = card(10.4, 6.2, np.array([0.0, 0.0, 0.0]), rad=0.3, sw=4)
        spark = bullet(np.array([-5.05, 2.45, 0.0]), r=0.16)
        self.play(FadeIn(window), FadeIn(spark), run_time=0.9)
        hello = T("Olá, Liam", size=40, bold=True).move_to(
            np.array([-3.0, 2.45, 0.0]))
        comp = card(9.2, 3.9, np.array([0.0, -0.35, 0.0]), rad=0.22, sw=3)
        self.play(FadeIn(hello), FadeIn(comp), run_time=0.8)
        ask1 = T("Why does the AI sound so sure", size=28).move_to(
            np.array([0.0, 1.15, 0.0]))
        ask2 = T("when it's wrong?", size=28).move_to(
            np.array([0.0, 0.65, 0.0]))
        cursor = Dot(radius=0.12, color=TERRA, fill_opacity=1).move_to(
            np.array([2.5, 0.65, 0.0]))
        self.play(Write(ask1), Write(ask2), FadeIn(cursor), run_time=0.9)
        run = T("thinking…", size=24, color=DIM).move_to(
            np.array([-3.9, -0.05, 0.0]))
        spin = bullet(np.array([-4.55, -0.05, 0.0]), r=0.1)
        self.play(FadeIn(run), FadeIn(spin), run_time=0.7)
        out1 = T("It predicts words, not truth.", size=26, bold=True).move_to(
            np.array([0.2, -0.75, 0.0]))
        out2 = T("the habits that keep you safe.", size=24, color=DIM).move_to(
            np.array([0.2, -1.35, 0.0]))
        tick1 = bullet(np.array([-4.35, -0.72, 0.0]), r=0.09)
        tick2 = bullet(np.array([-4.35, -1.32, 0.0]), r=0.09)
        self.play(Write(out1), Write(out2), FadeIn(tick1), FadeIn(tick2),
                  run_time=0.9)
        self.wait(15.9)


class M02_Bluf(Scene):
    def construct(self):
        self.add(bug())
        paper = card(9.6, 3.6, np.array([0.0, 0.5, 0.0]), rad=0.25, sw=4)
        cursor = Dot(radius=0.14, color=TERRA, fill_opacity=1).move_to(
            np.array([-4.2, 0.5, 0.0]))
        self.play(FadeIn(paper), FadeIn(cursor), run_time=0.9)
        t_a = T("AI lies because it's ", size=36).move_to(
            np.array([-2.6, 0.5, 0.0]))
        t_b = T("badly trained.", size=36).next_to(t_a, RIGHT, buff=0.15)
        self.play(Write(t_a), run_time=0.8)
        self.play(Write(t_b), run_time=0.8)
        strike = Line(t_b.get_left() + np.array([-0.15, 0.0, 0.0]),
                      t_b.get_right() + np.array([0.15, 0.0, 0.0]),
                      color=TERRA, stroke_width=9)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeOut(t_a), FadeOut(t_b), FadeOut(strike), run_time=0.7)
        t_c1 = T("AI guesses the most likely words,", size=36, bold=True
                 ).move_to(np.array([0.0, 0.9, 0.0]))
        t_c2 = T("not the truth.", size=36, bold=True).move_to(
            np.array([0.0, 0.2, 0.0]))
        self.play(Write(t_c1), Write(t_c2), run_time=1.0)
        self.wait(9.4)

class M03_Mechanism(Scene):
    def construct(self):
        self.add(bug())
        stem = card(8.8, 1.8, np.array([0.0, 2.3, 0.0]), rad=0.16)
        stem1 = T("The capital of France", size=30).move_to(
            np.array([0.0, 2.6, 0.0]))
        stem2 = T("is __________.", size=30).move_to(
            np.array([0.0, 2.0, 0.0]))
        self.play(FadeIn(stem), FadeIn(stem1), FadeIn(stem2), run_time=0.7)
        rows = [("Paris", 4.4, TERRA, 0.6), ("Lyon", 1.2, GHOST, -0.5),
                ("Nice", 0.9, GHOST, -1.6)]
        for word, bw, col, y in rows:
            chip = card(1.7, 0.62, np.array([-4.3, y, 0.0]), rad=0.12, sw=2)
            wt = T(word, size=28).move_to(np.array([-4.3, y, 0.0]))
            bar = Rectangle(width=bw, height=0.5, fill_color=col,
                            fill_opacity=1, stroke_width=0).move_to(
                                np.array([-2.6 + bw / 2, y, 0.0]))
            self.play(FadeIn(chip), FadeIn(wt), FadeIn(bar), run_time=0.6)
        ring = Circle(radius=0.95, color=TERRA, stroke_width=6).move_to(
            np.array([-4.3, 0.6, 0.0]))
        arrow = Arrow(np.array([-1.6, 0.6, 0.0]), np.array([-0.4, 1.55, 0.0]),
                      color=TERRA, stroke_width=6, buff=0.1)
        self.play(FadeIn(ring), GrowArrow(arrow), run_time=0.7)
        paris = T("Paris", size=34, bold=True).move_to(
            np.array([0.35, 2.0, 0.0]))
        cap = plate_tag("most likely ≠ always right",
                        np.array([0.0, -2.85, 0.0]), fs=28, color=TERRA)
        self.play(Write(paris), FadeIn(cap), run_time=0.9)
        self.wait(21.3)


class M04_ConfidentTone(Scene):
    def construct(self):
        self.add(bug())
        left = card(4.6, 2.6, np.array([-3.1, 0.5, 0.0]), rad=0.2)
        right = card(4.6, 2.6, np.array([3.1, 0.5, 0.0]), rad=0.2)
        conf_l = T("Definitely.", size=26, color=DIM).move_to(
            np.array([-3.1, 1.45, 0.0]))
        conf_r = T("Definitely.", size=26, color=DIM).move_to(
            np.array([3.1, 1.45, 0.0]))
        ans_l = T("“Signed in 1847.”", size=26).move_to(
            np.array([-3.1, 0.45, 0.0]))
        ans_r = T("“Signed in 1847.”", size=26).move_to(
            np.array([3.1, 0.45, 0.0]))
        self.play(FadeIn(left), FadeIn(right), FadeIn(conf_l), FadeIn(conf_r),
                  FadeIn(ans_l), FadeIn(ans_r), run_time=0.9)
        stamp_l = x_mark(np.array([-3.1, 0.5, 0.0]), scale=1.5)
        lab_l = T("made up", size=28, color=TERRA, bold=True).move_to(
            np.array([-3.1, -1.35, 0.0]))
        self.play(GrowFromCenter(stamp_l), FadeIn(lab_l), run_time=0.7)
        stamp_r = check_mark(np.array([3.1, 0.5, 0.0]), scale=1.2)
        lab_r = T("true", size=28, color=INK, bold=True).move_to(
            np.array([3.1, -1.35, 0.0]))
        self.play(GrowFromCenter(stamp_r), FadeIn(lab_r), run_time=0.7)
        rule = plate_tag("confident ≠ proof", np.array([0.0, -2.6, 0.0]),
                         fs=30, color=TERRA)
        self.play(FadeIn(rule), run_time=0.8)
        self.wait(22.9)


class M05_LawyerStory(Scene):
    def construct(self):
        self.add(bug())
        brief = card(10.4, 4.7, np.array([0.0, 0.35, 0.0]), rad=0.2, sw=4)
        head = T("BRIEF — filed in court", size=24, color=DIM).move_to(
            np.array([-3.6, 2.2, 0.0]))
        self.play(FadeIn(brief), FadeIn(head), run_time=0.8)
        c1a = T("Varghese v. China Southern…", size=19).move_to(
            np.array([-1.9, 1.35, 0.0]))
        c1b = T("925 F.3d 1339 (11th Cir. 2019)", size=19).move_to(
            np.array([-1.9, 0.95, 0.0]))
        self.play(FadeIn(c1a), FadeIn(c1b), run_time=0.6)
        c2 = T("citation 2 of 6 — invented", size=19, color=DIM).move_to(
            np.array([-1.9, 0.35, 0.0]))
        self.play(FadeIn(c2), run_time=0.6)
        c3 = T("citation 3 of 6 — invented", size=19, color=DIM).move_to(
            np.array([-1.9, -0.25, 0.0]))
        self.play(FadeIn(c3), run_time=0.6)
        for y in (1.15, 0.35, -0.25):
            stamp = x_mark(np.array([3.6, y, 0.0]), scale=0.9)
            lab = T("NOT A REAL CASE", size=16, color=TERRA, bold=True
                    ).move_to(np.array([3.6, y - 0.55, 0.0]))
            self.play(GrowFromCenter(stamp), FadeIn(lab), run_time=0.6)
        fine = plate_tag("$5,000 fine", np.array([0.0, -2.55, 0.0]), fs=30,
                         color=TERRA)
        self.play(FadeIn(fine), run_time=0.7)
        cap = T("nobody checked, because nobody doubted", size=24,
                color=DIM).move_to(np.array([0.0, -3.25, 0.0]))
        capline = Line(np.array([-3.2, -3.05, 0.0]),
                       np.array([3.2, -3.05, 0.0]), color=GHOST, stroke_width=2)
        self.play(FadeIn(capline), FadeIn(cap), run_time=0.7)
        self.wait(21.0)

class M06_Grounding(Scene):
    def construct(self):
        self.add(bug())
        frame = card(10.4, 6.0, np.array([0.0, 0.0, 0.0]), rad=0.25, sw=3,
                     fill=STAGE)
        self.play(FadeIn(frame), run_time=0.8)
        doc = card(3.4, 3.8, np.array([-2.9, 0.3, 0.0]), rad=0.16)
        doc_t = T("the source", size=26, bold=True).move_to(
            np.array([-2.9, 1.75, 0.0]))
        self.play(FadeIn(doc), FadeIn(doc_t), run_time=0.7)
        for i in range(4):
            gl = ghost_line(np.array([-2.9, 1.05 - i * 0.5, 0.0]), 2.5)
            self.add(gl)
        instr1 = T("Answer only", size=30, bold=True).move_to(
            np.array([2.75, 1.7, 0.0]))
        instr2 = T("from this text.", size=30, bold=True).move_to(
            np.array([2.75, 1.1, 0.0]))
        cursor = Dot(radius=0.11, color=TERRA, fill_opacity=1).move_to(
            np.array([4.6, 1.1, 0.0]))
        self.play(Write(instr1), Write(instr2), FadeIn(cursor), run_time=0.9)
        tether = Line(np.array([-1.2, 0.3, 0.0]), np.array([1.2, 0.3, 0.0]),
                      color=TERRA, stroke_width=6)
        ans = card(3.2, 1.5, np.array([2.75, -0.6, 0.0]), rad=0.14)
        ans_t = T("the answer", size=28).move_to(np.array([2.75, -0.6, 0.0]))
        self.play(Create(tether), FadeIn(ans), FadeIn(ans_t), run_time=0.8)
        tag = plate_tag("a reader can be checked",
                        np.array([0.0, -2.55, 0.0]), fs=26, color=TERRA)
        self.play(FadeIn(tag), run_time=0.7)
        self.wait(23.1)


class M07_IDontKnow(Scene):
    def construct(self):
        self.add(bug())
        q = card(8.0, 1.5, np.array([-2.2, 1.6, 0.0]), rad=0.16)
        q_t = T("What is the capital of Peru?", size=26).move_to(
            np.array([-2.2, 1.6, 0.0]))
        self.play(FadeIn(q), FadeIn(q_t), run_time=0.8)
        doc = card(3.4, 3.4, np.array([3.3, 0.2, 0.0]), rad=0.16)
        doc_t = T("Notes on cats", size=26, bold=True).move_to(
            np.array([3.3, 1.35, 0.0]))
        self.play(FadeIn(doc), FadeIn(doc_t), run_time=0.7)
        for i in range(3):
            self.add(ghost_line(np.array([3.3, 0.6 - i * 0.5, 0.0]), 2.5))
        gap = Line(np.array([0.2, 0.5, 0.0]), np.array([0.2, -0.9, 0.0]),
                   color=TERRA, stroke_width=5)
        gap_l = T("gap", size=24, color=TERRA, bold=True).move_to(
            np.array([0.2, -1.25, 0.0]))
        self.play(Create(gap), FadeIn(gap_l), run_time=0.7)
        a = card(6.4, 1.7, np.array([-1.4, -1.5, 0.0]), rad=0.16)
        a1 = T("I don't know —", size=28, bold=True).move_to(
            np.array([-1.4, -1.2, 0.0]))
        a2 = T("it's not in the text.", size=28, bold=True).move_to(
            np.array([-1.4, -1.8, 0.0]))
        self.play(FadeIn(a), Write(a1), Write(a2), run_time=0.9)
        ring = Ellipse(width=4.6, height=1.0, color=TERRA,
                       stroke_width=6).move_to(np.array([-1.4, -1.2, 0.0]))
        self.play(FadeIn(ring), run_time=0.7)
        self.wait(22.4)


class M08_CitationAudit(Scene):
    def construct(self):
        self.add(bug())
        ans = card(6.4, 2.4, np.array([-3.0, 1.0, 0.0]), rad=0.16)
        ans_t = T("the answer", size=24, bold=True).move_to(
            np.array([-3.0, 1.85, 0.0]))
        self.play(FadeIn(ans), FadeIn(ans_t), run_time=0.9)
        quote = T("“The meeting is on Tuesday.”", size=24).move_to(
            np.array([-3.0, 0.85, 0.0]))
        qline = Line(np.array([-5.9, 0.45, 0.0]), np.array([-0.1, 0.45, 0.0]),
                     color=TERRA, stroke_width=3)
        self.play(Write(quote), Create(qline), run_time=0.6)
        doc = card(6.0, 3.0, np.array([3.7, 0.7, 0.0]), rad=0.16)
        doc_t = T("SAMPLE DOCUMENT", size=22, color=DIM).move_to(
            np.array([3.7, 1.85, 0.0]))
        self.play(FadeIn(doc), FadeIn(doc_t), run_time=0.6)
        match_t = T("The meeting is on Tuesday.", size=22).move_to(
            np.array([3.7, 0.5, 0.0]))
        self.add(match_t)
        mag = Circle(radius=0.55, color=TERRA, stroke_width=6).move_to(
            np.array([-3.0, 0.85, 0.0]))
        handle = Line(np.array([-2.6, 0.5, 0.0]), np.array([-1.9, -0.1, 0.0]),
                      color=TERRA, stroke_width=6)
        self.play(FadeIn(mag), FadeIn(handle), run_time=0.6)
        self.play(mag.animate.move_to(np.array([3.7, 0.5, 0.0])),
                  handle.animate.move_to(np.array([4.1, 0.15, 0.0])),
                  run_time=0.7)
        chk = check_mark(np.array([5.9, 0.5, 0.0]), scale=0.8, color=INK)
        self.play(GrowFromCenter(chk), run_time=0.6)
        bad = T("“The meeting is on Friday.”", size=22, color=DIM).move_to(
            np.array([-3.0, -1.6, 0.0]))
        badcard = card(6.4, 1.1, np.array([-3.0, -1.6, 0.0]), rad=0.12)
        self.play(FadeIn(badcard), Write(bad), run_time=0.7)
        badx = x_mark(np.array([-3.0, -1.6, 0.0]), scale=0.9)
        badlab = T("hallucinated citation", size=22, color=TERRA,
                   bold=True).move_to(np.array([3.7, -1.6, 0.0]))
        self.play(GrowFromCenter(badx), FadeIn(badlab), run_time=0.7)
        self.wait(21.0)

class M09_CrossCheck(Scene):
    def construct(self):
        self.add(bug())
        claim = card(8.8, 1.5, np.array([0.0, 1.5, 0.0]), rad=0.16)
        claim_t = T("“The new policy starts Monday.”", size=28).move_to(
            np.array([0.0, 1.5, 0.0]))
        self.play(FadeIn(claim), FadeIn(claim_t), run_time=0.8)
        sa = card(3.0, 2.0, np.array([-4.3, -0.9, 0.0]), rad=0.14)
        sa_t = T("source A", size=26, bold=True).move_to(
            np.array([-4.3, -0.4, 0.0]))
        sb = card(3.0, 2.0, np.array([4.3, -0.9, 0.0]), rad=0.14)
        sb_t = T("source B", size=26, bold=True).move_to(
            np.array([4.3, -0.4, 0.0]))
        self.play(FadeIn(sa), FadeIn(sa_t), FadeIn(sb), FadeIn(sb_t),
                  run_time=0.7)
        ca = check_mark(np.array([-4.3, -1.25, 0.0]), scale=0.9, color=INK)
        self.play(GrowFromCenter(ca), run_time=0.7)
        cb = check_mark(np.array([4.3, -1.25, 0.0]), scale=0.9, color=INK)
        self.play(GrowFromCenter(cb), run_time=0.7)
        badge = plate_tag("confident tone ≠ proof",
                          np.array([0.0, -2.75, 0.0]), fs=28, color=TERRA)
        self.play(FadeIn(badge), run_time=0.8)
        self.wait(21.3)


class M10_ThreeSentences(Scene):
    def construct(self):
        self.add(bug())
        cards = [
            (["1. Paste the source.", "Answer only from this text."],
             1.7, INK),
            (["2. If the answer isn't in the text,",
              "say you don't know."], 0.1, INK),
            (["3. Quote the exact sentence", "— and check it."],
             -1.5, TERRA),
        ]
        for lines, y, edge in cards:
            c = card(9.0, 1.3, np.array([0.0, y, 0.0]), rad=0.14, edge=edge,
                     sw=4 if edge == TERRA else 3)
            t1 = T(lines[0], size=24, bold=True).move_to(
                np.array([0.0, y + 0.28, 0.0]))
            t2 = T(lines[1], size=24, bold=True).move_to(
                np.array([0.0, y - 0.32, 0.0]))
            chk = check_mark(np.array([4.0, y, 0.0]), scale=0.7)
            self.play(FadeIn(c), FadeIn(t1), FadeIn(t2), FadeIn(chk),
                      run_time=0.8)
        self.wait(22.6)


class M11_Recap(Scene):
    def construct(self):
        self.add(bug())
        groups = [
            (["It guesses words, not truth."], 1.7),
            (["Ground it: give it the source;",
              "answer only from that."], 0.28),
            (["Audit it: quote the passage;",
              "check it; cross-check it."], -1.42),
        ]
        for lines, y in groups:
            d = bullet(np.array([-5.2, y, 0.0]))
            ts = [T(ln, size=28).move_to(np.array([0.2, y + 0.28 - i * 0.55, 0.0]))
                  for i, ln in enumerate(lines)]
            self.play(FadeIn(d), *[Write(t) for t in ts], run_time=0.8)
        self.wait(20.6)


class M12_YourTurn(Scene):
    def construct(self):
        self.add(bug())
        window = card(12.4, 5.6, np.array([0.0, 0.2, 0.0]), rad=0.25, sw=4)
        head = T("Your turn.", size=40, bold=True).move_to(
            np.array([-3.5, 2.35, 0.0]))
        spark = bullet(np.array([-5.85, 2.35, 0.0]), r=0.16)
        self.play(FadeIn(window), FadeIn(head), FadeIn(spark), run_time=0.9)
        lines = [
            ("“Answer only from the text above.", 1.25, 8.2),
            ("If the answer isn't in the text,", 0.55, 8.0),
            ("say you don't know.”", -0.05, 5.0),
            ("“Quote the exact sentence you draw from.”", -0.85, 10.2),
        ]
        for txt, y, bw in lines:
            t = T(txt, size=24).move_to(np.array([0.0, y, 0.0]))
            bar = Line(np.array([-bw / 2, y - 0.38, 0.0]),
                       np.array([bw / 2, y - 0.38, 0.0]),
                       color=TERRA, stroke_width=3)
            self.play(Write(t), Create(bar), run_time=0.8)
        tag = plate_tag("paste into Claude", np.array([0.0, -1.9, 0.0]),
                        fs=28, color=TERRA)
        self.play(FadeIn(tag), run_time=0.6)
        self.wait(24.1)


class M13_Outro(Scene):
    def construct(self):
        self.add(bug())
        title = T("Don't get fooled", size=64, bold=True).move_to(
            np.array([-0.15, 0.6, 0.0]))
        self.play(Write(title), run_time=1.2)
        rule = Line(np.array([-2.6, -0.35, 0.0]), np.array([2.6, -0.35, 0.0]),
                    color=TERRA, stroke_width=6)
        self.play(Create(rule), run_time=0.6)
        dot = Circle(radius=0.13, fill_color=TERRA, fill_opacity=1,
                     stroke_width=0).move_to(np.array([5.05, 0.15, 0.0]))
        self.play(FadeIn(dot), run_time=0.5)
        handle = T("@NikBearBrown", size=36, color=DIM).move_to(
            np.array([0.0, -1.5, 0.0]))
        self.play(FadeIn(handle), run_time=0.6)
        self.wait(6.1)
