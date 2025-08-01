# To run this code, save it as a .py file (e.g., proof.py)
# and run the following command in your terminal:
# manim -pql proof.py PythagoreanTheorem

from manim import *

class PythagoreanTheorem(Scene):
    """
    A Manim scene that visually proves the Pythagorean Theorem.

    The proof is demonstrated by rearranging four identical right-angled
    triangles within a larger square.
    1. Initially, the triangles are arranged to form a central square with area c^2.
    2. The triangles are then animated to new positions.
    3. This rearrangement reveals two new empty squares with areas a^2 and b^2,
       proving that a^2 + b^2 = c^2.
    """
    def construct(self):
        # Define side lengths for the right triangle
        a = 3.0
        b = 4.0
        
        # Colors for visual clarity
        tri_color = BLUE
        sq_a_color = RED_C
        sq_b_color = YELLOW_C
        sq_c_color = GREEN_C
        
        # Set up the initial layout and title
        self.camera.background_color = WHITE
        Mobject.set_default(color=BLACK)
        
        title = Title("Visual Proof of the Pythagorean Theorem", color=BLACK)
        equation = MathTex("a^2", "+", "b^2", "=", "c^2", color=BLACK).next_to(title, DOWN, buff=0.5)
        self.play(Write(title), Write(equation))
        self.wait(1)

        # Move the equation to the top right corner to make space for the animation
        self.play(equation.animate.to_corner(UR))
        
        # --- Arrangement 1: Showing the c^2 square ---

        # Define the vertices for the four triangles and the central c^2 square
        # These are arranged within a larger square of side length (a+b)
        
        # Vertices of the inner c^2 square
        p1 = np.array([a, 0, 0])
        p2 = np.array([a + b, a, 0])
        p3 = np.array([b, a + b, 0])
        p4 = np.array([0, b, 0])
        
        # Vertices of the outer (a+b) square
        c1 = np.array([0, 0, 0])
        c2 = np.array([a + b, 0, 0])
        c3 = np.array([a + b, a + b, 0])
        c4 = np.array([0, a + b, 0])

        # Create the mobjects (triangles and squares)
        T1 = Polygon(c1, p1, p4, color=tri_color, fill_opacity=0.7)
        T2 = Polygon(c2, p2, p1, color=tri_color, fill_opacity=0.7)
        T3 = Polygon(c3, p3, p2, color=tri_color, fill_opacity=0.7)
        T4 = Polygon(c4, p4, p3, color=tri_color, fill_opacity=0.7)
        sq_c = Polygon(p1, p2, p3, p4, color=sq_c_color, fill_opacity=0.7)
        
        # Add labels to the first triangle to represent sides a, b, c
        label_a = MathTex("a", color=BLACK).next_to(T1.get_edge_center(p1-c1), DOWN)
        label_b = MathTex("b", color=BLACK).next_to(T1.get_edge_center(p4-c1), LEFT)
        label_c = MathTex("c", color=BLACK).move_to(T1.get_hypotenuse()).shift(UL*0.2)

        # Group all shapes for animation and positioning
        arrangement1 = VGroup(T1, T2, T3, T4, sq_c, label_a, label_b, label_c).center()
        
        self.play(Create(arrangement1))
        
        # Add the area label for the c^2 square
        c_sq_label = MathTex("c^2", color=BLACK).move_to(sq_c.get_center())
        self.play(Write(c_sq_label))
        self.wait(2)
        
        # --- Arrangement 2: Rearranging to show a^2 and b^2 ---
        
        # Define the target polygons for the rearrangement
        T1_target = Polygon(np.array([b, 0, 0]), np.array([a+b, 0, 0]), np.array([b, b, 0]), color=tri_color, fill_opacity=0.7)
        T2_target = Polygon(np.array([a+b, 0, 0]), np.array([a+b, b, 0]), np.array([b, b, 0]), color=tri_color, fill_opacity=0.7)
        T3_target = Polygon(np.array([0, b, 0]), np.array([b, b, 0]), np.array([0, a+b, 0]), color=tri_color, fill_opacity=0.7)
        T4_target = Polygon(np.array([b, b, 0]), np.array([b, a+b, 0]), np.array([0, a+b, 0]), color=tri_color, fill_opacity=0.7)

        # Center the target polygons to match the current arrangement's position
        target_group = VGroup(T1_target, T2_target, T3_target, T4_target).move_to(arrangement1.get_center())

        # Animate the transformation
        self.play(
            FadeOut(label_a, label_b, label_c),
            Transform(T1, T1_target),
            Transform(T2, T2_target),
            Transform(T3, T3_target),
            Transform(T4, T4_target),
            FadeOut(sq_c),
            FadeOut(c_sq_label)
        )
        self.wait(1)

        # Create the new squares a^2 and b^2 in the empty spaces
        sq_a = Square(side_length=a, color=sq_a_color, fill_opacity=0.7)
        sq_b = Square(side_length=b, color=sq_b_color, fill_opacity=0.7)
        
        # Position the new squares correctly within the rearranged figure
        squares_group = VGroup(sq_a, sq_b).center().move_to(arrangement1.get_center())
        sq_a.align_to(T4_target, DOWN).align_to(T1_target, RIGHT)
        sq_b.align_to(T1_target, UP).align_to(T4_target, LEFT)

        # Add area labels for a^2 and b^2
        a_sq_label = MathTex("a^2", color=BLACK).move_to(sq_a.get_center())
        b_sq_label = MathTex("b^2", color=BLACK).move_to(sq_b.get_center())
        
        # Animate the appearance of the new squares and their labels
        self.play(
            Create(sq_a),
            Create(sq_b),
            Write(a_sq_label),
            Write(b_sq_label)
        )
        self.wait(2)
        
        # --- Conclusion ---
        
        # Highlight the final components matching the equation
        final_group = VGroup(sq_a, sq_b, T1, T2, T3, T4, a_sq_label, b_sq_label)
        
        # Create a rectangle to highlight the 'a^2' part of the equation
        rect_a = SurroundingRectangle(equation[0], buff=0.1)
        # Create a rectangle to highlight the 'b^2' part of the equation
        rect_b = SurroundingRectangle(equation[2], buff=0.1)
        # Create a rectangle to highlight the 'c^2' part of the equation
        rect_c = SurroundingRectangle(equation[4], buff=0.1)

        # Relate the visual proof back to the initial equation
        self.play(
            FadeToColor(a_sq_label, sq_a_color),
            FadeToColor(sq_a, sq_a_color),
            Create(rect_a, run_time=1.5)
        )
        self.play(
            FadeToColor(b_sq_label, sq_b_color),
            FadeToColor(sq_b, sq_b_color),
            Create(rect_b, run_time=1.5)
        )
        self.wait(1)
        
        # Flash the c^2 part of the equation, referencing the initial state
        self.play(Indicate(rect_c, color=sq_c_color, scale_factor=1.2))
        self.wait(0.5)

        # Highlight the entire equation to conclude the proof
        final_rect = SurroundingRectangle(equation, buff=0.2)
        self.play(
            FadeOut(rect_a, rect_b),
            Create(final_rect)
        )
        self.wait(3)
        self.play(FadeOut(final_rect, final_group, title, equation))
        self.wait(1)