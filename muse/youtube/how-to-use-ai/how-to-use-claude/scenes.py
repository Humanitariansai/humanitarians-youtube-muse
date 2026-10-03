"""scenes.py — show-tell: How to Use Claude (Liam, Teardown, claude-liam).

Nine drawn body beats, one Manim scene per beat. The iso_kit block is pasted
verbatim at the top (Gate A copies only this file — never import the kit).
Film helpers (chat window, doc cards, labels) follow the kit; every scene
class is written literally as `class BNN_Name(Scene):`.

Drawing laws obeyed: labels sit beside objects (never inside, never on
terracotta); terracotta only for tape/dots/lights/checks/scan lines; chart
blocks in BAR1/BAR2/BAR3 with gaps; type >= 32; every coordinate inside
+-6.2 x +-3.3; every scene adds a new non-text shape after its first frame;
no path_arc, no ease_in_quad/ease_out_cubic; no MoveAlongPath + .animate on
the same object in one play; major motion is kept off the clip midpoint via
until() phrase timing (see SHOTLIST.md).

Pacing: until()/finish() read beat_sheet.json beside this file (the measured
Kokoro audio at render time); with no sheet they degrade to short waits.
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


# ═════════════════════════════ film helpers (how-to-use-claude) ═════════════════════════════
def chat_window(cx=0.0, cy=0.0, w=5.2, h=3.1, composer=True):
    """Front-facing Claude chat window: ink-outlined cream card, thin dark title
    strip (carries contrast on the pale panel), composer pill at the bottom."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    bar = RoundedRectangle(width=w - 0.04, height=0.5, corner_radius=0.15, fill_color=DARK_TOP,
                           fill_opacity=1, stroke_width=0).move_to([cx, cy + h / 2 - 0.26, 0])
    parts = [body, bar]
    if composer:
        comp = RoundedRectangle(width=w * 0.8, height=0.58, corner_radius=0.29, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([cx, cy - h / 2 + 0.6, 0])
        parts.append(comp)
    return VGroup(*parts)


def doc_card(x, y, w=1.5, h=1.9, outline=DIM, dot=True, lines=3):
    """Small flat document card. Grey outline so it stays legible inside
    ink-outlined containers (GATE T: ink-in-ink reads as overlapping text)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=outline, stroke_width=2).move_to([x, y, 0])
    ls = VGroup(*[Line([x - w / 2 + 0.24, y + h / 2 - 0.42 - i * 0.36, 0],
                       [x + w / 2 - 0.24 - (0.35 if i == lines - 1 else 0), y + h / 2 - 0.42 - i * 0.36, 0],
                       color=GHOST, stroke_width=4) for i in range(lines)])
    parts = [card, ls]
    if dot:
        parts.append(Dot([x - w / 2 + 0.3, y + h / 2 - 0.24, 0], radius=0.06, color=TERRA))
    return VGroup(*parts)


def tag(text, lx, ly, ox, oy, size=36):
    """Ink label at (lx, ly) with a dim leader line from object point (ox, oy).
    The leader stops 0.35 units short of the label (GATE T: a touching leader fails)."""
    lab = T(text, size=size).move_to([lx, ly, 0])
    half = lab.width / 2 + 0.35
    d = np.array([lx - ox, ly - oy, 0.0])
    n = np.linalg.norm(d)
    d = d / n if n > 1e-6 else np.array([1.0, 0.0, 0.0])
    end = np.array([lx, ly, 0.0]) - d * half
    line = Line([ox, oy, 0], end, color=DIM, stroke_width=2)
    return VGroup(line, lab)


# ═════════════════════════════ scenes ═════════════════════════════
class B00_ChatWindow(Scene):
    """The hero object: the Claude chat window drops in; cursor lands in the
    composer; reply lines appear above it."""

    def construct(self):
        win = chat_window(-0.8, 0.05)
        win.shift(UP * 0.8)
        lab = tag("chat window", 3.7, 1.5, 1.8, 0.9)
        self.play(FadeIn(win), win.animate.shift(DOWN * 0.8), FadeIn(lab), run_time=1.0)
        until(self, "You type at the bottom")
        cur = cursor(-2.35, -0.72)
        self.play(FadeIn(cur), run_time=0.6)
        until(self, "answer appears above")
        reply = VGroup(
            Line([-2.9, 0.55, 0], [0.4, 0.55, 0], color=INK, stroke_width=5),
            Line([-2.9, 0.2, 0], [-0.5, 0.2, 0], color=INK, stroke_width=5))
        self.play(Create(reply), run_time=0.8)
        finish(self)


class B01_ModelBehind(Scene):
    """What it is: a dark model block fades in behind the window; its lights come on."""

    def construct(self):
        win = chat_window(0.9, 0.0, w=4.6, h=2.9)
        self.add(win)
        model = RoundedRectangle(width=3.0, height=2.2, corner_radius=0.2, fill_color=DARK_TOP,
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-2.6, -0.15, 0])
        lab = tag("model", -2.6, 1.6, -2.6, 0.95)
        self.play(FadeIn(model), FadeIn(lab), run_time=0.9)
        self.bring_to_front(win)
        until(self, "answer questions well")
        lights = VGroup(*[Dot([x, 0.6, 0], radius=0.09, color=TERRA) for x in (-3.7, -3.1, -2.5)])
        self.play(FadeIn(lights), run_time=0.7)
        finish(self)


class B02_Stranger(Scene):
    """The failure: one question, one thin answer, tab closed — answering a stranger."""

    def construct(self):
        win = chat_window(-0.5, 0.1)
        self.add(win)
        until(self, "One question")
        qb = VGroup(
            RoundedRectangle(width=2.7, height=0.62, corner_radius=0.31, fill_color="#FFFFFF",
                             fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([-0.5, -0.85, 0]),
            Line([-1.55, -0.85, 0], [0.35, -0.85, 0], color=GHOST, stroke_width=4))
        self.play(FadeIn(qb), run_time=0.6)
        until(self, "one answer")
        reply = VGroup(
            Line([-2.7, 0.62, 0], [-0.9, 0.62, 0], color=INK, stroke_width=5),
            Line([-2.7, 0.28, 0], [-1.6, 0.28, 0], color=INK, stroke_width=5))
        self.play(Create(reply), run_time=0.6)
        until(self, "close the tab")
        self.play(FadeOut(win), FadeOut(qb), run_time=0.8)
        until(self, "answers a stranger")
        lab = tag("a stranger", 2.9, 0.45, -0.9, 0.45)
        self.play(FadeIn(lab), run_time=0.6)
        finish(self)


class B03_ContextIn(Scene):
    """The mechanism: context cards drop into the window; the reply grows full."""

    def construct(self):
        win = chat_window(-1.2, 0.0, w=5.6, h=3.4, composer=False)
        self.add(win)
        lab_c = tag("context", 2.75, 1.15, 0.4, 0.9)
        until(self, "your project")
        c1 = doc_card(-3.3, 0.62, 1.35, 1.5)
        c1.shift(UP * 1.5)
        self.play(FadeIn(c1), c1.animate.shift(DOWN * 1.5), FadeIn(lab_c), run_time=0.8)
        until(self, "your constraints")
        c2 = doc_card(-1.85, 0.62, 1.35, 1.5)
        c2.shift(UP * 1.5)
        self.play(FadeIn(c2), c2.animate.shift(DOWN * 1.5), run_time=0.8)
        until(self, "an example")
        c3 = doc_card(-0.4, 0.62, 1.35, 1.5)
        c3.shift(UP * 1.5)
        self.play(FadeIn(c3), c3.animate.shift(DOWN * 1.5), run_time=0.8)
        until(self, "lands close")
        ans = doc_card(-1.2, -0.85, 2.7, 1.0, lines=4, dot=False)
        lab_a = tag("answer", 2.75, -1.05, 0.15, -0.85)
        self.play(GrowFromCenter(ans), FadeIn(lab_a), run_time=1.0)
        finish(self)


class B04_Project(Scene):
    """The fix: a Project box; style, rules and example drop in once; a chat
    rides through and an informed reply comes out."""

    def construct(self):
        iso = Iso(-3.6, -1.0, 1.05)
        back, front = iso.open_box(0, 0, 0, 2.1, 2.1, 1.6)
        lab = tag("project", -0.3, 1.35, -1.9, 0.55)
        self.play(FadeIn(back), FadeIn(front), FadeIn(lab), run_time=1.0)
        until(self, "your style")
        s1 = doc_card(-4.35, 1.7, 1.2, 1.5); s1.shift(UP * 1.2)
        t1 = T("style", size=32).move_to([-4.35, -0.15, 0])
        self.play(FadeIn(s1), s1.animate.shift(DOWN * 1.2), FadeIn(t1), run_time=0.8)
        until(self, "your constraints")
        s2 = doc_card(-3.35, 1.7, 1.2, 1.5); s2.shift(UP * 1.2)
        t2 = T("rules", size=32).move_to([-3.35, -0.15, 0])
        self.play(FadeIn(s2), s2.animate.shift(DOWN * 1.2), FadeIn(t2), run_time=0.8)
        until(self, "an example you like")
        s3 = doc_card(-2.35, 1.7, 1.2, 1.5); s3.shift(UP * 1.2)
        t3 = T("example", size=32).move_to([-2.35, -0.15, 0])
        self.play(FadeIn(s3), s3.animate.shift(DOWN * 1.2), FadeIn(t3), run_time=0.8)
        until(self, "every chat inside")
        msg = pill(4.4, 0.5, 2.3)
        self.play(FadeIn(msg), run_time=0.5)
        self.play(MoveAlongPath(msg, ArcBetweenPoints(np.array([4.4, 0.5, 0]),
                                                      np.array([0.7, 0.5, 0]), angle=0.35)), run_time=1.0)
        out = doc_card(2.9, -1.35, 2.0, 1.4, lines=4, dot=False)
        self.play(GrowFromCenter(out), run_time=0.8)
        finish(self)


class B05_Artifact(Scene):
    """Strength one: artifacts — a finished piece built in a panel beside the chat."""

    def construct(self):
        win = chat_window(-2.4, 0.0, w=3.6, h=2.9)
        self.add(win)
        until(self, "finished piece")
        panel = RoundedRectangle(width=2.8, height=3.0, corner_radius=0.15, fill_color="#FFFFFF",
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([2.4, 0.0, 0])
        lab = tag("artifact", 2.4, 2.1, 2.4, 1.5)
        self.play(GrowFromCenter(panel), FadeIn(lab), run_time=1.2)
        page = doc_card(2.4, 0.05, 2.2, 2.3)
        self.play(FadeIn(page), run_time=0.6)
        finish(self)


class B06_Analysis(Scene):
    """Strength two: analysis — a scan sweeps the long document; its structure map appears."""

    def construct(self):
        pages = VGroup(*[doc_card(-3.4 + i * 0.12, -0.1 + i * 0.2, 1.8, 2.4) for i in range(3)])
        self.play(FadeIn(pages), run_time=0.8)
        until(self, "something long")
        scan = Line([-4.55, 1.5, 0], [-2.25, 1.5, 0], color=TERRA, stroke_width=5)
        self.play(Create(scan), run_time=0.3)
        self.play(scan.animate.shift(DOWN * 2.9), run_time=1.2)
        self.play(FadeOut(scan), run_time=0.3)
        until(self, "shape of the thing")
        struct = VGroup(*[RoundedRectangle(width=2.8, height=0.55, corner_radius=0.08,
                                           fill_color=c, fill_opacity=1,
                                           stroke_color=DIM, stroke_width=1).move_to([1.9, y, 0])
                           for c, y in ((BAR1, 0.75), (BAR2, 0.0), (BAR3, -0.75))])
        lab = tag("analysis", 1.9, 1.8, 1.9, 1.05)
        self.play(FadeIn(struct), FadeIn(lab), run_time=0.8)
        finish(self)


class B07_Rewrite(Scene):
    """Strength three: rewriting — rough draft plus a voice example in; a polished page out."""

    def construct(self):
        draft = doc_card(-3.7, 0.0, 1.7, 2.3)
        lab1 = tag("rough draft", -3.7, 1.75, -3.7, 1.15)
        self.play(FadeIn(draft), FadeIn(lab1), run_time=0.8)
        until(self, "the voice you want")
        voice = doc_card(-1.3, 0.0, 1.7, 2.3)
        lab2 = tag("your voice", -1.3, 1.75, -1.3, 1.15)
        self.play(FadeIn(voice), FadeIn(lab2), run_time=0.8)
        until(self, "and you spend your time")
        final = doc_card(2.9, 0.0, 2.0, 2.5, lines=4)
        chk = check(2.9, 0.35, s=0.4, color=TERRA, w=9)
        self.play(GrowFromCenter(final), run_time=1.0)
        self.play(FadeIn(chk), run_time=0.5)
        finish(self)


class B08_CheckIt(Scene):
    """The catch: one factual claim in a bubble; a check stamps onto it."""

    def construct(self):
        bubble = RoundedRectangle(width=5.8, height=1.3, corner_radius=0.2, fill_color="#FFFFFF",
                                  fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0, 0.7, 0])
        claim = T("The Eiffel Tower is 330 metres tall.", size=32).move_to([0, 0.7, 0])
        lab = tag("check it", -3.7, -1.5, -2.3, 0.05)
        self.play(FadeIn(bubble), FadeIn(claim), FadeIn(lab), run_time=0.8)
        until(self, "check them")
        chk = check(3.15, 0.7, s=0.5, color=TERRA, w=10)
        self.play(GrowFromCenter(chk), run_time=0.6)
        finish(self)
