"""
scenes.py — show-tell drawings for your-song-in-a-minute (How to AI).

Eight isometric Manim scenes (B00..B07), one per body beat. The iso_kit block is
pasted at the top (Gate A copies only this file). Film helpers below it: a
music note, a vinyl record, a song card, a music-tool window, and a waveform.
Pacing: every motion is keyed to a narration phrase inside the first ~35% of
its beat via until(), so nothing is mid-motion at the clip midpoint under
GATE T/Gate V sampling, whatever the measured Kokoro audio comes out as.
finish() holds to the audio.
"""
from manim import *
import numpy as np
import math as _math
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
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z0)], BOX_IN2))
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
def floor_shadow(cx=0.0, cy=-2.9, w=7.0):
    return Ellipse(width=w, height=0.7, fill_color=GHOST, fill_opacity=0.55,
                   stroke_width=0).move_to([cx, cy, 0])


def prompt_card(cx, cy, w=3.2, h=2.0, n_lines=4, short=False):
    """A flat prompt/answer page in iso. short=True draws short simple lines."""
    iso = Iso(cx, cy, 0.9)
    slab = iso.box(-w / 2, -h / 2, 0, w, h, 0.10, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    zt = 0.10
    lines = []
    for i in range(n_lines):
        f = 0.25 + 0.5 * i / max(1, n_lines - 1)
        x1 = -w / 2 + 0.35
        x2 = (-w / 2 + 0.35 + (w - 0.7) * 0.55) if short else (w / 2 - 0.35)
        lines.append(Line(iso.p(x1, -h / 2 + h * f, zt), iso.p(x2, -h / 2 + h * f, zt),
                          color=GHOST, stroke_width=5))
    return VGroup(slab, VGroup(*lines))


def name_tag(text, cx, cy, w=2.6, stroke=INK):
    """A small white name-tag carrying a word. Ink text, terracotta seal dot (house pattern)."""
    tag = RoundedRectangle(width=w, height=0.72, corner_radius=0.36,
                           fill_color="#FFFFFF", fill_opacity=1,
                           stroke_color=stroke, stroke_width=2.5).move_to([cx, cy, 0])
    t = T(text, size=34, color=INK).move_to([cx - 0.1, cy - 0.02, 0])
    dot = Dot([cx + w / 2 - 0.28, cy, 0], radius=0.09, color=TERRA)
    return VGroup(tag, t, dot)


def music_window(cx, cy, w=3.4, h=2.6):
    """A pale AI music-tool window carried by a grey title band (BAR1, not dark: GATE T)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    band = Rectangle(width=w - 0.06, height=0.55, fill_color=BAR1, fill_opacity=1,
                     stroke_width=0).move_to([cx, cy + h / 2 - 0.30, 0])
    title = T("music tool", size=32, color=INK).move_to([cx - w / 2 + 0.95, cy + h / 2 - 0.30, 0])
    n = note(cx + w / 2 - 0.55, cy + h / 2 - 0.85, s=0.42)
    line1 = Line([cx - w / 2 + 0.4, cy - 0.2, 0], [cx + w / 2 - 1.2, cy - 0.2, 0],
                 color=GHOST, stroke_width=5)
    return VGroup(card, band, title, n, line1)


def note(x, y, s=0.55, color=INK):
    """A simple eighth note: ink head, stem and flag. Big enough to read (never tiny)."""
    head = Ellipse(width=0.52 * s, height=0.4 * s, fill_color=color, fill_opacity=1,
                   stroke_width=0).move_to([x, y, 0])
    sx = x + 0.24 * s
    stem = Line([sx, y, 0], [sx, y + 1.15 * s, 0], color=color, stroke_width=7)
    flag = Polygon([sx, y + 1.15 * s, 0], [sx + 0.72 * s, y + 0.92 * s, 0], [sx, y + 0.6 * s, 0],
                   fill_color=color, fill_opacity=1, stroke_width=0)
    return VGroup(head, stem, flag)


def disc(x, y, r=0.85):
    """A vinyl record: dark disc (carries Gate V contrast), kraft label ring, terracotta center dot."""
    d = Circle(radius=r, fill_color=DARK_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    lab = Circle(radius=r * 0.38, fill_color=BOX_TOP, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    hole = Dot([x, y, 0], radius=0.09, color=TERRA)
    return VGroup(d, lab, hole)


def song_card(cx, cy, w=2.6, h=1.9):
    """A finished-song card: CARD rectangle with ink outline, small dark disc, an ink note, ghost track lines."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    d = disc(cx - w / 2 + 0.62, cy + 0.18, r=0.48)
    n = note(cx + w / 2 - 0.62, cy - 0.52, s=0.45)
    lines = VGroup(*[Line([cx - w / 2 + 1.35, cy + 0.45 - 0.35 * i, 0],
                           [cx + w / 2 - 0.35, cy + 0.45 - 0.35 * i, 0],
                           color=GHOST, stroke_width=5) for i in range(2)])
    return VGroup(card, d, n, lines)


def waveform(cx, cy, w=6.4, n=24, hmax=1.1, seed=1.0):
    """A row of grey bars that reads as an audio waveform (greys only, with gaps: GATE T)."""
    bw = w / n
    bars = []
    for i in range(n):
        h = hmax * (0.25 + 0.75 * abs(_math.sin(i * 1.7 + seed)))
        b = Rectangle(width=bw * 0.55, height=max(0.08, h),
                      fill_color=BAR2 if i % 2 else BAR1, fill_opacity=1, stroke_width=0)
        b.move_to([cx - w / 2 + bw * (i + 0.5), cy, 0])
        bars.append(b)
    return VGroup(*bars)


def ink_cross(cx, cy, arm=0.4, w=8):
    return VGroup(Line([cx - arm, cy - arm, 0], [cx + arm, cy + arm, 0], color=INK, stroke_width=w),
                  Line([cx - arm, cy + arm, 0], [cx + arm, cy - arm, 0], color=INK, stroke_width=w))


# ═════════════════════════════ scenes ═════════════════════════════
class B00_BirthdaySong(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 8.0)
        rec = disc(0, 0.6, r=1.1)
        rec.shift(UP * 2.6)                      # drop start stays inside the ±3.3 safe area
        n1 = note(-2.3, 1.1, s=0.6)
        n2 = note(2.3, 1.5, s=0.5)
        n3 = note(1.7, -1.0, s=0.45)
        lab = T("your song", size=40, color=INK).move_to([0, -1.7, 0])
        chk = check(2.9, 1.3, s=0.22, color=TERRA, w=8)

        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "A birthday song")
        self.play(rec.animate.shift(DOWN * 2.6), rate_func=ease_in, run_time=0.8)
        until(self, "ready in about a minute")
        self.play(FadeIn(n1, n2, n3, lab), run_time=0.6)
        until(self, "That is the whole trick")
        self.play(FadeIn(chk), run_time=0.5)
        finish(self)


class B01_HowItWorks(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        card = prompt_card(-3.7, 0.5, 2.8, 1.8, 3)
        clab = T("your words", size=34, color=INK).move_to([-3.7, -1.15, 0])
        win = music_window(2.9, 0.5, 3.0, 2.4)
        song = song_card(-0.7, 0.5, 2.8, 2.0)
        song.shift(UP * 2.6)                     # drop start stays inside the ±3.3 safe area
        slab = T("a finished song", size=34, color=INK).move_to([-0.7, -1.35, 0])
        n = note(1.7, 1.3, s=0.5)

        self.play(FadeIn(shadow, card, clab, win), run_time=0.7)
        until(self, "Your description goes in")
        self.play(card.animate.shift(RIGHT * 3.5), run_time=0.8)
        self.play(FadeOut(card, clab), run_time=0.5)
        until(self, "The tool writes the music")
        self.play(song.animate.shift(DOWN * 2.6), rate_func=ease_in, run_time=0.8)
        self.play(FadeIn(slab, n), run_time=0.5)
        finish(self)


class B02_ThreeIngredients(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        win = music_window(0, 0.2, 4.2, 3.0)
        t1 = name_tag("a birthday", 0, 0.85, w=2.4)
        t2 = name_tag("dinosaurs", 0, 0.0, w=2.4)
        t3 = name_tag("cheerful", 0, -0.85, w=2.4)
        for t in (t1, t2, t3):
            t.shift(UP * 1.65)                   # all drop starts stay inside the ±3.3 safe area
        npop = note(3.4, 1.9, s=0.55)
        banner = T("occasion, subject, style", size=34, color=INK).move_to([0, -2.5, 0])

        self.play(FadeIn(shadow, win), run_time=0.6)
        until(self, "One: the occasion")
        self.play(t1.animate.shift(DOWN * 1.65), rate_func=ease_in, run_time=0.5)
        until(self, "Two: the subject")
        self.play(t2.animate.shift(DOWN * 1.65), rate_func=ease_in, run_time=0.5)
        until(self, "Three: the style")
        self.play(t3.animate.shift(DOWN * 1.65), rate_func=ease_in, run_time=0.5)
        until(self, "Occasion, subject, style")
        self.play(FadeIn(npop, banner), run_time=0.6)
        finish(self)


class B03_ListenFirst(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        card = song_card(0, 1.0, 3.4, 2.0)
        wave = waveform(0, -1.4, w=6.4, n=24)
        pp = pill(4.0, 1.0, 1.3)
        tri = Polygon([3.85, 1.2, 0], [3.85, 0.8, 0], [4.2, 1.0, 0],
                      fill_color=INK, fill_opacity=1, stroke_width=0)
        head = Line([-3.2, -0.8, 0], [-3.2, -2.0, 0], color=INK, stroke_width=5)
        path = Line([-3.2, -1.4, 0], [3.2, -1.4, 0])
        lab = T("listen first", size=36, color=INK).move_to([0, -2.6, 0])
        ring = Circle(radius=0.95, stroke_color=TERRA, stroke_width=5).move_to([4.0, 1.0, 0])

        self.play(FadeIn(shadow, card, wave, pp, tri, head), run_time=0.7)
        until(self, "Always listen")
        self.play(MoveAlongPath(head, path), run_time=1.2)
        until(self, "So listen first")
        # membership change after the move (Gate A ignores moves): a terracotta ring grows, then fades
        self.play(GrowFromCenter(ring), FadeIn(lab), run_time=0.6)
        self.play(FadeOut(ring), run_time=0.4)
        finish(self)


class B04_TheLoop(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        draft = song_card(-2.9, 0.5, 2.6, 1.9)
        dlab = T("a draft", size=34, color=INK).move_to([-2.9, -1.2, 0])
        win = music_window(3.1, 0.5, 2.8, 2.4)
        shaft = Line([-1.3, 0.5, 0], [1.4, 0.5, 0], color=INK, stroke_width=5)
        ahead = Polygon([1.4, 0.5, 0], [1.12, 0.68, 0], [1.12, 0.32, 0],
                        fill_color=INK, fill_opacity=1, stroke_width=0)
        arrow = VGroup(shaft, ahead)
        fixed = song_card(-2.9, 0.5, 2.6, 1.9)
        chk = check(-1.1, 1.5, s=0.2, color=TERRA, w=8)
        lab2 = T("describe, listen, fix", size=34, color=INK).move_to([3.1, -1.35, 0])

        self.play(FadeIn(shadow, draft, dlab, win), run_time=0.8)
        until(self, "It makes another version")
        self.play(Create(arrow), run_time=0.8)
        until(self, "two or three rounds")
        self.play(FadeOut(draft, dlab), FadeIn(fixed), run_time=0.6)
        self.play(FadeIn(chk, lab2), run_time=0.6)
        finish(self)


class B05_SweetSpot(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 11.0)
        c1 = song_card(-3.6, 0.7, 2.7, 2.0)
        l1 = T("birthday", size=34, color=INK).move_to([-3.6, -1.0, 0])
        c2 = song_card(0, 0.7, 2.7, 2.0)
        l2 = T("a jingle", size=34, color=INK).move_to([0, -1.0, 0])
        c3 = song_card(3.6, 0.7, 2.7, 2.0)
        l3 = T("a lullaby", size=34, color=INK).move_to([3.6, -1.0, 0])

        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "Short, personal things")
        self.play(AnimationGroup(GrowFromCenter(c1), FadeIn(l1),
                                 GrowFromCenter(c2), FadeIn(l2),
                                 GrowFromCenter(c3), FadeIn(l3),
                                 lag_ratio=0.25), run_time=1.6)
        finish(self)


class B06_KeepItShort(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.0)
        # a long track that wanders and fizzles: amplitude decays along x (ink, never terracotta mid-draw)
        track = ParametricFunction(
            lambda t: np.array([t, 0.7 + 0.55 * np.sin(t * 2.2) * max(0.0, (1.5 - t) / 6.5), 0]),
            t_range=[-5.0, 1.5, 0.1], color=INK, stroke_width=6)
        cross = ink_cross(2.9, 0.6, arm=0.4)
        lab1 = T("too long", size=36, color=INK).move_to([0, -2.2, 0])
        lab2 = T("under three minutes", size=36, color=INK).move_to([0, -2.2, 0])

        self.play(FadeIn(shadow), run_time=0.4)
        until(self, "Ask for a five-minute epic")
        self.play(Create(track), run_time=1.0)
        until(self, "the ending fizzles")
        self.play(FadeIn(cross, lab1), run_time=0.5)
        until(self, "So keep it short")
        self.play(FadeOut(lab1), run_time=0.4)
        self.play(FadeIn(lab2), run_time=0.5)
        finish(self)


class B07_WhyNow(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.0)
        hero = T("44%", size=150, color=INK, bold=True).move_to([-3.0, 0.7, 0])
        sub = T("AI-made uploads", size=36, color=INK).move_to([-3.0, -1.15, 0])
        curve = ParametricFunction(lambda t: np.array([t, -1.6 + 3.4 * ((t + 2.2) / 5.4) ** 2, 0]),
                                   t_range=[-2.2, 3.2, 0.05], color=INK, stroke_width=7)
        enddot = Dot([3.2, 1.8, 0], radius=0.11, color=TERRA)
        caption = T("per Deezer", size=32, color=INK).move_to([0.5, -2.2, 0])

        self.play(FadeIn(shadow), run_time=0.4)
        until(self, "Deezer")
        self.play(FadeIn(hero, sub), run_time=0.7)
        self.play(Create(curve), FadeIn(enddot), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.6)
        finish(self)
