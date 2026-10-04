"""
iso_kit.py — the show-tell drawing kit. PASTE this block at the top of a reel's scenes.py;
do not import it (Gate A copies only scenes.py into its sandbox).

Drawn isometric objects in the Claude palette: cardboard boxes (closed, open, taped), dark
MCP blocks with ports, flat skill pages, server stacks with lights, checks, a cursor, pills.
Pacing helpers read the reel's beat_sheet.json so scenes wait for their spoken phrase.

Every rule in ../SKILL.md "DRAWING LAWS" is already obeyed by these primitives; keep it that
way when you add one (label beside, never inside; terracotta never under text; dim greys
with gaps for chart blocks; type floor 32).
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)
# FILM HELPERS - "Make It Interview You First" (original to this film).
# Flat UI shapes in the Claude palette: composer card, typed lines, answer
# pages, question bubbles, question cards, answer chips, envelope, labels.
# All coordinates stay inside +-6.2 x +-3.3; labels sit beside objects (or as
# captions below, the approved card-row pattern), never inside an outline;
# type floor 32; leader lines keep >=0.3 gap from their labels.


def composer_at(y=-2.1, w=7.6):
    """Flat chat composer card with a cursor; the typed line is added by the scene."""
    card = RoundedRectangle(width=w, height=1.15, corner_radius=0.28,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=2).move_to([0, y, 0])
    cur = cursor(-w / 2 + 0.55, y + 0.30, s=0.34)
    return card, cur


def typed_in(s, left, y, size=36):
    """A typed line starting at `left` (cursor position); returns (text, est width)."""
    t = T(s, size=size, color=INK)
    w_est = len(s) * size * 0.0075
    t.move_to([left + w_est / 2, y, 0])
    return t, w_est


def page(x, y, w=3.2, h=2.3, nlines=6, dim=False, lw=0.78):
    """Flat answer page: slab + ghost text lines. `dim` = the old generic answer."""
    fill = "#FFFFFF" if not dim else "#ECEAE2"
    outl = INK if not dim else "#8B8F96"
    slab = Polygon([x - w / 2, y - h / 2, 0], [x + w / 2, y - h / 2, 0],
                   [x + w / 2, y + h / 2, 0], [x - w / 2, y + h / 2, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=outl, stroke_width=2)
    lines = VGroup(*[Line([x - w / 2 + 0.28, y + h / 2 - 0.5 - i * 0.32, 0],
                         [x - w / 2 + 0.28 + w * lw, y + h / 2 - 0.5 - i * 0.32, 0],
                         color=GHOST, stroke_width=5)
                     for i in range(nlines)])
    return VGroup(slab, lines)


def qbubble(x, y, r=0.32):
    """A question bubble: white circle, ink outline, terracotta dot."""
    c = Circle(radius=r, fill_color="#FFFFFF", fill_opacity=1,
               stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    d = Dot([x, y, 0], radius=0.075, color=TERRA)
    return VGroup(c, d)


def qcard(x, y, w=1.9, h=0.95, word="", hl=True):
    """A question card: rounded rect + terracotta dot, one-word caption below."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.22,
                            fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=INK if hl else "#B4AFA6",
                            stroke_width=3 if hl else 2).move_to([x, y, 0])
    d = Dot([x - w / 2 + 0.3, y + h / 2 - 0.28, 0], radius=0.08,
            color=TERRA if hl else "#B4AFA6")
    lab = T(word, size=36, color=INK if hl else "#8B8F96").move_to([x, y - h / 2 - 0.42, 0])
    return VGroup(body, d, lab)


def chip(x, y, s, size=34):
    """An answer chip: ink-outlined pill with its answer word."""
    p = pill(x, y, len(s) * size * 0.0075 + 0.9, h=0.62, fill="#FFFFFF")
    p.set_stroke(INK, width=2)
    t = T(s, size=size).move_to([x, y, 0])
    return VGroup(p, t)


def envelope(x, y, w=2.6, h=1.7):
    """A simple envelope: ink-outlined rect with a flap."""
    body = Polygon([x - w / 2, y - h / 2, 0], [x + w / 2, y - h / 2, 0],
                   [x + w / 2, y + h / 2, 0], [x - w / 2, y + h / 2, 0],
                   fill_color="#FFFFFF", fill_opacity=1, stroke_color=INK, stroke_width=2)
    f1 = Line([x - w / 2, y + h / 2, 0], [x, y + 0.1, 0], color=INK, stroke_width=2)
    f2 = Line([x + w / 2, y + h / 2, 0], [x, y + 0.1, 0], color=INK, stroke_width=2)
    return VGroup(body, f1, f2)


def shadow(x, y, w=4.4, h=0.7):
    return Ellipse(width=w, height=h, fill_color="#D9D4C7",
                   fill_opacity=1, stroke_width=0).move_to([x, y, 0])


def label(s, x, y, size=36):
    return T(s, size=size, color=INK).move_to([x, y, 0])


def leader(x1, y1, x2, y2):
    return Line([x1, y1, 0], [x2, y2, 0], color=INK, stroke_width=3)


# ═════════════════════════════ SCENES (one per body beat) ═════════════════════════════


class B00_AskOnce(Scene):
    """The hero: a one-line ask goes in, a thin generic answer comes out."""

    def construct(self):
        card, cur = composer_at(y=-2.1, w=7.6)
        self.play(FadeIn(card), FadeIn(cur), run_time=0.6)
        until(self, "Start here.")
        typed, _ = typed_in("plan my trip", -2.9, -2.1, size=40)
        self.play(Write(typed), run_time=0.7)
        until(self, "You type 'plan my trip'")
        pg = page(0, 0.9, w=3.4, h=2.2, nlines=3, lw=0.55)
        self.play(GrowFromCenter(pg), run_time=0.7)
        until(self, "Claude answers")
        lab = label("generic answer", 3.9, 1.2)
        lead = leader(1.95, 1.05, 2.35, 1.1)
        self.play(FadeIn(lab), Create(lead), run_time=0.5)
        until(self, "A generic list")
        finish(self)


class B01_AskFirst(Scene):
    """The move: 'Ask me 5 questions first.' — five question bubbles drop in."""

    def construct(self):
        card, cur = composer_at(y=-2.1, w=8.4)
        self.play(FadeIn(card), FadeIn(cur), run_time=0.6)
        until(self, "Now change one line.")
        typed, _ = typed_in("Ask me 5 questions first.", -3.3, -2.1, size=36)
        self.play(Write(typed), run_time=0.8)
        until(self, "you add:")
        bubbles = VGroup(*[qbubble(-2.4 + i * 1.2, 0.9) for i in range(5)])
        self.play(*[FadeIn(b) for b in bubbles], lag_ratio=0.18, run_time=1.4)
        until(self, "Five question")
        lab = label("the interview", 3.9, 1.6)
        lead = leader(2.75, 1.15, 3.15, 1.45)
        self.play(FadeIn(lab), Create(lead), run_time=0.5)
        until(self, "The interview,")
        finish(self)


class B02_FiveQuestions(Scene):
    """The five questions land — budget, dates, who, pace, must-see — then a scan line."""

    def construct(self):
        words = ["budget", "dates", "who", "pace", "must-see"]
        triggers = ["Watch what the questions do.", "Dates.", "Who is going.",
                    "Fast or slow.", "One must-see."]
        xs = [-4.4, -2.2, 0.0, 2.2, 4.4]
        cards = [qcard(x, 0.4, word=w) for x, w in zip(xs, words)]
        self.play(FadeIn(cards[0]), run_time=0.4)
        until(self, triggers[0])
        for card, trig in zip(cards[1:], triggers[1:]):
            self.play(FadeIn(card), run_time=0.35)
            until(self, trig)
        scan = Line([-5.4, -1.1, 0], [-5.0, -1.1, 0], color=TERRA, stroke_width=8)
        path = Line([-5.4, -1.1, 0], [5.4, -1.1, 0])
        self.play(MoveAlongPath(scan, path), run_time=0.8)
        until(self, "would have guessed wrong.")
        finish(self)


class B03_BriefBuilt(Scene):
    """Your answers drop as chips into the open brief box."""

    def construct(self):
        iso = Iso(ox=-1.2, oy=-0.6, s=1.0)
        back, front = iso.open_box(-1.3, -1.0, 0, 2.6, 2.0, 1.1)
        sh = shadow(-1.2, -1.95)
        self.play(FadeIn(sh), FadeIn(back), FadeIn(front), run_time=0.7)
        until(self, "Now you answer — briefly.")
        lab = label("your brief", 3.5, 1.15)
        lead = leader(0.95, 1.05, 1.85, 1.1)
        self.play(FadeIn(lab), Create(lead), run_time=0.5)
        answers = [("tight", "Tight budget.", (-2.2, 0.25)),
                   ("November", "November.", (-0.2, 0.25)),
                   ("2 + 1", "Two adults and a kid.", (-2.3, -0.35)),
                   ("slow", "Slow pace.", (-0.9, -0.35)),
                   ("fish market", "The fish market at opening.", (-1.25, -0.95))]
        for word, trig, slot in answers:
            c = chip(slot[0], slot[1] + 2.2, word)
            c.set_z_index(1)
            self.play(FadeIn(c), run_time=0.3)
            self.play(c.animate.shift(DOWN * 2.2), run_time=0.45)
            until(self, trig)
        finish(self)


class B04_TailoredPlan(Scene):
    """The brief feeds a full tailored plan; the old thin answer sits dimmed beside it."""

    def construct(self):
        thin = page(-4.7, 1.1, w=1.9, h=1.7, nlines=3, lw=0.5, dim=True)
        iso = Iso(ox=-4.3, oy=-1.9, s=0.7)
        back, front = iso.open_box(-1.3, -1.0, 0, 2.6, 2.0, 1.1)
        chips = VGroup(*[pill(px, py, 1.1, h=0.5, fill="#FFFFFF")
                         for px, py in [(-4.97, -1.97), (-4.0, -1.83), (-4.78, -1.66)]])
        for p in chips:
            p.set_stroke(INK, width=2)
        arrow = Line([-2.7, -1.3, 0], [-0.4, -0.5, 0], color=INK, stroke_width=5)
        self.play(FadeIn(thin), FadeIn(back), FadeIn(front), FadeIn(chips),
                  Create(arrow), run_time=0.8)
        until(self, "Now the plan comes back —")
        big = page(1.8, 0.4, w=3.6, h=3.1, nlines=0)
        self.play(GrowFromCenter(big), run_time=0.7)
        until(self, "and look at it.")
        lines1 = VGroup(*[Line([0.28, 1.45 - i * 0.32, 0], [3.09, 1.45 - i * 0.32, 0],
                               color=GHOST, stroke_width=5) for i in range(4)])
        self.play(Create(lines1), run_time=0.6)
        until(self, "Not a generic list:")
        lines2 = VGroup(*[Line([0.28, 0.17 - i * 0.32, 0], [3.09, 0.17 - i * 0.32, 0],
                               color=GHOST, stroke_width=5) for i in range(4)])
        self.play(Create(lines2), run_time=0.6)
        until(self, "the fish market")
        lab = label("tailored plan", 1.8, -1.75)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "Same AI, same task.")
        chk = check(3.05, 1.5, s=0.32, color=TERRA, w=10)
        self.play(GrowFromCenter(chk), run_time=0.5)
        until(self, "The only thing")
        finish(self)


class B05_SecondDemo(Scene):
    """Second demo: a difficult email. The AI asks three questions, then the draft lands."""

    def construct(self):
        env = envelope(-3.4, 0.6)
        lab = label("difficult email", -3.4, -0.7)
        self.play(FadeIn(env), FadeIn(lab), run_time=0.6)
        until(self, "Second example —")
        bubbles = VGroup(*[qbubble(x, 1.3) for x in (-0.9, 0.3, 1.5)])
        self.play(*[FadeIn(b) for b in bubbles], lag_ratio=0.2, run_time=0.9)
        until(self, "So it asks first:")
        letter = page(3.6, 0.3, w=3.0, h=2.8, nlines=7)
        self.play(FadeIn(letter), run_time=0.6)
        until(self, "Three questions —")
        chk = check(3.6, 2.05, s=0.3, color=INK, w=9)
        self.play(GrowFromCenter(chk), run_time=0.5)
        until(self, "it was aimed.")
        finish(self)


class B06_SharpQuestions(Scene):
    """Sharpen the move: ask for questions that would change your answer."""

    def construct(self):
        lazy = qcard(-2.6, 0.7, w=2.6, h=1.1, word="favourite colour?", hl=False)
        strike = Line([-3.8, 1.0, 0], [-1.4, 0.4, 0], color="#8B8F96", stroke_width=5)
        self.play(FadeIn(lazy), Create(strike), run_time=0.6)
        until(self, "Sharpen the move:")
        sharp = qcard(2.4, 0.7, w=2.6, h=1.1, word="changes the answer?", hl=True)
        chk = check(3.3, 1.35, s=0.28, color=TERRA, w=9)
        self.play(FadeIn(sharp), GrowFromCenter(chk), run_time=0.7)
        until(self, "A sharp one pays you back.")
        lab = label("ask what changes the answer", 0, -1.9)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "skip any question")
        finish(self)


class B07_TheRule(Scene):
    """The rule of thumb: interview when the answer depends on you; skip for plain facts."""

    def construct(self):
        def task_card(x):
            return RoundedRectangle(width=3.4, height=2.6, corner_radius=0.3,
                                    fill_color="#FFFFFF", fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 0.4, 0])
        left, right = task_card(-2.6), task_card(2.6)
        t1 = T("your trip", size=36).move_to([-2.6, 1.05, 0])
        t2 = T("your email", size=36).move_to([-2.6, 0.25, 0])
        t3 = T("Tokyo time?", size=36).move_to([2.6, 1.05, 0])
        self.play(FadeIn(left), FadeIn(right), FadeIn(t1), FadeIn(t2), FadeIn(t3),
                  run_time=0.7)
        until(self, "The rule of thumb:")
        b1, b2 = qbubble(-3.3, -0.35, r=0.28), qbubble(-2.5, -0.35, r=0.28)
        chk = check(-1.75, -0.3, s=0.26, color=INK, w=8)
        self.play(FadeIn(b1), FadeIn(b2), GrowFromCenter(chk), run_time=0.7)
        until(self, "Your trip, your email,")
        arr = Line([1.85, 0.0, 0], [3.35, 0.0, 0], color=INK, stroke_width=5)
        lab2 = label("skip", 2.6, -1.35)
        self.play(Create(arr), FadeIn(lab2), run_time=0.5)
        until(self, "And skip it when it doesn't")
        lab1 = label("needs you", -2.6, -1.35)
        self.play(FadeIn(lab1), run_time=0.4)
        until(self, "Your context is the missing ingredient;")
        finish(self)
