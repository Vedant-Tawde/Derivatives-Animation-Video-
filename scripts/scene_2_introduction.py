"""
Scene 2: Concept Introduction
Duration: ~36 seconds
Topic: f(x) = x², parabola, points A and B, secant line
"""

from manim import *

BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"
POINT_COLOR = "#ffd700"
SECANT_COLOR = "#ff8c00"
TANGENT_COLOR = "#00ff88"
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE

def add_axis_numbers(axes, x_values, y_values):
    labels = VGroup()
    for x in x_values:
        lbl = Text(str(x), font_size=16, color=TEXT_COLOR).next_to(axes.c2p(x, 0), DOWN, buff=0.18)
        labels.add(lbl)
    for y in y_values:
        if y != 0:
            lbl = Text(str(y), font_size=16, color=TEXT_COLOR).next_to(axes.c2p(0, y), LEFT, buff=0.18)
            labels.add(lbl)
    return labels

class Scene2Introduction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        def make_sub(text, font_size=22):
            sub = Text(text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif")
            sub.to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.82, buff=0.15)
            return VGroup(sub_bg, sub)

        func_tex = Text("f(x) = x²", font_size=48, color=TEXT_COLOR, font="serif").shift(UP * 2)
        desc = Text("This function produces a parabola.", font_size=26, color=TEXT_COLOR
                     ).next_to(func_tex, DOWN, buff=0.4)
        sub1 = make_sub("Consider the function f(x) equals x squared, producing a parabola.")
        self.play(Write(func_tex), FadeIn(sub1), run_time=1.0)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.8)
        self.wait(4.7)
        self.play(FadeOut(sub1), run_time=0.3)

        self.play(FadeOut(desc), func_tex.animate.scale(0.65).to_corner(UR, buff=0.5), run_time=0.8)

        axes = Axes(x_range=[-1, 5, 1], y_range=[-1, 20, 5],
                     x_length=7, y_length=5,
                     axis_config={"color": TEXT_COLOR, "include_numbers": False},
                     tips=True).shift(DOWN * 0.3 + LEFT * 0.5)
        axis_nums = add_axis_numbers(axes, range(0, 5), [5, 10, 15, 20])
        xl = Text("x", font_size=18, color=TEXT_COLOR).next_to(axes.x_axis, RIGHT, buff=0.2)
        yl = Text("f(x)", font_size=18, color=TEXT_COLOR).next_to(axes.y_axis, UP, buff=0.2)
        curve = axes.plot(lambda x: x ** 2, x_range=[-0.5, 4.3], color=CURVE_COLOR, stroke_width=3)
        clbl = Text("f(x) = x²", font_size=22, color=CURVE_COLOR, font="serif").next_to(axes.c2p(3.8, 14.5), RIGHT, buff=0.15)

        sub2 = make_sub("Here is its graph on the Cartesian coordinate plane.")
        self.play(Create(axes), FadeIn(axis_nums), Write(xl), Write(yl), FadeIn(sub2), run_time=1.2)
        self.play(Create(curve), run_time=1.5)
        self.play(Write(clbl), run_time=0.6)
        self.wait(4.5)
        self.play(FadeOut(sub2), run_time=0.3)

        pA = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.1, z_index=5)
        lA = Text("A = (2, 4)", font_size=20, color=POINT_COLOR).next_to(pA, LEFT + UP, buff=0.15)

        h = 1; bx = 3; by = 9
        pB = Dot(axes.c2p(bx, by), color=SECANT_COLOR, radius=0.1, z_index=5)
        lB = Text("B = (2+h, (2+h)²)", font_size=20, color=SECANT_COLOR).next_to(pB, RIGHT + UP, buff=0.15)

        hbrace = BraceBetweenPoints(axes.c2p(2, -0.8), axes.c2p(3, -0.8),
                                     direction=DOWN, color=TEXT_COLOR)
        hlbl = Text("h", font_size=22, color=TEXT_COLOR, font="serif").next_to(hbrace, DOWN, buff=0.12)

        sub3 = make_sub("We choose a fixed point A at x = 2, and a neighboring point B at x = 2 + h.")
        self.play(FadeIn(pA), Write(lA), FadeIn(sub3), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(pB), Write(lB), run_time=0.8)
        self.play(Create(hbrace), Write(hlbl), run_time=0.7)
        self.wait(5.5)
        self.play(FadeOut(sub3), run_time=0.3)

        sec_slope = 5
        sec = Line(axes.c2p(0.5, 4 + sec_slope * (0.5 - 2)),
                   axes.c2p(4.5, 4 + sec_slope * (4.5 - 2)),
                   color=SECANT_COLOR, stroke_width=3)
        slbl = Text("Secant Line", font_size=20, color=SECANT_COLOR).next_to(axes.c2p(4, 14), RIGHT, buff=0.25)

        sub4 = make_sub("The straight line passing through both points is called a secant line.")
        self.play(Create(sec), FadeIn(sub4), run_time=1.0)
        self.play(Write(slbl), run_time=0.6)
        self.wait(5.5)
        self.play(FadeOut(sub4), run_time=0.3)

        all2 = VGroup(axes, axis_nums, xl, yl, curve, clbl, pA, lA, pB, lB,
                       hbrace, hlbl, sec, slbl, func_tex)
        self.play(FadeOut(all2), run_time=0.8)
