"""
Enhanced Relativity Explainer with Narration and Advanced Features

This script creates a more comprehensive explainer video with:
- Narrator text overlays
- Interactive demonstrations
- Real-world examples
- Advanced animations
"""

from manim import *
import numpy as np

class EnhancedRelativityExplainer(Scene):
    """Enhanced version with narration and more detailed explanations"""
    
    def construct(self):
        self.camera.background_color = "#001122"  # Dark space-like background
        
        # Complete video sequence
        self.opening_sequence()
        self.wait(2)
        self.clear()
        
        self.historical_context()
        self.wait(2)
        self.clear()
        
        self.special_relativity_detailed()
        self.wait(2)
        self.clear()
        
        self.twin_paradox()
        self.wait(2)
        self.clear()
        
        self.relativistic_velocity_addition()
        self.wait(2)
        self.clear()
        
        self.general_relativity_detailed()
        self.wait(2)
        self.clear()
        
        self.real_world_applications()
        self.wait(2)
        self.clear()
        
        self.modern_implications()
        self.wait(3)

    def opening_sequence(self):
        """Enhanced opening with space background and Einstein quote"""
        # Title with glowing effect
        main_title = Text("Einstein's Theory of Relativity", 
                         font_size=48, 
                         gradient=(BLUE, PURPLE))
        
        subtitle = Text("A Journey Through Space and Time", 
                       font_size=28, 
                       color=WHITE)
        subtitle.next_to(main_title, DOWN, buff=0.5)
        
        # Einstein's famous quote
        quote = Text('"Imagination is more important than knowledge"', 
                    font_size=24, 
                    color=YELLOW, 
                    slant=ITALIC)
        quote.next_to(subtitle, DOWN, buff=1)
        
        author = Text("- Albert Einstein", 
                     font_size=20, 
                     color=GRAY)
        author.next_to(quote, DOWN, buff=0.3)
        
        # Animate with stars background
        stars = self.create_starfield()
        
        self.add(stars)
        self.play(Write(main_title), run_time=2)
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(Write(quote), run_time=2)
        self.play(Write(author))
        
    def create_starfield(self):
        """Create animated starfield background"""
        stars = VGroup()
        for _ in range(50):
            star = Dot(
                point=[
                    np.random.uniform(-7, 7),
                    np.random.uniform(-4, 4),
                    0
                ],
                radius=np.random.uniform(0.01, 0.05),
                color=WHITE
            )
            stars.add(star)
        return stars

    def historical_context(self):
        """Provide historical context for Einstein's discoveries"""
        title = Text("The Year That Changed Physics: 1905", 
                    font_size=36, 
                    color=GOLD)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Timeline
        timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        timeline.shift(DOWN * 0.5)
        
        events = [
            ("1900", "Planck's quantum theory", LEFT * 4),
            ("1905", "Einstein's miracle year", ORIGIN),
            ("1915", "General Relativity", RIGHT * 4),
        ]
        
        self.play(Create(timeline))
        
        for year, event, position in events:
            marker = Dot(color=YELLOW).move_to(position + DOWN * 0.5)
            year_text = Text(year, font_size=16, color=YELLOW).next_to(marker, UP)
            event_text = Text(event, font_size=14, color=WHITE).next_to(marker, DOWN)
            
            self.play(Create(marker), Write(year_text), Write(event_text))
            self.wait(0.5)
        
        # Context text
        context = VGroup(
            Text("In 1905, a 26-year-old patent clerk", font_size=20),
            Text("published papers that revolutionized physics:", font_size=20),
            Text("• Photoelectric Effect", font_size=18, color=YELLOW),
            Text("• Brownian Motion", font_size=18, color=YELLOW),
            Text("• Special Relativity", font_size=18, color=YELLOW),
            Text("• Mass-Energy Equivalence", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        
        context.shift(DOWN * 2.5)
        
        for line in context:
            self.play(Write(line))
            self.wait(0.3)

    def special_relativity_detailed(self):
        """Detailed explanation of special relativity"""
        title = Text("Special Relativity: The Foundation", 
                    font_size=32, 
                    color=BLUE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Two postulates with visual demonstrations
        postulate1 = Text("Postulate 1: Laws of physics are identical", 
                         font_size=24, 
                         color=WHITE)
        postulate1_sub = Text("in all inertial reference frames", 
                             font_size=20, 
                             color=GRAY)
        postulate1_sub.next_to(postulate1, DOWN, buff=0.1)
        
        self.play(Write(postulate1), Write(postulate1_sub))
        
        # Demonstrate with two moving frames
        frame1 = Rectangle(width=2, height=1.5, color=BLUE).shift(LEFT * 3 + DOWN * 0.5)
        frame2 = Rectangle(width=2, height=1.5, color=RED).shift(RIGHT * 3 + DOWN * 0.5)
        
        ball1 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(frame1.get_center())
        ball2 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(frame2.get_center())
        
        self.play(Create(frame1), Create(frame2))
        self.play(Create(ball1), Create(ball2))
        
        # Both balls fall with same physics
        self.play(
            ball1.animate.shift(DOWN * 0.5),
            ball2.animate.shift(DOWN * 0.5),
            run_time=1
        )
        
        self.wait(1)
        self.clear()
        
        # Postulate 2
        title.to_edge(UP)
        self.play(Write(title))
        
        postulate2 = Text("Postulate 2: Speed of light is constant", 
                         font_size=24, 
                         color=WHITE)
        postulate2_sub = Text("for all observers (c = 299,792,458 m/s)", 
                             font_size=20, 
                             color=YELLOW)
        postulate2_sub.next_to(postulate2, DOWN, buff=0.1)
        
        self.play(Write(postulate2), Write(postulate2_sub))
        
        # Light speed demonstration
        self.demonstrate_light_speed_constancy()

    def demonstrate_light_speed_constancy(self):
        """Show that light speed is constant for all observers"""
        # Two observers - one stationary, one moving
        observer1 = Circle(radius=0.3, color=BLUE, fill_opacity=0.7).shift(LEFT * 3)
        observer2 = Circle(radius=0.3, color=RED, fill_opacity=0.7).shift(RIGHT * 3)
        
        obs1_label = Text("Stationary", font_size=14).next_to(observer1, DOWN)
        obs2_label = Text("Moving", font_size=14).next_to(observer2, DOWN)
        
        self.play(Create(observer1), Create(observer2))
        self.play(Write(obs1_label), Write(obs2_label))
        
        # Light pulses from both observers
        for i in range(3):
            pulse1 = Circle(radius=0.1, color=YELLOW, fill_opacity=0.8).move_to(observer1.get_center())
            pulse2 = Circle(radius=0.1, color=YELLOW, fill_opacity=0.8).move_to(observer2.get_center())
            
            self.add(pulse1, pulse2)
            self.play(
                pulse1.animate.scale(10).set_fill(opacity=0.1),
                pulse2.animate.scale(10).set_fill(opacity=0.1),
                run_time=1
            )
            self.remove(pulse1, pulse2)
        
        # Speed measurements
        speed_text1 = Text("Measures: c", font_size=16, color=YELLOW).next_to(observer1, UP)
        speed_text2 = Text("Also measures: c", font_size=16, color=YELLOW).next_to(observer2, UP)
        
        self.play(Write(speed_text1))
        self.wait(0.5)
        self.play(Write(speed_text2))

    def twin_paradox(self):
        """Illustrate the famous twin paradox"""
        title = Text("The Twin Paradox", font_size=36, color=PURPLE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Setup: Two identical twins
        earth = Circle(radius=0.8, color=BLUE, fill_opacity=0.8).shift(LEFT * 4)
        earth_label = Text("Earth", font_size=16, color=WHITE).next_to(earth, DOWN)
        
        twin_earth = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to(earth.get_center())
        twin_space = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to(earth.get_center())
        
        self.play(Create(earth), Write(earth_label))
        self.play(Create(twin_earth), Create(twin_space))
        
        # Space twin travels to distant star
        star = Circle(radius=0.6, color=YELLOW, fill_opacity=0.8).shift(RIGHT * 4)
        star_label = Text("Distant Star", font_size=16, color=WHITE).next_to(star, DOWN)
        
        self.play(Create(star), Write(star_label))
        
        # Journey animation
        journey_path = Line(earth.get_center(), star.get_center(), color=RED)
        self.play(Create(journey_path))
        
        # Space twin travels at high speed
        self.play(
            twin_space.animate.move_to(star.get_center()),
            run_time=2
        )
        
        # Time passes differently
        earth_clock = self.create_clock(earth.get_center() + UP * 1.5, "Earth Time")
        space_clock = self.create_clock(star.get_center() + UP * 1.5, "Space Time")
        
        # Show time dilation during journey
        for i in range(5):
            self.play(
                Rotate(earth_clock[1], PI/3),  # Earth clock ticks faster
                Rotate(space_clock[1], PI/6),  # Space clock ticks slower
                run_time=0.4
            )
        
        # Return journey
        return_path = Line(star.get_center(), earth.get_center(), color=ORANGE)
        self.play(Create(return_path))
        self.play(
            twin_space.animate.move_to(earth.get_center()),
            run_time=2
        )
        
        # Final comparison
        age_diff = Text("Space twin is younger!", font_size=24, color=YELLOW)
        age_diff.shift(DOWN * 2)
        self.play(Write(age_diff))

    def create_clock(self, position, label):
        """Create a visual clock"""
        clock_circle = Circle(radius=0.4, color=WHITE).move_to(position)
        clock_hand = Line(ORIGIN, UP * 0.3, color=RED).move_to(position)
        clock_label = Text(label, font_size=12).next_to(clock_circle, UP, buff=0.1)
        
        self.play(Create(clock_circle), Create(clock_hand), Write(clock_label))
        return VGroup(clock_circle, clock_hand, clock_label)

    def relativistic_velocity_addition(self):
        """Show how velocities add in relativity"""
        title = Text("Relativistic Velocity Addition", font_size=32, color=ORANGE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Classical vs Relativistic
        classical = Text("Classical Physics:", font_size=24, color=WHITE)
        classical.shift(UP * 1 + LEFT * 3)
        
        classical_formula = MathTex("v = v_1 + v_2", font_size=20)
        classical_formula.next_to(classical, DOWN)
        
        relativistic = Text("Relativistic Physics:", font_size=24, color=WHITE)
        relativistic.shift(UP * 1 + RIGHT * 3)
        
        relativistic_formula = MathTex(
            r"v = \frac{v_1 + v_2}{1 + \frac{v_1 v_2}{c^2}}", 
            font_size=20
        )
        relativistic_formula.next_to(relativistic, DOWN)
        
        self.play(Write(classical), Write(classical_formula))
        self.play(Write(relativistic), Write(relativistic_formula))
        
        # Example calculation
        example = VGroup(
            Text("Example: Two spaceships approaching each other", font_size=18),
            Text("Each traveling at 0.8c relative to Earth", font_size=18),
            Text("Classical: v = 0.8c + 0.8c = 1.6c (IMPOSSIBLE!)", font_size=16, color=RED),
            Text("Relativistic: v = (0.8c + 0.8c)/(1 + 0.64) = 0.976c ✓", font_size=16, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        
        example.shift(DOWN * 1.5)
        
        for line in example:
            self.play(Write(line))
            self.wait(0.5)

    def general_relativity_detailed(self):
        """Detailed explanation of general relativity"""
        title = Text("General Relativity: Gravity as Geometry", 
                    font_size=32, 
                    color=RED)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Einstein's insight
        insight = VGroup(
            Text("Einstein's Revolutionary Insight:", font_size=24, color=YELLOW),
            Text("Gravity is not a force...", font_size=20),
            Text("It's the curvature of spacetime!", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        
        for line in insight:
            self.play(Write(line))
            self.wait(0.5)
        
        self.wait(1)
        self.clear()
        
        # Demonstrate with rubber sheet analogy
        self.rubber_sheet_analogy()

    def rubber_sheet_analogy(self):
        """Demonstrate spacetime curvature with rubber sheet analogy"""
        title = Text("The Rubber Sheet Analogy", font_size=28, color=BLUE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create flat spacetime grid
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 0.6}
        )
        
        self.play(Create(grid))
        
        # Add massive object (bowling ball on rubber sheet)
        mass = Circle(radius=0.8, color=YELLOW, fill_opacity=1)
        mass_label = Text("Massive Star", font_size=16, color=BLACK).move_to(mass.get_center())
        
        self.play(Create(mass), Write(mass_label))
        
        # Show curvature effect
        curved_lines = VGroup()
        for x in range(-3, 4):
            for y in range(-2, 3):
                if x**2 + y**2 > 1:  # Don't draw lines inside the mass
                    r = np.sqrt(x**2 + y**2)
                    curve_factor = 0.5 / r
                    start = np.array([x, y, 0])
                    end = np.array([x, y - curve_factor, 0])
                    curved_line = Line(start, end, color=BLUE, stroke_width=1)
                    curved_lines.add(curved_line)
        
        self.play(Transform(grid, curved_lines))
        
        # Add orbiting object
        planet = Circle(radius=0.15, color=BLUE, fill_opacity=1).shift(RIGHT * 3)
        
        # Orbital path
        orbit_path = ParametricFunction(
            lambda t: np.array([3*np.cos(t), 1.5*np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=GREEN
        )
        
        self.play(Create(orbit_path))
        self.play(Create(planet))
        self.play(MoveAlongPath(planet, orbit_path), run_time=4)
        
        # Explanation
        explanation = Text("Planet follows the 'straightest' path in curved spacetime",
                          font_size=18, color=WHITE)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

    def real_world_applications(self):
        """Show real-world applications of relativity"""
        title = Text("Relativity in Daily Life", font_size=36, color=GREEN)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        applications = [
            ("GPS Satellites", "Need relativistic corrections", self.gps_demo),
            ("Particle Accelerators", "Particles gain relativistic mass", self.accelerator_demo),
            ("Nuclear Power", "E=mc² converts mass to energy", self.nuclear_demo),
            ("Black Holes", "Extreme spacetime curvature", self.black_hole_demo),
        ]
        
        for i, (app_name, description, demo_func) in enumerate(applications):
            self.clear()
            title.to_edge(UP)
            self.add(title)
            
            app_title = Text(f"{i+1}. {app_name}", font_size=28, color=YELLOW)
            app_desc = Text(description, font_size=20, color=WHITE)
            app_desc.next_to(app_title, DOWN)
            
            self.play(Write(app_title), Write(app_desc))
            demo_func()
            self.wait(2)

    def gps_demo(self):
        """Demonstrate GPS relativistic corrections"""
        # Earth and satellites
        earth = Circle(radius=1, color=BLUE, fill_opacity=0.8)
        satellites = VGroup(*[
            Circle(radius=0.1, color=YELLOW, fill_opacity=1).shift(
                2.5 * np.array([np.cos(i*PI/2), np.sin(i*PI/2), 0])
            ) for i in range(4)
        ])
        
        self.play(Create(earth))
        self.play(Create(satellites))
        
        # Time difference
        time_diff = Text("Without relativistic corrections:", font_size=16)
        time_diff.shift(DOWN * 2)
        error = Text("GPS would be off by 10 km per day!", font_size=16, color=RED)
        error.next_to(time_diff, DOWN)
        
        self.play(Write(time_diff), Write(error))

    def accelerator_demo(self):
        """Demonstrate particle acceleration"""
        # Particle path
        accelerator_ring = Circle(radius=2, color=WHITE)
        particle = Circle(radius=0.05, color=RED, fill_opacity=1).move_to(accelerator_ring.point_at_angle(0))
        
        self.play(Create(accelerator_ring), Create(particle))
        
        # Show increasing speed and mass
        for i in range(3):
            speed = 0.5 + i * 0.2
            self.play(
                MoveAlongPath(particle, accelerator_ring),
                particle.animate.scale(1 + i * 0.3),  # Increasing "mass"
                run_time=2 - i * 0.3
            )

    def nuclear_demo(self):
        """Demonstrate nuclear energy"""
        # Small amount of matter
        matter = Circle(radius=0.2, color=WHITE, fill_opacity=1)
        matter_label = Text("Small amount of matter", font_size=14).next_to(matter, UP)
        
        self.play(Create(matter), Write(matter_label))
        
        # Conversion to energy
        energy_burst = Circle(radius=2, color=YELLOW, fill_opacity=0.3)
        energy_label = Text("ENORMOUS amount of energy!", font_size=16, color=YELLOW)
        energy_label.next_to(energy_burst, DOWN)
        
        self.play(
            Transform(matter, energy_burst),
            Write(energy_label)
        )

    def black_hole_demo(self):
        """Demonstrate black hole spacetime curvature"""
        # Extreme curvature visualization
        black_hole = Circle(radius=0.5, color=BLACK, fill_opacity=1)
        event_horizon = Circle(radius=0.5, color=WHITE, fill_opacity=0)
        
        self.play(Create(event_horizon), Create(black_hole))
        
        # Light bending
        light_paths = VGroup()
        for angle in [PI/4, PI/2, 3*PI/4]:
            path = ParametricFunction(
                lambda t: np.array([
                    2*np.cos(angle) * (1-t) + 0.6*np.cos(angle + PI/2) * t,
                    2*np.sin(angle) * (1-t) + 0.6*np.sin(angle + PI/2) * t,
                    0
                ]),
                t_range=[0, 1],
                color=YELLOW
            )
            light_paths.add(path)
        
        self.play(Create(light_paths))

    def modern_implications(self):
        """Discuss modern implications and future"""
        title = Text("Modern Physics & Future Implications", 
                    font_size=32, 
                    color=PURPLE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        implications = VGroup(
            Text("🌌 Understanding the Universe:", font_size=20),
            Text("  • Big Bang cosmology", font_size=18, color=YELLOW),
            Text("  • Dark matter and dark energy", font_size=18, color=YELLOW),
            Text("  • Gravitational waves (LIGO discoveries)", font_size=18, color=YELLOW),
            Text("", font_size=10),  # Spacer
            Text("🚀 Future Technologies:", font_size=20),
            Text("  • Quantum computing", font_size=18, color=GREEN),
            Text("  • Fusion energy", font_size=18, color=GREEN),
            Text("  • Space-time engineering(?)", font_size=18, color=GREEN),
            Text("", font_size=10),  # Spacer
            Text("🤔 Philosophical Questions:", font_size=20),
            Text("  • Nature of time and space", font_size=18, color=ORANGE),
            Text("  • Multiple universes", font_size=18, color=ORANGE),
            Text("  • Quantum gravity", font_size=18, color=ORANGE),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        implications.shift(DOWN * 0.5)
        
        for line in implications:
            if line.text:  # Skip empty spacers
                self.play(Write(line), run_time=0.5)
                self.wait(0.2)
        
        # Final quote
        final_quote = Text('"The most incomprehensible thing about the universe"',
                          font_size=20, color=YELLOW, slant=ITALIC)
        final_quote2 = Text('"is that it is comprehensible." - Einstein',
                           font_size=20, color=YELLOW, slant=ITALIC)
        
        final_quote.shift(DOWN * 2.5)
        final_quote2.next_to(final_quote, DOWN, buff=0.2)
        
        self.play(Write(final_quote))
        self.play(Write(final_quote2))


if __name__ == "__main__":
    # To render: manim -pql relativity_explainer_enhanced.py EnhancedRelativityExplainer
    pass
