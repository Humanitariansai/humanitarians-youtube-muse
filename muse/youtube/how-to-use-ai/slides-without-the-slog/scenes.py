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

# ═════════════════════════════ FILM: slides-without-the-slog ═════════════════════════════
# Show-tell body scenes: one isometric drawing per beat, Claude palette.
# Cast, kept the same all film: the messy notes page (rough input), the
# slide card (white card, ink headline bar, ghost text lines), the wall
# card (a slide drowned in text lines), the outline card (numbered
# one-line-per-slide rows), the notes card (speaker notes), ink arrows
# (the flow from notes to deck), terracotta checks (approvals) and flag
# dots (problems), deep-kraft sight lines (the room looking at the slide).
# Labels sit beside objects, never inside; text >= 32.
# Pacing is narration-driven via until()/finish() from the kit above.
# Class names are literal `class BNN_Name(Scene):` so run.sh finds them.
# Layout: every explicit coordinate was hand-checked against the
# ±6.2 × ±3.3 safe area (iso screen-x = (x−y)·0.866, screen-y = (x+y)·0.5 + oy).

KRAFT_DK = "#9C8462"  # deep kraft: sight lines that must not fuse into ink blobs


def _shadow(x, y, w, h):
    return Ellipse(width=w, height=h, color=GHOST, fill_opacity=1, stroke_width=0).move_to([x, y, 0.0])


def _slide(iso, x0, y0, w=2.6, d=1.7, n_lines=4, headline=True):
    """A clean slide card: white slab, one ink headline bar, a few ghost text lines. Returns (group, lines)."""
    card = iso.box(x0, y0, 0.0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = 0.10
    parts = [card]
    if headline:
        hb = Line(iso.p(x0 + 0.25, y0 + d - 0.42, zt), iso.p(x0 + w * 0.72, y0 + d - 0.42, zt),
                  color=INK, stroke_width=7)
        parts.append(hb)
    lines = []
    for i in range(n_lines):
        f = 0.30 + i * (0.52 / max(n_lines - 1, 1))
        ln = Line(iso.p(x0 + 0.25, y0 + d * f, zt), iso.p(x0 + w - 0.25, y0 + d * f, zt),
                  color=GHOST, stroke_width=4)
        lines.append(ln)
        parts.append(ln)
    return VGroup(*parts), lines


def _wall(iso, x0, y0, w=2.8, d=3.4, n_lines=9):
    """A wall-of-text slide: dense grey lines filling the card. Returns (group, lines)."""
    card = iso.box(x0, y0, 0.0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = 0.10
    lines = []
    for i in range(n_lines):
        f = 0.12 + i * (0.76 / (n_lines - 1))
        ln = Line(iso.p(x0 + 0.2, y0 + d * f, zt), iso.p(x0 + w - 0.2, y0 + d * f, zt),
                  color=BAR2 if i % 2 else GHOST, stroke_width=4)
        lines.append(ln)
    return VGroup(card, *lines), lines


def _notes(iso, x0, y0, w=2.0, d=2.4):
    """The messy notes page: white slab with short scattered scribble fragments."""
    slab = iso.box(x0, y0, 0.0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = 0.10
    frags = [((0.20, 0.78, 0.52), (0.22, 0.72, 0.52)), ((0.55, 0.70, 0.40), (0.57, 0.64, 0.40)),
             ((0.30, 0.58, 0.60), (0.32, 0.53, 0.60)), ((0.62, 0.50, 0.30), (0.64, 0.45, 0.30)),
             ((0.25, 0.40, 0.45), (0.27, 0.34, 0.45)), ((0.55, 0.32, 0.55), (0.57, 0.27, 0.55)),
             ((0.35, 0.20, 0.40), (0.37, 0.14, 0.40))]
    lines = VGroup(*[Line(iso.p(x0 + w * fx, y0 + d * fy, zt + dz), iso.p(x0 + w * gx, y0 + d * gy, zt + dz),
                         color=DIM, stroke_width=4)
                     for (fx, fy, dz), (gx, gy, _) in frags])
    dot = Dot(iso.p(x0 + 0.25, y0 + d * 0.88, zt), radius=0.06, color=TERRA)
    return VGroup(slab, lines, dot)


def _outline_card(iso, x0, y0, w=2.6, d=3.6, rows=None):
    """The skeleton: a white card with numbered one-line-per-slide rows. Returns (group, rows)."""
    if rows is None:
        rows = ["the opening", "the problem", "the plan", "the budget", "the ask"]
    card = iso.box(x0, y0, 0.0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    rws = []
    for i, name in enumerate(rows):
        yy = y0 + d - 0.60 - i * (d - 1.0) / (len(rows) - 1)
        t = T(f"{i + 1}  {name}", size=32)
        p = iso.p(x0 + 0.28, yy, 0.10)
        t.move_to([p[0] + t.width / 2, p[1], 0.0])
        rws.append(t)
    return VGroup(card, *rws), rws


def _flag(iso, x, y, w, d, r=0.11):
    """A terracotta flag dot on a card: something the voice calls out."""
    return Dot(iso.p(x + w / 2, y + d / 2, 0.12), radius=r, color=TERRA)


def _arrow(x1, y1, x2, y2):
    return Arrow([x1, y1, 0.0], [x2, y2, 0.0], color=INK, stroke_width=5, buff=0.05)


class B00_Goal(Scene):
    def construct(self):
        iso = Iso(0, 0.6, 1.0)
        shadow = _shadow(-0.3, -2.5, 11.2, 1.3)
        notes = _notes(iso, -5.5, -0.9, 2.0, 2.4)
        a, _ = _slide(iso, -0.3, 0.7, 1.5, 1.0, 2)
        b, _ = _slide(iso, 1.2, -0.8, 1.5, 1.0, 2)
        c, _ = _slide(iso, 2.5, -2.1, 1.5, 1.0, 2)
        cards = VGroup(a, b, c)
        arrow = _arrow(-2.1, -0.9, -1.8, 0.7)
        label = T("the goal", size=36).move_to([-4.6, 0.9, 0.0])
        leader = Line([-4.15, 0.72, 0.0], [-4.05, -0.15, 0.0], color=INK, stroke_width=3)
        chk = check(5.55, 1.75, s=0.2, color=TERRA)

        until(self, "Start with the goal")
        self.play(FadeIn(shadow), FadeIn(notes, shift=np.array([0.0, 1.8, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "a five-slide deck out")
        self.play(Create(arrow), run_time=0.4)
        self.play(*[FadeIn(k, shift=np.array([0.0, 1.2, 0.0])) for k in (a, b, c)], run_time=0.7, rate_func=ease_in)
        until(self, "No walls of text")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        until(self, "without the slog")
        self.play(FadeIn(chk), run_time=0.4)
        finish(self)


class B01_Walls(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(0, -2.6, 8.4, 1.3)
        back2, _ = _wall(iso, -1.1, -1.6, 2.8, 3.4, 9)
        back1, _ = _wall(iso, -1.3, -1.8, 2.8, 3.4, 9)
        wall, wlines = _wall(iso, -1.5, -2.0, 2.8, 3.4, 9)
        backs = VGroup(back2, back1)
        label = T("all at once", size=36).move_to([4.35, 2.25, 0.0])
        leader = Line([3.45, 2.1, 0.0], [2.9, 0.0, 0.0], color=INK, stroke_width=3)
        d1 = _flag(iso, -0.6, 0.2, 1.0, 0.6)
        d2 = _flag(iso, 0.0, -0.8, 1.0, 0.6)
        d3 = _flag(iso, -1.0, -1.5, 1.0, 0.6)

        until(self, "So he pasted the notes")
        self.play(FadeIn(shadow), FadeIn(wall, shift=np.array([0.0, 2.0, 0.0])), rate_func=ease_in, run_time=0.8)
        until(self, "every single one")
        self.play(FadeIn(backs), FadeIn(label), FadeIn(leader), run_time=0.6)
        until(self, "did not know what mattered")
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3), run_time=0.4)
        finish(self)


class B02_WhyRead(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(1.6, -2.4, 8.0, 1.3)
        wall, _ = _wall(iso, 0.4, -1.5, 3.2, 3.0, 8)
        dots = VGroup(*[Dot([x, y, 0.0], radius=0.16, color=INK)
                        for x, y in ((-4.6, 1.1), (-4.9, 0.1), (-4.3, -0.9))])
        eye = iso.p(0.4, 0.0, 0.10)
        sights = VGroup(*[Line([x, y, 0.0], [eye[0] - 0.15, eye[1], 0.0], color=KRAFT_DK, stroke_width=3)
                          for x, y in ((-4.6, 1.1), (-4.9, 0.1), (-4.3, -0.9))])
        label = T("walls get read", size=36).move_to([-4.35, 2.45, 0.0])
        leader = Line([-3.35, 2.28, 0.0], [-1.35, 1.25, 0.0], color=INK, stroke_width=3)

        until(self, "Here\u2019s why")
        self.play(FadeIn(shadow), FadeIn(wall, shift=np.array([0.0, 1.8, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "the room reads the slide")
        self.play(FadeIn(dots), run_time=0.4)
        until(self, "instead of listening to you")
        self.play(*[Create(s) for s in sights], run_time=0.6)
        until(self, "it cannot know what you would cut")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        finish(self)


class B03_Outline(Scene):
    def construct(self):
        iso = Iso(0, 0.3, 1.0)
        shadow = _shadow(0, -2.5, 7.4, 1.3)
        card, rows = _outline_card(iso, -1.3, -1.8, 2.6, 3.6)
        chk = check(2.15, 1.55, s=0.22, color=TERRA)
        label = T("move one: outline", size=36).move_to([-4.35, 2.5, 0.0])
        leader = Line([-3.3, 2.35, 0.0], [-2.6, 1.0, 0.0], color=INK, stroke_width=3)

        until(self, "Move one")
        self.play(FadeIn(shadow), FadeIn(card, shift=np.array([0.0, 1.8, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "one-line-per-slide skeleton")
        self.play(*[Create(r) for r in rows], run_time=0.7)
        until(self, "approve it")
        self.play(FadeIn(chk), run_time=0.4)
        until(self, "The outline is the contract")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        finish(self)


class B04_OneSlide(Scene):
    def construct(self):
        iso = Iso(0, 0.3, 1.0)
        shadow = _shadow(-0.8, -2.5, 10.2, 1.3)
        card, _ = _outline_card(iso, -1.3, -1.8, 2.6, 3.6)
        slide, _ = _slide(iso, 1.6, -1.35, 2.6, 1.7, 3)
        chk = check(5.0, 1.2, s=0.2, color=TERRA)
        arrow = _arrow(0.68, 0.85, 1.0, 0.85)
        label = T("move two: one slide", size=36).move_to([-4.35, 2.55, 0.0])
        leader = Line([-3.25, 2.4, 0.0], [-2.6, 0.95, 0.0], color=INK, stroke_width=3)
        self.add(shadow, card)

        until(self, "Move two")
        self.play(card.animate.shift(np.array([-2.4, 0.0, 0.0])),
                  FadeIn(slide, shift=np.array([0.0, 1.6, 0.0])), rate_func=ease_in, run_time=0.8)
        until(self, "with the outline beside it")
        self.play(Create(arrow), FadeIn(label), FadeIn(leader), run_time=0.6)
        until(self, "before slide two starts")
        self.play(FadeIn(chk), run_time=0.4)
        finish(self)


class B05_Polish(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(0, -2.6, 8.4, 1.2)
        slide, lines = _slide(iso, -1.4, -0.4, 2.8, 2.2, 6)
        ncard, _ = _slide(iso, -3.0, -3.3, 2.8, 1.1, 2, headline=False)
        nlabel = T("notes", size=32).move_to([3.55, -2.1, 0.0])
        nleader = Line([3.05, -2.1, 0.0], [2.82, -2.0, 0.0], color=INK, stroke_width=3)
        label = T("the polish: cut", size=36).move_to([-4.35, 2.45, 0.0])
        leader = Line([-3.25, 2.28, 0.0], [-1.35, 1.5, 0.0], color=INK, stroke_width=3)
        chk = check(2.05, 1.15, s=0.2, color=TERRA)
        self.add(shadow, slide[0], slide[1])

        until(self, "Then the polish")
        self.play(*[FadeIn(ln) for ln in lines], run_time=0.5)
        until(self, "cut the words")
        self.play(*[FadeOut(ln, shift=np.array([0.0, 0.8, 0.0])) for ln in lines], run_time=0.8)
        until(self, "into the speaker notes")
        self.play(FadeIn(ncard, shift=np.array([0.0, 1.0, 0.0])), FadeIn(nlabel), FadeIn(nleader),
                  run_time=0.6, rate_func=ease_in)
        until(self, "the lines only you see")
        self.play(FadeIn(label), FadeIn(leader), FadeIn(chk), run_time=0.5)
        finish(self)


class B06_BackRow(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(0, -2.5, 8.4, 1.3)
        slide, _ = _slide(iso, -1.4, -0.9, 2.8, 1.8, 3)
        self.add(shadow, slide)
        small = slide.copy().scale(0.42).move_to([3.9, -0.9, 0.0])
        chk = check(5.35, 0.15, s=0.2, color=TERRA)
        label = T("the back-row test", size=36).move_to([3.55, 2.35, 0.0])
        leader = Line([3.45, 2.15, 0.0], [3.75, -0.1, 0.0], color=INK, stroke_width=3)

        until(self, "Last move")
        self.wait(0.3)
        until(self, "Step back from the screen")
        self.play(FadeOut(slide), FadeIn(small), run_time=0.7)
        until(self, "cannot catch the headline")
        self.play(FadeIn(chk), run_time=0.4)
        until(self, "Cut again")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        finish(self)


class B07_SideBySide(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(0, -2.6, 11.4, 1.3)
        w1, _ = _wall(iso, -4.6, 0.0, 1.6, 1.8, 7)
        w2, _ = _wall(iso, -1.0, 0.0, 1.6, 1.8, 7)
        left = VGroup(w1, w2)
        llabel = T("one giant prompt", size=36).move_to([-3.75, 1.6, 0.0])
        lleader = Line([-3.5, 1.42, 0.0], [-4.0, -0.2, 0.0], color=INK, stroke_width=3)
        pages = VGroup(*[iso.page(2.6, -2.3, i * 0.16, 1.8, 1.2) for i in range(4)])
        chk = check(3.2, 2.5, s=0.2, color=TERRA)
        rlabel = T("outline, slides, polish", size=32).move_to([3.9, 3.0, 0.0])

        until(self, "On the left")
        self.play(FadeIn(shadow), *[FadeIn(k, shift=np.array([0.0, 1.4, 0.0])) for k in (w1, w2)],
                  run_time=0.7, rate_func=ease_in)
        until(self, "one-prompt deck")
        self.play(FadeIn(llabel), FadeIn(lleader), run_time=0.4)
        until(self, "On the right")
        self.play(*[FadeIn(p, shift=np.array([0.0, 1.4, 0.0])) for p in pages],
                  run_time=0.7, rate_func=ease_in)
        until(self, "polished at the end")
        self.play(FadeIn(rlabel), FadeIn(chk), run_time=0.5)
        finish(self)


class B08_Habit(Scene):
    def construct(self):
        iso = Iso(0, 0.0, 1.0)
        shadow = _shadow(0, -2.5, 9.4, 1.3)
        card = iso.box(-1.7, -1.3, 0.0, 3.4, 2.6, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        names = ["outline first", "one slide per prompt", "polish last"]
        rows = []
        for i, name in enumerate(names):
            yy = -1.3 + 2.6 - 0.62 - i * 0.68
            t = T(name, size=32)
            p = iso.p(-1.7 + 0.32, yy, 0.10)
            t.move_to([p[0] + t.width / 2, p[1], 0.0])
            rows.append(t)
        chk = check(2.95, 0.6, s=0.22, color=TERRA)

        until(self, "Make it a habit")
        self.play(FadeIn(shadow), FadeIn(card, shift=np.array([0.0, 1.8, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "Outline first")
        self.play(FadeIn(rows[0]), run_time=0.3)
        until(self, "One slide per prompt")
        self.play(FadeIn(rows[1]), run_time=0.3)
        until(self, "Polish last")
        self.play(FadeIn(rows[2]), run_time=0.3)
        until(self, "three moves")
        self.play(FadeIn(chk), run_time=0.4)
        finish(self)
