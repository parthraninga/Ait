"""
Einstein's Theory of Relativity Explainer Video
Created using Manim (Mathematical Animation Engine)

This script creates an animated video explaining key concepts of Einstein's Theory of Relativity:
- Special Relativity
- Time Dilation
- Length Contraction
- E=mc²
- General Relativity and Spacetime Curvature
"""

from manim import *
import numpy as np

class RelativityExplainer(Scene):
    def construct(self):
        # Title Scene
        self.create_title()
        self.wait(2)
        self.clear()
        
        # Introduction to Special Relativity
        self.special_relativity_intro()
        self.wait(2)
        self.clear()
        
        # Time Dilation Animation
        self.time_dilation_demo()
        self.wait(2)
        self.clear()
        
        # Length Contraction
        self.length_contraction_demo()
        self.wait(2)
        self.clear()
        
        # E=mc² explanation
        self.energy_mass_equivalence()
        self.wait(2)
        self.clear()
        
        # General Relativity - Spacetime Curvature
        self.spacetime_curvature()
        self.wait(2)
        self.clear()
        
        # Conclusion
        self.conclusion()
        self.wait(3)

    def create_title(self):
        """Create animated title sequence"""
        title = Text("Einstein's Theory of Relativity", font_size=48, color=BLUE)
        subtitle = Text("An Animated Explanation", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Animate title appearance
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        
        # Add Einstein's portrait (represented as a circle with text)
        einstein = Circle(radius=1, color=YELLOW).shift(DOWN * 2)
        einstein_text = Text("Einstein", font_size=24).move_to(einstein.get_center())
        
        self.play(Create(einstein), Write(einstein_text))

    def special_relativity_intro(self):
        """Introduce the postulates of special relativity"""
        title = Text("Special Relativity (1905)", font_size=36, color=YELLOW)
        title.to_edge(UP)
        
        postulates = VGroup(
            Text("1. Laws of physics are the same in all inertial frames", font_size=24),
            Text("2. Speed of light is constant for all observers", font_size=24),
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(postulates[0]))
        self.wait(1)
        self.play(Write(postulates[1]))
        
        # Animate light beam
        light_beam = Arrow(LEFT * 3, RIGHT * 3, color=YELLOW, buff=0)
        light_beam.shift(DOWN * 1.5)
        light_label = Text("c = 299,792,458 m/s", font_size=20, color=YELLOW)
        light_label.next_to(light_beam, DOWN)
        
        self.play(Create(light_beam), Write(light_label))

    def time_dilation_demo(self):
        """Demonstrate time dilation with moving clocks"""
        title = Text("Time Dilation", font_size=36, color=RED)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create two reference frames
        stationary_frame = Rectangle(width=3, height=2, color=BLUE).shift(LEFT * 3)
        moving_frame = Rectangle(width=3, height=2, color=RED).shift(RIGHT * 3)
        
        stationary_label = Text("Stationary", font_size=16).next_to(stationary_frame, UP)
        moving_label = Text("Moving at 0.8c", font_size=16).next_to(moving_frame, UP)
        
        self.play(Create(stationary_frame), Create(moving_frame))
        self.play(Write(stationary_label), Write(moving_label))
        
        # Add clocks
        stationary_clock = Circle(radius=0.5, color=WHITE).move_to(stationary_frame.get_center())
        moving_clock = Circle(radius=0.5, color=WHITE).move_to(moving_frame.get_center())
        
        # Clock hands
        stat_hand = Line(ORIGIN, UP * 0.3, color=WHITE).move_to(stationary_clock.get_center())
        mov_hand = Line(ORIGIN, UP * 0.3, color=WHITE).move_to(moving_clock.get_center())
        
        self.play(Create(stationary_clock), Create(moving_clock))
        self.play(Create(stat_hand), Create(mov_hand))
        
        # Animate time dilation - stationary clock runs faster
        for i in range(4):
            self.play(
                Rotate(stat_hand, PI/2, about_point=stationary_clock.get_center()),
                Rotate(mov_hand, PI/4, about_point=moving_clock.get_center()),
                run_time=0.5
            )
        
        # Add time dilation formula
        formula = MathTex(r"\Delta t' = \gamma \Delta t", font_size=32)
        gamma_formula = MathTex(r"\gamma = \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}", font_size=24)
        gamma_formula.next_to(formula, DOWN)
        
        formula.shift(DOWN * 2)
        gamma_formula.shift(DOWN * 2)
        
        self.play(Write(formula))
        self.play(Write(gamma_formula))

    def length_contraction_demo(self):
        """Demonstrate length contraction"""
        title = Text("Length Contraction", font_size=36, color=GREEN)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Show a ruler at rest
        rest_ruler = Rectangle(width=4, height=0.3, color=BLUE)
        rest_ruler.shift(UP * 1)
        rest_label = Text("Ruler at rest: L₀", font_size=20).next_to(rest_ruler, UP)
        
        self.play(Create(rest_ruler), Write(rest_label))
        
        # Show the same ruler moving
        moving_ruler = Rectangle(width=2.4, height=0.3, color=RED)  # Contracted by factor of 0.6
        moving_ruler.shift(DOWN * 1)
        moving_label = Text("Same ruler moving: L = L₀/γ", font_size=20).next_to(moving_ruler, DOWN)
        
        # Add motion lines
        motion_lines = VGroup(*[
            Line(LEFT * 0.3, RIGHT * 0.3, color=YELLOW).shift(RIGHT * i * 0.5 + DOWN * 1)
            for i in range(-3, 4)
        ])
        
        self.play(Create(moving_ruler), Write(moving_label))
        self.play(Create(motion_lines))
        
        # Length contraction formula
        formula = MathTex(r"L = \frac{L_0}{\gamma} = L_0\sqrt{1-\frac{v^2}{c^2}}", font_size=28)
        formula.shift(DOWN * 2.5)
        
        self.play(Write(formula))

    def energy_mass_equivalence(self):
        """Explain E=mc²"""
        title = Text("Mass-Energy Equivalence", font_size=36, color=PURPLE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # The famous equation
        equation = MathTex("E = mc^2", font_size=72, color=GOLD)
        equation.move_to(ORIGIN)
        
        self.play(Write(equation))
        self.wait(1)
        
        # Explanation text
        explanation = VGroup(
            Text("E = Energy", font_size=24),
            Text("m = Mass", font_size=24),
            Text("c = Speed of light", font_size=24),
            Text("Even tiny mass contains enormous energy!", font_size=20, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(DOWN * 2)
        
        for line in explanation:
            self.play(Write(line))
            self.wait(0.5)
        
        # Visual representation - small mass, big energy
        mass_circle = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(LEFT * 2 + UP * 0.5)
        mass_label = Text("m", font_size=16).move_to(mass_circle.get_center())
        
        energy_explosion = Circle(radius=1.5, color=YELLOW, fill_opacity=0.3).shift(RIGHT * 2 + UP * 0.5)
        energy_label = Text("E = mc²", font_size=20, color=YELLOW).move_to(energy_explosion.get_center())
        
        arrow = Arrow(mass_circle.get_right(), energy_explosion.get_left(), color=RED)
        
        self.play(Create(mass_circle), Write(mass_label))
        self.play(Create(arrow))
        self.play(Create(energy_explosion), Write(energy_label))

    def spacetime_curvature(self):
        """Demonstrate general relativity and spacetime curvature"""
        title = Text("General Relativity: Spacetime Curvature", font_size=32, color=ORANGE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create a grid representing spacetime
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1}
        )
        
        self.play(Create(grid))
        
        # Add a massive object (sun)
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        sun_label = Text("Sun", font_size=16, color=BLACK).move_to(sun.get_center())
        
        self.play(Create(sun), Write(sun_label))
        
        # Show how spacetime curves around the mass
        # Create curved grid lines around the sun
        def curve_function(x, y):
            r = np.sqrt(x**2 + y**2)
            if r < 0.1:  # Avoid division by zero
                r = 0.1
            factor = 1 + 0.5 / r  # Simplified curvature
            return [x, y * factor]
        
        # Animate the curvature
        curved_grid = grid.copy()
        self.play(Transform(grid, curved_grid))
        
        # Add a planet following curved path
        planet = Circle(radius=0.1, color=BLUE, fill_opacity=1).shift(RIGHT * 2)
        planet_path = ParametricFunction(
            lambda t: np.array([2 * np.cos(t), 1 * np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=GREEN
        )
        
        self.play(Create(planet_path))
        self.play(Create(planet))
        self.play(MoveAlongPath(planet, planet_path), run_time=3)
        
        # Einstein's field equation
        field_equation = MathTex(r"G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}", font_size=24)
        field_equation.to_corner(DR)
        field_label = Text("Einstein's Field Equation", font_size=16).next_to(field_equation, UP)
        
        self.play(Write(field_label), Write(field_equation))

    def conclusion(self):
        """Conclusion with key takeaways"""
        title = Text("Key Takeaways", font_size=36, color=GREEN)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        takeaways = VGroup(
            Text("• Time and space are relative to the observer", font_size=24),
            Text("• Nothing can travel faster than light", font_size=24),
            Text("• Mass and energy are equivalent (E=mc²)", font_size=24),
            Text("• Gravity is the curvature of spacetime", font_size=24),
            Text("• These effects become significant at high speeds", font_size=24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        takeaways.shift(DOWN * 0.5)
        
        for takeaway in takeaways:
            self.play(Write(takeaway))
            self.wait(0.5)
        
        # Final message
        final_msg = Text("Einstein revolutionized our understanding of the universe!", 
                        font_size=28, color=GOLD)
        final_msg.shift(DOWN * 2.5)
        
        self.play(Write(final_msg))


# Additional scene for interactive elements
class RelativityCalculator(Scene):
    def construct(self):
        """Interactive calculator for relativistic effects"""
        title = Text("Relativistic Effects Calculator", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create input fields (simulated)
        velocity_input = Rectangle(width=3, height=0.5, color=WHITE)
        velocity_label = Text("Velocity (fraction of c):", font_size=16).next_to(velocity_input, LEFT)
        velocity_value = Text("0.8", font_size=16, color=YELLOW).move_to(velocity_input.get_center())
        
        velocity_group = VGroup(velocity_label, velocity_input, velocity_value)
        velocity_group.shift(UP * 1)
        
        self.play(Create(velocity_input), Write(velocity_label), Write(velocity_value))
        
        # Calculate and display results
        v = 0.8  # 80% speed of light
        gamma = 1 / np.sqrt(1 - v**2)
        
        results = VGroup(
            Text(f"Lorentz Factor (γ): {gamma:.2f}", font_size=20),
            Text(f"Time Dilation: Time runs {gamma:.2f}x slower", font_size=20),
            Text(f"Length Contraction: Length is {1/gamma:.2f}x shorter", font_size=20),
        ).arrange(DOWN, buff=0.3)
        
        results.shift(DOWN * 1)
        
        for result in results:
            self.play(Write(result))
            self.wait(0.5)


if __name__ == "__main__":
    # To render the video, you would run:
    # manim -pql relativity_explainer.py RelativityExplainer
    # manim -pql relativity_explainer.py RelativityCalculator
    pass
