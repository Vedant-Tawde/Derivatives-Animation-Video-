# M3 Mathematics Educational Animation: Derivative and Rate of Change
## Topic: From Secant Line to Tangent Line

**Course:** Linear Algebra and Calculus (M3) • Internal Assessment  
**Concept:** Derivative as Instantaneous Rate of Change via the Limit of Secant Slopes  
**Central Mathematical Example:** $f(x) = x^2$ evaluated at $x = 2$  
**Target Audience:** Engineering and College Mathematics Students  

---

## 📽️ Project Overview

This repository contains the complete production files, source code, visual animations, mathematical proofs, and subtitle data for the M3 Internal Assessment project: **"Derivative and Rate of Change: From Secant to Tangent"**.

The animation visually demonstrates how the average rate of change between two points on a curve approaches the instantaneous rate of change as the distance between them approaches zero.

### Key Video Specifications
- **Duration:** ~4 minutes 45 seconds (Target: 5 minutes, strict max: 7 minutes)
- **Resolution:** 1920 × 1080 (1080p Full HD)
- **Aspect Ratio:** 16:9 Landscape
- **Frame Rate:** 30 FPS
- **Format:** MP4 (H.264 video codec, silent for voiceover addition)
- **Subtitles:** Both permanently burned into the video and provided as an editable `.srt` file.

---

## 📁 Repository Structure

```
M3_Derivative_Animation/
│
├── output/
│   ├── M3_Derivative_Animation.mp4       # Final rendered 1080p 30fps MP4 video
│   └── subtitles.srt                     # Synchronized subtitle track (SRT format)
│
├── scripts/
│   ├── main.py                           # Master production script (renders complete 6-scene video)
│   ├── scene_1_hook.py                   # Scene 1: Real-world context (car on road, instantaneous speed)
│   ├── scene_2_introduction.py           # Scene 2: Function f(x)=x², parabola, points A and B, secant line
│   ├── scene_3_visual_intuition.py       # Scene 3: Animated rotation of secant lines as h → 0
│   ├── scene_4_worked_example.py         # Scene 4: Complete step-by-step limit derivation of f'(2) = 4
│   ├── scene_5_interpretation.py         # Scene 5: Tangent line equation y = 4x - 4 and geometric meaning
│   └── scene_6_summary.py                # Scene 6: Three core takeaways and closing assessment credits
│
├── assets/                               # Media and asset directory
│
├── documentation/
│   ├── voiceover_script.txt              # Complete timestamped script matching subtitles word-for-word
│   ├── storyboard.md                     # Scene-by-scene storyboard and visual timeline
│   └── mathematical_verification.md      # Formal step-by-step mathematical proofs and checks
│
└── README.md                             # Project documentation and submission details
```

---

## 📐 Mathematical Framework & Verification

### 1. Function and Points
- Curve: $f(x) = x^2$
- Fixed Point $A$: $(2, f(2)) = (2, 4)$
- Moving Point $B$: $(2+h, f(2+h)) = (2+h, (2+h)^2)$

### 2. Secant Slope (Average Rate of Change)
$$\text{Slope}_{AB} = \frac{f(2+h) - f(2)}{(2+h) - 2} = \frac{(2+h)^2 - 4}{h} = \frac{4 + 4h + h^2 - 4}{h} = \frac{h(4+h)}{h} = 4 + h$$

Numerical progression demonstrated in Scene 3:
- $h = 2.0 \implies \text{Slope} = 6.0$ (point $B(4, 16)$)
- $h = 1.0 \implies \text{Slope} = 5.0$ (point $B(3, 9)$)
- $h = 0.5 \implies \text{Slope} = 4.5$ (point $B(2.5, 6.25)$)
- $h = 0.1 \implies \text{Slope} = 4.1$ (point $B(2.1, 4.41)$)
- $\lim_{h \to 0} (4+h) = 4$

### 3. Derivative via First Principles (Limit Definition)
$$f'(2) = \lim_{h \to 0} \frac{f(2+h) - f(2)}{h} = \lim_{h \to 0} \frac{(2+h)^2 - 2^2}{h} = \lim_{h \to 0} \frac{4h + h^2}{h} = \lim_{h \to 0} (4+h) = 4$$

### 4. Tangent Line Equation
Using point-slope form $y - y_1 = m(x - x_1)$ with $(x_1, y_1) = (2, 4)$ and $m = 4$:
$$y - 4 = 4(x - 2) \implies y = 4x - 4$$

---

## 🎬 Six-Scene Storyboard Summary

1. **Scene 1: Hook / Real-World Context (0:00 - 0:30)**  
   Animated automobile travelling along a road. Poses the central dilemma: how do we calculate the exact speed at one instant in time when speed is defined as change in distance over elapsed time?
2. **Scene 2: Concept Introduction (0:30 - 1:05)**  
   Introduces $f(x) = x^2$ on the coordinate plane. Defines point $A(2,4)$ and nearby point $B(2+h, (2+h)^2)$. Constructs the secant line passing through both points.
3. **Scene 3: Visual Intuition (1:05 - 2:00)**  
   Dynamically animates point $B$ sliding towards point $A$ across four decreasing values of $h$ ($2, 1, 0.5, 0.1$). Shows the secant slopes decreasing from $6 \to 5 \to 4.5 \to 4.1$, smoothly pivoting into the green tangent line of slope 4.
4. **Scene 4: Complete Worked Example (2:00 - 3:30)**  
   A clean algebraic workspace proving $f'(2) = 4$ step-by-step from the limit definition. Explains why $h$ can be legally canceled prior to evaluating the limit ($h \to 0, h \neq 0$).
5. **Scene 5: Geometric Interpretation (3:30 - 4:20)**  
   Returns to the coordinate graph. Plots the tangent line $y = 4x - 4$ in green against the cyan parabola. Connects slope 4 directly back to the vehicle's instantaneous speedometer reading.
6. **Scene 6: Summary and Credits (4:20 - 4:45)**  
   Recaps the three core principles, shows the final result box, and presents student assessment submission credentials with AI usage disclosure.

---

## 🎙️ Adding Voiceover Narration

The exported MP4 video is rendered **without voiceover or synthetic narration**, leaving a silent audio track ready for recording.

### Step-by-Step Voiceover Sync Guide:
1. Open your preferred video editing software (DaVinci Resolve, Premiere Pro, CapCut, iMovie, or Audacity).
2. Import `output/M3_Derivative_Animation.mp4`.
3. Open `documentation/voiceover_script.txt` on a second monitor or mobile device.
4. Record your narration following the indicated timestamps. The on-screen burned-in subtitles match the script word-for-word.
5. Align your audio track with the visuals, adjust levels (voice at -3dB to -6dB peak), and export your final submission.

---

## 🛠️ How to Render from Source

### Prerequisites
- Python 3.9+
- Homebrew (macOS)
- FFmpeg (`brew install ffmpeg`)
- Pango & Cairo (`brew install pango pkg-config py3cairo`)
- Manim Community Edition v0.19.0+ (`pip install manim`)

### Rendering Commands
To render the entire full-length animation in 1080p 30 FPS:
```bash
cd M3_Derivative_Animation
manim render -qh --fps 30 scripts/main.py FullAnimation
```

To render an individual scene (e.g. Scene 3):
```bash
manim render -qh --fps 30 scripts/scene_3_visual_intuition.py Scene3VisualIntuition
```

---

## 📜 Academic Integrity & AI Disclosure
**Course:** M3 – Linear Algebra and Calculus  
**Assessment:** Internal Assessment (10% Weightage)  
**Student Name:** [INSERT STUDENT NAME]  
**Student ID:** [INSERT STUDENT ID]  

*AI Disclosure:* AI tools were utilized to assist in programmatic 2D motion graphics development (Python Manim CE) and visual storyboard structuring. All underlying calculus definitions, algebraic derivations, limit theorems, coordinate transformations, and geometric principles were verified for mathematical precision.
