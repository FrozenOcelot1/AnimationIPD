from manim import *

class CreateAnimation(Scene):
    def construct(self):
        scale=0.5
        shiftx=-1
        shifty=1.5
        # Utility function for coordinate transformation
        def xy(a,b):
            return [a*scale+shiftx,b*scale+shifty,0]
         # Draw equation
        equation = MathTex(
            "a^2 = b^2 + c^2", color=YELLOW, font_size=96
        )
        equation2 = MathTex (
            "a^2 = b^2 + c^2", color=YELLOW, font_size=50
        )
        self.add(equation)
        self.wait(0.5)
        #self.play(FadeOut(equation))
        triangle = Polygon(xy(-3,-2),xy(3,-2),xy(-3,2),fill_color=RED, fill_opacity=0.9, color=WHITE)
        square1 = Square(2).set_fill(BLUE, opacity=0.6)
        square2 = Square(3).set_fill(BLUE, opacity=0.6)
        square1.next_to(triangle, LEFT)
        square2.next_to(triangle, DOWN)
        hypotenuse = Square(3.6).set_fill(BLUE, opacity=0.6)
        self.play(Transform(equation,equation2))
        self.play(equation.animate.shift(DOWN))
        self.wait(0.5)
        self.play(DrawBorderThenFill(triangle), run_time=0.75)
        self.play(FadeOut(equation))
        self.play(triangle.animate.shift(DOWN * 1), run_time=0.9)
        self.play(Create(square1))
        self.play(Create(square2))
        self.wait(0.5)
        self.play(FadeOut(square1))
        self.play(FadeOut(square2))
        #self.play(triangle.animate.shift(DOWN * 1), run_time=0.9)
        self.play(Create(hypotenuse))
        #self.remove(triangle)
        self.wait(3)

