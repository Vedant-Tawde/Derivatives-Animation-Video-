"""
Scene 3: Visual Intuition — Animated secant lines approaching the tangent
Duration: ~55 seconds (1:05 - 2:00)

This is the core visual scene. Point B slides toward A, secant lines rotate.
"""

from manim import *

BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"
POINT_COLOR = "#ffd700"
SECANT_COLOR = "#ff8c00"
TANGENT_COLOR = "#00ff88"
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE

class Scene3VisualIntuition(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        def subtitle_persistent(text, font_size=22):
            sub = Text(
                text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            return VGroup(sub_bg, sub)

        # ============================================================
        # Setup: Axes and curve
        # ============================================================

        axes = Axes(
            x_range=[-0.5, 5.5, 1], y_range=[-1, 22, 5],
            x_length=7.5, y_length=5.5,
            axis_config={
                "color": TEXT_COLOR,
                "include_numbers": True,
                "font_size": 20,
            },
            tips=True,
        ).shift(LEFT * 1.5 + DOWN * 0.2)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2).set_color(TEXT_COLOR).scale(0.7)
        y_label = axes.get_y_axis_label("f(x)", edge=UP, direction=UP, buff=0.2).set_color(TEXT_COLOR).scale(0.7)

        curve = axes.plot(
            lambda x: x ** 2,
            x_range=[-0.3, 4.6],
            color=CURVE_COLOR,
            stroke_width=3,
        )

        curve_label = MathTex(r"f(x) = x^2", font_size=24, color=CURVE_COLOR).next_to(
            axes.c2p(4.3, 18), RIGHT, buff=0.2
        )

        # Point A fixed
        point_a = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.1, z_index=5)
        label_a = MathTex(r"A(2,4)", font_size=22, color=POINT_COLOR).next_to(point_a, LEFT + UP, buff=0.15)

        sub_intro = subtitle_persistent("Now watch what happens as point B moves closer to point A.")

        self.play(
            Create(axes), Write(x_label), Write(y_label),
            run_time=0.8,
        )
        self.play(Create(curve), Write(curve_label), run_time=1)
        self.play(FadeIn(point_a), Write(label_a), FadeIn(sub_intro), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(sub_intro), run_time=0.2)

        # ============================================================
        # Info table on the right side
        # ============================================================

        # Table header
        table_title = Text("Secant Slopes", font_size=22, color=TEXT_COLOR, weight=BOLD).to_edge(RIGHT, buff=0.5).shift(UP * 2.8)
        h_col = Text("h", font_size=20, color=TEXT_COLOR).next_to(table_title, DOWN, buff=0.3).shift(LEFT * 0.6)
        slope_col = Text("slope", font_size=20, color=TEXT_COLOR).next_to(table_title, DOWN, buff=0.3).shift(RIGHT * 0.6)
        header_line = Line(
            h_col.get_left() + DOWN * 0.2 + LEFT * 0.2,
            slope_col.get_right() + DOWN * 0.2 + RIGHT * 0.2,
            color=TEXT_COLOR, stroke_width=1,
        )

        self.play(Write(table_title), Write(h_col), Write(slope_col), Create(header_line), run_time=0.6)

        # ============================================================
        # Animate secant lines for each h value
        # ============================================================

        h_values = [2, 1, 0.5, 0.1]
        slopes = [6, 5, 4.5, 4.1]
        subtitles_text = [
            "With h = 2, B is at (4, 16). The secant slope is 6.",
            "With h = 1, B is at (3, 9). The secant slope is 5.",
            "With h = 0.5, B is at (2.5, 6.25). The slope is 4.5.",
            "With h = 0.1, B is at (2.1, 4.41). The slope is 4.1.",
        ]

        table_entries = []
        prev_secant = None
        prev_point_b = None
        prev_label_b = None

        for i, (h, slope, sub_text) in enumerate(zip(h_values, slopes, subtitles_text)):
            bx = 2 + h
            by = bx ** 2

            # Create objects
            new_point_b = Dot(axes.c2p(bx, by), color=SECANT_COLOR, radius=0.1, z_index=5)

            if h >= 0.5:
                new_label_b = MathTex(
                    f"B({bx:.1f},{by:.2f})" if by != int(by) else f"B({int(bx)},{int(by)})",
                    font_size=20, color=SECANT_COLOR,
                ).next_to(new_point_b, RIGHT + UP, buff=0.15)
            else:
                new_label_b = MathTex(
                    f"B({bx:.1f},{by:.2f})",
                    font_size=20, color=SECANT_COLOR,
                ).next_to(new_point_b, RIGHT + UP, buff=0.15)

            # Secant line through A(2,4) and B(bx, by)
            sec_slope = (by - 4) / (bx - 2)
            x_start = max(-0.3, 2 - 3)
            x_end = min(5, 2 + 3)
            new_secant = Line(
                axes.c2p(x_start, 4 + sec_slope * (x_start - 2)),
                axes.c2p(x_end, 4 + sec_slope * (x_end - 2)),
                color=SECANT_COLOR,
                stroke_width=2.5,
            )

            # Table entry
            h_text = f"{h}" if h == int(h) else f"{h}"
            slope_text = f"{slope}" if slope == int(slope) else f"{slope}"
            h_entry = MathTex(h_text, font_size=20, color=SECANT_COLOR).next_to(h_col, DOWN, buff=0.3 + i * 0.4)
            slope_entry = MathTex(slope_text, font_size=20, color=SECANT_COLOR).next_to(slope_col, DOWN, buff=0.3 + i * 0.4)

            sub = subtitle_persistent(sub_text, font_size=20)

            if prev_secant is None:
                # First secant
                self.play(
                    FadeIn(new_point_b), Write(new_label_b),
                    Create(new_secant),
                    Write(h_entry), Write(slope_entry),
                    FadeIn(sub),
                    run_time=1,
                )
            else:
                # Transform from previous
                self.play(
                    ReplacementTransform(prev_point_b, new_point_b),
                    ReplacementTransform(prev_label_b, new_label_b),
                    ReplacementTransform(prev_secant, new_secant),
                    Write(h_entry), Write(slope_entry),
                    FadeIn(sub),
                    run_time=1.2,
                )

            self.wait(2)
            self.play(FadeOut(sub), run_time=0.2)

            prev_secant = new_secant
            prev_point_b = new_point_b
            prev_label_b = new_label_b
            table_entries.extend([h_entry, slope_entry])

        # ============================================================
        # Show the limiting tangent line
        # ============================================================

        sub_limit = subtitle_persistent("As h approaches zero, the secant line approaches the tangent line.")

        # Tangent line at x = 2 with slope = 4: y - 4 = 4(x - 2) → y = 4x - 4
        tangent = Line(
            axes.c2p(0, -4),
            axes.c2p(4.5, 4 * 4.5 - 4),
            color=TANGENT_COLOR,
            stroke_width=3,
        )

        tangent_label = Text("Tangent Line", font_size=20, color=TANGENT_COLOR).next_to(
            axes.c2p(4, 12), RIGHT, buff=0.3
        )

        # Arrow showing limit
        limit_text = MathTex(r"\text{slope} \to 4", font_size=22, color=TANGENT_COLOR).next_to(
            slope_col, DOWN, buff=0.3 + 4 * 0.4
        )

        self.play(
            ReplacementTransform(prev_secant, tangent),
            FadeOut(prev_point_b), FadeOut(prev_label_b),
            Write(tangent_label),
            Write(limit_text),
            FadeIn(sub_limit),
            run_time=1.5,
        )
        self.wait(2.5)
        self.play(FadeOut(sub_limit), run_time=0.2)

        sub_inst = subtitle_persistent("The tangent line gives the instantaneous rate of change at x = 2.")
        self.play(FadeIn(sub_inst), run_time=0.3)
        self.wait(2.5)
        self.play(FadeOut(sub_inst), run_time=0.2)

        # Fade all out
        all_objects = VGroup(
            axes, x_label, y_label, curve, curve_label,
            point_a, label_a, tangent, tangent_label,
            table_title, h_col, slope_col, header_line,
            limit_text, *table_entries,
        )
        self.play(FadeOut(all_objects), run_time=0.8)
