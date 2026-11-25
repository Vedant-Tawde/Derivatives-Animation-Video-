"""
M3 Derivative Animation - Complete Main Script
==============================================
Topic: Derivative and Rate of Change – From Secant Line to Tangent Line
Duration: ~4 minutes 45 seconds (1080p, 30 FPS)
Course: Linear Algebra and Calculus (M3)

Features:
- Professional 2D educational animation
- Dark navy theme (#1a1a2e)
- Color coding: Cyan (parabola), Yellow (point A), Orange (secant), Green (tangent)
- Auto-exports subtitles.srt and voiceover_script.txt with synchronized timestamps
- 100% standalone (uses Pango/Cairo text, no LaTeX dependency)
"""

import os
from manim import *
import numpy as np

# Global Color Palette
BG_COLOR = "#1a1a2e"
CURVE_COLOR = "#00d4ff"      # Cyan for function curve
POINT_COLOR = "#ffd700"      # Yellow for fixed point A
SECANT_COLOR = "#ff8c00"     # Orange for secant line and point B
TANGENT_COLOR = "#00ff88"    # Green for tangent line
TEXT_COLOR = WHITE
SUBTITLE_COLOR = WHITE
HIGHLIGHT_COLOR = "#ffff00"

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

def format_timestamp_srt(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        secs += 1
        millis = 0
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def format_timestamp_human(seconds):
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"

class FullAnimation(Scene):
    """Complete M3 Derivative Animation — all 6 scenes in sequence."""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.subtitles_log = []

        self.scene_1_hook()
        self.scene_2_introduction()
        self.scene_3_visual_intuition()
        self.scene_4_worked_example()
        self.scene_5_interpretation()
        self.scene_6_summary()

        self.export_subtitles_and_script()

    # Subtitle Helpers
    def make_sub_mobject(self, text, font_size=22):
        sub = Text(text, font_size=font_size, color=SUBTITLE_COLOR, font="sans-serif")
        sub.to_edge(DOWN, buff=0.4)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.82, buff=0.15)
        return VGroup(sub_bg, sub)

    def start_sub(self, text, font_size=22):
        sub = self.make_sub_mobject(text, font_size)
        start_t = self.renderer.time
        self.play(FadeIn(sub), run_time=0.35)
        return sub, start_t, text

    def end_sub(self, sub_record):
        sub, start_t, text = sub_record
        self.play(FadeOut(sub), run_time=0.3)
        end_t = self.renderer.time
        self.subtitles_log.append((start_t, end_t, text))

    def export_subtitles_and_script(self):
        # 1. SRT file
        srt_lines = []
        for idx, (st, et, txt) in enumerate(self.subtitles_log, 1):
            srt_lines.append(f"{idx}\n{format_timestamp_srt(st)} --> {format_timestamp_srt(et)}\n{txt}\n")
        srt_content = "\n".join(srt_lines)

        # 2. Voiceover script file
        vo_lines = [
            "==================================================================",
            "M3 MATHEMATICS EDUCATIONAL ANIMATION — SYNCHRONIZED VOICEOVER SCRIPT",
            "Topic: Derivative and Rate of Change – From Secant Line to Tangent Line",
            "Target Duration: ~4:45 | Resolution: 1080p | FPS: 30",
            "==================================================================\n",
            "INSTRUCTIONS FOR VOICEOVER RECORDING:",
            "- Speak naturally, clearly, and at a calm, educational pace.",
            "- Follow the exact timestamps below for perfect video synchronization.",
            "- Each numbered dialogue matches the on-screen visual and burned-in subtitles.\n",
            "------------------------------------------------------------------\n"
        ]
        for idx, (st, et, txt) in enumerate(self.subtitles_log, 1):
            st_h = format_timestamp_human(st)
            et_h = format_timestamp_human(et)
            vo_lines.append(f"[{st_h} - {et_h}] ({idx}) {txt}\n")
        vo_content = "\n".join(vo_lines)

        paths_to_write = [
            ("/Users/vedanttawde/M3_Derivative_Animation/output/subtitles.srt", srt_content),
            ("/Users/vedanttawde/M3_Derivative_Animation/documentation/voiceover_script.txt", vo_content),
            ("/Users/vedanttawde/Desktop/maths vid/M3_Derivative_Animation/output/subtitles.srt", srt_content),
            ("/Users/vedanttawde/Desktop/maths vid/M3_Derivative_Animation/documentation/voiceover_script.txt", vo_content),
        ]
        for p, c in paths_to_write:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(c)

    # ================================================================
    # SCENE 1 — Hook / Real-World Context (0:00 - 0:30)
    # ================================================================
    def scene_1_hook(self):
        road = Rectangle(width=14, height=1.2,
                         fill_color="#333333", fill_opacity=1,
                         stroke_color="#555555", stroke_width=1).shift(DOWN * 1.0)
        dashes = VGroup(*[
            Line(LEFT * 0.3, RIGHT * 0.3, color=YELLOW, stroke_width=2)
            .move_to(road.get_center() + RIGHT * i)
            for i in range(-6, 7)
        ])

        car_body = RoundedRectangle(corner_radius=0.15, width=1.6, height=0.6,
                                    fill_color="#e74c3c", fill_opacity=1,
                                    stroke_color="#c0392b", stroke_width=2)
        car_top = RoundedRectangle(corner_radius=0.1, width=0.9, height=0.4,
                                   fill_color="#e74c3c", fill_opacity=1,
                                   stroke_color="#c0392b", stroke_width=2).shift(UP * 0.4)
        w1 = Circle(radius=0.15, fill_color="#2c3e50", fill_opacity=1,
                     stroke_color=WHITE, stroke_width=1).shift(LEFT * 0.5 + DOWN * 0.35)
        w2 = w1.copy().shift(RIGHT * 1)
        car = VGroup(car_body, car_top, w1, w2).move_to(LEFT * 5 + DOWN * 0.3)

        self.play(FadeIn(road), FadeIn(dashes), run_time=0.8)
        self.play(FadeIn(car), run_time=0.4)

        sub1 = self.start_sub("Imagine a car driving along a road…")
        self.play(car.animate.shift(RIGHT * 4), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(2.5)
        self.end_sub(sub1)

        sub2 = self.start_sub("How do we measure its speed at one exact instant?")
        sp_axes = Axes(x_range=[0, 5, 1], y_range=[0, 60, 20],
                       x_length=3, y_length=2,
                       axis_config={"color": TEXT_COLOR, "include_numbers": False},
                       tips=False).shift(UP * 2 + RIGHT * 3)
        sp_labels = VGroup(
            Text("time", font_size=14, color=TEXT_COLOR).next_to(sp_axes.x_axis, DOWN, buff=0.1),
            Text("speed", font_size=14, color=TEXT_COLOR).next_to(sp_axes.y_axis, LEFT, buff=0.1).rotate(PI / 2),
        )
        sp_curve = sp_axes.plot(lambda x: 10 * x + 5 * np.sin(2 * x),
                                x_range=[0, 4.5], color=CURVE_COLOR)
        yval = 10 * 2.5 + 5 * np.sin(5)
        dot_sp = Dot(sp_axes.c2p(2.5, yval), color=POINT_COLOR, radius=0.08)
        dash_sp = DashedLine(sp_axes.c2p(2.5, 0), sp_axes.c2p(2.5, yval),
                             color=POINT_COLOR, dash_length=0.08)

        self.play(Create(sp_axes), Write(sp_labels), run_time=0.8)
        self.play(Create(sp_curve), run_time=1.5)
        self.play(Create(dash_sp), FadeIn(dot_sp), run_time=0.8)
        self.wait(3.5)
        self.end_sub(sub2)

        sub3 = self.start_sub("Average speed uses distance over time, but instantaneous speed needs calculus.")
        self.wait(5.3)
        self.end_sub(sub3)

        car_scene = VGroup(road, dashes, car, sp_axes, sp_labels,
                           sp_curve, dot_sp, dash_sp)
        self.play(FadeOut(car_scene), run_time=0.8)

        # Title Card
        title = Text("DERIVATIVES", font_size=56, color=TEXT_COLOR, weight=BOLD).shift(UP * 0.5)
        subtitle = Text("FROM SECANT TO TANGENT", font_size=32, color=CURVE_COLOR
                         ).next_to(title, DOWN, buff=0.4)
        accent = Line(LEFT * 3, RIGHT * 3, color=TANGENT_COLOR, stroke_width=3
                       ).next_to(subtitle, DOWN, buff=0.3)
        sub4 = self.start_sub("Derivatives: From Secant to Tangent")

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle, shift=UP * 0.3), Create(accent), run_time=1.0)
        self.wait(4.7)
        self.end_sub(sub4)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(accent), run_time=0.8)

    # ================================================================
    # SCENE 2 — Concept Introduction (0:30 - 1:05)
    # ================================================================
    def scene_2_introduction(self):
        func_tex = Text("f(x) = x²", font_size=48, color=TEXT_COLOR, font="serif").shift(UP * 2)
        desc = Text("This function produces a parabola.", font_size=26, color=TEXT_COLOR
                     ).next_to(func_tex, DOWN, buff=0.4)
        sub1 = self.start_sub("Consider the function f(x) equals x squared, producing a parabola.")
        self.play(Write(func_tex), run_time=1.0)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.8)
        self.wait(4.7)
        self.end_sub(sub1)

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

        sub2 = self.start_sub("Here is its graph on the Cartesian coordinate plane.")
        self.play(Create(axes), FadeIn(axis_nums), Write(xl), Write(yl), run_time=1.2)
        self.play(Create(curve), run_time=1.5)
        self.play(Write(clbl), run_time=0.6)
        self.wait(4.5)
        self.end_sub(sub2)

        pA = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.1, z_index=5)
        lA = Text("A = (2, 4)", font_size=20, color=POINT_COLOR).next_to(pA, LEFT + UP, buff=0.15)

        h = 1; bx = 3; by = 9
        pB = Dot(axes.c2p(bx, by), color=SECANT_COLOR, radius=0.1, z_index=5)
        lB = Text("B = (2+h, (2+h)²)", font_size=20, color=SECANT_COLOR).next_to(pB, RIGHT + UP, buff=0.15)

        hbrace = BraceBetweenPoints(axes.c2p(2, -0.8), axes.c2p(3, -0.8),
                                     direction=DOWN, color=TEXT_COLOR)
        hlbl = Text("h", font_size=22, color=TEXT_COLOR, font="serif").next_to(hbrace, DOWN, buff=0.12)

        sub3 = self.start_sub("We choose a fixed point A at x = 2, and a neighboring point B at x = 2 + h.")
        self.play(FadeIn(pA), Write(lA), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(pB), Write(lB), run_time=0.8)
        self.play(Create(hbrace), Write(hlbl), run_time=0.7)
        self.wait(5.5)
        self.end_sub(sub3)

        sec_slope = 5
        sec = Line(axes.c2p(0.5, 4 + sec_slope * (0.5 - 2)),
                   axes.c2p(4.5, 4 + sec_slope * (4.5 - 2)),
                   color=SECANT_COLOR, stroke_width=3)
        slbl = Text("Secant Line", font_size=20, color=SECANT_COLOR).next_to(axes.c2p(4, 14), RIGHT, buff=0.25)

        sub4 = self.start_sub("The straight line passing through both points is called a secant line.")
        self.play(Create(sec), run_time=1.0)
        self.play(Write(slbl), run_time=0.6)
        self.wait(5.5)
        self.end_sub(sub4)

        all2 = VGroup(axes, axis_nums, xl, yl, curve, clbl, pA, lA, pB, lB,
                       hbrace, hlbl, sec, slbl, func_tex)
        self.play(FadeOut(all2), run_time=0.8)

    # ================================================================
    # SCENE 3 — Visual Intuition (1:05 - 2:00)
    # ================================================================
    def scene_3_visual_intuition(self):
        axes = Axes(x_range=[-0.5, 5.5, 1], y_range=[-1, 22, 5],
                     x_length=7.5, y_length=5.5,
                     axis_config={"color": TEXT_COLOR, "include_numbers": False},
                     tips=True).shift(LEFT * 1.5 + DOWN * 0.2)
        axis_nums = add_axis_numbers(axes, range(0, 6), [5, 10, 15, 20])
        xl = Text("x", font_size=16, color=TEXT_COLOR).next_to(axes.x_axis, RIGHT, buff=0.2)
        yl = Text("f(x)", font_size=16, color=TEXT_COLOR).next_to(axes.y_axis, UP, buff=0.2)
        curve = axes.plot(lambda x: x ** 2, x_range=[-0.3, 4.6], color=CURVE_COLOR, stroke_width=3)
        clbl = Text("f(x) = x²", font_size=20, color=CURVE_COLOR, font="serif").next_to(axes.c2p(4.3, 18), RIGHT, buff=0.15)

        pA = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.1, z_index=5)
        lA = Text("A(2, 4)", font_size=18, color=POINT_COLOR).next_to(pA, LEFT + UP, buff=0.12)

        sub_intro = self.start_sub("Watch what happens as point B moves progressively closer to point A.")
        self.play(Create(axes), FadeIn(axis_nums), Write(xl), Write(yl), run_time=0.8)
        self.play(Create(curve), Write(clbl), run_time=1.0)
        self.play(FadeIn(pA), Write(lA), run_time=0.7)
        self.wait(4.5)
        self.end_sub(sub_intro)

        ttl = Text("Secant Slopes", font_size=20, color=TEXT_COLOR, weight=BOLD
                    ).to_edge(RIGHT, buff=0.5).shift(UP * 2.8)
        hcol = Text("h", font_size=18, color=TEXT_COLOR, font="serif").next_to(ttl, DOWN, buff=0.25).shift(LEFT * 0.6)
        scol = Text("slope", font_size=18, color=TEXT_COLOR).next_to(ttl, DOWN, buff=0.25).shift(RIGHT * 0.6)
        hline = Line(hcol.get_left() + DOWN * 0.18 + LEFT * 0.15,
                     scol.get_right() + DOWN * 0.18 + RIGHT * 0.15,
                     color=TEXT_COLOR, stroke_width=1)
        self.play(Write(ttl), Write(hcol), Write(scol), Create(hline), run_time=0.6)

        h_vals = [2, 1, 0.5, 0.1]
        slopes = [6, 5, 4.5, 4.1]
        sub_txts = [
            "With h = 2, B is at (4, 16). The average secant slope is 6.",
            "With h = 1, B moves to (3, 9). The secant slope becomes 5.",
            "With h = 0.5, B is at (2.5, 6.25). The slope reduces to 4.5.",
            "With h = 0.1, B is at (2.1, 4.41). The secant slope is now 4.1.",
        ]

        table_mobs = []
        prev_sec = prev_pB = prev_lB = None

        for i, (h, sl, stxt) in enumerate(zip(h_vals, slopes, sub_txts)):
            bx = 2 + h; by = bx ** 2
            new_pB = Dot(axes.c2p(bx, by), color=SECANT_COLOR, radius=0.1, z_index=5)
            if by == int(by) and bx == int(bx):
                blbl_str = f"B({int(bx)}, {int(by)})"
            else:
                blbl_str = f"B({bx:.1f}, {by:.2f})"
            new_lB = Text(blbl_str, font_size=18, color=SECANT_COLOR
                          ).next_to(new_pB, RIGHT + UP, buff=0.12)

            m = (by - 4) / (bx - 2)
            x0 = max(-0.3, 2 - 2.5); x1 = min(5.2, 2 + 2.5)
            new_sec = Line(axes.c2p(x0, 4 + m * (x0 - 2)),
                           axes.c2p(x1, 4 + m * (x1 - 2)),
                           color=SECANT_COLOR, stroke_width=2.5)

            h_e = Text(str(h), font_size=18, color=SECANT_COLOR, font="serif"
                       ).next_to(hcol, DOWN, buff=0.25 + i * 0.4)
            s_e = Text(str(sl), font_size=18, color=SECANT_COLOR, font="serif"
                       ).next_to(scol, DOWN, buff=0.25 + i * 0.4)

            sub = self.start_sub(stxt, font_size=20)

            if prev_sec is None:
                self.play(FadeIn(new_pB), Write(new_lB), Create(new_sec),
                          Write(h_e), Write(s_e), run_time=1.0)
            else:
                self.play(ReplacementTransform(prev_pB, new_pB),
                          ReplacementTransform(prev_lB, new_lB),
                          ReplacementTransform(prev_sec, new_sec),
                          Write(h_e), Write(s_e), run_time=1.2)
            self.wait(5.5)
            self.end_sub(sub)
            prev_sec, prev_pB, prev_lB = new_sec, new_pB, new_lB
            table_mobs += [h_e, s_e]

        sub_lim = self.start_sub("As h approaches zero, the secant line approaches a unique limiting line: the tangent line.")
        tangent = Line(axes.c2p(0, -4), axes.c2p(4.5, 4 * 4.5 - 4),
                       color=TANGENT_COLOR, stroke_width=3)
        tlbl = Text("Tangent Line", font_size=18, color=TANGENT_COLOR
                     ).next_to(axes.c2p(4, 12), RIGHT, buff=0.2)
        lim_txt = Text("slope → 4", font_size=18, color=TANGENT_COLOR, font="serif"
                       ).next_to(scol, DOWN, buff=0.25 + 4 * 0.4)

        self.play(ReplacementTransform(prev_sec, tangent),
                  FadeOut(prev_pB), FadeOut(prev_lB),
                  Write(tlbl), Write(lim_txt), run_time=1.5)
        self.wait(6.5)
        self.end_sub(sub_lim)

        sub_inst = self.start_sub("This tangent line slope represents the instantaneous rate of change at x = 2.")
        self.wait(5.5)
        self.end_sub(sub_inst)

        all3 = VGroup(axes, axis_nums, xl, yl, curve, clbl, pA, lA, tangent, tlbl,
                       ttl, hcol, scol, hline, lim_txt, *table_mobs)
        self.play(FadeOut(all3), run_time=0.8)

    # ================================================================
    # SCENE 4 — Worked Example (2:00 - 3:30)
    # ================================================================
    def scene_4_worked_example(self):
        heading = Text("Finding the Derivative", font_size=34, color=TEXT_COLOR,
                        weight=BOLD).to_edge(UP, buff=0.5)
        func = Text("f(x) = x²", font_size=38, color=CURVE_COLOR, font="serif").shift(UP * 1.5)
        goal = Text("Find  f′(2)", font_size=34, color=POINT_COLOR, font="serif"
                    ).next_to(func, DOWN, buff=0.5)
        sub1 = self.start_sub("Now let us calculate the exact derivative using the limit definition.")
        self.play(Write(heading), run_time=0.6)
        self.play(Write(func), run_time=0.8)
        self.play(Write(goal), run_time=0.6)
        self.wait(5.0)
        self.end_sub(sub1)
        self.play(FadeOut(heading), FadeOut(func), FadeOut(goal), run_time=0.6)

        def step_lbl(text):
            return Text(text, font_size=22, color=TANGENT_COLOR
                        ).to_edge(UP, buff=0.45).to_edge(LEFT, buff=0.7)

        # Step 1
        sub2 = self.start_sub("The derivative f prime of 2 is defined as the limit of [f(2+h) - f(2)] over h as h approaches 0.")
        lbl1 = step_lbl("Step 1: Limit Definition")
        eq1 = Text("f′(2) = lim (h→0) [ f(2+h) − f(2) ] / h",
                   font_size=34, color=TEXT_COLOR, font="serif").shift(UP * 1.0)
        self.play(Write(lbl1), run_time=0.5)
        self.play(Write(eq1), run_time=1.5)
        self.wait(6.5)
        self.end_sub(sub2)

        sub2b = self.start_sub("f(2+h) is the output at 2+h, f(2) is the output at 2, and h is the interval width.")
        self.wait(7.0)
        self.end_sub(sub2b)

        # Step 2
        sub3 = self.start_sub("Step two: substitute the function f(x) = x squared into the formula.")
        lbl2 = step_lbl("Step 2: Substitute")
        eq2 = Text("= lim (h→0) [ (2+h)² − 2² ] / h",
                   font_size=34, color=TEXT_COLOR, font="serif").shift(UP * 0.1)
        self.play(ReplacementTransform(lbl1, lbl2), run_time=0.5)
        self.play(eq1.animate.shift(UP * 0.5).set_opacity(0.35), run_time=0.4)
        self.play(Write(eq2), run_time=1.2)
        self.wait(6.3)
        self.end_sub(sub3)

        # Step 3
        sub4 = self.start_sub("Step three: expand (2+h) squared to obtain 4 + 4h + h squared.")
        lbl3 = step_lbl("Step 3: Expand")
        eq3 = Text("= lim (h→0) [ 4 + 4h + h² − 4 ] / h",
                   font_size=34, color=TEXT_COLOR, font="serif").next_to(eq2, DOWN, buff=0.45)
        self.play(ReplacementTransform(lbl2, lbl3), FadeOut(eq1), run_time=0.5)
        self.play(eq2.animate.shift(UP * 0.6), run_time=0.3)
        self.play(Write(eq3), run_time=1.2)
        self.wait(6.5)
        self.end_sub(sub4)

        # Step 4
        sub5 = self.start_sub("Step four: the constant 4 cancels out with minus 4, leaving (4h + h squared) over h.")
        lbl4 = step_lbl("Step 4: Simplify")
        eq4 = Text("= lim (h→0) [ 4h + h² ] / h",
                   font_size=34, color=TEXT_COLOR, font="serif").next_to(eq3, DOWN, buff=0.45)
        self.play(ReplacementTransform(lbl3, lbl4), FadeOut(eq2), run_time=0.5)
        self.play(eq3.animate.shift(UP * 0.6), run_time=0.3)
        self.play(Write(eq4), run_time=1.0)
        self.wait(6.5)
        self.end_sub(sub5)

        # Step 5
        sub6 = self.start_sub("Step five: factor h from the numerator. Since h approaches zero but is never zero, we cancel h.")
        lbl5 = step_lbl("Step 5: Factor & Cancel")
        eq5a = Text("= lim (h→0) [ h(4 + h) ] / h",
                    font_size=34, color=TEXT_COLOR, font="serif").next_to(eq4, DOWN, buff=0.4)
        eq5b = Text("= lim (h→0) (4 + h)", font_size=34,
                    color=TEXT_COLOR, font="serif").next_to(eq5a, DOWN, buff=0.35)

        self.play(ReplacementTransform(lbl4, lbl5), FadeOut(eq3), run_time=0.5)
        self.play(eq4.animate.shift(UP * 0.6), run_time=0.3)
        self.play(Write(eq5a), run_time=1.0)
        self.wait(1.0)
        self.play(Write(eq5b), run_time=0.8)
        self.wait(8.0)
        self.end_sub(sub6)

        # Step 6
        sub7 = self.start_sub("Step six: evaluate the limit as h goes to zero. 4 plus zero equals 4.")
        lbl6 = step_lbl("Step 6: Evaluate")
        self.play(FadeOut(eq4), FadeOut(eq5a), FadeOut(eq5b),
                  ReplacementTransform(lbl5, lbl6), run_time=0.6)

        result = Text("f′(2) = 4", font_size=56, color=TANGENT_COLOR, font="serif")
        rbox = SurroundingRectangle(result, color=TANGENT_COLOR, buff=0.3, corner_radius=0.1)
        self.play(Write(result), run_time=1.0)
        self.play(Create(rbox), run_time=0.5)
        self.play(result.animate.set_color(HIGHLIGHT_COLOR), run_time=0.3)
        self.play(result.animate.set_color(TANGENT_COLOR), run_time=0.3)
        self.wait(7.5)
        self.end_sub(sub7)

        sub7b = self.start_sub("Therefore, the instantaneous rate of change f prime of 2 equals exactly 4.")
        self.wait(7.0)
        self.end_sub(sub7b)

        self.play(FadeOut(result), FadeOut(rbox), FadeOut(lbl6), run_time=0.7)

    # ================================================================
    # SCENE 5 — Geometric Interpretation (3:30 - 4:20)
    # ================================================================
    def scene_5_interpretation(self):
        axes = Axes(x_range=[-1, 5.5, 1], y_range=[-5, 20, 5],
                     x_length=7.5, y_length=5.5,
                     axis_config={"color": TEXT_COLOR, "include_numbers": False},
                     tips=True).shift(LEFT * 1 + DOWN * 0.3)
        axis_nums = add_axis_numbers(axes, range(0, 6), [-5, 5, 10, 15, 20])
        xl = Text("x", font_size=16, color=TEXT_COLOR).next_to(axes.x_axis, RIGHT, buff=0.2)
        yl = Text("f(x)", font_size=16, color=TEXT_COLOR).next_to(axes.y_axis, UP, buff=0.2)
        curve = axes.plot(lambda x: x ** 2, x_range=[-0.5, 4.4], color=CURVE_COLOR, stroke_width=3)
        clbl = Text("f(x) = x²", font_size=20, color=CURVE_COLOR, font="serif").next_to(axes.c2p(4, 16), UR, buff=0.12)
        pA = Dot(axes.c2p(2, 4), color=POINT_COLOR, radius=0.11, z_index=5)
        lA = Text("(2, 4)", font_size=18, color=POINT_COLOR).next_to(pA, LEFT + UP, buff=0.12)

        sub1 = self.start_sub("Returning to the graph, let us draw the tangent line at point A(2, 4).")
        self.play(Create(axes), FadeIn(axis_nums), Write(xl), Write(yl), Create(curve), Write(clbl), run_time=1.0)
        self.play(FadeIn(pA), Write(lA), run_time=0.7)
        self.wait(1.5)

        tangent = axes.plot(lambda x: 4 * x - 4, x_range=[0, 4.5],
                             color=TANGENT_COLOR, stroke_width=3)
        tlbl = Text("Tangent Line", font_size=18, color=TANGENT_COLOR
                     ).next_to(axes.c2p(4, 12), RIGHT, buff=0.12)
        self.play(Create(tangent), Write(tlbl), run_time=1.0)
        self.wait(4.0)
        self.end_sub(sub1)

        eq_pos = RIGHT * 3.5 + UP * 2
        sub2 = self.start_sub("Using point-slope form: y minus y1 equals m times (x minus x1).")
        eq_lbl = Text("Point-slope form", font_size=16, color=TANGENT_COLOR).move_to(eq_pos + UP * 0.4)
        eq1 = Text("y − y₁ = m(x − x₁)", font_size=24, font="serif").move_to(eq_pos)
        self.play(Write(eq_lbl), Write(eq1), run_time=0.8)
        self.wait(5.5)
        self.end_sub(sub2)

        sub3 = self.start_sub("Substitute point (2, 4) and our calculated slope m = 4: y minus 4 equals 4 times (x minus 2).")
        eq2 = Text("y − 4 = 4(x − 2)", font_size=24, font="serif").next_to(eq1, DOWN, buff=0.35)
        self.play(Write(eq2), run_time=0.8)
        self.wait(6.0)
        self.end_sub(sub3)

        sub4 = self.start_sub("Expanding and simplifying gives the tangent line equation: y equals 4x minus 4.")
        eq3 = Text("y = 4x − 4", font_size=28, color=TANGENT_COLOR, font="serif").next_to(eq2, DOWN, buff=0.35)
        eb = SurroundingRectangle(eq3, color=TANGENT_COLOR, buff=0.12, corner_radius=0.07)
        self.play(Write(eq3), Create(eb), run_time=0.8)
        self.wait(5.8)
        self.end_sub(sub4)

        sub5 = self.start_sub("Blue: parabola. Green: tangent at x = 2 with slope 4.")
        leg = VGroup(
            VGroup(Line(LEFT * 0.25, RIGHT * 0.25, color=CURVE_COLOR, stroke_width=3),
                   Text("f(x) = x²", font_size=16, color=CURVE_COLOR, font="serif")).arrange(RIGHT, buff=0.12),
            VGroup(Line(LEFT * 0.25, RIGHT * 0.25, color=TANGENT_COLOR, stroke_width=3),
                   Text("y = 4x − 4", font_size=16, color=TANGENT_COLOR, font="serif")).arrange(RIGHT, buff=0.12),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).to_corner(DL, buff=0.7).shift(UP * 0.7)
        lbg = BackgroundRectangle(leg, color=BG_COLOR, fill_opacity=0.85, buff=0.12)
        self.play(FadeIn(lbg), Write(leg), run_time=0.8)
        self.wait(5.5)
        self.end_sub(sub5)

        sub6 = self.start_sub("The green tangent slope of 4 represents the exact instantaneous rate of change at x = 2.")
        sl_h = Text("slope = f′(2) = 4", font_size=26, color=POINT_COLOR, font="serif"
                    ).next_to(eb, DOWN, buff=0.4)
        self.play(Write(sl_h), run_time=0.8)
        self.wait(5.7)
        self.end_sub(sub6)

        all5 = VGroup(axes, axis_nums, xl, yl, curve, clbl, pA, lA, tangent, tlbl,
                       eq_lbl, eq1, eq2, eq3, eb, lbg, leg, sl_h)
        self.play(FadeOut(all5), run_time=0.8)

    # ================================================================
    # SCENE 6 — Summary & Credits (4:20 - 4:45)
    # ================================================================
    def scene_6_summary(self):
        heading = Text("Key Takeaways", font_size=34, color=TEXT_COLOR, weight=BOLD
                        ).to_edge(UP, buff=0.5)
        sub0 = self.start_sub("To summarize our three core takeaways from this lesson:")
        self.play(Write(heading), run_time=0.6)
        self.wait(3.2)
        self.end_sub(sub0)

        items = [
            ("1.", "A secant line connects two distinct points on a curve,\nmeasuring average rate of change.", SECANT_COLOR,
             "First: a secant line connects two distinct points on a curve, measuring average rate of change."),
            ("2.", "A tangent line touches at a single point, representing\nthe instantaneous rate of change.", TANGENT_COLOR,
             "Second: a tangent line touches at a single point, representing the instantaneous rate of change."),
            ("3.", "A derivative is the limiting value of the secant slopes\nas the interval h approaches zero.", CURVE_COLOR,
             "Third: the derivative is the limiting value of the secant slopes as the interval h approaches zero."),
        ]

        groups = VGroup()
        for num, txt, col, _ in items:
            n = Text(num, font_size=22, color=col, weight=BOLD)
            t = Text(txt, font_size=18, color=TEXT_COLOR, line_spacing=1.2)
            g = VGroup(n, t).arrange(RIGHT, buff=0.15, aligned_edge=UP)
            groups.add(g)
        groups.arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(DOWN * 0.1)

        for i, g in enumerate(groups):
            sub = self.start_sub(items[i][3], font_size=20)
            self.play(FadeIn(g, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(4.5)
            self.end_sub(sub)

        res = Text("f(x) = x²   ⇒   f′(2) = 4", font_size=34,
                   color=POINT_COLOR, font="serif").next_to(groups, DOWN, buff=0.5)
        rbox = SurroundingRectangle(res, color=POINT_COLOR, buff=0.18, corner_radius=0.08)
        sr = self.start_sub("For f(x) = x squared at x = 2, our derivative f prime of 2 is 4.")
        self.play(Write(res), Create(rbox), run_time=0.8)
        self.wait(4.5)
        self.end_sub(sr)

        self.play(FadeOut(heading), FadeOut(groups), FadeOut(res), FadeOut(rbox), run_time=0.8)

        # Credits
        sc = self.start_sub("Thank you for watching this M3 Linear Algebra and Calculus presentation.")
        cr = VGroup(
            Text("M3 – LINEAR ALGEBRA AND CALCULUS", font_size=26, color=CURVE_COLOR, weight=BOLD),
            Text("Topic: Derivative and Rate of Change", font_size=20, color=TEXT_COLOR),
            Text("Student Name: [INSERT STUDENT NAME]", font_size=20, color=TEXT_COLOR),
            Text("Student ID: [INSERT STUDENT ID]", font_size=20, color=TEXT_COLOR),
            Line(LEFT * 3.5, RIGHT * 3.5, color=TANGENT_COLOR, stroke_width=2),
            Text("AI Disclosure: AI tools assisted in animation development\n"
                 "and visual production. Mathematical calculations and\n"
                 "explanations were reviewed for accuracy.",
                 font_size=14, color="#888888", line_spacing=1.3),
        ).arrange(DOWN, buff=0.25).shift(DOWN * 0.1)

        self.play(FadeIn(cr, shift=UP * 0.3), run_time=1.2)
        self.wait(5.5)
        self.end_sub(sc)
        self.wait(0.5)
        self.play(FadeOut(cr), run_time=1.0)
