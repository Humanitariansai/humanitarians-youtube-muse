"""
scenes.py — Muse Does the Assignment (lecture, INFO 6205).

14 Manim scenes, one per body beat (B01–B14). Claude palette, EB Garamond,
16:9 stage. Every number on screen is a computed value from the real solution
runs (see FACTCHECK.md); nothing is invented.

Grid helper draws the assignment's grids; BFS orders are computed inline with
a tiny BFS (same algorithm as solution.py) so the waves are honest.
"""
from manim import *
import numpy as np
from collections import deque

config.background_color = "#F2F0E9"

STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"
GHOST = "#D9D4C7"; CARD = "#FAF9F5"; KRAFT = "#F3E9D8"
SERIF = "EB Garamond"


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size,
                weight="BOLD" if bold else "NORMAL")


def bfs_order(grid, src):
    """BFS visit order (list of cells) from src on a grid; 'O' blocks."""
    rows, cols = len(grid), len(grid[0])
    seen = {src}; q = deque([src]); order = []
    while q:
        r, c = q.popleft(); order.append((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "O" \
                    and (nr, nc) not in seen:
                seen.add((nr, nc)); q.append((nr, nc))
    return order


class Grid:
    """A labeled grid on the stage. Row 0 at top. center = grid center."""

    def __init__(self, rows, cols, cell=0.95, center=LEFT * 2.2):
        self.rows, self.cols, self.cell = rows, cols, cell
        self.cx, self.cy = center[0], center[1]
        self.squares = VGroup(*[
            Rectangle(width=cell, height=cell, stroke_color=INK,
                      stroke_width=3, fill_color=CARD, fill_opacity=1)
            .move_to(self.at(r, c))
            for r in range(rows) for c in range(cols)])
        self.group = VGroup(self.squares)

    def at(self, r, c):
        x = self.cx + (c - (self.cols - 1) / 2) * self.cell
        y = self.cy - (r - (self.rows - 1) / 2) * self.cell
        return np.array([x, y, 0.0])

    def mark(self, r, c, text, color=INK, size=40, bold=True):
        t = T(text, size=size, color=color, bold=bold).move_to(self.at(r, c))
        self.group.add(t)
        return t

    def shade(self, r, c, color):
        idx = r * self.cols + c
        self.squares[idx].set_fill(color, opacity=1)

    def path_vm(self, cells, color=TERRA, width=8):
        pts = [self.at(r, c) for r, c in cells]
        return VMobject().set_points_as_corners(pts).set_stroke(color, width)

    def dot(self, r, c, color=TERRA, radius=0.14):
        return Dot(self.at(r, c), radius=radius, color=color,
                   stroke_color=INK, stroke_width=2)


EXAMPLE = [
    ["B", ".", "H"],
    ["O", "O", "."],
    ["H", ".", "H"],
]
# The optimal 12-step tour on EXAMPLE (verified by solution.py).
TOUR12 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1),
          (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0)]
TOUR6 = TOUR12[:7]  # the no-return tour the assignment's "6" describes

TRAP = [
    ["B", ".", ".", "."],
    [".", "H", ".", "."],
    ["H", ".", ".", "."],
    [".", "H", ".", "."],
]
GREEDY10 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0),
            (1, 1), (2, 1), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0)]
# greedy: B -> (1,1) -> (2,0) -> (3,1) -> B = 2+2+2+4 = 10 steps
OPT8 = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (2, 1),
        (1, 1), (0, 1), (0, 0)]
# optimal: B -> (2,0) -> (3,1) -> (1,1) -> B = 2+2+2+2 = 8 steps


def legend_row():
    return VGroup(
        T("B start", size=30), T("H honey", size=30),
        T("O blocked", size=30)).arrange(RIGHT, buff=0.6)


def checkmark(pos, scale=1.0, color=TERRA):
    """A drawn check mark (two strokes) — a real shape, not a text glyph."""
    p1 = np.array([-0.22, -0.02, 0.0]) * scale + pos
    p2 = np.array([-0.02, -0.20, 0.0]) * scale + pos
    p3 = np.array([0.26, 0.22, 0.0]) * scale + pos
    return VGroup(Line(p1, p2, stroke_color=color, stroke_width=9),
                  Line(p2, p3, stroke_color=color, stroke_width=9))


class B01_Grid(Scene):
    def construct(self):
        g = Grid(3, 3)
        self.play(Create(g.squares), run_time=1.6)
        marks = VGroup(g.mark(0, 0, "B", TERRA), g.mark(0, 2, "H"),
                       g.mark(2, 0, "H"), g.mark(2, 2, "H"),
                       g.mark(1, 0, "O", DIM), g.mark(1, 1, "O", DIM))
        self.play(FadeIn(marks), run_time=1.4)
        labels = VGroup(
            T("start", size=28, color=DIM).next_to(g.at(0, 0), UP, buff=0.55),
            T("honey", size=28, color=DIM).next_to(g.at(0, 2), UP, buff=0.55),
            T("blocked", size=28, color=DIM).next_to(g.at(1, 0), LEFT, buff=0.6),
        )
        self.play(FadeIn(labels), run_time=1.2)
        dot = g.dot(0, 0)
        self.play(FadeIn(dot), run_time=0.6)
        self.play(dot.animate.scale(1.35), run_time=0.5)
        self.play(dot.animate.scale(1 / 1.35), run_time=0.5)
        title = T("Beary's grid", size=40, bold=True).to_edge(UP, buff=0.6).shift(RIGHT * 2.2)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(8.0)


class B02_Rules(Scene):
    def construct(self):
        g = Grid(3, 3, center=LEFT * 2.6)
        for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
            g.mark(*args)
        for (r, c) in [(1, 0), (1, 1)]:
            g.mark(r, c, "O", DIM)
        self.add(g.group)
        path = g.path_vm(TOUR12, color=GHOST, width=6)
        self.play(Create(path), run_time=1.2)
        counter = T("0", size=56, bold=True, color=TERRA).move_to(RIGHT * 3.4 + UP * 1.6)
        clabel = T("steps", size=30, color=DIM).next_to(counter, DOWN, buff=0.15)
        self.play(FadeIn(VGroup(counter, clabel)), run_time=0.6)
        dot = g.dot(*TOUR12[0])
        self.add(dot)
        honey_cells = {(0, 2), (2, 2), (2, 0)}
        step = 0
        for i in range(1, len(TOUR12)):
            step += 1
            new = T(str(step), size=56, bold=True, color=TERRA).move_to(counter.get_center())
            anims = [dot.animate.move_to(g.at(*TOUR12[i])), Transform(counter, new)]
            if TOUR12[i] in honey_cells:
                check = checkmark(g.at(*TOUR12[i]) + UP * 0.62, scale=0.9)
                anims.append(FadeIn(check))
                honey_cells.discard(TOUR12[i])
            self.play(*anims, run_time=0.55)
        home = T("home", size=30, color=TERRA, bold=True).next_to(g.at(0, 0), DOWN, buff=0.5)
        rule = T("collect all · return · fewest steps", size=30, color=DIM).move_to(RIGHT * 3.4 + DOWN * 1.4)
        self.play(FadeIn(VGroup(home, rule)), run_time=1.0)
        self.wait(3.0)


class B03_Example(Scene):
    def construct(self):
        g = Grid(3, 3, center=LEFT * 2.4)
        for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
            g.mark(*args)
        for (r, c) in [(1, 0), (1, 1)]:
            g.mark(r, c, "O", DIM)
        self.add(g.group)
        tag = T("says: 6", size=44, bold=True, color=INK)
        tag.move_to(RIGHT * 3.2 + UP * 1.8)
        tagbox = SurroundingRectangle(tag, color=INK, buff=0.25, stroke_width=3)
        self.play(FadeIn(VGroup(tag, tagbox)), run_time=0.8)
        tour = g.path_vm(TOUR6, color=DIM, width=7)
        self.play(Create(tour), run_time=2.2)
        ret = g.path_vm(TOUR12[6:], color=TERRA, width=7)
        self.play(Create(ret), run_time=2.0)
        q = T("?", size=72, bold=True, color=TERRA).move_to(tag.get_center())
        self.play(Transform(tag, q), run_time=0.9)
        note = T("we'll come back to this", size=30, color=DIM).move_to(RIGHT * 3.2 + DOWN * 0.6)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(6.0)


class B04_Legs(Scene):
    def construct(self):
        g = Grid(3, 3, center=LEFT * 3.0)
        for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
            g.mark(*args)
        for (r, c) in [(1, 0), (1, 1)]:
            g.mark(r, c, "O", DIM)
        self.add(g.group)
        order = bfs_order(EXAMPLE, (0, 0))
        dist = {}
        dq = deque([(0, 0, 0)]); seen = {(0, 0)}
        while dq:
            r, c, d = dq.popleft(); dist[(r, c)] = d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < 3 and 0 <= nc < 3 and EXAMPLE[nr][nc] != "O" and (nr, nc) not in seen:
                    seen.add((nr, nc)); dq.append((nr, nc, d + 1))
        # wave: light cells ring by ring with overlay highlights (new shapes,
        # so the motion registers; mutating fill in place would not)
        def overlay(cells):
            vg = VGroup(*[
                Rectangle(width=g.cell, height=g.cell, stroke_width=0,
                          fill_color=TERRA, fill_opacity=0.30).move_to(g.at(r, c))
                for (r, c) in cells])
            g.group.add(vg)
            return vg
        batches = [[c for c, d in dist.items() if d in (1, 2)],
                   [c for c, d in dist.items() if d in (3, 4)],
                   [c for c, d in dist.items() if d in (5, 6)]]
        for batch in batches:
            if batch:
                self.play(FadeIn(overlay(batch)), run_time=0.9)
        for (r, c), want in [((0, 2), 2), ((2, 2), 4), ((2, 0), 6)]:
            lab = T(str(want), size=30, color=TERRA, bold=True).next_to(g.at(r, c), DOWN, buff=0.45)
            self.play(FadeIn(lab), run_time=0.4)
        table = VGroup(
            T("leg   steps", size=30, bold=True),
            T("B → H1      2", size=30),
            T("B → H2      4", size=30),
            T("B → H3      6", size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(RIGHT * 3.6 + UP * 0.4)
        tbox = Rectangle(width=3.6, height=2.4, stroke_color=INK, stroke_width=3,
                         fill_color=CARD, fill_opacity=1).move_to(table.get_center())
        self.play(FadeIn(VGroup(tbox, table)), run_time=1.2)
        self.wait(8.0)


class B05_Order(Scene):
    def construct(self):
        title = T("every subset, cheapest finish", size=36, bold=True).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.7)
        # subset lattice for 3 honey pots: columns by subset size
        cols = [[()], [(0,), (1,), (2,)], [(0, 1), (0, 2), (1, 2)], [(0, 1, 2)]]
        nodes = {}
        for ci, col in enumerate(cols):
            x = -4.5 + ci * 3.0
            for ri, s in enumerate(col):
                y = (len(col) - 1) / 2 * -1.1 + ri * 1.1
                label = "{}" if not s else "".join(f"H{i+1}" for i in s)
                node = VGroup(
                    Circle(radius=0.42, stroke_color=INK, stroke_width=3,
                           fill_color=CARD, fill_opacity=1),
                    T(label, size=26, bold=True))
                node.move_to([x, y, 0])
                nodes[s] = (node, np.array([x, y, 0]))
        self.play(*[FadeIn(nodes[s][0]) for col in cols for s in col], run_time=1.4)
        edges = []
        for s, (node, pos) in nodes.items():
            for i in (0, 1, 2):
                if i not in s:
                    ns = tuple(sorted(s + (i,)))
                    npos = nodes[ns][1]
                    e = Line(pos, npos, stroke_color=GHOST, stroke_width=4)
                    edges.append(e)
        self.play(*[Create(e) for e in edges], run_time=1.6)
        # cheapest costs per subset (computed by the DP; verified values)
        costs = {(): 0, (0,): 2, (1,): 4, (2,): 6, (0, 1): 4, (0, 2): 6,
                 (1, 2): 6, (0, 1, 2): 6}
        for s in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]:
            node, pos = nodes[s]
            tag = T(str(costs[s]), size=26, color=TERRA, bold=True).next_to(pos, DOWN, buff=0.5)
            self.play(FadeIn(tag), run_time=0.35)
        # winning order path: () -> (H1) -> (H1,H2) -> (H1,H2,H3)
        win = [( ), (0,), (0, 1), (0, 1, 2)]
        wpath = VMobject().set_points_as_corners([nodes[s][1] for s in win])
        wpath.set_stroke(TERRA, 7)
        self.play(Create(wpath), run_time=1.4)
        note = T("cheapest order wins", size=30, color=DIM).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(7.0)


class B06_Twelve(Scene):
    def construct(self):
        g = Grid(3, 3, center=LEFT * 3.0)
        for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
            g.mark(*args)
        for (r, c) in [(1, 0), (1, 1)]:
            g.mark(r, c, "O", DIM)
        self.add(g.group)
        out = g.path_vm(TOUR12[:7], color=TERRA, width=7)
        self.play(Create(out), run_time=1.6)
        back = g.path_vm(TOUR12[6:], color=TERRA, width=7)
        self.play(Create(back), run_time=1.4)
        hero = T("12", size=120, bold=True, color=TERRA).move_to(RIGHT * 3.6 + UP * 1.2)
        ring = Circle(radius=1.05, stroke_color=TERRA, stroke_width=6).move_to(hero.get_center())
        sub = T("provably optimal", size=32, color=INK).next_to(hero, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(hero, sub)), FadeIn(ring), run_time=1.2)
        fine = T("work doubles per honey pot", size=28, color=DIM).move_to(RIGHT * 3.6 + DOWN * 1.8)
        self.play(FadeIn(fine), run_time=0.9)
        self.wait(8.0)


class B07_States(Scene):
    def construct(self):
        title = T("position = cell + what's collected", size=36, bold=True).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.7)
        layers = []
        for li, (label, collected) in enumerate([("got: H1", {(0, 2)}),
                                                 ("got: H1 H2", {(0, 2), (2, 2)}),
                                                 ("got: all", {(0, 2), (2, 2), (2, 0)})]):
            gg = Grid(3, 3, cell=0.62, center=LEFT * 3.6 + li * RIGHT * 3.6 + DOWN * 0.3)
            for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
                gg.mark(*args)
            for (r, c) in [(1, 0), (1, 1)]:
                gg.mark(r, c, "O", DIM)
            for (r, c) in collected:
                gg.shade(r, c, "#F5E3D3")
            lab = T(label, size=26, color=DIM).next_to(gg.group, DOWN, buff=0.25)
            layers.append(VGroup(gg.group, lab))
        self.play(*[FadeIn(l) for l in layers], run_time=1.6)
        # frontier dot climbs the layers
        d = Dot(LEFT * 3.6 + DOWN * 0.3, radius=0.14, color=TERRA,
                stroke_color=INK, stroke_width=2)
        self.play(FadeIn(d), run_time=0.5)
        for li in range(3):
            target = LEFT * 3.6 + li * RIGHT * 3.6 + DOWN * 0.3
            self.play(d.animate.move_to(target), run_time=1.2)
        tag = T("first arrival home = shortest", size=30, color=TERRA, bold=True
                ).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(tag), run_time=0.9)
        self.wait(9.0)


class B08_Crosscheck(Scene):
    def construct(self):
        card = RoundedRectangle(width=10.5, height=4.6, corner_radius=0.25,
                               stroke_color=INK, stroke_width=3,
                               fill_color=INK, fill_opacity=1)
        self.play(FadeIn(card), run_time=0.7)
        prompt = T("$ python3 test_solution.py", size=32, color="#F2F0E9"
                    ).move_to(card.get_top() + DOWN * 0.7 + LEFT * 3.6)
        self.play(Write(prompt), run_time=1.2)
        # verbatim output of the real run (see FACTCHECK.md #8)
        lines = ["25 passed, 0 failed", "ALL TESTS PASSED"]
        y = card.get_top()[1] - 1.7
        for i, ln in enumerate(lines):
            t = T(ln, size=36, color="#F2F0E9", bold=True
                  ).move_to([card.get_center()[0] - 2.6, y - i * 0.9, 0])
            chk = checkmark(np.array([card.get_center()[0] + 2.9, y - i * 0.9, 0]),
                            scale=1.1, color=TERRA)
            self.play(Write(t), run_time=1.0)
            self.play(FadeIn(chk), run_time=0.4)
        note = T("two methods · 300 random grids · zero disagreements",
                 size=28, color="#F2F0E9").move_to(
            [card.get_center()[0], card.get_bottom()[1] + 0.6, 0])
        self.play(FadeIn(note), run_time=0.9)
        self.wait(6.0)


class B09_Greedy(Scene):
    def construct(self):
        g = Grid(4, 4, cell=0.8, center=LEFT * 2.6)
        g.mark(0, 0, "B", TERRA)
        for (r, c) in [(1, 1), (2, 0), (3, 1)]:
            g.mark(r, c, "H")
        self.add(g.group)
        title = T("nearest first", size=36, bold=True).move_to(RIGHT * 3.4 + UP * 2.2)
        self.play(FadeIn(title), run_time=0.7)
        dot = g.dot(0, 0)
        self.add(dot)
        # first two greedy hops: B -> (1,1) -> (2,0)
        for dest in [(1, 1), (2, 0)]:
            self.play(dot.animate.move_to(g.at(*dest)), run_time=1.6)
        tag = T("feels right", size=34, color=DIM).move_to(RIGHT * 3.4 + DOWN * 0.4)
        self.play(FadeIn(tag), run_time=0.8)
        self.play(FadeOut(tag), run_time=0.8)
        warn = T("…in general, wrong", size=34, color=TERRA, bold=True
                 ).move_to(RIGHT * 3.4 + DOWN * 0.4)
        self.play(FadeIn(warn), run_time=0.9)
        self.wait(5.0)


class B10_Trap(Scene):
    def construct(self):
        gl = Grid(4, 4, cell=0.62, center=LEFT * 3.9)
        gr = Grid(4, 4, cell=0.62, center=RIGHT * 3.9)
        for gg in (gl, gr):
            gg.mark(0, 0, "B", TERRA)
            for (r, c) in [(1, 1), (2, 0), (3, 1)]:
                gg.mark(r, c, "H")
        self.add(gl.group, gr.group)
        lab_l = T("greedy", size=32, color=DIM).next_to(gl.group, UP, buff=0.3)
        lab_r = T("optimal", size=32, color=TERRA, bold=True).next_to(gr.group, UP, buff=0.3)
        self.play(FadeIn(VGroup(lab_l, lab_r)), run_time=0.7)
        pl = gl.path_vm(GREEDY10, color=DIM, width=5)
        self.play(Create(pl), run_time=2.4)
        ten = T("10 steps", size=40, bold=True, color=DIM).next_to(gl.group, DOWN, buff=0.35)
        self.play(FadeIn(ten), run_time=0.6)
        pr = gr.path_vm(OPT8, color=TERRA, width=6)
        self.play(Create(pr), run_time=2.2)
        eight = T("8 steps", size=40, bold=True, color=TERRA).next_to(gr.group, DOWN, buff=0.35)
        self.play(FadeIn(eight), run_time=0.6)
        self.play(ten.animate.scale(1.25), eight.animate.scale(1.25), run_time=0.6)
        self.play(ten.animate.scale(1 / 1.25), eight.animate.scale(1 / 1.25), run_time=0.6)
        self.wait(4.0)


class B11_Wall(Scene):
    def construct(self):
        # axes drawn explicitly (the stub's Axes.plot returns the axes itself,
        # so a hand-built VMobject curve is both stub-clean and render-clean)
        x0, x1, y0, y1 = -4.75, 4.75, -2.6, 1.8
        xax = Line([x0, y0, 0], [x1, y0, 0], stroke_color=INK, stroke_width=3)
        yax = Line([x0, y0, 0], [x0, y1, 0], stroke_color=INK, stroke_width=3)
        xlabel = T("honey pots (K)", size=28, color=DIM).next_to(xax, DOWN, buff=0.25)
        ylabel = T("subsets (2^K)", size=28, color=DIM).rotate(90 * DEGREES)
        ylabel.next_to(yax, LEFT, buff=0.4)
        self.play(Create(VGroup(xax, yax)), FadeIn(VGroup(xlabel, ylabel)), run_time=1.0)

        def pt(k):
            x = x0 + k * (x1 - x0) / 32
            y = y0 + (y1 - y0) * (2 ** k) / (2 ** 30)
            return np.array([x, y, 0.0])

        curve = VMobject().set_points_as_corners([pt(k) for k in range(0, 31)])
        curve.set_stroke(TERRA, 7)
        self.play(Create(curve), run_time=2.4)

        d8 = Dot(pt(8), radius=0.11, color=TERRA)
        m8 = VGroup(T("K=8", size=30, bold=True),
                    T("256 · nothing", size=26, color=DIM)
                    ).arrange(DOWN, buff=0.1).next_to(pt(8), UP, buff=0.3)
        self.play(FadeIn(VGroup(d8, m8)), run_time=0.8)

        d30 = Dot(pt(30), radius=0.11, color=TERRA)
        m30 = VGroup(T("K=30", size=30, bold=True),
                     T("over a billion · impossible", size=26, color=TERRA, bold=True)
                     ).arrange(DOWN, buff=0.1).next_to(pt(30), UP, buff=0.3)
        self.play(FadeIn(VGroup(d30, m30)), run_time=0.9)
        self.wait(7.0)


class B12_Rule(Scene):
    def construct(self):
        title = T("the number of targets decides", size=38, bold=True).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.7)
        branches = VGroup(
            VGroup(T("few targets", size=32, bold=True, color=TERRA),
                   T("bitmask DP — exact, clean", size=28, color=DIM)),
            VGroup(T("want obvious correctness", size=32, bold=True, color=TERRA),
                   T("state-space BFS", size=28, color=DIM)),
            VGroup(T("dozens of targets", size=32, bold=True, color=TERRA),
                   T("greedy — or approximate", size=28, color=DIM)),
        )
        for b in branches:
            b.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        branches.arrange(DOWN, buff=0.7, aligned_edge=LEFT).move_to(LEFT * 1.2 + DOWN * 0.3)
        for b in branches:
            box = Rectangle(width=6.4, height=1.55, stroke_color=INK, stroke_width=3,
                            fill_color=CARD, fill_opacity=1).move_to(b.get_center())
            self.play(FadeIn(VGroup(box, b)), run_time=0.9)
        dial_bg = Line(LEFT * 1.6, RIGHT * 1.6, stroke_color=GHOST, stroke_width=10
                       ).move_to(RIGHT * 4.2 + DOWN * 0.3)
        knob = Dot(color=TERRA, radius=0.22).move_to(dial_bg.get_start())
        dlab = T("K", size=30, bold=True, color=DIM).next_to(dial_bg, UP, buff=0.25)
        self.play(FadeIn(VGroup(dial_bg, knob, dlab)), run_time=0.7)
        self.play(knob.animate.move_to(dial_bg.get_end()), run_time=1.6)
        note = T("not your cleverness", size=30, color=DIM).next_to(dial_bg, DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(6.0)


class B13_SixVsTwelve(Scene):
    def construct(self):
        gl = Grid(3, 3, cell=0.72, center=LEFT * 3.9 + DOWN * 0.2)
        gr = Grid(3, 3, cell=0.72, center=RIGHT * 3.9 + DOWN * 0.2)
        for gg in (gl, gr):
            for args in [(0, 0, "B", TERRA), (0, 2, "H"), (2, 0, "H"), (2, 2, "H")]:
                gg.mark(*args)
            for (r, c) in [(1, 0), (1, 1)]:
                gg.mark(r, c, "O", DIM)
        self.add(gl.group, gr.group)
        p6 = gl.path_vm(TOUR6, color=DIM, width=6)
        self.play(Create(p6), run_time=1.8)
        six = T("6", size=64, bold=True, color=DIM).next_to(gl.group, UP, buff=0.35)
        tag6 = T("never comes home", size=28, color=DIM).next_to(six, UP, buff=0.15)
        self.play(FadeIn(VGroup(six, tag6)), run_time=0.8)
        p12 = gr.path_vm(TOUR12, color=TERRA, width=6)
        self.play(Create(p12), run_time=2.6)
        twelve = T("12", size=64, bold=True, color=TERRA).next_to(gr.group, UP, buff=0.35)
        tag12 = T("the real answer", size=28, color=TERRA, bold=True).next_to(twelve, UP, buff=0.15)
        self.play(FadeIn(VGroup(twelve, tag12)), run_time=0.8)
        self.wait(8.0)


class B14_Fixes(Scene):
    def construct(self):
        title = T("four fixes, one corrected notebook", size=38, bold=True).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.7)
        items = [
            "example answer 6 → 12",
            "minus-one contradiction resolved",
            "no diagonals, stated",
            "exactly one start cell",
        ]
        card_items = VGroup()
        circles = []
        for it in items:
            circ = Circle(radius=0.26, stroke_color=DIM, stroke_width=4)
            row = VGroup(circ, T(it, size=32)).arrange(RIGHT, buff=0.4, aligned_edge=ORIGIN)
            circles.append(circ)
            card_items.add(row)
        card_items.arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(DOWN * 0.2)
        box = Rectangle(width=8.6, height=4.6, stroke_color=INK, stroke_width=3,
                        fill_color=CARD, fill_opacity=1).move_to(card_items.get_center())
        self.play(FadeIn(VGroup(box, card_items)), run_time=1.0)
        for circ in circles:
            chk = checkmark(np.array([circ.get_center()[0],
                                      circ.get_center()[1], 0.0]), scale=0.9)
            self.play(Transform(circ, chk), run_time=0.6)
            self.wait(0.4)
        tag = T("the grader, graded", size=30, color=DIM).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(tag), run_time=0.8)
        self.wait(5.0)
