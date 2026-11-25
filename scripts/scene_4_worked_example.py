"""
Scene 4: Complete Worked Mathematical Example
Duration: ~90 seconds (2:00 - 3:30)

Step-by-step derivative calculation using the limit definition.
"""

from manim import *

BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"
POINT_COLOR = "#ffd700"
SECANT_COLOR = "#ff8c00"
TANGENT_COLOR = "#00ff88"
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE
HIGHLIGHT_COLOR = "#ffff00"

class Scene4WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        def subtitle_persistent(text, font_size=22):
            sub = Text(
                text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            return VGroup(sub_bg, sub)

        # ============================================================
        # Part 1: Setup — state the goal (2:00 - 2:10)
        # ============================================================

        heading = Text(
            "Finding the Derivative", font_size=36,
            color=TEXT_COLOR, weight=BOLD,
        ).to_edge(UP, buff=0.6)

        sub1 = subtitle_persistent("Let us now calculate the derivative of f(x) = x² at x = 2.")

        func = MathTex(r"f(x) = x^2", font_size=40, color=CURVE_COLOR).shift(UP * 1.5)
        goal = MathTex(r"\text{Find } f'(2)", font_size=36, color=POINT_COLOR).next_to(func, DOWN, buff=0.5)

        self.play(Write(heading), run_time=0.6)
        self.play(Write(func), FadeIn(sub1), run_time=0.8)
        self.play(Write(goal), run_time=0.6)
        self.wait(2)
        self.play(FadeOut(sub1), run_time=0.2)

        # Clear for derivation
        self.play(FadeOut(heading), FadeOut(func), FadeOut(goal), run_time=0.6)

        # ============================================================
        # Part 2: Limit definition (2:10 - 2:25)
        # ============================================================

        sub2 = subtitle_persistent("We use the limit definition of the derivative.")

        step_label = Text("Step 1: Limit Definition", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        limit_def = MathTex(
            r"f'(2)", r"=", r"\lim_{h \to 0}",
            r"\frac{f(2+h) - f(2)}{h}",
            font_size=40,
            color=TEXT_COLOR,
        ).shift(UP * 1)

        self.play(Write(step_label), FadeIn(sub2), run_time=0.5)
        self.play(Write(limit_def), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(sub2), run_time=0.2)

        # Explain parts
        sub2b = subtitle_persistent("f(2+h) is the output at the nearby point. f(2) is the output at x = 2.")
        self.play(FadeIn(sub2b), run_time=0.3)

        # Highlight f(2+h)
        box1 = SurroundingRectangle(limit_def[3][0:6], color=SECANT_COLOR, buff=0.08)
        explain1 = Text("output at nearby point", font_size=18, color=SECANT_COLOR).next_to(box1, DOWN, buff=0.3)
        self.play(Create(box1), Write(explain1), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(box1), FadeOut(explain1), run_time=0.3)

        self.play(FadeOut(sub2b), run_time=0.2)

        sub2c = subtitle_persistent("Dividing by h gives the average rate of change over that interval.")
        self.play(FadeIn(sub2c), run_time=0.3)
        self.wait(2)
        self.play(FadeOut(sub2c), run_time=0.2)

        # ============================================================
        # Part 3: Substitute (2:25 - 2:40)
        # ============================================================

        sub3 = subtitle_persistent("Now substitute f(x) = x² into the formula.")

        step_label2 = Text("Step 2: Substitute", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        step2 = MathTex(
            r"f'(2) = \lim_{h \to 0} \frac{(2+h)^2 - 2^2}{h}",
            font_size=38,
            color=TEXT_COLOR,
        ).shift(DOWN * 0.3)

        self.play(
            ReplacementTransform(step_label, step_label2),
            FadeIn(sub3),
            run_time=0.5,
        )
        self.play(limit_def.animate.shift(UP * 0.8).set_opacity(0.4), run_time=0.4)
        self.play(Write(step2), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(sub3), run_time=0.2)

        # ============================================================
        # Part 4: Expand (2:40 - 2:55)
        # ============================================================

        sub4 = subtitle_persistent("Expand (2 + h) squared to get 4 + 4h + h squared.")

        step_label3 = Text("Step 3: Expand", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        step3 = MathTex(
            r"= \lim_{h \to 0} \frac{4 + 4h + h^2 - 4}{h}",
            font_size=38,
            color=TEXT_COLOR,
        ).next_to(step2, DOWN, buff=0.5)

        self.play(
            ReplacementTransform(step_label2, step_label3),
            FadeOut(limit_def),
            FadeIn(sub4),
            run_time=0.5,
        )
        self.play(step2.animate.shift(UP * 0.8), run_time=0.3)
        self.play(Write(step3), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(sub4), run_time=0.2)

        # ============================================================
        # Part 5: Simplify (2:55 - 3:05)
        # ============================================================

        sub5 = subtitle_persistent("The 4 and minus 4 cancel, leaving 4h + h squared over h.")

        step_label4 = Text("Step 4: Simplify", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        step4 = MathTex(
            r"= \lim_{h \to 0} \frac{4h + h^2}{h}",
            font_size=38,
            color=TEXT_COLOR,
        ).next_to(step3, DOWN, buff=0.5)

        self.play(
            ReplacementTransform(step_label3, step_label4),
            FadeOut(step2),
            FadeIn(sub5),
            run_time=0.5,
        )
        self.play(step3.animate.shift(UP * 0.8), run_time=0.3)
        self.play(Write(step4), run_time=1)
        self.wait(2)
        self.play(FadeOut(sub5), run_time=0.2)

        # ============================================================
        # Part 6: Factor and cancel (3:05 - 3:20)
        # ============================================================

        sub6 = subtitle_persistent("Factor h from the numerator. Since h approaches zero but is not zero, we can cancel.")

        step_label5 = Text("Step 5: Factor & Cancel", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        step5a = MathTex(
            r"= \lim_{h \to 0} \frac{h(4 + h)}{h}",
            font_size=38,
            color=TEXT_COLOR,
        ).next_to(step4, DOWN, buff=0.5)

        step5b = MathTex(
            r"= \lim_{h \to 0} (4 + h)",
            font_size=38,
            color=TEXT_COLOR,
        ).next_to(step5a, DOWN, buff=0.4)

        self.play(
            ReplacementTransform(step_label4, step_label5),
            FadeOut(step3),
            FadeIn(sub6),
            run_time=0.5,
        )
        self.play(step4.animate.shift(UP * 0.8), run_time=0.3)
        self.play(Write(step5a), run_time=1)
        self.wait(0.8)

        # Strike through h/h
        cancel_line = Line(
            step5a[0][10:11].get_left() + LEFT * 0.05,
            step5a[0][15:16].get_right() + RIGHT * 0.05,
            color=RED, stroke_width=3,
        )
        self.play(Create(cancel_line), run_time=0.5)
        self.play(Write(step5b), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(sub6), run_time=0.2)

        # ============================================================
        # Part 7: Evaluate the limit (3:20 - 3:30)
        # ============================================================

        sub7 = subtitle_persistent("Now let h go to zero. We get f prime of 2 equals 4.")

        step_label6 = Text("Step 6: Evaluate", font_size=24, color=TANGENT_COLOR).to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.8)

        # Clear previous steps
        self.play(
            FadeOut(step4), FadeOut(step5a), FadeOut(cancel_line),
            FadeOut(step5b),
            ReplacementTransform(step_label5, step_label6),
            FadeIn(sub7),
            run_time=0.6,
        )

        result = MathTex(
            r"f'(2) = 4",
            font_size=56,
            color=TANGENT_COLOR,
        ).shift(ORIGIN)

        result_box = SurroundingRectangle(result, color=TANGENT_COLOR, buff=0.3, corner_radius=0.1)

        self.play(Write(result), run_time=1)
        self.play(Create(result_box), run_time=0.5)

        # Flash effect
        self.play(
            result.animate.set_color(HIGHLIGHT_COLOR),
            run_time=0.3,
        )
        self.play(
            result.animate.set_color(TANGENT_COLOR),
            run_time=0.3,
        )

        self.wait(2)
        self.play(FadeOut(sub7), run_time=0.2)

        # Fade all
        self.play(
            FadeOut(result), FadeOut(result_box), FadeOut(step_label6),
            run_time=0.8,
        )
