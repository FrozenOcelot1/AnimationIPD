from manim import *
import math
import numpy as np

class CreateAnimation(Scene):
    def construct(self):
        
        tex = Tex('Teorema de Pitagoras', font_size=34)
        tex.move_to(3*UP)

        pythag = MathTex("a^2 + b^2 = c^2")
        pythag.move_to(3*RIGHT + 1.3*UP)
        pythag.scale(0.85)
        pythag[0][0].set_color(DARK_BLUE)
        pythag[0][3].set_color(GREEN)
        pythag[0][6].set_color(RED)

        pi = MathTex(r"\pi", font_size=96)
        square = Square(4)
        circle = Circle(2.25, WHITE)

        colorList = [RED, GREEN, DARK_BLUE, YELLOW]

        # Introduction

        START_1 = (-1.5,-1.5,0)
        END_1 =   (-1.5,1.5,0)

        START_2 = (-1.5,1.5,0)
        END_2 =   (1.5,-1.5,0)

        START_3 = (1.5,-1.5,0)
        END_3 =   (-1.5025,-1.5,0)

        START_4 = (-1.2,-1.5,0)
        END_4 =   (-1.2,-1.2,0)

        START_5 = (-1.2,-1.2,0)
        END_5 =   (-1.5025,-1.2,0)

        # Proof

        START_6 = (-1,2,0)
        END_6 = (-1,-2,0)
        
        START_7 = (1,2,0)
        END_7 = (-1,-2,0)

        dot1 = Dot((2,2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot2 = Dot((1,2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot3 = Dot((0,2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot4 = Dot((-1,2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot5 = Dot((-2,2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot6 = Dot((2,-2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot7 = Dot((1,-2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot8 = Dot((0,-2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot9 = Dot((-1,-2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)
        dot10 = Dot((-2,-2,0), DEFAULT_SMALL_DOT_RADIUS, color=DARK_BLUE)

        # Introduction

        line_1 = Line(START_1,END_1)
        line_2 = Line(START_2,END_2)
        line_3 = Line(START_3,END_3)
        line_4 = Line(START_4,END_4)
        line_5 = Line(START_5,END_5)   

        # Proof

        line_6 = Line(START_6,END_6)
        line_7 = Line(START_7,END_7)     

        b1 = Brace(line_7, direction=line_7.copy().rotate(PI / 2).get_unit_vector())

        x = Tex("a")
        x.set_color_by_tex("a", BLUE)
        x.next_to(line_1, LEFT)
        x.scale(0.75)

        y = Tex("b")
        y.set_color_by_tex("b", GREEN)
        y.next_to(line_3, DOWN)
        y.scale(0.75)

        z = Tex("c")
        z.set_color_by_tex("c", RED)
        z.move_to(0.4*RIGHT)
        z.scale(0.75)

        a = MathTex("8")
        a[0][0].set_color(BLUE)
        a.next_to(square, LEFT)
        a.scale(0.75)

        b = MathTex("4")
        b[0][0].set_color(BLUE)
        b.move_to(2.3*UP)
        b.scale(0.75)

        c = MathTex("9")
        c[0][0].set_color(GREEN)
        c.move_to(RIGHT * 0.6)
        c.scale(0.75)

        h = MathTex(r"4\sqrt{5}")
        h[0][0:4].set_color(GREEN)
        h.move_to(RIGHT * 0.6)
        h.scale(0.75)

        area = MathTex(r"\pi  \cdot (2\sqrt5)^2 = \pi \cdot 20")
        # area[0][0:9].set_color(np.random.choice(colorList))
        area.next_to(dot1, RIGHT*2.5)
        area.scale(0.75)

        equation1 = MathTex(r"\pi \approx \frac{8^2}{2} = \frac{64}{20} = 3,2")
        equation1.next_to(area, DOWN)
        equation1.scale(0.75)

        equation2 = MathTex(r"\pi \approx \frac{8^2}{\frac{9}{2}^2} = \frac{16^2}{9^2} = 3,1604")
        equation2.next_to(dot1, RIGHT)
        equation2.scale(0.75)

        self.play(Write(tex))
        self.wait(1.5)

        self.play(Create(line_1))
        self.play(Create(line_2))
        self.play(Create(line_3))
        self.wait(1.5)
        self.play(Create(line_4))
        self.play(Create(line_5))


        self.play(Write(x))
        self.play(Write(y))
        self.play(Write(z))
        self.wait(1)

        self.play(Write(pythag), run_time = 1.5)

        self.play(ReplacementTransform(x.copy(), pythag[0][0]))
        self.play(ReplacementTransform(y.copy(), pythag[0][3]))
        self.play(ReplacementTransform(z.copy(), pythag[0][6]))
        self.wait(2)

        self.play(FadeOut(line_1), FadeOut(line_2),  FadeOut(line_3), FadeOut(line_4), 
        FadeOut(line_5), FadeOut(x), FadeOut(y), FadeOut(z), FadeOut(tex),FadeOut(pythag)) 

        self.play(Write(pi), run_time=1)
        self.play(FadeOut(pi))

        self.play(Create(square))
        self.play(Write(a))
        self.play(Create(dot1), Create(dot2), Create(dot3), Create(dot4), Create(dot5),
        Create(dot6), Create(dot7), Create(dot8), Create(dot9), Create(dot10), run_time=1)
        self.wait(1)
        self.play(Create(circle))
        self.wait(1.5)
        self.play(Create(line_6))
        self.play(Create(line_7))

        y = Tex('{\it B}')
        y.next_to(dot4, UP)

        z = Tex('{\it C}')
        z.next_to(dot2, UP)

        x = Tex('{\it A}')
        x.next_to(dot9, DOWN)

        self.play(Write(x))
        self.play(Write(y))
        self.play(Write(z))

        self.play(a.animate.shift(RIGHT * 1), run_time=1)
        self.play(Write(b))
        self.wait(1)
        self.play(Write(h))

        self.wait(1)
        self.play(AddTextWordByWord(area, run_time=1))
        self.wait(1)
        self.play(square.animate.set_fill(RED, opacity=0.3), run_time=1)
        self.play(square.animate.set_fill(BLACK))
        self.play(AddTextWordByWord(equation1, run_time=1))
        self.wait(1)
        self.play(FadeOut(area), FadeOut(equation1))
        self.wait(1)
        self.play(FadeOut(h))
        self.play(Create(b1))
        self.wait(1)
        self.play(FadeOut(b1))

        h = MathTex(r"4\sqrt{5} \approx 8,94")
        h[0][0:9].set_color(GREEN)
        h.move_to(RIGHT * 1)
        h.scale(0.75)

        self.play(Write(h))
        self.wait(1.5)
        self.play(FadeOut(h))
        self.play(Write(c))
        self.play(AddTextWordByWord(equation2, run_time=1))

        self.wait(2)



