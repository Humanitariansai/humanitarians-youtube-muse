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

"""
just-talk-to-it — scenes.py (show-tell).

The iso_kit.py block (top of file) is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py — Gate A copies only
scenes.py, so the kit must live here, not be imported.

Cast for the whole film: the mic button (ink ring, mic glyph, one terracotta
dot), ink sound-wave arcs, simple ink heads, kraft pages, the open tray.
Every scene: all motion lands in the first ~40% of the beat (fully opaque,
nothing half-done at the midpoint GATE T samples), then `until()` holds on a
settled labelled frame and `finish()` pads to the audio.
"""


# ═════════════════════════════ local helpers ═════════════════════════════
def wave_arc(x, y, r, a0=-55, a1=55, color=INK, w=6):
    """One sound-wave arc centred on (x, y), opening to the right by default."""
    return Arc(radius=r, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
               arc_center=[x, y, 0], color=color, stroke_width=w)


def waves(x, y, r0=0.55, n=3, a0=-55, a1=55, color=INK, w=6):
    """A fan of concentric wave arcs — the film's signature motif."""
    return VGroup(*[wave_arc(x, y, r0 + i * 0.45, a0, a1, color, w) for i in range(n)])


def mic_glyph(x, y, s=1.0):
    """Mic glyph in ink: capsule body, cradle arc, stem, foot."""
    body = RoundedRectangle(width=0.34 * s, height=0.52 * s, corner_radius=0.17 * s,
                            fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, y + 0.10 * s, 0])
    cradle = Arc(radius=0.30 * s, start_angle=200 * DEGREES, angle=140 * DEGREES,
                 arc_center=[x, y + 0.04 * s, 0], color=INK, stroke_width=7 * s)
    stem = Line([x, y - 0.26 * s, 0], [x, y - 0.44 * s, 0], color=INK, stroke_width=7 * s)
    foot = Line([x - 0.18 * s, y - 0.44 * s, 0], [x + 0.18 * s, y - 0.44 * s, 0], color=INK, stroke_width=7 * s)
    return VGroup(body, cradle, stem, foot)


def mic_button(x, y, r=0.62):
    """The film's hero object: cream button, ink ring, mic glyph, one terracotta dot."""
    fill = Circle(radius=r, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    ring = Circle(radius=r, color=INK, stroke_width=5).move_to([x, y, 0])
    glyph = mic_glyph(x, y, s=1.0)
    dot = Dot([x + r * 0.72, y + r * 0.72, 0], radius=0.09, color=TERRA)
    return VGroup(fill, ring, glyph, dot)


def head(x, y, r=0.5, fill=GHOST):
    """A simple person: ink-outlined head circle + shoulders, ghost fill."""
    c = Circle(radius=r, color=INK, stroke_width=5, fill_color=fill, fill_opacity=1).move_to([x, y, 0])
    sh = Polygon([x - r * 0.95, y - r * 2.0, 0], [x + r * 0.95, y - r * 2.0, 0],
                 [x + r * 0.55, y - r * 0.85, 0], [x - r * 0.55, y - r * 0.85, 0],
                 fill_color=fill, fill_opacity=1, color=INK, stroke_width=5)
    return VGroup(c, sh)


def label(text, x, y, size=40):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def leader(x0, x1, y, color=DIM):
    """A short dim leader line; callers keep ≥0.3 gap to the label."""
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)


# ═════════════════════════════ B00 — the mic button ═════════════════════════════
class B00_MicHero(Scene):
    def construct(self):
        card = RoundedRectangle(width=5.4, height=3.1, corner_radius=0.25,
                                fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([0, 0, 0])
        mb = mic_button(0, 0.1)
        lab = label("mic", 3.7, 0.1)
        lead = leader(0.95, 3.15, 0.1)
        self.play(FadeIn(card), FadeIn(mb), run_time=0.7)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.5)
        w = waves(0, 0.1, r0=1.05, n=3)
        self.play(GrowFromCenter(w), run_time=0.7)
        until(self, "Most AI apps")
        finish(self)


# ═════════════════════════════ B01 — talk back and forth ═════════════════════════════
class B01_StartTalk(Scene):
    def construct(self):
        you = head(-3.6, 0.5)
        you_lab = label("you", -3.6, -1.35)
        panel = RoundedRectangle(width=2.2, height=2.2, corner_radius=0.3,
                                 fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([3.4, 0.4, 0])
        panel_w = waves(3.4, 0.4, r0=0.35, n=2, w=5)
        claude_lab = label("claude", 3.4, -1.35)
        self.play(FadeIn(you), FadeIn(you_lab), FadeIn(panel), FadeIn(panel_w), FadeIn(claude_lab), run_time=0.7)
        out_w = waves(-3.6, 0.5, r0=0.9, n=3, a0=-55, a1=55)
        self.play(GrowFromCenter(out_w), run_time=0.6)
        back_w = waves(3.4, 0.4, r0=0.9, n=3, a0=125, a1=235)
        self.play(GrowFromCenter(back_w), run_time=0.6)
        until(self, "answers out loud")
        finish(self)


# ═════════════════════════════ B02 — brainstorm aloud ═════════════════════════════
class B02_Brainstorm(Scene):
    def construct(self):
        h = head(-3.4, -0.2)
        dots = VGroup(*[Dot([-3.4 + 0.35 * i, 1.15 + 0.28 * i, 0], radius=0.08, color=INK) for i in range(3)])
        bulb = Circle(radius=0.75, color=INK, stroke_width=5, fill_color=CARD, fill_opacity=1).move_to([3.2, 0.3, 0])
        glow = Dot([3.2, 0.3, 0], radius=0.22, color=TERRA)
        rays = VGroup(*[Line([3.2 + 1.0 * np.cos(a), 0.3 + 1.0 * np.sin(a), 0],
                             [3.2 + 1.25 * np.cos(a), 0.3 + 1.25 * np.sin(a), 0],
                             color=INK, stroke_width=5) for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)])
        lab = label("ideas", 3.2, -1.35)
        self.play(FadeIn(h), FadeIn(bulb), FadeIn(rays), FadeIn(lab), run_time=0.7)
        self.play(FadeIn(dots), run_time=0.4)
        self.play(dots.animate.shift(UP * 0.45), run_time=0.4)
        w = waves(-3.4, -0.2, r0=1.0, n=3, a0=-50, a1=50)
        self.play(GrowFromCenter(w), run_time=0.6)
        self.play(GrowFromCenter(glow), run_time=0.4)
        until(self, "sort them")
        finish(self)


# ═════════════════════════════ B03 — hands busy in the kitchen ═════════════════════════════
class B03_KitchenHands(Scene):
    def construct(self):
        iso = Iso(-3.3, -1.2, 1.0)
        back, front = iso.open_box(0, 0, 0, 1.6, 1.6, 1.0)
        steam = VGroup(*[Line([-3.3 - 0.4 + 0.4 * i, 0.9, 0], [-3.3 - 0.4 + 0.4 * i, 1.7, 0],
                               color=GHOST, stroke_width=7) for i in range(3)])
        lab = label("hands busy", -2.9, -2.2)
        h = head(3.2, 0.0)
        self.play(FadeIn(back), FadeIn(front), FadeIn(steam), FadeIn(h), FadeIn(lab), run_time=0.7)
        self.play(steam.animate.shift(UP * 0.5), run_time=0.5)
        w = waves(-2.2, 0.2, r0=0.8, n=3, a0=-55, a1=55)
        w2 = waves(3.2, 0.0, r0=0.8, n=3, a0=125, a1=235)
        self.play(GrowFromCenter(w), GrowFromCenter(w2), run_time=0.7)
        until(self, "never touch the screen")
        finish(self)


# ═════════════════════════════ B04 — rehearse the hard talk ═════════════════════════════
class B04_ToughTalk(Scene):
    def construct(self):
        a = head(-2.8, 0.2)
        b = head(2.8, 0.2)
        lab = label("rehearse", 0, -1.7)
        self.play(FadeIn(a), FadeIn(b), FadeIn(lab), run_time=0.7)
        w = waves(-2.8, 0.2, r0=1.0, n=3, a0=-50, a1=50)
        w2 = waves(2.8, 0.2, r0=1.0, n=3, a0=130, a1=230)
        self.play(GrowFromCenter(w), GrowFromCenter(w2), run_time=0.7)
        ck = check(2.8, 1.75, s=0.22, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "hear how it lands")
        finish(self)


# ═════════════════════════════ B05 — language practice ═════════════════════════════
class B05_Language(Scene):
    def construct(self):
        h = head(-3.6, 0.0)
        bubble = RoundedRectangle(width=3.4, height=1.9, corner_radius=0.4,
                                  fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([2.6, 0.4, 0])
        tail = Triangle(color=INK, fill_color=CARD, fill_opacity=1, stroke_width=5
                        ).scale(0.5).rotate(-115 * DEGREES).move_to([0.75, -0.15, 0])
        answer = waves(2.6, 0.4, r0=0.4, n=2, a0=-60, a1=60, w=5)
        lab = label("bonjour", 5.15, 0.4)
        lead = leader(4.35, 4.75, 0.4)
        self.play(FadeIn(h), FadeIn(bubble), FadeIn(tail), FadeIn(lead), FadeIn(lab), run_time=0.7)
        w = waves(-3.6, 0.0, r0=1.0, n=3, a0=-50, a1=50)
        self.play(GrowFromCenter(w), run_time=0.6)
        self.play(GrowFromCenter(answer), run_time=0.5)
        until(self, "corrects you gently")
        finish(self)


# ═════════════════════════════ B06 — keep it: type ═════════════════════════════
class B06_KeepIt(Scene):
    def construct(self):
        iso = Iso(-1.1, -1.5, 1.0)
        back, front = iso.open_box(0, 0, 0, 2.2, 1.8, 1.1)
        page = iso.page(0.55, 0.2, 2.6, 1.1, 1.4)
        lab = label("keep", 3.9, -0.9)
        lead = leader(1.9, 3.35, -0.9)
        self.play(FadeIn(back), FadeIn(front), FadeIn(lead), FadeIn(lab), run_time=0.7)
        self.play(FadeIn(page), run_time=0.5)
        self.play(page.animate.shift(DOWN * 1.9), run_time=0.6)
        ck = check(1.15, 0.15, s=0.22, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.4)
        until(self, "type it")
        finish(self)


# ═════════════════════════════ B07 — exactness: typed beats heard ═════════════════════════════
class B07_Precise(Scene):
    def construct(self):
        card_t = RoundedRectangle(width=3.3, height=2.5, corner_radius=0.2,
                                  fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([-2.9, 0.2, 0])
        straight = VGroup(*[Line([-4.1, 0.9 - 0.45 * i, 0], [-1.7, 0.9 - 0.45 * i, 0],
                                 color=BAR1, stroke_width=6) for i in range(3)])
        lab_t = label("typed", -2.9, -1.6)
        card_h = RoundedRectangle(width=3.3, height=2.5, corner_radius=0.2,
                                  fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([2.9, 0.2, 0])
        garbled = VGroup(*[wave_arc(2.9, 0.9 - 0.45 * i, 0.28, a0=-70, a1=70, color=BAR2, w=6) for i in range(3)])
        lab_h = label("heard", 2.9, -1.6)
        self.play(FadeIn(card_t), FadeIn(straight), FadeIn(lab_t),
                  FadeIn(card_h), FadeIn(garbled), FadeIn(lab_h), run_time=0.8)
        x1 = Line([2.15, 1.15, 0], [3.65, -0.35, 0], color=INK, stroke_width=9)
        x2 = Line([2.15, -0.35, 0], [3.65, 1.15, 0], color=INK, stroke_width=9)
        self.play(GrowFromCenter(VGroup(x1, x2)), run_time=0.5)
        until(self, "eyes do not")
        finish(self)


# ═════════════════════════════ B08 — in public, type ═════════════════════════════
class B08_PublicPlaces(Scene):
    def construct(self):
        heads = VGroup(*[head(-2.2 + 2.2 * i, 1.1, r=0.42) for i in range(3)])
        mb = mic_button(0, -0.9, r=0.55)
        slash = Line([-0.75, -0.15, 0], [0.75, -1.65, 0], color=INK, stroke_width=9)
        kb = RoundedRectangle(width=3.8, height=1.0, corner_radius=0.3,
                              fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([0, -0.9, 0])
        keys = VGroup(*[Dot([-1.2 + 0.6 * i, -0.9, 0], radius=0.11, color=BAR1) for i in range(5)])
        lab = label("type quietly", 0, -2.3)
        self.play(FadeIn(heads), FadeIn(mb), run_time=0.7)
        self.play(Create(slash), run_time=0.5)
        self.play(FadeOut(mb), FadeOut(slash), FadeIn(kb), FadeIn(keys), FadeIn(lab), run_time=0.6)
        until(self, "type quietly")
        finish(self)


# ═════════════════════════════ B09 — full thoughts, not fragments ═════════════════════════════
class B09_FullThoughts(Scene):
    def construct(self):
        frags = VGroup(*[wave_arc(-3.6, 0.3, 0.5 + 0.25 * i, a0=-70, a1=20, color=DIM, w=6) for i in range(3)])
        lab_f = label("fragments", -3.6, -1.5)
        full = waves(2.2, 0.3, r0=0.55, n=3, a0=-60, a1=60)
        iso = Iso(4.35, -0.55, 0.8)
        pg = iso.page(0, 0, 0, 1.1, 1.4)
        lab_t = label("full thoughts", 2.2, -1.5)
        self.play(FadeIn(frags), FadeIn(lab_f), run_time=0.6)
        self.play(GrowFromCenter(full), FadeIn(pg), FadeIn(lab_t), run_time=0.8)
        until(self, "something real")
        finish(self)


# ═════════════════════════════ B10 — interrupt freely ═════════════════════════════
class B10_Interrupt(Scene):
    def construct(self):
        bumps = VGroup()
        for i in range(6):
            cx = -3.75 + 1.5 * i
            a0, a1 = (0, 180) if i % 2 == 0 else (180, 360)
            bumps.add(Arc(radius=0.75, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
                          arc_center=[cx, 0.2, 0], color=INK, stroke_width=7))
        left = VGroup(*bumps[:3])
        right = VGroup(*bumps[3:])
        lab = label("interrupt", 3.3, 1.9)
        self.play(FadeIn(left), FadeIn(right), FadeIn(lab), run_time=0.7)
        shaft = Line([0.4, 2.0, 0], [-0.5, -0.6, 0], color=INK, stroke_width=10)
        tip = Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0
                       ).scale(0.42).rotate(-72 * DEGREES).move_to([-0.62, -0.85, 0])
        arrow = VGroup(shaft, tip)
        self.play(GrowFromCenter(arrow), run_time=0.5)
        self.play(FadeOut(right), run_time=0.4)
        until(self, "talk over it")
        finish(self)


# ═════════════════════════════ B11 — ask for the summary ═════════════════════════════
class B11_Summarize(Scene):
    def construct(self):
        talk = waves(-3.8, 0.2, r0=0.6, n=3, color=DIM)
        lab_t = label("talk", -3.8, -1.5)
        arrow = Line([-1.9, 0.2, 0], [-0.5, 0.2, 0], color=INK, stroke_width=7)
        ahead = Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0
                         ).scale(0.35).rotate(-90 * DEGREES).move_to([-0.35, 0.2, 0])
        iso = Iso(0.9, -0.5, 0.95)
        pg = iso.page(0, 0, 0, 1.3, 1.7)
        lab_s = label("summary", 2.6, -1.9)
        self.play(FadeIn(talk), FadeIn(lab_t), FadeIn(pg), FadeIn(lab_s), run_time=0.8)
        self.play(Create(arrow), FadeIn(ahead), run_time=0.5)
        until(self, "does the remembering")
        finish(self)
