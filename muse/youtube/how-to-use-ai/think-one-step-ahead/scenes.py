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

# ═════════════════════════════ film helpers ═════════════════════════════
# Flat-drawn Claude window + paper cast (Claude palette). Labels sit beside
# objects with a leader line (never inside an outline, never on terracotta).
WIN_W, WIN_H, WIN_CY = 7.6, 4.4, -0.15


def _window():
    win = RoundedRectangle(width=WIN_W, height=WIN_H, corner_radius=0.18,
                           fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0, WIN_CY, 0])
    bar = Rectangle(width=WIN_W, height=0.8, fill_color=DARK_TOP, fill_opacity=1,
                    stroke_color=INK, stroke_width=4).move_to([0, WIN_CY + WIN_H / 2 - 0.4, 0])
    title = T("Claude", size=40, color=CARD).move_to([0, WIN_CY + WIN_H / 2 - 0.4, 0])
    return win, bar, title


def _slip(x, y):
    pg = RoundedRectangle(width=2.4, height=0.8, corner_radius=0.08, fill_color="#FFFFFF",
                          fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    ls = VGroup(*[Line([x - 0.9, y + 0.15 - 0.3 * i, 0], [x + 0.9, y + 0.15 - 0.3 * i, 0],
                       color=GHOST, stroke_width=4) for i in range(2)])
    return VGroup(pg, ls)


def _answer_page(x, y, w=5.6, h=2.3):
    return RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])


def _word(x, y, w=0.52):
    return RoundedRectangle(width=w, height=0.17, corner_radius=0.085, fill_color=BAR2,
                            fill_opacity=1, stroke_width=0).move_to([x, y, 0])


def _word_rows(cx, top_y, rows=4, cols=5, dx=1.0, dy=0.42, w=0.52):
    x0 = cx - (cols - 1) * dx / 2
    return [VGroup(*[_word(x0 + c * dx, top_y - r * dy, w) for c in range(cols)]) for r in range(rows)]


def _xmark(x, y, s=0.16, color=INK, w=6):
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w))


def _label(text, x, y, size=34):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def _leader(x1, y1, x2, y2):
    return Line([x1, y1, 0], [x2, y2, 0], color=DIM, stroke_width=2)


# ═════════════════════════════ B00 — one word at a time ═════════════════════════════
class B00_Window(Scene):
    def construct(self):
        win, bar, title = _window()
        self.play(FadeIn(win), FadeIn(bar), FadeIn(title), run_time=0.8)
        until(self, "Claude does not think")
        slip = _slip(0, 0.72)
        self.play(FadeIn(slip), run_time=0.5)
        until(self, "one word at a time")
        page = _answer_page(0, -1.15)
        self.play(FadeIn(page), run_time=0.5)
        rows = _word_rows(0, -0.5, rows=4, cols=5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.35)
        until(self, "no going back")
        lab = _label("word by word", -4.9, -1.15)
        ld = _leader(-2.8, -1.15, -3.4, -1.15)
        self.play(FadeIn(lab), FadeIn(ld), run_time=0.5)
        finish(self)


# ═════════════════════════════ B01 — before: the first word leads ═════════════════════════════
class B01_Before(Scene):
    def construct(self):
        win, bar, title = _window()
        slip = _slip(0, 0.72)
        page = _answer_page(0, -1.15)
        rows = _word_rows(0, -0.5, rows=4, cols=5)
        self.add(win, bar, title, slip, page, rows[0], rows[1])  # two lines printed so far
        until(self, "The very first line")
        dot = Dot([-2.0, -0.5, 0], radius=0.14, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.5)
        until(self, "every word after it")
        bracket = ArcBetweenPoints([-1.55, -0.5, 0], [2.45, -0.5, 0], angle=0.6,
                                   color=INK, stroke_width=5)
        self.play(Create(bracket), run_time=0.7)
        self.play(FadeIn(rows[2]), FadeIn(rows[3]), run_time=0.6)
        until(self, "It defends it")
        lab = _label("the first word leads", 4.6, -1.15)
        ld = _leader(2.8, -1.15, 3.35, -1.15)
        self.play(FadeIn(lab), FadeIn(ld), run_time=0.5)
        finish(self)


# ═════════════════════════════ B02 — the thinking page ═════════════════════════════
class B02_Scratchpad(Scene):
    def construct(self):
        win, bar, title = _window()
        think = RoundedRectangle(width=2.6, height=2.9, corner_radius=0.1, fill_color="#FFFFFF",
                                 fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([-1.55, -0.55, 0])
        think_lab = _label("thinking", -1.55, 0.95, size=32)
        slot = Rectangle(width=2.6, height=2.9, fill_opacity=0, stroke_color=DIM, stroke_width=2).move_to([1.55, -0.55, 0])
        slot_lab = _label("answer", 1.55, 0.95, size=32)
        self.play(FadeIn(win), FadeIn(bar), FadeIn(title), FadeIn(think), FadeIn(think_lab),
                  FadeIn(slot), FadeIn(slot_lab), run_time=0.8)
        until(self, "It tries one idea")
        idea_ys = [0.3, -0.1, -0.5, -0.9]
        ideas = VGroup(*[Line([-2.5, y, 0], [-0.6, y, 0], color=GHOST, stroke_width=5) for y in idea_ys])
        for line in ideas:
            self.play(FadeIn(line), run_time=0.3)
        until(self, "crosses it out")
        x = _xmark(-1.55, -0.1)
        self.play(FadeIn(x), run_time=0.5)
        until(self, "catches the mistake")
        fix = Line([-2.5, -1.3, 0], [-0.9, -1.3, 0], color=BAR1, stroke_width=5)
        self.play(FadeIn(fix), run_time=0.5)
        until(self, "before one word of the answer exists")
        lab = _label("the thinking page", 0, -2.95)
        self.play(FadeIn(lab), run_time=0.5)
        finish(self)


# ═════════════════════════════ B03 — after: the answer, checked ═════════════════════════════
class B03_After(Scene):
    def construct(self):
        win, bar, title = _window()
        think = RoundedRectangle(width=2.2, height=2.5, corner_radius=0.1, fill_color="#FFFFFF",
                                 fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([-2.3, -0.55, 0])
        think_lab = _label("thinking", -2.3, 0.85, size=32)
        x = _xmark(-2.3, -0.65)
        self.add(win, bar, title, think, think_lab, x)  # the crossed-out thinking, kept on stage
        until(self, "written once")
        page = _answer_page(1.15, -0.55, w=3.4, h=2.9)
        self.play(FadeIn(page), run_time=0.5)
        rows = _word_rows(1.15, 0.35, rows=3, cols=4, dx=0.75, w=0.45)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
        until(self, "Better answer")
        chk = check(3.35, 0.75, s=0.22, color=TERRA, w=8)
        self.play(GrowFromCenter(chk), run_time=0.5)
        until(self, "thought before it spoke")
        lab = _label("the answer", 0, -2.95)
        self.play(FadeIn(lab), run_time=0.5)
        finish(self)


# ═════════════════════════════ B04 — the scratch-paper rule ═════════════════════════════
class B04_When(Scene):
    def construct(self):
        until(self, "scratch-paper rule")
        cards, labs = [], []
        for cx, name in [(-3.3, "a lookup"), (0, "a choice"), (3.3, "a math problem")]:
            cards.append(RoundedRectangle(width=2.5, height=1.5, corner_radius=0.12, fill_color=CARD,
                                          fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, 0.3, 0]))
            labs.append(_label(name, cx, -0.95, size=32))
        rule = _label("the scratch-paper rule", 0, 2.6)
        self.play(*[FadeIn(c) for c in cards], *[FadeIn(l) for l in labs], FadeIn(rule), run_time=0.8)
        until(self, "ask Claude to think first")
        pages = []
        for cx in (0, 3.3):
            pg = RoundedRectangle(width=1.7, height=1.1, corner_radius=0.08, fill_color="#FFFFFF",
                                  fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([cx, 0.3, 0])
            pages.append(pg)
            self.play(FadeIn(pg), run_time=0.5)
            chk = check(cx + 0.45, 0.55, s=0.16, color=INK, w=7)
            self.play(GrowFromCenter(chk), run_time=0.4)
        until(self, "extra words for nothing")
        finish(self)


# ═════════════════════════════ B05 — tomorrow's answer, today ═════════════════════════════
class B05_Ahead(Scene):
    def construct(self):
        win, bar, title = _window()
        self.play(FadeIn(win), FadeIn(bar), FadeIn(title), run_time=0.8)
        until(self, "today's answer")
        slip = _slip(0, 0.72)
        self.play(FadeIn(slip), run_time=0.5)
        until(self, "what to pack")
        page = _answer_page(0, -0.75, h=1.5)
        self.play(FadeIn(page), run_time=0.5)
        rows = _word_rows(0, -0.4, rows=2, cols=5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
        until(self, "what to buy before I leave")
        nxt = RoundedRectangle(width=5.6, height=0.55, corner_radius=0.1, fill_color="#FFFFFF",
                               fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([0, -1.9, 0])
        self.play(FadeIn(nxt), run_time=0.5)
        dot = Dot([2.2, -1.9, 0], radius=0.13, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.5)
        until(self, "tomorrow's answer, today")
        lab = _label("tomorrow's answer", 0, -2.95)
        ld = _leader(0, -2.18, 0, -2.6)
        self.play(FadeIn(lab), FadeIn(ld), run_time=0.5)
        finish(self)
