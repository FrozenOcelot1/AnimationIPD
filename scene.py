from manim import *
import math
import numpy as np

class CreateAnimation(Scene):
    def construct(self):
        
        tex = Tex('Teorema de Pitagoras', font_size=34)
        tex.move_to(3*UP)

        pythag = MathTex(
            "a^2 = b^2 + c^2"
        )
        pythag.move_to(3*RIGHT + 1.3*UP)
        pythag.scale(0.85)
        pythag[0][0].set_color(BLUE)
        pythag[0][3].set_color(GREEN)
        pythag[0][6].set_color(RED)

           
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


        line_1 = Line(START_1,END_1)
        line_2 = Line(START_2,END_2)
        line_3 = Line(START_3,END_3)
        line_4 = Line(START_4,END_4)
        line_5 = Line(START_5,END_5)

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

        self.play(Write(tex))
        self.wait(2)

        self.play(Create(line_1))
        self.play(Create(line_2))
        self.play(Create(line_3))
        self.wait(1.5)
        self.play(Create(line_4))
        self.play(Create(line_5))


        self.play(Write(x))
        self.play(Write(y))
        self.play(Write(z))
        self.wait(1.5)

        self.play(Write(pythag), run_time = 2)

        # self.play(ReplacementTransform(x.copy(), pythag[0]))
        # self.play(ReplacementTransform(y.copy(), pythag[3]))
        # self.play(ReplacementTransform(z.copy(), pythag[6]))
        self.wait(2)

        self.play(FadeOut(line_1), FadeOut(line_2),  FadeOut(line_3), FadeOut(line_4), 
        FadeOut(line_5), FadeOut(x), FadeOut(y), FadeOut(z), FadeOut(tex),FadeOut(pythag))

