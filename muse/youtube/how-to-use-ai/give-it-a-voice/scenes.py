"""scenes.py — "Give it a voice" (show-tell).

7 Manim scenes, B00-B06, one drawing per beat. House palette (cream stage,
warm ink, terracotta accents); iso_kit pasted at top (Gate A copies only
scenes.py). Each scene adds new non-text shapes via FadeIn/Create/
GrowFromCenter (never via .animate() alone); labels sit beside objects;
coords within +-6.2 x +-3.3 y; type floor 32. Cast: slide pages, the
Suno Speech box, one merged track bar, the Vids browser window.
"""

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


# ═════════════════════════════ B00 — the silent slides ═════════════════════════════
class B00_SilentSlides(Scene):
    def construct(self):
        iso = Iso(-2.2, -1.6, 0.9)
        pages = VGroup(*[iso.page(0, 0, i * 0.28, w=2.2, d=1.7) for i in range(3)])
        pl = lab("your slides", -2.0, -2.25, size=32)
        until(self, "starting point")
        self.play(FadeIn(pages), FadeIn(pl), run_time=0.6)

        sp = speaker_muted(2.9, 0.3)
        sl = lab("silent", 2.9, -1.1, size=32)
        until(self, "silent")
        self.play(FadeIn(sp), FadeIn(sl), run_time=0.5)

        p = pill(2.9, -2.0, 4.4)
        pxl = lab("needs a voice", 2.9, -2.0, size=32)
        until(self, "twenty takes")
        self.play(FadeIn(p), FadeIn(pxl), run_time=0.4)
        finish(self)


# ═════════════════════════════ B01 — Suno Speech ═════════════════════════════
class B01_SunoSpeech(Scene):
    def construct(self):
        iso = Iso(-3.4, -1.8, 0.95)
        back, front = iso.open_box(0, 0, 0, 2.8, 2.2, 1.7)
        bl = lab("Suno Speech", -3.15, -2.5, size=34)
        until(self, "Meet Suno Speech")
        self.play(FadeIn(back), FadeIn(front), FadeIn(bl), run_time=0.6)

        pg = iso.page(0.3, 0.25, 2.6, w=2.2, d=1.7)
        pg.set_z_index(1)
        until(self, "This October")
        self.play(FadeIn(pg), run_time=0.4)
        self.play(pg.animate.shift(iso.v(0, 0, -1.9)), run_time=0.7)

        wave = voice_wave(-0.7, 0.4)
        trail = music_trail(-0.7, -0.35)
        until(self, "You give it your script", lead=2.0)
        self.play(Create(wave), FadeIn(trail), run_time=0.6)

        bar = track_bar(1.9, -1.7, w=5.6)
        tl = lab("one track", 1.9, -2.5, size=32)
        until(self, "background music")
        self.play(FadeIn(bar), FadeIn(tl), run_time=0.5)
        finish(self)


# ═════════════════════════════ B02 — the two ways ═════════════════════════════
class B02_TwoWays(Scene):
    def construct(self):
        c1 = card(-3.0, 0.4, w=4.6, h=3.0)
        c2 = card(3.0, 0.4, w=4.6, h=3.0)
        l1 = lab("Simple — describe it", -3.0, -1.55, size=32)
        l2 = lab("Advanced — your script", 3.0, -1.55, size=32)
        until(self, "two ways")
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(l1), FadeIn(l2), run_time=0.6)

        flag = VGroup(Dot([-3.0, 0.9, 0], radius=0.14, color=TERRA),
                      Polygon([-3.0, 1.04, 0], [-3.0, 0.5, 0], [-2.35, 0.77, 0],
                              fill_color=INK, fill_opacity=1, stroke_width=0))
        until(self, "pirate captain")
        self.play(FadeIn(flag), run_time=0.4)

        sliders = VGroup(*[voice_slider(3.0, 1.15 - i * 0.55, knob=0.25 + i * 0.25) for i in range(3)])
        until(self, "fine-tune the voice")
        self.play(FadeIn(sliders), run_time=0.5)
        finish(self)


# ═════════════════════════════ B03 — the workflow ═════════════════════════════
class B03_Workflow(Scene):
    def construct(self):
        p1 = tag("script or vibe", -3.9, 0.9, 3.0)
        p2 = tag("voice + music", 0.0, 0.9, 3.0)
        p3 = tag("generate", 3.9, 0.9, 3.0)
        a1 = Arrow([-2.3, 0.9, 0], [-1.6, 0.9, 0], color=INK, stroke_width=6, buff=0)
        a2 = Arrow([1.6, 0.9, 0], [2.3, 0.9, 0], color=INK, stroke_width=6, buff=0)
        until(self, "three steps")
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(p3), Create(a1), Create(a2), run_time=0.7)

        bar = track_bar(0, -1.7, w=7.0)
        tl = lab("one track", 0, -2.5, size=32)
        until(self, "generate", lead=0.6)
        self.play(FadeIn(bar), FadeIn(tl), run_time=0.5)
        finish(self)


# ═════════════════════════════ B04 — beta means rough ═════════════════════════════
class B04_BetaRough(Scene):
    def construct(self):
        bar = track_bar(0, 0.9, w=8.0)
        until(self, "honest part")
        self.play(FadeIn(bar), run_time=0.6)

        tg = tag("accents wander", 0, -1.7, 3.8)
        arc = CurvedArrow([-1.9, 0.55, 0], [1.9, 0.55, 0], angle=-0.9,
                          color=INK, stroke_width=5)
        until(self, "Accents can wander")
        self.play(FadeIn(tg), Create(arc), run_time=0.5)

        t1 = Line([-1.2, 0.5, 0], [-1.2, 1.3, 0], color=INK, stroke_width=6)
        t2 = Line([1.2, 0.5, 0], [1.2, 1.3, 0], color=INK, stroke_width=6)
        gl = lab("long pause", 0, -0.15, size=32)
        until(self, "dramatic pauses")
        self.play(Create(t1), Create(t2), FadeIn(gl), run_time=0.5)

        ck = check(2.9, -1.7, s=0.24, color=TERRA)
        cl = lab("listen first", 4.8, -1.7, size=32)
        until(self, "listen to the whole take")
        self.play(FadeIn(ck), FadeIn(cl), run_time=0.4)
        finish(self)


# ═════════════════════════════ B05 — Vids has it built in ═════════════════════════════
class B05_VidsBuiltIn(Scene):
    def construct(self):
        win = browser_win(0, 0.2, w=9.6, h=4.6, title="Vids")
        until(self, "Google Vids")
        self.play(FadeIn(win), run_time=0.6)

        pg = mini_page(-2.9, 0.35, w=3.0, h=2.0)
        sp = tag("script per scene", 1.9, 0.85, 3.9)
        until(self, "type the script per scene", lead=1.2)
        self.play(FadeIn(pg), FadeIn(sp), run_time=0.5)

        vp = tag("30 voices", -2.9, -1.35, 3.0)
        until(self, "thirty voices")
        self.play(FadeIn(vp), run_time=0.4)

        tg = tag("[excitedly]", 1.9, -0.75, 3.4)
        until(self, "bracket tags")
        self.play(FadeIn(tg), run_time=0.4)

        ck = check(3.2, -1.3, s=0.24, color=TERRA)
        cl = lab("built in", 3.2, -1.9, size=30)
        until(self, "no separate audio file")
        self.play(FadeIn(ck), FadeIn(cl), run_time=0.4)
        finish(self)


# ═════════════════════════════ B06 — the rule: it reads what you wrote ═════════════════════════════
class B06_TheRule(Scene):
    def construct(self):
        pg = typo_page(-2.2, 0.7)
        until(self, "One rule")
        self.play(FadeIn(pg), run_time=0.6)

        sp = speaker_live(3.1, 0.7)
        until(self, "reads exactly what you wrote")
        self.play(FadeIn(sp), run_time=0.5)

        x = typo_x(-2.2, 0.7)
        until(self, "typos")
        self.play(FadeIn(x), run_time=0.4)

        clean = mini_page(-2.2, -1.95, w=3.6, h=1.5)
        ck = check(0.6, -1.95, s=0.24, color=TERRA)
        cl = lab("clean copy", 2.35, -1.95, size=32)
        until(self, "read it aloud yourself")
        self.play(FadeIn(clean), FadeIn(ck), FadeIn(cl), run_time=0.5)
        finish(self)


# ═════════════════════════════ film helpers (attached after the class lines) ═════════════════════════════
def lab(s, x, y, size=34, color=INK, bold=False):
    return T(s, size=size, color=color, bold=bold).move_to([x, y, 0])


def card(x, y, w=4.6, h=3.0):
    """White content card: ghost text lines + one terracotta dot."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.12,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    for i in range(3):
        yy = y + h / 2 - 0.7 - i * 0.5
        g.add(Line([x - w / 2 + 0.5, yy, 0], [x + w / 2 - 0.5, yy, 0],
                   color=GHOST, stroke_width=5))
    g.add(Dot([x - w / 2 + 0.8, y - h / 2 + 0.6, 0], radius=0.09, color=TERRA))
    return g


def tag(text, x, y, w, size=32):
    """White pill carrying short ink text (a UI chip)."""
    g = VGroup()
    g.add(pill(x, y, w))
    g.add(lab(text, x, y, size=size))
    return g


def mini_page(x, y, w=3.0, h=2.0):
    """Flat white page with ghost text lines."""
    g = VGroup()
    g.add(Rectangle(width=w, height=h, fill_color="#FFFFFF", fill_opacity=1,
                    stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    for i in range(3):
        yy = y + h / 2 - 0.55 - i * 0.45
        g.add(Line([x - w / 2 + 0.45, yy, 0], [x + w / 2 - 0.45, yy, 0],
                   color=GHOST, stroke_width=5))
    return g


def typo_page(x, y):
    """A page with one ink typo word on its middle line."""
    g = mini_page(x, y, w=3.6, h=2.4)
    g.add(lab("teh", x, y, size=34))
    return g


def typo_x(x, y):
    """Terracotta X over the typo word."""
    d = 0.42
    return VGroup(
        Line([x - d, y - d * 0.7, 0], [x + d, y + d * 0.7, 0], color=TERRA, stroke_width=8),
        Line([x - d, y + d * 0.7, 0], [x + d, y - d * 0.7, 0], color=TERRA, stroke_width=8))


def speaker_base(x, y, s=1.0):
    """Speaker: cone pointing left + body, ink outlines on white."""
    cone = Polygon([x - 0.15 * s, y + 0.5 * s, 0], [x - 0.15 * s, y - 0.5 * s, 0],
                   [x - 0.85 * s, y - 0.28 * s, 0], [x - 0.85 * s, y + 0.28 * s, 0],
                   fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4)
    body = Rectangle(width=0.5 * s, height=1.0 * s, fill_color=CARD, fill_opacity=1,
                     stroke_color=INK, stroke_width=4).move_to([x + 0.1 * s, y, 0])
    return VGroup(cone, body)


def speaker_muted(x, y):
    """Speaker with an ink X: no voice yet."""
    g = speaker_base(x, y)
    g.add(Line([x + 0.55, y + 0.32, 0], [x + 1.15, y - 0.32, 0], color=INK, stroke_width=6))
    g.add(Line([x + 0.55, y - 0.32, 0], [x + 1.15, y + 0.32, 0], color=INK, stroke_width=6))
    return g


def speaker_live(x, y):
    """Speaker with three sound arcs opening toward the left."""
    g = speaker_base(x, y)
    arcs = VGroup(*[Arc(radius=0.55 + i * 0.35, start_angle=np.pi - 0.65, angle=1.3,
                        color=INK, stroke_width=5).move_to([x - 0.85, y, 0])
                     for i in range(3)])
    g.add(arcs)
    return g


def voice_wave(x, y, w=2.4):
    """Ink zigzag: the voice stream leaving the box."""
    pts = [[x + w * i / 12, y + (0.28 if i % 2 == 0 else -0.28), 0] for i in range(13)]
    pts[0][1] = y
    pts[-1][1] = y
    return VMobject().set_points_as_corners(pts).set_stroke(color=INK, width=6)


def music_trail(x, y, w=2.2):
    """Terracotta dots: the music stream leaving the box."""
    return VGroup(*[Dot([x + w * i / 4, y + 0.12 * (-1) ** i, 0],
                        radius=0.09, color=TERRA) for i in range(5)])


def track_bar(x, y, w=8.0, h=0.5):
    """The merged track: one bar, ink waveform ticks, terracotta playhead."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=h / 2,
                           fill_color="#EFE9DC", fill_opacity=1,
                           stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    for i, f in enumerate([-0.38, -0.22, -0.05, 0.14, 0.30]):
        hh = 0.16 + 0.08 * ((i * 7) % 3)
        g.add(Line([x + f * w, y - hh / 2, 0], [x + f * w, y + hh / 2, 0],
                   color=INK, stroke_width=5))
    g.add(Dot([x + 0.42 * w, y, 0], radius=0.11, color=TERRA))
    return g


def voice_slider(x, y, w=2.6, knob=0.3):
    """One voice control: ghost rail, terracotta knob."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=0.18, corner_radius=0.09,
                           fill_color=GHOST, fill_opacity=1,
                           stroke_width=0).move_to([x, y, 0]))
    g.add(Dot([x - w / 2 + w * knob, y, 0], radius=0.14, color=TERRA))
    return g


def browser_win(x, y, w=9.6, h=4.6, title="Vids"):
    """Pale UI panel with a dark title bar (carries the contrast)."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.18,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=4).move_to([x, y, 0]))
    g.add(RoundedRectangle(width=w, height=0.72, corner_radius=0.18,
                           fill_color=DARK_TOP, fill_opacity=1,
                           stroke_width=0).move_to([x, y + h / 2 - 0.36, 0]))
    g.add(lab(title, x - w / 2 + 0.9, y + h / 2 - 0.36, size=30, color="#FFFFFF"))
    return g
