"""
Scene 5: Geometric Interpretation
Duration: ~50 seconds (3:30 - 4:20)

Return to graph. Show tangent line, derive its equation, connect to real-world meaning.
"""

from manim import *

BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"
POINT_COLOR = "#ffd700"
SECANT_COLOR = "#ff8c00"
TANGENT_COLOR = "#00ff88"
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE

class Scene5Interpretation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        def subtitle_persistent(text, font_size=22):
            sub = Text(
                text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            return VGroup(sub_bg, sub)

        # ============================================================
        # Part 1: Return to graph (3:30 - 3:45)
        # ============================================================

        axes = Axes(
            x_range=[-1, 5.5, 1], y_range=[-5, 20, 5],
            x_length=7.5, y_length=5.5,
            axis_config={
                "color": TEXT_COLOR,
                "include_numbers": True,
                "font_size": 20,
            },
            tips=True,
        ).shift(LEFT * 1 + DOWN * 0.3)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2).set_color(TEXT_COLOR).scale(0.7)
        y_label = axes.get_y_axis_label("f(x)", edge=UP, direction=UP, buff=0.2).set_color(TEXT_COLOR).scale(0.7)

        curve = axes.plot(
            lambda x: x ** 2,
            x_range=[-0.5, 4.4],
            color=CURVE_COLOR,
            stroke_width=3,
        )

        curve_label = MathTex(r"f(x) = x^2", font_size=22, color=CURVE_COLOR).next_to(
            axes.c2p(4, 16), UR, buff=0.15
        )

        point_a = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.12, z_index=5)
        label_a = MathTex(r"(2, 4)", font_size=22, color=POINT_COLOR).next_to(point_a, LEFT + UP, buff=0.15)

        sub1 = subtitle_persistent("Let us return to the graph and draw the tangent line at x = 2.")

        self.play(
            Create(axes), Write(x_label), Write(y_label),
            Create(curve), Write(curve_label),
            run_time=1,
        )
        self.play(FadeIn(point_a), Write(label_a), FadeIn(sub1), run_time=0.6)
        self.wait(1.5)

        # Tangent line: y = 4x - 4
        tangent = axes.plot(
            lambda x: 4 * x - 4,
            x_range=[0, 4.5],
            color=TANGENT_COLOR,
            stroke_width=3,
        )

        tangent_label = Text("Tangent Line", font_size=20, color=TANGENT_COLOR).next_to(
            axes.c2p(4, 12), RIGHT, buff=0.15
        )

        self.play(Create(tangent), Write(tangent_label), run_time=1)
        self.wait(1)
        self.play(FadeOut(sub1), run_time=0.2)

        # ============================================================
        # Part 2: Derive tangent equation (3:45 - 4:05)
        # ============================================================

        sub2 = subtitle_persistent("We find the tangent line equation using point-slope form.")
        self.play(FadeIn(sub2), run_time=0.3)

        # Equation derivation on the right side
        eq_group_pos = RIGHT * 3.5 + UP * 2

        eq1 = MathTex(r"y - y_1 = m(x - x_1)", font_size=28, color=TEXT_COLOR).move_to(eq_group_pos)
        eq1_label = Text("Point-slope form", font_size=16, color=TANGENT_COLOR).next_to(eq1, UP, buff=0.2)

        self.play(Write(eq1_label), Write(eq1), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(sub2), run_time=0.2)

        sub3 = subtitle_persistent("Substitute the point (2, 4) and slope m = 4.")
        self.play(FadeIn(sub3), run_time=0.3)

        eq2 = MathTex(r"y - 4 = 4(x - 2)", font_size=28, color=TEXT_COLOR).next_to(eq1, DOWN, buff=0.4)
        self.play(Write(eq2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(sub3), run_time=0.2)

        sub4 = subtitle_persistent("Simplify to get y = 4x minus 4.")
        self.play(FadeIn(sub4), run_time=0.3)

        eq3 = MathTex(r"y = 4x - 4", font_size=32, color=TANGENT_COLOR).next_to(eq2, DOWN, buff=0.4)
        eq3_box = SurroundingRectangle(eq3, color=TANGENT_COLOR, buff=0.15, corner_radius=0.08)

        self.play(Write(eq3), run_time=0.6)
        self.play(Create(eq3_box), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(sub4), run_time=0.2)

        # ============================================================
        # Part 3: Show all three elements together (4:05 - 4:15)
        # ============================================================

        sub5 = subtitle_persistent("The blue curve is f(x) = x². The green line is the tangent at x = 2.")
        self.play(FadeIn(sub5), run_time=0.3)

        # Legend
        legend_items = VGroup(
            VGroup(
                Line(LEFT * 0.3, RIGHT * 0.3, color=CURVE_COLOR, stroke_width=3),
                MathTex(r"f(x) = x^2", font_size=18, color=CURVE_COLOR),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Line(LEFT * 0.3, RIGHT * 0.3, color=TANGENT_COLOR, stroke_width=3),
                MathTex(r"y = 4x - 4", font_size=18, color=TANGENT_COLOR),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(DL, buff=0.8).shift(UP * 0.8)

        legend_bg = BackgroundRectangle(legend_items, color=BG_COLOR, fill_opacity=0.8, buff=0.15)

        self.play(FadeIn(legend_bg), Write(legend_items), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(sub5), run_time=0.2)

        # ============================================================
        # Part 4: Connect to real-world meaning (4:15 - 4:20)
        # ============================================================

        sub6 = subtitle_persistent("The slope 4 is the instantaneous rate of change — just like the car's exact speed.")
        self.play(FadeIn(sub6), run_time=0.3)

        slope_highlight = MathTex(r"\text{slope} = f'(2) = 4", font_size=30, color=POINT_COLOR).next_to(
            eq3_box, DOWN, buff=0.5
        )
        self.play(Write(slope_highlight), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(sub6), run_time=0.2)

        # Fade all
        all_obj = VGroup(
            axes, x_label, y_label, curve, curve_label,
            point_a, label_a, tangent, tangent_label,
            eq1, eq1_label, eq2, eq3, eq3_box,
            legend_bg, legend_items, slope_highlight,
        )
        self.play(FadeOut(all_obj), run_time=0.8)
