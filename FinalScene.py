from manim import *


class Tutorial(Scene):
    def construct(self):
        text1 = Text("Final Scene...")
        self.play(Write(text1,run_time=2))
        self.play(Unwrite(text1,run_time=2))

        dot1 = Dot([6,.5,0]) # vertices of our triangle
        dot2 = Dot([3,2.5,0])
        dot3 = Dot([5,-2.5,0])
        
        #make the angles
        angle_gamma = Angle(Line(dot2,dot1), Line(dot3, dot1),radius=.325,quadrant=(-1,-1)) # Angle gamma
        gamma = MathTex("\\gamma").next_to(dot1, LEFT*1.5+DOWN/15) # Positioning gamma
        angle_alpha = Angle(Line(dot3,dot2), Line(dot1,dot2),radius=.7,quadrant=(-1,-1)) # Angle alpha
        alpha= MathTex("\\alpha").next_to(dot2, RIGHT*2+DOWN*2.5).scale(.9) # Positioning alpha
        angle_beta = Angle(Line(dot1,dot3), Line(dot2,dot3),radius=.5,quadrant=(-1,-1)) # Angle beta
        beta = MathTex("\\beta").next_to(dot3, UP*2.5).scale(.9) # Positioning beta


        law_of_sines = Text("Law of Sines",color=BLUE_C).move_to([-4,3,0]) # Law Of Sines and moving to position
        law = MathTex(r"\frac{\sin \alpha }{\alpha } = \frac{\sin \beta }{\beta } =\frac{\sin \gamma }{\gamma }").move_to([-4,0,0]) # Formula in Latex

        triangle = Polygon([6,.5,0],[3,2.5,0],[5,-2.5,0]) # Creates triangle shape

        self.play(Create(dot1), Create(dot2),Create(dot3),Create(triangle)) # Animates creation of triangle

        self.play( #Animating the creation of everything at the same time
            Create(angle_gamma),
            Create(gamma),
            Create(angle_alpha),
            Create(alpha),
            Create(angle_beta),
            Create(beta),
            Write(law_of_sines),
            Write(law),run_time = 1.5)

        self.wait(4) # Allow the scene to stay on screen for 4 seconds

        self.play(*[FadeOut(mobj) for mobj in self.mobjects]) # Uncreates every object in the scene




