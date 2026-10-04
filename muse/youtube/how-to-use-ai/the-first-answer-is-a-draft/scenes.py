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


# ═════════════════════════════ "The first answer is a draft" — scenes ═════════════════════════════
# Cast: one object the whole film — the draft page (a standing white card with text lines
# and a kraft DRAFT n tag). B02→B05 mutate the same page so the viewer watches it evolve.


def standing_card(iso, x, y, z, w, h):
    """A card standing upright in the x-z plane, with a thin iso side edge for depth."""
    x1, z1 = x + w, z + h
    face = iso.quad([(x, y, z), (x1, y, z), (x1, y, z1), (x, y, z1)], PAGE_TOP)
    edge = iso.quad([(x1, y, z), (x1, y + 0.16, z), (x1, y + 0.16, z1), (x1, y, z1)], PAGE_R, sw=2)
    return VGroup(face, edge)


def card_line(iso, x0, x1, z, color, y=0.02, w=5):
    """A text line on the card face, drawn slightly in front of the face plane."""
    return Line(iso.p(x0, y, z), iso.p(x1, y, z), color=color, stroke_width=w)


def draft_tag(text, x, y, w=1.7, h=0.55, fill=BOX_TOP):
    """A kraft tag clipped onto the page corner (the DRAFT n stamp)."""
    g = RoundedRectangle(width=w, height=h, corner_radius=h / 3, fill_color=fill, fill_opacity=1,
                         stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    t = T(text, size=32).move_to([x, y, 0])
    return VGroup(g, t)


def pushback_pill(text, x, y, w):
    """The viewer's pushback: a white pill with an ink outline, ink text."""
    g = pill(x, y, w)
    g.set_stroke(INK, width=3)
    t = T(text, size=32).move_to([x, y - 0.02, 0])
    return VGroup(g, t)


def label_right(text, x, y, lx0, size=36):
    """An ink label at (x, y) with a leader line from lx0 — 0.3+ gap kept."""
    t = T(text, size=size).move_to([x, y, 0])
    lead = Line([lx0, y, 0], [x - 1.05, y, 0], color=INK, stroke_width=3)
    return VGroup(lead, t)


# Page geometry shared by every beat: card in iso coords, six line heights (z), top → bottom.
PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H = -1.1, 0.0, 0.0, 2.2, 2.6
LINE_ZS = [2.05, 1.72, 1.39, 1.06, 0.73, 0.40]


class B00_DraftOne(Scene):
    def construct(self):
        iso = Iso(0.0, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        lines = VGroup(*[card_line(iso, -0.75, 0.75, z, GHOST) for z in LINE_ZS[:5]])
        dtag = draft_tag("DRAFT 1", -1.50, 2.45)
        lab = label_right("draft one", 3.15, 0.40, 1.20)
        self.play(FadeIn(page), run_time=0.6)
        self.play(FadeIn(VGroup(lines, dtag)), run_time=0.6)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "Just the first try")
        finish(self)


class B01_TooEarly(Scene):
    def construct(self):
        iso = Iso(0.0, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        lines = VGroup(*[card_line(iso, -0.75, 0.75, z, GHOST) for z in LINE_ZS[:5]])
        dtag = draft_tag("DRAFT 1", -1.50, 2.45)
        stamp_body = RoundedRectangle(width=2.2, height=0.9, corner_radius=0.2, fill_color=CARD,
                                      fill_opacity=1, stroke_color=TERRA, stroke_width=6)
        stamp_word = T("FINAL", size=44, bold=True).move_to([0, 2.9, 0])
        stamp = VGroup(stamp_body.move_to([0, 2.9, 0]), stamp_word)
        lab = label_right("too early", 3.15, 1.50, 1.30)
        self.play(FadeIn(VGroup(page, lines, dtag)), run_time=0.6)
        self.play(FadeIn(stamp), run_time=0.3)
        self.play(stamp.animate.shift(DOWN * 1.0), rate_func=ease_in, run_time=0.45)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "doesn't know your life yet")
        finish(self)


class B02_FirstTry(Scene):
    def construct(self):
        iso = Iso(-1.2, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        dtag = draft_tag("DRAFT 1", -2.70, 2.45)
        qpill = pushback_pill("plan dinners", -1.20, 2.90, 2.6)
        lines = [card_line(iso, -0.75, 0.75, z, GHOST) for z in LINE_ZS]
        lab = label_right("draft 1", 2.60, 0.30, 0.10)
        self.play(FadeIn(VGroup(page, dtag, qpill)), run_time=0.6)
        self.play(FadeIn(VGroup(*lines[:3])), run_time=0.5)
        self.play(FadeIn(VGroup(*lines[3:])), run_time=0.5)
        self.play(FadeIn(lab), run_time=0.3)
        until(self, "dishes you'll never cook")
        finish(self)


class B03_Shorter(Scene):
    def construct(self):
        iso = Iso(-1.2, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        dtag = draft_tag("DRAFT 1", -2.70, 2.45)
        qpill = pushback_pill("plan dinners", -1.20, 2.90, 2.6)
        lines = [card_line(iso, -0.75, 0.75, z, GHOST) for z in LINE_ZS]
        ppill = pushback_pill("shorter", -4.05, 0.60, 1.9)
        plab = T("pushback", size=32).move_to([-4.05, -0.25, 0])
        xs = VGroup(*[VGroup(
            Line(iso.p(-0.15, 0.04, z + 0.07), iso.p(0.15, 0.04, z - 0.07), color=INK, stroke_width=6),
            Line(iso.p(-0.15, 0.04, z - 0.07), iso.p(0.15, 0.04, z + 0.07), color=INK, stroke_width=6))
            for z in LINE_ZS[3:]])
        self.play(FadeIn(VGroup(page, dtag, qpill, VGroup(*lines))), run_time=0.6)
        self.play(FadeIn(VGroup(ppill, plab)), run_time=0.4)
        self.play(Create(xs), run_time=0.5)
        self.play(FadeOut(VGroup(*lines[3:])), FadeOut(xs), run_time=0.4)
        until(self, "half the words")
        finish(self)


class B04_Concrete(Scene):
    def construct(self):
        iso = Iso(-1.2, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        dtag = draft_tag("DRAFT 2", -2.70, 2.45)
        qpill = pushback_pill("plan dinners", -1.20, 2.90, 2.6)
        ghosts = VGroup(*[card_line(iso, -0.75, 0.75, z, GHOST) for z in LINE_ZS[:3]])
        sharp = VGroup(*[card_line(iso, -0.75, 0.30, z, INK, w=6) for z in LINE_ZS[:3]])
        ppill = pushback_pill("more concrete", -4.05, 0.60, 2.5)
        dinners = ["taco night", "soup", "stir-fry"]
        dlabels = VGroup(*[VGroup(
            Line([iso.p(0.42, 0.02, z)[0], iso.p(0.42, 0.02, z)[1], 0],
                 [0.30, iso.p(0.42, 0.02, z)[1], 0], color=INK, stroke_width=3),
            T(name, size=32).move_to([1.35, iso.p(0.42, 0.02, z)[1], 0]))
            for z, name in zip(LINE_ZS[:3], dinners)])
        self.play(FadeIn(VGroup(page, dtag, qpill, ghosts)), run_time=0.6)
        self.play(FadeIn(ppill), run_time=0.4)
        self.play(FadeOut(ghosts), FadeIn(sharp), run_time=0.5)
        self.play(FadeIn(dlabels), run_time=0.4)
        until(self, "actually buy for")
        finish(self)


class B05_BusyParent(Scene):
    def construct(self):
        iso = Iso(-1.2, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        dtag = draft_tag("DRAFT 2", -2.70, 2.45)
        qpill = pushback_pill("plan dinners", -1.20, 2.90, 2.6)
        sharp = VGroup(*[card_line(iso, -0.75, 0.30, z, INK, w=6) for z in LINE_ZS[:3]])
        ppill = pushback_pill("for a busy parent", -4.05, 0.60, 3.0)
        clock_face = Circle(radius=0.55, color=INK, stroke_width=4).move_to([2.90, -1.30, 0])
        hand1 = Line([2.90, -1.30, 0], [2.90, -0.90, 0], color=INK, stroke_width=5)
        hand2 = Line([2.90, -1.30, 0], [3.25, -1.30, 0], color=INK, stroke_width=5)
        hub = Dot([2.90, -1.30, 0], radius=0.07, color=TERRA)
        clock = VGroup(clock_face, hand1, hand2, hub)
        tags = VGroup(*[draft_tag("15 min", 3.10, iso.p(0.42, 0.02, z)[1], w=1.15, h=0.50)
                        for z in LINE_ZS[:3]])
        self.play(FadeIn(VGroup(page, dtag, qpill, sharp)), run_time=0.6)
        self.play(FadeIn(ppill), run_time=0.4)
        self.play(FadeIn(clock), run_time=0.5)
        self.play(FadeIn(tags), run_time=0.5)
        until(self, "not a stranger's")
        finish(self)


class B06_SideBySide(Scene):
    def construct(self):
        iso_l = Iso(-3.0, -0.35, 1.0)
        iso_r = Iso(1.0, -0.35, 1.0)
        old = VGroup(standing_card(iso_l, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H),
                     VGroup(*[card_line(iso_l, -0.75, 0.75, z, GHOST) for z in LINE_ZS[:5]]),
                     draft_tag("DRAFT 1", -4.50, 2.45))
        new = VGroup(standing_card(iso_r, -0.9, PAGE_Y, PAGE_Z, 1.8, PAGE_H),
                     VGroup(*[card_line(iso_r, -0.55, 0.55, z, INK, w=6) for z in LINE_ZS[:3]]),
                     draft_tag("DRAFT 3", 0.45, 2.45))
        ck = check(1.55, 1.55, s=0.28, color=TERRA, w=8)
        lab = label_right("yours", 3.30, 0.40, 2.30)
        self.play(FadeIn(old), run_time=0.6)
        self.play(FadeIn(new, shift=UP * 0.6), run_time=0.6)
        self.play(Create(ck), run_time=0.4)
        self.play(FadeIn(lab), run_time=0.3)
        until(self, "you steered it")
        finish(self)


class B07_Drift(Scene):
    def construct(self):
        iso = Iso(-1.2, -0.35, 1.0)
        page = standing_card(iso, PAGE_X, PAGE_Y, PAGE_Z, PAGE_W, PAGE_H)
        dtag = draft_tag("DRAFT 3", -2.70, 2.45)
        sharp = VGroup(*[card_line(iso, -0.75, 0.30, z, INK, w=6) for z in LINE_ZS[:3]])
        stray = Line(iso.p(-0.75, 0.04, 0.90), iso.p(0.90, 0.04, 0.30), color=GHOST, stroke_width=5)
        qmark = T("?", size=44).move_to([0.30, 1.30, 0])
        drift = VGroup(stray, qmark)
        ppill = pushback_pill("stick to weeknights", -4.05, 0.60, 3.1)
        self.play(FadeIn(VGroup(page, dtag, sharp)), run_time=0.6)
        self.play(FadeIn(drift), run_time=0.5)
        self.play(FadeIn(ppill), run_time=0.4)
        self.play(FadeOut(drift), run_time=0.4)
        until(self, "stick to weeknights")
        finish(self)


class B08_Recipe(Scene):
    def construct(self):
        p1 = pushback_pill("shorter", -3.60, 0.50, 2.0)
        p2 = pushback_pill("more concrete", 0.00, 0.50, 2.7)
        p3 = pushback_pill("for someone", 3.60, 0.50, 2.4)
        arrow = Arrow([-3.60, -0.75, 0], [3.60, -0.75, 0], color=INK, stroke_width=5, buff=0.1)
        self.play(FadeIn(p1), run_time=0.4)
        self.play(FadeIn(p2), run_time=0.4)
        self.play(FadeIn(p3), run_time=0.4)
        self.play(Create(arrow), run_time=0.5)
        until(self, "Remember those three")
        finish(self)
