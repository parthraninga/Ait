"""
Einstein's Theory of Relativity Explainer Video with Voiceover
Created using Manim (Mathematical Animation Engine) + Text-to-Speech

This script creates an animated video with professional narration explaining 
key concepts of Einstein's Theory of Relativity.
"""

from manim import *
import numpy as np
import asyncio
import edge_tts
import pygame
import os
from pathlib import Path
import tempfile

class VoiceoverRelativityExplainer(Scene):
    def __init__(self):
        super().__init__()
        self.audio_dir = Path("audio")
        self.audio_dir.mkdir(exist_ok=True)
        pygame.mixer.init()
        
        # Voice settings (you can change these)
        self.voice = "en-US-AriaNeural"  # Microsoft Edge TTS voice
        self.rate = "+0%"  # Speech rate
        self.volume = "+0%"  # Volume
        
    def construct(self):
        # Title Scene with Voiceover
        self.create_title_with_voiceover()
        self.wait(3)
        self.clear()
        
        # Introduction to Special Relativity
        self.special_relativity_intro_with_voiceover()
        self.wait(3)
        self.clear()
        
        # Time Dilation Animation
        self.time_dilation_demo_with_voiceover()
        self.wait(3)
        self.clear()
        
        # Length Contraction
        self.length_contraction_demo_with_voiceover()
        self.wait(3)
        self.clear()
        
        # E=mc² explanation
        self.energy_mass_equivalence_with_voiceover()
        self.wait(3)
        self.clear()
        
        # General Relativity - Spacetime Curvature
        self.spacetime_curvature_with_voiceover()
        self.wait(3)
        self.clear()
        
        # Conclusion
        self.conclusion_with_voiceover()
        self.wait(4)

    async def generate_speech(self, text, filename):
        """Generate speech audio file using Edge TTS"""
        audio_path = self.audio_dir / f"{filename}.mp3"
        
        if not audio_path.exists():
            communicate = edge_tts.Communicate(text, self.voice, rate=self.rate, volume=self.volume)
            await communicate.save(str(audio_path))
        
        return str(audio_path)

    def play_audio_sync(self, text, filename):
        """Play audio synchronously with animation"""
        try:
            # Generate audio file
            audio_path = asyncio.run(self.generate_speech(text, filename))
            
            # Actually add the audio to the scene
            print(f"🔊 Adding audio: {filename}.mp3")
            self.add_sound(audio_path)
            
            # Also print for debugging
            print(f"📝 NARRATION: {text[:100]}...")
            
        except Exception as e:
            print(f"❌ Audio generation failed: {e}")
            print(f"📝 TEXT ONLY: {text}")

    def create_title_with_voiceover(self):
        """Create animated title sequence with narration"""
        narration = """Welcome to Einstein's Theory of Relativity explained. 
                      Today we'll explore one of the most revolutionary theories in physics, 
                      which changed our understanding of space, time, and the universe itself."""
        
        self.play_audio_sync(narration, "title_intro")
        
        title = Text("Einstein's Theory of Relativity", font_size=48, color=BLUE)
        subtitle = Text("An Animated Explanation with Narration", font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Animate title appearance
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        
        # Add Einstein's portrait
        einstein = Circle(radius=1, color=YELLOW).shift(DOWN * 2)
        einstein_text = Text("Einstein", font_size=24).move_to(einstein.get_center())
        
        self.play(Create(einstein), Write(einstein_text))

    def special_relativity_intro_with_voiceover(self):
        """Introduce special relativity with narration"""
        narration = """Einstein's Special Theory of Relativity, published in 1905, 
                      is built on two fundamental postulates. First, the laws of physics 
                      are the same in all inertial reference frames. Second, the speed of light 
                      in a vacuum is constant for all observers, regardless of their motion."""
        
        self.play_audio_sync(narration, "special_relativity_intro")
        
        title = Text("Special Relativity (1905)", font_size=36, color=YELLOW)
        title.to_edge(UP)
        
        postulates = VGroup(
            Text("1. Laws of physics are the same in all inertial frames", font_size=22),
            Text("2. Speed of light is constant for all observers", font_size=22),
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

    def time_dilation_demo_with_voiceover(self):
        """Demonstrate time dilation with narration"""
        narration = """One of the most mind-bending consequences of special relativity is time dilation. 
                      When objects move at high speeds relative to an observer, time actually runs slower 
                      for the moving object. Watch as these two clocks demonstrate this effect. 
                      The stationary clock runs normally, while the clock moving at 80% the speed of light 
                      runs significantly slower."""
        
        self.play_audio_sync(narration, "time_dilation")
        
        title = Text("Time Dilation", font_size=36, color=RED)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create two reference frames
        stationary_frame = Rectangle(width=3, height=2, color=BLUE).shift(LEFT * 3)
        moving_frame = Rectangle(width=3, height=2, color=RED).shift(RIGHT * 3)
        
        stationary_label = Text("Stationary Observer", font_size=14).next_to(stationary_frame, UP)
        moving_label = Text("Moving at 0.8c", font_size=14).next_to(moving_frame, UP)
        
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
        
        # Animate time dilation
        for i in range(6):
            self.play(
                Rotate(stat_hand, PI/2, about_point=stationary_clock.get_center()),
                Rotate(mov_hand, PI/4, about_point=moving_clock.get_center()),
                run_time=0.8
            )
        
        # Add formula explanation
        formula_narration = """The mathematical relationship is given by the time dilation formula, 
                             where gamma is the Lorentz factor. For an object moving at 80% the speed of light, 
                             gamma equals 1.67, meaning time runs 67% slower."""
        
        self.play_audio_sync(formula_narration, "time_dilation_formula")
        
        # Use Text instead of MathTex to avoid LaTeX issues
        formula = Text("Δt' = γΔt", font_size=32, color=YELLOW)
        gamma_formula = Text("γ = 1/√(1-v²/c²)", font_size=24, color=YELLOW)
        gamma_value = Text("For v=0.8c: γ = 1.67", font_size=20, color=GREEN)
        
        formula.shift(DOWN * 1.5)
        gamma_formula.next_to(formula, DOWN, buff=0.3)
        gamma_value.next_to(gamma_formula, DOWN, buff=0.3)
        
        self.play(Write(formula))
        self.play(Write(gamma_formula))
        self.play(Write(gamma_value))

    def length_contraction_demo_with_voiceover(self):
        """Demonstrate length contraction with narration"""
        narration = """Another fascinating effect is length contraction. Objects moving at high speeds 
                      appear shorter in the direction of motion when observed from a stationary frame. 
                      Here we see a ruler that is 8 units long at rest, but when moving at 80% the speed of light, 
                      it appears to contract to only 4.8 units."""
        
        self.play_audio_sync(narration, "length_contraction")
        
        title = Text("Length Contraction", font_size=36, color=GREEN)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Show rulers
        rest_ruler = Rectangle(width=4, height=0.3, color=BLUE)
        rest_ruler.shift(UP * 1)
        rest_label = Text("Ruler at rest: L₀ = 8 units", font_size=18).next_to(rest_ruler, UP)
        
        self.play(Create(rest_ruler), Write(rest_label))
        
        # Contracted ruler
        gamma = 1/np.sqrt(1-0.8**2)
        contracted_length = 4 / gamma  # Visual scaling
        moving_ruler = Rectangle(width=contracted_length, height=0.3, color=RED)
        moving_ruler.shift(DOWN * 1)
        moving_label = Text(f"Same ruler moving: L = {8/gamma:.1f} units", font_size=18).next_to(moving_ruler, DOWN)
        
        # Motion lines
        motion_lines = VGroup(*[
            Line(LEFT * 0.2, RIGHT * 0.2, color=YELLOW).shift(RIGHT * i * 0.4 + DOWN * 1)
            for i in range(-4, 5)
        ])
        
        self.play(Create(moving_ruler), Write(moving_label))
        self.play(Create(motion_lines))
        
        # Formula
        formula = Text("L = L₀/γ = L₀√(1-v²/c²)", font_size=24, color=YELLOW)
        formula.shift(DOWN * 2.5)
        self.play(Write(formula))

    def energy_mass_equivalence_with_voiceover(self):
        """Explain E=mc² with narration"""
        narration = """Perhaps Einstein's most famous equation is E equals MC squared. 
                      This reveals that mass and energy are equivalent - even a tiny amount of mass 
                      contains an enormous amount of energy. One gram of matter, if completely converted 
                      to energy, would release 90 trillion joules - enough to power a large city for hours."""
        
        self.play_audio_sync(narration, "energy_mass")
        
        title = Text("Mass-Energy Equivalence", font_size=36, color=PURPLE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # The famous equation
        equation = Text("E = mc²", font_size=72, color=GOLD)
        equation.move_to(ORIGIN)
        
        self.play(Write(equation))
        self.wait(1)
        
        # Explanation
        explanation = VGroup(
            Text("E = Energy", font_size=24),
            Text("m = Mass", font_size=24),
            Text("c = Speed of light", font_size=24),
            Text("1 gram = 90 trillion joules!", font_size=18, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(DOWN * 2)
        
        for line in explanation:
            self.play(Write(line))
            self.wait(0.5)
        
        # Visual representation
        mass_circle = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(LEFT * 3 + UP * 0.5)
        mass_label = Text("tiny mass", font_size=12).next_to(mass_circle, DOWN)
        
        energy_explosion = Circle(radius=1.5, color=GOLD, fill_opacity=0.3).shift(RIGHT * 2 + UP * 0.5)
        energy_label = Text("ENORMOUS\nENERGY", font_size=16, color=GOLD).move_to(energy_explosion.get_center())
        
        arrow = Arrow(mass_circle.get_right(), energy_explosion.get_left(), color=RED)
        
        self.play(Create(mass_circle), Write(mass_label))
        self.play(Create(arrow))
        self.play(Create(energy_explosion), Write(energy_label))

    def spacetime_curvature_with_voiceover(self):
        """Demonstrate spacetime curvature with narration"""
        narration = """Einstein's General Theory of Relativity reveals that gravity is not a force, 
                      but the curvature of spacetime itself. Massive objects like stars warp the fabric 
                      of spacetime, and this curvature is what we experience as gravity. Planets orbit 
                      not because they're pulled by a force, but because they're following the curved 
                      paths in spacetime."""
        
        self.play_audio_sync(narration, "spacetime_curvature")
        
        title = Text("General Relativity: Spacetime Curvature", font_size=28, color=ORANGE)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create grid
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1}
        )
        
        self.play(Create(grid))
        
        # Add sun
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        sun_label = Text("⭐", font_size=24).move_to(sun.get_center())
        
        self.play(Create(sun), Write(sun_label))
        
        # Orbital path
        planet_path = ParametricFunction(
            lambda t: np.array([2.5 * np.cos(t), 1.2 * np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=GREEN
        )
        
        self.play(Create(planet_path))
        
        # Planet
        planet = Circle(radius=0.15, color=BLUE, fill_opacity=1).shift(RIGHT * 2.5)
        self.play(Create(planet))
        self.play(MoveAlongPath(planet, planet_path), run_time=4)
        
        # Field equation
        field_equation = Text("Gμν = (8πG/c⁴)Tμν", font_size=18, color=YELLOW)
        field_equation.to_corner(DR)
        field_label = Text("Einstein's Field Equation", font_size=14).next_to(field_equation, UP)
        
        self.play(Write(field_label), Write(field_equation))

    def conclusion_with_voiceover(self):
        """Conclusion with narration"""
        narration = """Einstein's theories revolutionized our understanding of the universe. 
                      Time and space are relative to the observer. Nothing can travel faster than light. 
                      Mass and energy are equivalent. Gravity is the curvature of spacetime itself. 
                      These aren't just abstract concepts - they're measurable effects that impact 
                      everything from GPS satellites to particle accelerators. As Einstein once said, 
                      imagination is more important than knowledge."""
        
        self.play_audio_sync(narration, "conclusion")
        
        title = Text("Einstein's Revolutionary Legacy", font_size=32, color=GREEN)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        takeaways = VGroup(
            Text("• Time and space are relative", font_size=20),
            Text("• Nothing travels faster than light", font_size=20),
            Text("• Mass and energy are equivalent", font_size=20),
            Text("• Gravity curves spacetime", font_size=20),
            Text("• These effects are real and measurable!", font_size=20),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        takeaways.shift(DOWN * 0.5)
        
        for takeaway in takeaways:
            self.play(Write(takeaway))
            self.wait(0.8)
        
        # Quote
        quote = Text('"Imagination is more important than knowledge"', 
                    font_size=18, color=YELLOW, slant=ITALIC)
        attribution = Text("- Albert Einstein", font_size=14, color=YELLOW)
        
        quote.shift(DOWN * 2.5)
        attribution.next_to(quote, DOWN, buff=0.2)
        
        self.play(Write(quote))
        self.play(Write(attribution))


# Alternative version without audio generation (for testing)
class SimpleNarratedRelativity(Scene):
    def construct(self):
        """Simple version that just prints narration text"""
        
        # Title with narration text
        print("🎙️ NARRATION: Welcome to Einstein's Theory of Relativity...")
        
        title = Text("Einstein's Theory of Relativity", font_size=48, color=BLUE)
        subtitle = Text("With Professional Narration", font_size=24, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(3)


if __name__ == "__main__":
    # Install required packages first:
    # pip install edge-tts pygame pydub
    
    print("🎬 Einstein's Relativity Explainer with Voiceover")
    print("="*50)
    print("This version includes professional text-to-speech narration!")
    print("\nTo render with voiceover:")
    print("manim -pql relativity_explainer_with_voiceover.py VoiceoverRelativityExplainer")
    print("\nTo test without audio:")
    print("manim -pql relativity_explainer_with_voiceover.py SimpleNarratedRelativity")
