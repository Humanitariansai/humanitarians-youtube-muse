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


# ═════════════════════════════ YOUR LANGUAGE COACH — scenes ═════════════════════════════
# 7 Manim scenes (B00–B06), one per body beat. Cast, kept whole film: your speech
# bubble (kraft), the coach's speech bubble (white, terracotta lamp), word pills,
# the terracotta caret + check, the rule card, the cafe awning + counter, hello pills.
# Labels sit beside objects (never inside, never on terracotta), type floor 32,
# all coords inside ±6.2 x / ±3.3 y. Every on-screen word is spoken in its beat
# (no French is voiced: the one French rule is stated in English for Kokoro).
# Every animation lands before mid−0.35 s or starts after mid+0.35 s (GATE T
# samples each clip at its midpoint), paced by until()/finish() against beat_sheet.json.
# Every scene adds at least one NEW shape after its first frame (Gate A).

config.pixel_width = 1920
config.pixel_height = 1080


def speech_bubble(x, y, w=3.2, h=2.0, fill=CARD, tail="left"):
    """A rounded speech bubble with a small tail. Tail points down-left or down-right."""
    b = RoundedRectangle(corner_radius=0.25, width=w, height=h, fill_color=fill,
                         fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    if tail == "left":
        t = Polygon([x - w / 2 + 0.25, y - h / 2 + 0.02, 0],
                    [x - w / 2 + 0.95, y - h / 2 + 0.02, 0],
                    [x - w / 2 + 0.30, y - h / 2 - 0.55, 0],
                    fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=3)
    else:
        t = Polygon([x + w / 2 - 0.95, y - h / 2 + 0.02, 0],
                    [x + w / 2 - 0.25, y - h / 2 + 0.02, 0],
                    [x + w / 2 - 0.30, y - h / 2 - 0.55, 0],
                    fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=3)
    return VGroup(b, t)


def coach_card(x, y, w=3.2, h=2.0):
    """The AI as language coach: white bubble, terracotta 'on' lamp."""
    b = speech_bubble(x, y, w, h, fill=CARD, tail="right")
    lamp = Dot([x + w / 2 - 0.45, y + h / 2 - 0.45, 0], radius=0.10, color=TERRA)
    return VGroup(b, lamp)


def wpill(x, y, s, size=32):
    """A white word pill carrying a short SPOKEN phrase. Ink outline so it reads on cream."""
    w = len(s) * 0.22 + 0.9
    p = RoundedRectangle(corner_radius=0.31, width=w, height=0.72, fill_color=CARD,
                         fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    t = T(s, size).move_to([x, y - 0.03, 0])
    return VGroup(p, t)


def hello_pill(x, y, s):
    """A small pill carrying one spoken greeting word."""
    return wpill(x, y, s, size=36)


def caret(x, y, s=0.32, color=TERRA, w=7):
    """A small terracotta caret mark (a correction strike)."""
    return VGroup(Line([x - s, y - s * 0.6, 0], [x, y + s * 0.45, 0], color=color, stroke_width=w),
                  Line([x, y + s * 0.45, 0], [x + s, y - s * 0.6, 0], color=color, stroke_width=w))


def squiggle(x, y, wdt=1.5, color=TERRA):
    """A gentle terracotta strike-through wave (a stumble, not a failure)."""
    pts = [Line([x - wdt / 2 + i * wdt / 4, y + (0.12 if i % 2 == 0 else -0.12), 0],
                [x - wdt / 2 + (i + 1) * wdt / 4, y + (-0.12 if i % 2 == 0 else 0.12), 0],
                color=color, stroke_width=5) for i in range(4)]
    return VGroup(*pts)


def awning(x, y, w=3.8):
    """A kraft cafe awning: slanted canopy + ink posts, one terracotta seal dot."""
    canopy = Polygon([x - w / 2, y, 0], [x + w / 2, y, 0],
                     [x + w / 2 - 0.35, y - 0.55, 0], [x - w / 2 - 0.35, y - 0.55, 0],
                     fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    seal = Dot([x, y - 0.28, 0], radius=0.09, color=TERRA)
    post_l = Line([x - w / 2 + 0.1, y - 0.55, 0], [x - w / 2 + 0.1, y - 2.4, 0], color=INK, stroke_width=4)
    post_r = Line([x + w / 2 - 0.45, y - 0.55, 0], [x + w / 2 - 0.45, y - 2.4, 0], color=INK, stroke_width=4)
    return VGroup(canopy, seal, post_l, post_r)


class B00_Coach(Scene):
    def construct(self):
        coach = coach_card(2.7, 0.7)
        clabel = T("coach", 32).move_to([5.15, 0.7, 0])
        you = speech_bubble(-2.7, -0.7, w=3.0, h=1.8, fill=BOX_TOP, tail="left")
        ylabel = T("you", 32).move_to([-5.05, -0.7, 0])
        d1 = Dot([-1.1, 0.35, 0], radius=0.10, color=TERRA)
        d2 = Dot([-0.3, 0.55, 0], radius=0.10, color=TERRA)
        d3 = Dot([0.5, 0.72, 0], radius=0.10, color=TERRA)
        back = Dot([1.1, 0.35, 0], radius=0.10, color=TERRA)
        self.play(FadeIn(coach, shift=DOWN * 0.8), run_time=1.2)
        self.play(FadeIn(clabel, shift=LEFT * 0.2), run_time=0.8)
        until(self, "This bubble is you", lead=0.2)
        self.play(FadeIn(you, shift=UP * 0.6), FadeIn(ylabel, shift=RIGHT * 0.2), run_time=1.2)
        until(self, "just start talking", lead=2.6)
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3), run_time=1.0)
        until(self, "The conversation is the lesson", lead=0.8)
        self.play(FadeIn(back, shift=LEFT * 0.3), run_time=0.8)
        finish(self)


class B01_Patience(Scene):
    def construct(self):
        coach = coach_card(2.7, 0.7)
        clabel = T("coach", 32).move_to([5.15, 0.7, 0])
        you = speech_bubble(-2.7, -0.7, w=3.0, h=1.8, fill=BOX_TOP, tail="left")
        ylabel = T("you", 32).move_to([-5.05, -0.7, 0])
        # three wordless try-pills: the stumbles are motion, not words
        tries = VGroup(*[pill(-0.6, 1.75 - i * 1.05, 2.2) for i in range(3)])
        sq1 = squiggle(-0.6, 1.75)
        sq2 = squiggle(-0.6, 0.70)
        tick = check(-0.6, -0.35, s=0.30, color=TERRA, w=8)
        tag = T("no clock", 32).move_to([2.7, -1.75, 0])
        self.play(FadeIn(coach), FadeIn(clabel), FadeIn(you), FadeIn(ylabel), run_time=1.2)
        until(self, "you would be embarrassed to stumble", lead=1.4)
        self.play(FadeIn(tries[0], shift=RIGHT * 0.4), run_time=0.9)
        self.play(Create(sq1), run_time=0.7)
        until(self, "you try the sentence a third time", lead=2.2)
        self.play(FadeIn(tries[1], shift=RIGHT * 0.4), run_time=0.9)
        self.play(Create(sq2), run_time=0.7)
        until(self, "the coach just waits", lead=0.6)
        self.play(FadeIn(tries[2], shift=RIGHT * 0.4), run_time=0.9)
        self.play(GrowFromCenter(tick), run_time=0.7)
        until(self, "There is no clock", lead=0.2)
        self.play(FadeIn(tag, shift=UP * 0.2), run_time=0.8)
        finish(self)


class B02_Correction(Scene):
    def construct(self):
        coach = coach_card(2.7, 0.7)
        clabel = T("coach", 32).move_to([5.15, 0.7, 0])
        you = speech_bubble(-2.7, -0.7, w=3.0, h=1.8, fill=BOX_TOP, tail="left")
        ylabel = T("you", 32).move_to([-5.05, -0.7, 0])
        wrong = wpill(-0.8, 0.9, "I am twelve")
        mark = caret(-0.8, 1.45)
        fixed = wpill(-1.2, -0.75, "I have twelve years")
        tick = check(1.5, -0.75, s=0.26, color=TERRA, w=8)
        tag = T("instant", 32).move_to([-0.8, 2.35, 0])
        self.play(FadeIn(coach), FadeIn(clabel), FadeIn(you), FadeIn(ylabel), run_time=1.0)
        until(self, "You say: I am twelve", lead=2.0)
        self.play(FadeIn(wrong, shift=RIGHT * 0.5), run_time=0.8)
        until(self, "Wrong verb", lead=1.0)
        self.play(GrowFromCenter(mark), run_time=0.4)
        self.play(FadeIn(fixed, shift=RIGHT * 0.5), GrowFromCenter(tick), run_time=0.7)
        until(self, "settle into a habit", lead=0.2)
        self.play(FadeIn(tag, shift=DOWN * 0.2), run_time=0.8)
        finish(self)


class B03_Rule(Scene):
    def construct(self):
        coach = coach_card(2.7, 0.7)
        clabel = T("coach", 32).move_to([5.15, 0.7, 0])
        fixed = wpill(-2.9, 0.9, "I have twelve years")
        tick = check(-0.1, 0.9, s=0.26, color=TERRA, w=8)
        card = RoundedRectangle(corner_radius=0.2, width=5.2, height=1.6, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0.9, -1.3, 0])
        ruleline = T("I have twelve years", 34).move_to([0.9, -1.25, 0])
        rlabel = T("the rule", 32).move_to([0.9, -2.55, 0])
        self.play(FadeIn(coach), FadeIn(clabel), FadeIn(fixed), GrowFromCenter(tick), run_time=1.4)
        until(self, "tells you the rule", lead=0.8)
        self.play(GrowFromCenter(card), run_time=1.0)
        until(self, "You say I have twelve years", lead=0.0)
        self.play(FadeIn(ruleline, shift=UP * 0.15), run_time=0.8)
        until(self, "every sentence after it", lead=0.6)
        self.play(FadeIn(rlabel, shift=UP * 0.15), run_time=0.8)
        finish(self)


class B04_Roleplay(Scene):
    def construct(self):
        coach = coach_card(2.7, 1.3, w=3.2, h=1.8)
        counter = RoundedRectangle(corner_radius=0.15, width=3.6, height=0.8, fill_color=BOX_L,
                                   fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([2.7, -0.5, 0])
        shade = awning(2.7, 2.9)
        clabel = T("cafe", 32).move_to([5.15, 1.3, 0])
        you = speech_bubble(-3.1, -1.1, w=2.8, h=1.7, fill=BOX_TOP, tail="left")
        ylabel = T("you", 32).move_to([-5.3, -1.1, 0])
        order = wpill(-2.2, 0.4, "coffee", size=30)
        reply = pill(-1.4, -0.7, 1.5, fill=CARD)
        dot_r = Dot([-1.4, -0.7, 0], radius=0.10, color=TERRA)
        self.play(FadeIn(counter), FadeIn(coach), FadeIn(you), FadeIn(ylabel), run_time=1.4)
        until(self, "we are in a cafe in Paris", lead=1.2)
        self.play(FadeIn(shade, shift=DOWN * 0.5), run_time=1.0)
        self.play(FadeIn(clabel, shift=LEFT * 0.2), run_time=0.8)
        until(self, "ordering coffee", lead=2.4)
        self.play(MoveAlongPath(order, Line(np.array([-2.2, 0.4, 0]), np.array([1.1, 0.4, 0]))), run_time=1.4)
        until(self, "someone playing along", lead=1.2)
        self.play(FadeIn(reply, shift=LEFT * 0.3), FadeIn(dot_r), run_time=0.9)
        finish(self)


class B05_Level(Scene):
    def construct(self):
        coach = coach_card(2.7, 0.7)
        clabel = T("coach", 32).move_to([5.15, 0.7, 0])
        you = speech_bubble(-2.7, -0.7, w=3.0, h=1.8, fill=BOX_TOP, tail="left")
        ylabel = T("you", 32).move_to([-5.05, -0.7, 0])
        slow = wpill(-0.6, 1.9, "slower")
        long_b = speech_bubble(2.7, -1.5, w=3.4, h=1.2, fill=CARD, tail="right")
        long_lines = VGroup(*[Line([1.35, -1.25 - i * 0.3, 0], [4.05, -1.25 - i * 0.3, 0],
                                   color=GHOST, stroke_width=5) for i in range(3)])
        short_b = speech_bubble(2.7, -1.5, w=1.9, h=1.2, fill=CARD, tail="right")
        sdot = Dot([2.7, -1.5, 0], radius=0.10, color=TERRA)
        llabel = T("your level", 32).move_to([2.7, -2.6, 0])
        self.play(FadeIn(coach), FadeIn(clabel), FadeIn(you), FadeIn(ylabel), run_time=1.2)
        until(self, "Say slower", lead=1.0)
        self.play(FadeIn(slow, shift=RIGHT * 0.4), run_time=0.9)
        until(self, "it slows down", lead=1.2)
        self.play(FadeIn(long_b), FadeIn(long_lines), run_time=0.8)
        self.play(FadeOut(long_b), FadeOut(long_lines), run_time=0.8)
        self.play(GrowFromCenter(short_b), FadeIn(sdot), run_time=0.9)
        until(self, "raise the level", lead=0.0)
        self.play(FadeIn(llabel, shift=UP * 0.15), run_time=0.8)
        finish(self)


class B06_Languages(Scene):
    def construct(self):
        coach = coach_card(0.0, 0.5)
        clabel = T("coach", 32).move_to([2.7, 0.5, 0])
        p1 = hello_pill(-3.6, 1.5, "hola")
        p2 = hello_pill(3.6, 1.5, "bonjour")
        p3 = hello_pill(-3.6, -1.5, "konnichiwa")
        p4 = hello_pill(3.6, -1.5, "salaam")
        tag = T("name it", 32).move_to([0.0, -2.35, 0])
        tutor = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.4, fill_color=BOX_L,
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-4.4, -2.35, 0])
        tlabel = T("tutor", 32).move_to([-4.4, -1.35, 0])
        self.play(FadeIn(coach), FadeIn(clabel), run_time=1.2)
        until(self, "and it answers", lead=0.2)
        self.play(GrowFromCenter(p1), GrowFromCenter(p2), run_time=0.8)
        until(self, "Salaam", lead=0.2)
        self.play(GrowFromCenter(p3), GrowFromCenter(p4), run_time=0.8)
        self.play(FadeIn(tag, shift=UP * 0.15), run_time=0.8)
        until(self, "This film has a companion", lead=0.8)
        self.play(FadeIn(tutor, shift=RIGHT * 0.5), FadeIn(tlabel, shift=RIGHT * 0.3), run_time=1.0)
        finish(self)
