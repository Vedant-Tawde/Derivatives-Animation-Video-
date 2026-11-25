"""
Scene 6: Summary and Credits
Duration: ~25 seconds (4:20 - 4:45)

Three key takeaways, final result, closing credits.
"""

from manim import *

BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"
POINT_COLOR = "#ffd700"
SECANT_COLOR = "#ff8c00"
TANGENT_COLOR = "#00ff88"
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE

class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        def subtitle_persistent(text, font_size=22):
            sub = Text(
                text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif",
            ).to_edge(DOWN, buff=0.4)
            sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.7, buff=0.15)
            return VGroup(sub_bg, sub)

        # ============================================================
        # Part 1: Key Takeaways (4:20 - 4:35)
        # ============================================================

        heading = Text("Key Takeaways", font_size=36, color=TEXT_COLOR, weight=BOLD).to_edge(UP, buff=0.6)

        sub1 = subtitle_persistent("Let us summarize what we have learned.")
        self.play(Write(heading), FadeIn(sub1), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(sub1), run_time=0.2)

        # Three takeaways
        takeaways = [
            ("1.", "A secant line connects two distinct points on a curve.", SECANT_COLOR),
            ("2.", "A tangent line represents the instantaneous rate of change at a point.", TANGENT_COLOR),
            ("3.", "A derivative is the limit of the average rate of change as the interval approaches zero.", CURVE_COLOR),
        ]

        takeaway_groups = VGroup()
        sub_texts = [
            "First: a secant line connects two points on a curve.",
            "Second: a tangent line gives the instantaneous rate of change.",
            "Third: the derivative is the limit of the average rate of change.",
        ]

        for i, (num, text, color) in enumerate(takeaways):
            num_mob = Text(num, font_size=24, color=color, weight=BOLD)
            text_mob = Text(text, font_size=21, color=TEXT_COLOR)
            group = VGroup(num_mob, text_mob).arrange(RIGHT, buff=0.2, aligned_edge=UP)
            takeaway_groups.add(group)

        takeaway_groups.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(DOWN * 0.2)

        for i, group in enumerate(takeaway_groups):
            sub = subtitle_persistent(sub_texts[i], font_size=20)
            self.play(FadeIn(group, shift=RIGHT * 0.3), FadeIn(sub), run_time=0.6)
            self.wait(1.8)
            self.play(FadeOut(sub), run_time=0.2)

        # Final result
        sub_result = subtitle_persistent("For f(x) = x² at x = 2, the derivative equals 4.")

        result = MathTex(
            r"f(x) = x^2 \quad \Rightarrow \quad f'(2) = 4",
            font_size=36,
            color=POINT_COLOR,
        ).next_to(takeaway_groups, DOWN, buff=0.6)

        result_box = SurroundingRectangle(result, color=POINT_COLOR, buff=0.2, corner_radius=0.1)

        self.play(Write(result), Create(result_box), FadeIn(sub_result), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(sub_result), run_time=0.2)

        # Fade out summary
        self.play(
            FadeOut(heading), FadeOut(takeaway_groups),
            FadeOut(result), FadeOut(result_box),
            run_time=0.8,
        )

        # ============================================================
        # Part 2: Credits (4:35 - 4:45)
        # ============================================================

        sub_credits = subtitle_persistent("Thank you for watching.")

        credits_title = Text(
            "M3 – LINEAR ALGEBRA AND CALCULUS",
            font_size=28, color=CURVE_COLOR, weight=BOLD,
        ).shift(UP * 2)

        credits_topic = Text(
            "Topic: Derivative and Rate of Change",
            font_size=22, color=TEXT_COLOR,
        ).next_to(credits_title, DOWN, buff=0.4)

        credits_name = Text(
            "Student Name: [INSERT STUDENT NAME]",
            font_size=22, color=TEXT_COLOR,
        ).next_to(credits_topic, DOWN, buff=0.3)

        credits_id = Text(
            "Student ID: [INSERT STUDENT ID]",
            font_size=22, color=TEXT_COLOR,
        ).next_to(credits_name, DOWN, buff=0.2)

        credits_line = Line(LEFT * 4, RIGHT * 4, color=TANGENT_COLOR, stroke_width=2).next_to(credits_id, DOWN, buff=0.4)

        ai_disc = Text(
            "AI Disclosure: AI tools assisted in animation development\nand visual production. Mathematical calculations and\nexplanations were reviewed for accuracy.",
            font_size=16, color="#888888",
            line_spacing=1.3,
        ).next_to(credits_line, DOWN, buff=0.3)

        credits_group = VGroup(
            credits_title, credits_topic, credits_name, credits_id,
            credits_line, ai_disc,
        )

        self.play(
            FadeIn(credits_group, shift=UP * 0.3),
            FadeIn(sub_credits),
            run_time=1.2,
        )
        self.wait(3)
        self.play(FadeOut(sub_credits), run_time=0.2)
        self.wait(0.5)
        self.play(FadeOut(credits_group), run_time=1)
