"""scenes.py — "Claude, Not Your Answer." (show-tell).

9 Manim scenes, B00-B08, one drawn isometric illustration per beat.
House palette (cream stage, warm ink, terracotta accents); iso_kit pasted at top
(Gate A copies only scenes.py). Each scene adds new non-text shapes after
its first frame; labels sit beside objects; type floor 32; coords within
+-6.2 x +-3.3 y.
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

# ═════════════════════════════ film helpers ═════════════════════════════

def lab(s, x, y, size=34, color=INK):
    return T(s, size=size, color=color).move_to([x, y, 0])


def doc(x, y, w=1.7, h=2.1):
    """Flat document card: white card, ghost text lines, terracotta dot."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.12,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    for f in (0.30, 0.50, 0.70):
        ly = y + h / 2 - f * h
        g.add(Line([x - w / 2 + 0.25, ly, 0], [x + w / 2 - 0.25, ly, 0],
                   color=GHOST, stroke_width=5))
    g.add(Dot([x - w / 2 + 0.25, y + h / 2 - 0.13 * h, 0],
              radius=0.07, color=TERRA))
    return g


def chat_window(x, y, w=6.0, h=3.8, title="Claude"):
    """Pale UI panel with a dark title bar (carries the contrast)."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.18,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=4).move_to([x, y, 0]))
    g.add(RoundedRectangle(width=w, height=0.72, corner_radius=0.18,
                           fill_color=DARK_TOP, fill_opacity=1,
                           stroke_width=0).move_to([x, y + h / 2 - 0.36, 0]))
    g.add(T(title, size=30, color="#FFFFFF")
          .move_to([x - w / 2 + 1.0, y + h / 2 - 0.36, 0]))
    for fy in (0.28, 0.06, -0.16):
        g.add(RoundedRectangle(width=w - 1.6, height=0.3, corner_radius=0.15,
                               fill_color=GHOST, fill_opacity=1,
                               stroke_width=0).move_to([x - 0.2, y + fy * h, 0]))
    return g


def toggle(x, y, on=True):
    """A settings toggle: track + knob. Returns (group, knob)."""
    track = RoundedRectangle(width=2.1, height=0.85, corner_radius=0.42,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    kx = x + (0.63 if on else -0.63)
    knob = Circle(radius=0.32, fill_color=INK if on else DIM,
                  fill_opacity=1, stroke_width=0).move_to([kx, y, 0])
    return VGroup(track, knob), knob


def x_mark(x, y, s=0.55):
    return VGroup(
        Line([x - s, y + s * 0.8, 0], [x + s, y - s * 0.8, 0],
             color=INK, stroke_width=9),
        Line([x - s, y - s * 0.8, 0], [x + s, y + s * 0.8, 0],
             color=INK, stroke_width=9))


# ═════════════════════════════ scenes: one per body beat ═════════════════════════════

class B00_ThePaste(Scene):
    def construct(self):
        win = chat_window(1.5, 0.1, title="Claude")
        d = doc(-4.4, 0.6)
        cur = cursor(-3.2, 1.9)
        self.play(FadeIn(win), run_time=0.7)
        self.play(FadeIn(d), FadeIn(cur), run_time=0.6)
        until(self, "You paste it in")
        self.play(d.animate.move_to([1.5, 0.1, 0]),
                  cur.animate.move_to([2.9, 0.2, 0]), run_time=0.9)
        ring = Circle(radius=1.45, color=INK, stroke_width=5).move_to([1.5, 0.1, 0])
        self.play(GrowFromCenter(ring), run_time=0.6)
        self.play(FadeIn(lab("your chat", -0.3, -2.5)),
                  FadeIn(lab("the paste", 3.1, -2.5)), run_time=0.5)
        finish(self)


class B01_Samsung(Scene):
    def construct(self):
        win = chat_window(2.6, 0.1, w=4.8, h=3.4, title="ChatGPT")
        slots = [(-4.6, 2.1), (-4.6, 0.3), (-4.6, -1.5)]
        names = ["code", "code", "meeting"]
        docs = [doc(x, y) for x, y in slots]
        tags = [lab(n, -1.85, y) for n, (x, y) in zip(names, slots)]
        cues = ["source code", "equipment code", "a whole meeting"]
        self.play(FadeIn(win), run_time=0.7)
        for d, t, cue in zip(docs, tags, cues):
            until(self, cue)
            self.play(FadeIn(d), FadeIn(t), run_time=0.5)
            self.play(d.animate.move_to([2.6, 0.1, 0]), run_time=0.7)
            self.play(FadeOut(d), run_time=0.35)
        until(self, "banned the tools")
        ban = Circle(radius=2.0, color=INK, stroke_width=10).move_to([2.6, 0.1, 0])
        slash = Line([1.3, 1.5, 0], [3.9, -1.3, 0], color=INK, stroke_width=10)
        self.play(Create(ban), Create(slash), run_time=0.7)
        self.play(FadeIn(lab("banned", 2.6, -2.55)), run_time=0.5)
        finish(self)


class B02_TheMechanism(Scene):
    def construct(self):
        win = chat_window(-3.6, 0.3, w=3.4, h=2.6, title="Claude")
        iso = Iso(1.9, -0.9, 0.9)
        stack, lights = iso.server(0, 0, 0)
        cable = Line([-1.9, 0.3, 0], [0.5, -0.3, 0], color=DIM, stroke_width=5)
        self.play(FadeIn(win), FadeIn(lab("your chats", -3.6, -1.5)), run_time=0.7)
        self.play(FadeIn(stack), run_time=0.6)
        until(self, "train the model")
        self.play(Create(cable), run_time=0.6)
        dots = VGroup(*[Dot(iso.p(0.25, 0, 0.21 + i * 0.46),
                            radius=0.075, color=TERRA) for i in range(3)])
        self.play(FadeIn(dots), run_time=0.5)
        until(self, "five years")
        chip = pill(4.6, -0.5, 3.0)
        self.play(FadeIn(chip), FadeIn(lab("5 years", 4.6, -0.5)), run_time=0.5)
        until(self, "on by default")
        tg, knob = toggle(1.9, 2.15, on=True)
        self.play(FadeIn(tg), run_time=0.5)
        self.play(FadeIn(lab("training", 1.9, -1.75)), run_time=0.4)
        finish(self)


class B03_TheToggle(Scene):
    def construct(self):
        panel = RoundedRectangle(width=5.8, height=4.4, corner_radius=0.18,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4).move_to([-1.2, 0, 0])
        bar = RoundedRectangle(width=5.8, height=0.8, corner_radius=0.18,
                               fill_color=DARK_TOP, fill_opacity=1,
                               stroke_width=0).move_to([-1.2, 1.8, 0])
        title = T("Settings", size=34, color="#FFFFFF").move_to([-3.4, 1.8, 0])
        self.play(FadeIn(panel), FadeIn(bar), FadeIn(title), run_time=0.7)
        rows = VGroup()
        for nm, ry in [("General", 1.0), ("Privacy", 0.1), ("Data", -0.8)]:
            rows.add(RoundedRectangle(width=5.0, height=0.7, corner_radius=0.15,
                                      fill_color=GHOST, fill_opacity=1,
                                      stroke_width=0).move_to([-1.2, ry, 0]))
            rows.add(T(nm, size=30, color=INK).move_to([-2.4, ry, 0]))
        self.play(FadeIn(rows), run_time=0.6)
        until(self, "Settings, then Privacy")
        hi = RoundedRectangle(width=5.2, height=0.9, corner_radius=0.2,
                              fill_opacity=0,
                              stroke_color=INK, stroke_width=4).move_to([-1.2, 0.1, 0])
        self.play(Create(hi), run_time=0.5)
        tg, knob = toggle(3.9, 0.1, on=True)
        cur = cursor(5.0, 0.8)
        self.play(FadeIn(tg), FadeIn(cur), run_time=0.5)
        until(self, "switch the training toggle off")
        self.play(cur.animate.move_to([4.53, 0.1, 0]), run_time=0.5)
        self.play(knob.animate.move_to([3.9 - 0.63, 0.1, 0]).set_fill(DIM),
                  run_time=0.5)
        self.play(FadeIn(lab("OFF", 3.9, -0.85)), run_time=0.4)
        finish(self)


class B04_Everywhere(Scene):
    def construct(self):
        knobs = []
        for x, app in [(-4.1, "ChatGPT"), (0.0, "Grok"), (4.1, "Gemini")]:
            panel = RoundedRectangle(width=3.5, height=3.4, corner_radius=0.18,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=4).move_to([x, 0.1, 0])
            self.play(FadeIn(panel), FadeIn(lab(app, x, 1.25)), run_time=0.5)
            tg, knob = toggle(x, -0.5, on=True)
            knobs.append((x, knob))
            self.play(FadeIn(tg), run_time=0.4)
        for (x, knob), cue in zip(knobs, ["ChatGPT", "Grok", "Gemini"]):
            until(self, cue)
            self.play(knob.animate.move_to([x - 0.63, -0.5, 0]).set_fill(DIM),
                      run_time=0.5)
        finish(self)


class B05_GoingForward(Scene):
    def construct(self):
        tg, knob = toggle(-2.8, 0.3, on=False)
        self.play(FadeIn(tg), run_time=0.5)
        until(self, "going forward")
        arrow = Arrow([-1.4, 0.3, 0], [0.9, 0.3, 0], color=INK, stroke_width=8)
        self.play(Create(arrow), FadeIn(lab("from now on", -0.25, 1.2)),
                  run_time=0.6)
        until(self, "already used")
        iso = Iso(3.4, -1.7, 0.75)
        box = iso.box(0, 0, 0, 1.7, 1.7, 1.3)
        tape = iso.tape(0, 0, 1.3, 1.7, 1.7)
        lock = VGroup(
            RoundedRectangle(width=0.55, height=0.65, corner_radius=0.1,
                             fill_color=DARK_TOP, fill_opacity=1,
                             stroke_width=0).move_to([3.4, 0.0, 0]),
            Arc(radius=0.28, start_angle=0, angle=PI, color=DARK_TOP,
                stroke_width=8).move_to([3.4, 0.35, 0]))
        self.play(FadeIn(box), FadeIn(tape), run_time=0.6)
        self.play(FadeIn(lock), FadeIn(lab("already used", 3.4, -2.55)),
                  run_time=0.5)
        finish(self)


class B06_Legal(Scene):
    def construct(self):
        d = doc(0, 2.2, w=1.5, h=1.0)
        self.play(FadeIn(d), run_time=0.6)
        for x, nm, cue in [(-3.7, "NDA", "your NDA"),
                           (0.0, "data law", "data protection law"),
                           (3.7, "IT policy", "IT policy")]:
            until(self, cue)
            seal = RoundedRectangle(width=2.7, height=2.7, corner_radius=0.3,
                                    fill_color=BOX_TOP, fill_opacity=1,
                                    stroke_color=INK, stroke_width=4).move_to([x, -0.1, 0])
            self.play(GrowFromCenter(seal), run_time=0.55)
            self.play(FadeIn(lab(nm, x, -2.05)), run_time=0.4)
        finish(self)


class B07_CleanRoom(Scene):
    def construct(self):
        xs = [-4.65, -1.55, 1.55, 4.65]
        names = ["names", "financials", "code", "meetings"]
        cues = ["client names", "internal financials", "source code",
                "meeting recordings"]
        docs = [doc(x, 0.9, w=1.6, h=1.8) for x in xs]
        tags = [lab(nm, x, -0.4, size=32) for nm, x in zip(names, xs)]
        self.play(*[FadeIn(d) for d in docs], *[FadeIn(t) for t in tags],
                  run_time=0.7)
        for x, cue in zip(xs, cues):
            until(self, cue)
            self.play(Create(x_mark(x, 0.9)), run_time=0.5)
        until(self, "swap real names for placeholders")
        self.play(*[FadeOut(d) for d in docs], *[FadeOut(t) for t in tags],
                  run_time=0.5)
        demo = doc(0, 0.5, w=3.6, h=2.4)
        name = T("Acme Corp", size=32).move_to([0, 0.5, 0])
        self.play(FadeIn(demo), FadeIn(name), run_time=0.6)
        anon = T("[CLIENT]", size=32).move_to([0, 0.5, 0])
        self.play(FadeOut(name), FadeIn(anon),
                  FadeIn(lab("anonymize", 0, -1.55)), run_time=0.6)
        finish(self)


class B08_Enterprise(Scene):
    def construct(self):
        for by in [-1.5, -0.45, 0.6]:
            blk = RoundedRectangle(width=3.4, height=0.95, corner_radius=0.12,
                                   fill_color=BOX_TOP, fill_opacity=1,
                                   stroke_color=INK, stroke_width=4).move_to([-1.6, by, 0])
            self.play(FadeIn(blk), run_time=0.45)
        self.play(FadeIn(lab("Enterprise", -1.6, -2.35)), run_time=0.4)
        until(self, "do not train on your data")
        shield = Polygon([3.0, 1.4, 0], [4.0, 0.95, 0], [4.0, 0.0, 0],
                         [3.0, -0.9, 0], [2.0, 0.0, 0], [2.0, 0.95, 0],
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=4)
        self.play(GrowFromCenter(shield), run_time=0.6)
        self.play(Create(check(3.0, 0.15, s=0.3, color=TERRA)), run_time=0.5)
        self.play(FadeIn(lab("no training", 3.0, -1.6)), run_time=0.4)
        finish(self)
