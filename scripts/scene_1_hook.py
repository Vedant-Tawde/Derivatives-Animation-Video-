"""
Scene 1: Hook / Real-World Context
Duration: ~30 seconds (0:00 - 0:30)

Animated car, speed question, transition to mathematical graph.
"""

from manim import *

# Color palette
BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"     # Cyan for function curve
POINT_COLOR = "#ffd700"     # Yellow for moving point
SECANT_COLOR = "#ff8c00"    # Orange for secant line
TANGENT_COLOR = "#00ff88"   # Green for tangent line
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE
GRID_COLOR = "#333355"

class Scene1Hook(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # --- Subtitle helper ---
        def subtitle(text, duration=3):
            sub = Text(
                text,
                font_size=24,
                color=SUBTITLE_COLOR,
                font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            group = VGroup(sub_bg, sub)
            self.play(FadeIn(group), run_time=0.3)
            self.wait(duration - 0.6)
            self.play(FadeOut(group), run_time=0.3)

        def subtitle_persistent(text):
            sub = Text(
                text,
                font_size=24,
                color=SUBTITLE_COLOR,
                font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            return VGroup(sub_bg, sub)

        # ============================================================
        # Part 1: Animated car on a road (0:00 - 0:12)
        # ============================================================

        # Road
        road = Rectangle(
            width=14, height=1.2,
            fill_color="#333333", fill_opacity=1,
            stroke_color="#555555", stroke_width=1,
        ).shift(DOWN * 1)

        # Road markings (dashed center line)
        dashes = VGroup()
        for i in range(-6, 7):
            dash = Line(
                start=LEFT * 0.3, end=RIGHT * 0.3,
                color=YELLOW, stroke_width=2,
            ).move_to(road.get_center() + RIGHT * i)
            dashes.add(dash)

        # Simple car shape
        car_body = RoundedRectangle(
            corner_radius=0.15, width=1.6, height=0.6,
            fill_color="#e74c3c", fill_opacity=1,
            stroke_color="#c0392b", stroke_width=2,
        )
        car_top = RoundedRectangle(
            corner_radius=0.1, width=0.9, height=0.4,
            fill_color="#e74c3c", fill_opacity=1,
            stroke_color="#c0392b", stroke_width=2,
        ).shift(UP * 0.4)
        wheel1 = Circle(radius=0.15, fill_color="#2c3e50", fill_opacity=1, stroke_color=WHITE, stroke_width=1).shift(LEFT * 0.5 + DOWN * 0.35)
        wheel2 = Circle(radius=0.15, fill_color="#2c3e50", fill_opacity=1, stroke_color=WHITE, stroke_width=1).shift(RIGHT * 0.5 + DOWN * 0.35)

        car = VGroup(car_body, car_top, wheel1, wheel2)
        car.move_to(LEFT * 5 + DOWN * 0.3)

        self.play(FadeIn(road), FadeIn(dashes), run_time=0.5)
        self.play(FadeIn(car), run_time=0.3)

        sub1 = subtitle_persistent("Imagine a car driving along a road...")
        self.play(FadeIn(sub1), run_time=0.3)

        # Animate car moving
        self.play(car.animate.shift(RIGHT * 4), run_time=2, rate_func=rate_functions.ease_in_out_sine)
        self.play(FadeOut(sub1), run_time=0.2)

        # Speed vs time mini graph
        sub2 = subtitle_persistent("How do we measure its speed at one exact instant?")
        self.play(FadeIn(sub2), run_time=0.3)

        # Small speedometer-like display
        speed_axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 60, 20],
            x_length=3, y_length=2,
            axis_config={"color": TEXT_COLOR, "font_size": 18},
            tips=False,
        ).shift(UP * 2 + RIGHT * 3)

        speed_labels = VGroup(
            Text("time", font_size=16, color=TEXT_COLOR).next_to(speed_axes.x_axis, DOWN, buff=0.15),
            Text("speed", font_size=16, color=TEXT_COLOR).next_to(speed_axes.y_axis, LEFT, buff=0.15).rotate(PI/2),
        )

        speed_curve = speed_axes.plot(
            lambda x: 10 * x + 5 * np.sin(x * 2),
            x_range=[0, 4.5],
            color=CURVE_COLOR,
        )

        self.play(
            Create(speed_axes), Write(speed_labels),
            run_time=0.8,
        )
        self.play(Create(speed_curve), run_time=1.5)

        # Highlight a specific instant
        dot_on_curve = Dot(
            speed_axes.c2p(2.5, 10 * 2.5 + 5 * np.sin(5)),
            color=POINT_COLOR, radius=0.1,
        )
        instant_line = DashedLine(
            speed_axes.c2p(2.5, 0),
            speed_axes.c2p(2.5, 10 * 2.5 + 5 * np.sin(5)),
            color=POINT_COLOR, dash_length=0.1,
        )
        self.play(Create(instant_line), FadeIn(dot_on_curve), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(sub2), run_time=0.2)

        # ============================================================
        # Part 2: Transition to math (0:12 - 0:22)
        # ============================================================

        sub3 = subtitle_persistent("Average speed uses distance over time, but instantaneous speed needs calculus.")
        self.play(FadeIn(sub3), run_time=0.3)
        self.wait(2.5)
        self.play(FadeOut(sub3), run_time=0.2)

        # ============================================================
        # Part 3: Title card (0:22 - 0:30)
        # ============================================================

        # Fade out car scene
        car_scene = VGroup(road, dashes, car, speed_axes, speed_labels, speed_curve, dot_on_curve, instant_line)
        self.play(FadeOut(car_scene), run_time=0.8)

        # Title
        title = Text(
            "DERIVATIVES",
            font_size=56,
            color=TEXT_COLOR,
            weight=BOLD,
        ).shift(UP * 0.5)

        subtitle_text = Text(
            "FROM SECANT TO TANGENT",
            font_size=32,
            color=CURVE_COLOR,
        ).next_to(title, DOWN, buff=0.4)

        line_accent = Line(LEFT * 3, RIGHT * 3, color=TANGENT_COLOR, stroke_width=3).next_to(subtitle_text, DOWN, buff=0.3)

        sub4 = subtitle_persistent("Derivatives: From Secant to Tangent")
        self.play(
            Write(title),
            run_time=1,
        )
        self.play(
            FadeIn(subtitle_text, shift=UP * 0.3),
            Create(line_accent),
            FadeIn(sub4),
            run_time=1,
        )
        self.wait(2)

        # Fade out title
        self.play(
            FadeOut(title), FadeOut(subtitle_text), FadeOut(line_accent), FadeOut(sub4),
            run_time=0.8,
        )
