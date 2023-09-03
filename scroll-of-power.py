# manim scroll-of-power.py scroll_of_power; ffplay -seek_interval 1 /home/penguin/Desktop/Physics/hallway-gremlins/quadratic-pain/media/videos/scroll-of-power/1080p60/scroll_of_power.mp4 2>/dev/null >/dev/null
from manim import *


class scroll_of_power(Scene):
    def construct(self):
        # Functions
        # self.next_section(skip_animations=True)
        def show(mobject, opacity=0.8): return self.add(
            index_labels(mobject).set_opacity(opacity))

        def ct(a, b): return ReplacementTransform(a, b, path_arc=-np.pi)
        def cct(a, b): return ReplacementTransform(a, b, path_arc=np.pi)
        # Equation 1:
        dg = VGroup()
        # text = MathTex(
        #     *r"m   g   h   =   \frac{1}{2}   I   \omega   ^2".split("   "))
        text = VGroup(Tex("Equation 1:"), MathTex(
            *r"\overline{v}   =   {   d   \over   t   }".split("   "))).arrange(DOWN)
        text2 = VGroup(Tex("Equation 1:"), MathTex(
            r"\overline{v}   =   {   d   \over   t   }")).arrange(DOWN)
        dg.add(text)

        self.play(Write(text2, run_time=1))
        self.remove(text2)
        self.add(dg[0])
        self.play(Indicate(dg[0][1]), scale_factor=1.025)
        text = VGroup(Tex("Equation 1:"), MathTex(
            *r"\overline{v}   t   =   d".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 1:"), MathTex(
            *r"d   =   \overline{v}   t".split("   "))).arrange(DOWN)

        self.play(ct(text[1][3], text2[1][0]), ct(
            text[1][0:2], text2[1][2:]), ReplacementTransform(text[1][2], text2[1][1]), ReplacementTransform(text[0], text2[0]))
        text = text2
        dg[0] = text
        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 1:"), MathTex(
            *r"{   d   \over   \overline{v}   }   =   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 1:"), MathTex(
            *r"t   =   {   d   \over   \overline{v}   }".split("   "))).arrange(DOWN)
        self.play(ct(text[1][0:5], text2[1][2:]), ct(
            text[1][-1], text2[1][0]), ReplacementTransform(text[1][-2], text2[1][1]), ReplacementTransform(text[0], text2[0]))
        self.play(Indicate(text2[1]), scale_factor=1.025)
        self.play(FadeOut(text2))
        # Equation 2:
        dg = VGroup()
        # text = MathTex(
        #     *r"m   g   h   =   \frac{1}{2}   I   \omega   ^2".split("   "))
        text = VGroup(Tex("Equation 2:"), MathTex(
            *r"a   =   {   \Delta v   \over   t   }".split("   "))).arrange(DOWN)
        text2 = VGroup(Tex("Equation 2:"), MathTex(
            r"a   =   {   \Delta v   \over   t   }")).arrange(DOWN)
        dg.add(text)

        self.play(Write(text2, run_time=1))
        self.remove(text2)
        self.add(text)

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 2:"), MathTex(
            *r"a   t   =   \Delta v".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 2:"), MathTex(
            *r"\Delta v   =   a   t".split("   "))).arrange(DOWN)

        self.play(ct(text[1][3], text2[1][0]), ct(
            text[1][0:2], text2[1][2:]), ReplacementTransform(text[1][2], text2[1][1]), ReplacementTransform(text[0], text2[0]))
        text = text2
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 2:"), MathTex(
            *r"{   \Delta v   \over   a   }   =   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 2:"), MathTex(
            *r"t   =   {   \Delta v   \over   a   }".split("   "))).arrange(DOWN)
        self.play(ct(text[1][0:5], text2[1][2:]), ct(
            text[1][-1], text2[1][0]), ReplacementTransform(text[1][-2], text2[1][1]), ReplacementTransform(text[0], text2[0]))
        self.play(Indicate(text2[1]), scale_factor=1.025)

        self.play(FadeOut(text2))

        # Equation 3:
        dg = VGroup()
        # text = MathTex(
        #     *r"m   g   h   =   \frac{1}{2}   I   \omega   ^2".split("   "))
        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"v_f   =   v_i   +   a   t".split("   "))).arrange(DOWN)
        text2 = VGroup(Tex("Equation 3:"), MathTex(
            "v_f=v_i+at")).arrange(DOWN)
        dg.add(text)

        self.play(Write(text2, run_time=1))
        self.remove(text2)
        self.add(dg[0])

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        # Rotation!
        text2 = VGroup(Tex("Equation 3:"), MathTex(
            *r"v_f   -   a   t   =   v_i".split("   "))).arrange(DOWN)
        self.play(ReplacementTransform(
            text[1][0], text2[1][0]), FadeOut(text[1][3]), ct(text[1][4:], text2[1][2:4]), ReplacementTransform(text[1][1:3], text2[1][4:]), FadeIn(text2[1][1]), ReplacementTransform(text[0], text2[0]))

        self.remove(text2)

        text = text2
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 3:"), MathTex(
            *r"v_i   =   v_f   -   a   t".split("   "))).arrange(DOWN)
        self.play(cct(text[1][5], text2[1][0]), ct(
            text[1][4], text2[1][1]), ReplacementTransform(text[1][0:4], text2[1][2:]), ReplacementTransform(text[0], text2[0]))

        text = text2
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"v_i   -   v_f   =   -   a   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"v_f   -   v_i   =   a   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"{   v_f   -   v_i   \over   a   }   =   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Rotation!
        text2 = VGroup(Tex("Equation 3:"), MathTex(
            *r"t   =   {   v_f   -   v_i   \over   a   }".split("   "))).arrange(DOWN)
        self.play(ct(text[1][8], text2[1][0]),
                  ReplacementTransform(text[1][7], text2[1][1]), ReplacementTransform(text[0], text2[0]), ReplacementTransform(text[1][0:7], text2[1][2:]))

        text = text2
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"a   t   =   v_f   -   v_i".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 3:"), MathTex(
            *r"a   =   {   v_f   -   v_i   \over   t   }".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)
        self.remove(text)

        self.play(FadeOut(text))
        # Equation 4:
        dg = VGroup()
        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"d   =   v_i   t   +   \frac{1}{2}   a   t   ^   2".split("   "))).arrange(DOWN)
        text2 = VGroup(Tex("Equation 4:"), MathTex(
            r"d   =   v_i   t   +   \frac{1}{2}   a   t   ^   2")).arrange(DOWN)
        dg.add(text)

        self.play(Write(text2, run_time=1))
        self.remove(text2)
        self.add(dg[0])

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"d   =   v_i   t   +   0.5   a   t   ^   2".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"d   -   0.5   a   t   ^   2   =   v_i   t".split("   "))).arrange(DOWN)

        self.play(ct(text[1][5:], text2[1][2:7]),
                  ReplacementTransform(text[1][1:4], text2[1][7:]), FadeOut(text[1][4]), FadeIn(text2[1][1]), ReplacementTransform(text[0], text2[0]), ReplacementTransform(text[1][0], text2[1][0]))

        text = text2
        dg[0] = text

        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"{   d   -   0.5   a   t   ^   2   \over   t   }   =   v_i".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"{   d   \over   t   }   -   0.5   a   t   =   v_i".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"v_i   =   {   d   \over   t   }   -   0.5   a   t".split("   "))).arrange(DOWN)

        self.play(ct(text[1][0:9], text2[1][2:]), ct(
            text[1][-1], text2[1][0]), ct(text[0], text2[0]), ReplacementTransform(text[1][-2], text2[1][1]))

        text = text2
        dg[0] = text
        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"v_i   -   {   d   \over   t   }   =   -   0.5   a   t".split("   "))).arrange(DOWN)

        self.play(ct(text[1][2:7], text2[1][2:7]), ct(
            text[1][1], text2[1][7]), ReplacementTransform(text[1][7:], text2[1][8:]), FadeIn(text2[1][1]), ReplacementTransform(text[1][0], text2[1][0]), ReplacementTransform(text[0], text2[0]))

        text = text2
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"-   {   1   \over   0.5   }   \left(   v_i   -   {   d   \over   t   }   \right)   =   a   t".split("   "))).arrange(DOWN)
        dg[0] = text

        self.play(ct(text[1][9], text2[1][4]), ct(
            text[1][8], text2[1][0]), ReplacementTransform(text[1][0:7], text2[1][7:14]), FadeIn(text2[1][6], text2[1][14], text2[1][2], text2[1][3]), ReplacementTransform(text[1][7], text2[1][15]), ReplacementTransform(text[1][-2:], text2[1][-2:]), ReplacementTransform(text[0], text2[0]))

        text = text2
        dg[0] = text

        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"-   2   \left(   v_i   -   {   d   \over   t   }   \right)   =   a   t".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"-   {   2   \over   t   }   \left(   v_i   -   {   d   \over   t   }   \right)   =   a".split("   "))).arrange(DOWN)

        self.play(ct(text[1][-1], text2[1][4]),
                  ReplacementTransform(text[1][2:-1], text2[1][6:]), ReplacementTransform(text[1][1], text2[1][2]), ReplacementTransform(text[0], text2[0]), FadeIn(text2[1][3]), ReplacementTransform(text[1][0], text2[1][0]))

        text = text2
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"a   =   -   {   2   \over   t   }   \left(   v_i   -   {   d   \over   t   }   \right)".split("   "))).arrange(DOWN)

        self.play(ct(text[1][-1], text2[1][0]), ct(text[1][-2], text2[1][1]),
                  ReplacementTransform(text[1][:-2], text2[1][2:]), ReplacementTransform(text[0], text2[0]))
        text = text2
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = Tex("Let's reset for a second.").next_to(dg[0], DOWN)
        dg.add(text)
        self.play(FadeIn(text))

        dg -= text
        self.play(FadeOut(text))

        text = VGroup(Tex("Equation 4:"), MathTex(
            *r"d   =   v_i   t   +   \frac{1}{2}   a   t   ^   2".split("   "))).arrange(DOWN)

        self.play(ReplacementTransform(dg[0], text))
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"0   =   v_i   t   +   \frac{1}{2}   a   t   ^   2   -   d".split("   "))).arrange(DOWN)

        self.play(ReplacementTransform(
            text[1][1:], text2[1][1:-2]), FadeIn(text2[1][0], text2[1][-2]), cct(text[1][0], text2[1][-1]), ReplacementTransform(text[0], text2[0]))
        text = text2
        dg[0] = text

        text2 = VGroup(Tex("Equation 4:"), MathTex(
            *r"0   =   \frac{1}{2}   a   t   ^   2   +   v_i   t   -   d".split("   "))).arrange(DOWN)

        self.play(ReplacementTransform(text[1][0:2], text2[1][0:2]), ct(
            text[1][5:10], text2[1][2:7]), ct(text[1][2:4], text2[1][8:10]), ReplacementTransform(text[1][4], text2[1][7]), ReplacementTransform(text[0], text2[0]), ReplacementTransform(text[1][-2:], text2[1][-2:]))
        text = text2
        dg[0] = text

        quad = MathTex(
            *"t   =   {   -   B   \pm   \sqrt   {   B   ^   2   -   4   A   C   }   \over   2   A   }".split("   ")).next_to(text, DOWN)
        self.play(FadeIn(quad))
        dg.add(quad)

        # show(dg[0][1])
        # show(dg[1][0])

        self.play(dg[1][13].animate.set_color(RED),
                  dg[1][18].animate.set_color(RED), dg[0][1][2:4].animate.set_color(RED))

        quad = MathTex(
            *r"t   =   {   -   B   \pm   \sqrt   {   B   ^   2   -   4   \left(   \frac{1}{2}   a   \right)   C   }   \over   2   \left(   \frac{1}{2}   a   \right)   }".split("   ")).next_to(text, DOWN)

        quad[13:17].set_color(RED)
        quad[21:].set_color(RED)

        self.play(TransformMatchingTex(dg[1], quad))
        dg[1] = quad

        self.play(dg[0][1][8].animate.set_color(GREEN), dg[1][4].animate.set_color(
            GREEN), dg[1][8].animate.set_color(GREEN))

        # Switcherooni
        quad = MathTex(
            *r"t   =   {   -   B   \pm   \sqrt   {   B   ^   2   -   4   \left(\frac{1}{2}a\right)   C   }   \over   2   \left(\frac{1}{2}a\right)   }".split("   ")).next_to(text, DOWN)
        quad[13].set_color(RED)
        quad[18].set_color(RED)
        quad[4].set_color(GREEN)
        quad[8].set_color(GREEN)
        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t   =   {   -   \left(   v_i   \right)   \pm   \sqrt   {   \left(   v_i   \right)   ^   2   -   4   \left(\frac{1}{2}a\right)   C   }   \over   2   \left(\frac{1}{2}a\right)   }".split("   ")).next_to(text, DOWN)
        quad[17].set_color(RED)
        quad[22].set_color(RED)
        quad[4:7].set_color(GREEN)
        quad[10:13].set_color(GREEN)

        self.play(TransformMatchingTex(dg[1], quad))
        dg[1] = quad

        self.play(dg[0][1][10:].animate.set_color(
            BLUE), dg[1][18].animate.set_color(BLUE))

        # Switcherooni
        quad = MathTex(
            *r"t   =   {   -   \left(v_i \right)   \pm   \sqrt   {   \left(v_i \right)   ^   2   - 4   \left(\frac{1}{2}a\right)   C   }   \over   2   \left(\frac{1}{2}a\right)   }".split("   ")).next_to(text, DOWN)
        quad[12].set_color(RED)
        quad[17].set_color(RED)
        quad[4].set_color(GREEN)
        quad[8].set_color(GREEN)
        quad[13].set_color(BLUE)

        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t   =   {   -   \left(v_i \right)   \pm   \sqrt   {   \left(v_i \right)   ^   2   - 4   \left(\frac{1}{2}a\right)   \left(   -d   \right)   }   \over   2   \left(\frac{1}{2}a\right)   }".split("   ")).next_to(text, DOWN)
        quad[12].set_color(RED)
        quad[19].set_color(RED)
        quad[4].set_color(GREEN)
        quad[8].set_color(GREEN)
        quad[13:17].set_color(BLUE)

        self.play(TransformMatchingTex(dg[1], quad))
        dg[1] = quad

        self.play(dg.animate.set_color(WHITE))

        # Switcherooni
        quad = MathTex(
            *r"t   =   {   -   \left(v_i \right)   \pm   \sqrt   {   \left(v_i \right)   ^   2   - 4   \left(\frac{1}{2}a\right)   \left(-d\right)   }   \over   2   \left(   \frac{1}{2}   a   \right)   }".split("   ")).next_to(text, DOWN)
        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t   =   {   -   \left(v_i \right)   \pm   \sqrt   {   \left(v_i \right)   ^   2   - 4   \left(\frac{1}{2}a\right)   \left(-d\right)   }   \over   a   }".split("   ")).next_to(text, DOWN)
        self.play(ReplacementTransform(
            dg[1][:-6], quad[:-2]), FadeOut(dg[1][-6:-3], dg[1][-2]), ReplacementTransform(dg[1][-3], quad[-2]))

        dg[1] = quad

        # Switcherooni
        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2   -   4   \left(\frac{1}{2}a\right)   \left(   -   d   \right)}   \over a}".split("   ")).next_to(text, DOWN)

        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2   +   4   \left(\frac{1}{2}a\right)   \left(   d   \right)}   \over a}".split("   ")).next_to(text, DOWN)
        self.play(TransformMatchingTex(dg[1], quad))
        dg[1] = quad

        # Switcherooni
        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2+   4   \left(   \frac{1}{2}   a   \right)   \left(d\right)}\over a}".split("   ")).next_to(text, DOWN)

        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2+   2   \left(   a   \right)   \left(d\right)}\over a}".split("   ")).next_to(text, DOWN)
        self.play(TransformMatchingTex(dg[1], quad))
        dg[1] = quad

        # Switcherooni
        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2+   2   \left(   a   \right)   \left(   d   \right)   }\over a}".split("   ")).next_to(text, DOWN)

        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add((dg[1]))

        quad = MathTex(
            *r"t = {-\left(v_i \right) \pm \sqrt{\left(v_i \right)^2+   2   a   d   }\over a}".split("   ")).next_to(text, DOWN)
        self.play(ReplacementTransform(dg[1][0:2], quad[0:2]), FadeOut(
            dg[1][2], dg[1][4:6], dg[1][7]), ReplacementTransform(dg[1][3], quad[2]), ReplacementTransform(dg[1][6], quad[3]), ReplacementTransform(dg[1][-1], quad[-1]))
        dg[1] = quad

        # Switcherooni
        quad = MathTex(
            *r"t   =   {   -   \left(   v_i   \right)   \pm   \sqrt{   \left(   v   _   i   \right)   ^   2   +   2ad   }   \over   a   }".split("   ")).next_to(text, DOWN)
        # WHY ON EARTH IS self.remove() NOT WORKING
        self.play(FadeOut(dg[1]), run_time=0)
        dg[1] = quad
        self.add(dg[1])

        quad = MathTex(
            *r"t   =   {   -   v_i   \pm   \sqrt{   v   _   i   ^   2   +   2ad   }   \over   a   }".split("   ")).next_to(text, DOWN)
        self.play(FadeOut(dg[1][4], dg[1][6], dg[1][9], dg[1][13]),
                  ReplacementTransform(dg[1][14:16], quad[8:10]), ReplacementTransform(dg[1][10], quad[7]), ReplacementTransform(
                      dg[1][11:13], quad[10:12]), ReplacementTransform(dg[1][16:], quad[12:]), ReplacementTransform(dg[1][0:4], quad[0:4]), ReplacementTransform(dg[1][7], quad[5]), ReplacementTransform(dg[1][5], quad[4]), FadeTransform(dg[1][8], quad[6]), stretch=True)
        dg[1] = quad

        self.play(Indicate(dg[1]), scale_factor=1.025)

        self.play(FadeOut(dg))

        # Equation 5
        dg = VGroup()
        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_f   ^2   =   v_i^2+2ad".split("   "))).arrange(DOWN)
        dg.add(text)

        text2 = VGroup(Tex("Equation 5:"), MathTex(
            r"v_f^2=v_i^2+2ad")).arrange(DOWN)

        self.play(Write(text2))
        self.remove(text2)
        self.add(dg[0])

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_f   =   \sqrt{   v_i^2+2ad   }".split("   "))).arrange(DOWN)

        self.play(ReplacementTransform(
            dg[0][1][-1], text[1][-2]), FadeIn(text[1][2]), ReplacementTransform(dg[0][0], text[0]), ReplacementTransform(dg[0][1][2], text[1][1]), FadeOut(dg[0][1][0][1]), ReplacementTransform(dg[0][1][0][0], text[1][0][0]), ReplacementTransform(dg[0][1][1], text[1][0][1]))

        dg[0] = text
        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_f   ^2   =   v_i^2+2ad".split("   "))).arrange(DOWN)

        self.play(FadeOut(dg[0][1][2]), ReplacementTransform(
            dg[0][1][3], text[1][3]), ReplacementTransform(dg[0][0], text[0]), ReplacementTransform(dg[0][1][1], text[1][2]), ReplacementTransform(dg[0][1][0][0], text[1][0][0]), ReplacementTransform(dg[0][1][0][1], text[1][1]), FadeIn(text[1][0][1]))

        dg[0] = text

        # Switcherooni
        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v   _   f   ^   2   =   v   _   i   ^   2   +   2   a   d".split("   "))).arrange(DOWN)

        self.play(FadeOut(dg[0]), run_time=0)
        dg[0] = text
        self.add(dg[0])

        # show(text[1])

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v   _   f   ^   2   -   v   _   i   ^   2   =   2   a   d".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"{   v   _   f   ^   2   -   v   _   i   ^   2   \over   2   a   }   =   d".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"d   =   {   v   _   f   ^   2   -   v   _   i   ^   2   \over   2   a   }".split("   "))).arrange(DOWN)
        self.play(ct(dg[0][1][17], text[1][0]),
                  ct(dg[0][1][0:16], text[1][2:]), ReplacementTransform(dg[0][1][-2], text[1][1]), ReplacementTransform(dg[0][0], text[0]))
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        # Switcherooni
        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"d   =   {   v_f^2-v_i^2   \over   2   a   }".split("   "))).arrange(DOWN)
        self.play(FadeOut(dg[0]), run_time=0)
        dg[0] = text
        self.add(dg[0])

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"2   a   d   =   v_f^2-v_i^2".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"a   =   {   v_f^2-v_i^2   \over   2   d   }".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"2   a   d   =   v_f^2-v_i^2".split("   "))).arrange(DOWN)
        self.play(TransformMatchingTex(dg[0], text))
        dg[0] = text

        # Switcherooni
        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"2ad   =   v_f^2-   v_i^2".split("   "))).arrange(DOWN)
        self.play(FadeOut(dg[0]), run_time=0)
        dg[0] = text
        self.add(dg[0])

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_i^2   =   v_f^2-   2ad".split("   "))).arrange(DOWN)

        self.play(ct(dg[0][1][-1], text[1][0]), ct(dg[0][1][0], text[1]
                  [-1]), ReplacementTransform(dg[0][1][1], text[1][1]), ReplacementTransform(dg[0][0], text[0]), ReplacementTransform(dg[0][1][2], text[1][2]))

        # Switcherooni
        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_i   ^2   =   v_f^2-2ad".split("   "))).arrange(DOWN)
        self.play(FadeOut(dg[0]), run_time=0)
        dg[0] = text

        self.add(dg[0])

        text = VGroup(Tex("Equation 5:"), MathTex(
            *r"v_i   =   \sqrt   {   v_f^2-2ad   }".split("   "))).arrange(DOWN)
        self.play(ReplacementTransform(dg[0][0], text[0]), ReplacementTransform(
            dg[0][1][0][0], text[1][0][0]), ReplacementTransform(dg[0][1][1], text[1][0][1]), FadeOut(dg[0][1][0][1]), ReplacementTransform(dg[0][1][2], text[1][1]), ReplacementTransform(dg[0][1][3], text[1][4]), FadeIn(text[1][2]))
        dg[0] = text

        self.play(Indicate(dg[0][1]), scale_factor=1.025)

        self.play(FadeOut(dg))
