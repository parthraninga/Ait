"""
Einstein's Relativity Video with REAL Audio Integration
This version properly embeds audio into the final video file
"""

from manim import *
import numpy as np
import asyncio
import edge_tts
import os
from pathlib import Path

class RelativityWithRealAudio(Scene):
    def __init__(self):
        super().__init__()
        self.audio_dir = Path("audio")
        self.audio_dir.mkdir(exist_ok=True)
        
    def construct(self):
        """Main scene construction with embedded audio"""
        
        # Pre-generate all audio files
        print("🎵 Generating audio files...")
        asyncio.run(self.generate_all_audio())
        
        # Scene 1: Title with audio
        self.title_scene()
        
        # Scene 2: Time dilation with audio
        self.time_dilation_scene()
        
        # Scene 3: E=mc² with audio
        self.energy_mass_scene()
        
        # Scene 4: Conclusion with audio
        self.conclusion_scene()

    async def generate_all_audio(self):
        """Pre-generate all audio files before animation starts"""
        
        audio_scripts = {
            "title": """Welcome to Einstein's Theory of Relativity. 
                       Today we'll explore the revolutionary ideas that changed 
                       our understanding of space, time, and the universe forever.""",
            
            "time_dilation": """One of the most mind-bending effects of relativity 
                               is time dilation. When objects move at very high speeds, 
                               time actually runs slower for the moving object compared 
                               to a stationary observer. This isn't science fiction - 
                               it's a measurable reality.""",
            
            "energy_mass": """Einstein's most famous equation, E equals M C squared, 
                             reveals that mass and energy are two forms of the same thing. 
                             Even a tiny amount of mass contains enormous energy. 
                             This principle powers the sun and makes nuclear energy possible.""",
            
            "conclusion": """Einstein's theories revolutionized physics and continue 
                            to impact our daily lives. From GPS satellites that must 
                            account for time dilation, to nuclear energy, to our 
                            understanding of black holes and the expanding universe. 
                            The cosmos is far stranger and more beautiful than 
                            we ever imagined."""
        }
        
        voice = "en-US-AriaNeural"  # Clear female voice
        
        for filename, text in audio_scripts.items():
            audio_path = self.audio_dir / f"{filename}.wav"
            
            if not audio_path.exists():
                print(f"🎙️ Generating {filename}.wav...")
                # Clean up text
                clean_text = " ".join(text.split())
                
                # Generate audio
                communicate = edge_tts.Communicate(clean_text, voice)
                await communicate.save(str(audio_path))
                print(f"✅ Created {filename}.wav")
            else:
                print(f"📁 Using existing {filename}.wav")

    def add_narration(self, filename):
        """Add audio file to the scene"""
        audio_path = self.audio_dir / f"{filename}.wav"
        
        if audio_path.exists():
            print(f"🔊 Adding audio: {filename}.wav")
            self.add_sound(str(audio_path))
            return True
        else:
            print(f"⚠️ Audio file not found: {filename}.wav")
            return False

    def title_scene(self):
        """Title scene with embedded audio"""
        # Add audio at the start of this scene
        self.add_narration("title")
        
        # Title animation
        title = Text("Einstein's Theory", font_size=56, color=BLUE)
        subtitle = Text("of Relativity", font_size=56, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Animate title
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=2)
        
        # Add the famous equation
        equation = Text("E = mc²", font_size=48, color=GOLD)
        equation.shift(DOWN * 2)
        
        self.play(Write(equation), run_time=2)
        
        # Wait for audio to finish (adjust timing as needed)
        self.wait(6)
        self.clear()

    def time_dilation_scene(self):
        """Time dilation demonstration with audio"""
        self.add_narration("time_dilation")
        
        title = Text("Time Dilation", font_size=40, color=RED)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create two clocks
        clock1 = Circle(radius=0.8, color=BLUE).shift(LEFT * 3)
        clock2 = Circle(radius=0.8, color=RED).shift(RIGHT * 3)
        
        # Labels
        label1 = Text("Stationary", font_size=16).next_to(clock1, DOWN)
        label2 = Text("Moving at 90% light speed", font_size=14).next_to(clock2, DOWN)
        
        self.play(Create(clock1), Create(clock2))
        self.play(Write(label1), Write(label2))
        
        # Clock hands
        hand1 = Line(ORIGIN, UP * 0.6, color=WHITE).move_to(clock1.get_center())
        hand2 = Line(ORIGIN, UP * 0.6, color=WHITE).move_to(clock2.get_center())
        
        self.play(Create(hand1), Create(hand2))
        
        # Animate time difference
        for i in range(5):
            self.play(
                Rotate(hand1, PI/2, about_point=clock1.get_center()),
                Rotate(hand2, PI/6, about_point=clock2.get_center()),  # Much slower
                run_time=1.2
            )
        
        # Add explanation
        explanation = Text("Moving clocks run slower!", font_size=24, color=YELLOW)
        explanation.shift(DOWN * 2)
        self.play(Write(explanation))
        
        self.wait(8)  # Wait for narration to finish
        self.clear()

    def energy_mass_scene(self):
        """E=mc² demonstration with audio"""
        self.add_narration("energy_mass")
        
        title = Text("Mass-Energy Equivalence", font_size=36, color=PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # The famous equation
        equation = Text("E = mc²", font_size=80, color=GOLD)
        self.play(Write(equation), run_time=3)
        
        # Visual demonstration
        mass = Circle(radius=0.3, color=WHITE, fill_opacity=1).shift(LEFT * 4)
        mass_label = Text("tiny mass", font_size=14).next_to(mass, DOWN)
        
        # Arrow showing conversion
        arrow = Arrow(LEFT * 2, RIGHT * 1, color=RED, buff=0.3)
        arrow_label = Text("× c²", font_size=20, color=RED).next_to(arrow, UP)
        
        energy = Circle(radius=2.5, color=YELLOW, fill_opacity=0.3).shift(RIGHT * 3)
        energy_label = Text("ENORMOUS\nENERGY!", font_size=24, color=YELLOW, weight=BOLD)
        energy_label.move_to(energy.get_center())
        
        # Animate the conversion
        self.play(Create(mass), Write(mass_label))
        self.wait(1)
        self.play(Create(arrow), Write(arrow_label))
        self.wait(1)
        self.play(Create(energy), Write(energy_label))
        
        # Add practical examples
        examples = Text("Powers the Sun • Nuclear Energy • Particle Physics", 
                       font_size=16, color=GREEN)
        examples.shift(DOWN * 3)
        self.play(Write(examples))
        
        self.wait(8)  # Wait for narration
        self.clear()

    def conclusion_scene(self):
        """Conclusion with audio"""
        self.add_narration("conclusion")
        
        title = Text("Einstein's Legacy", font_size=40, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Key points
        points = VGroup(
            Text("🌟 Revolutionized physics", font_size=22),
            Text("📡 Enables GPS technology", font_size=22),
            Text("⚡ Made nuclear energy possible", font_size=22),
            Text("🌌 Revealed cosmic mysteries", font_size=22),
            Text("🔬 Guides modern science", font_size=22),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        
        points.shift(LEFT * 1)
        
        for point in points:
            self.play(Write(point))
            self.wait(1.5)
        
        # Final message
        final = Text("The universe is stranger than we imagined!", 
                    font_size=28, color=GOLD, weight=BOLD)
        final.shift(DOWN * 2)
        self.play(Write(final))
        
        # Einstein quote
        quote = Text('"Imagination is more important than knowledge"', 
                    font_size=18, color=YELLOW, slant=ITALIC)
        attribution = Text("- Albert Einstein", font_size=16, color=YELLOW)
        
        quote.shift(DOWN * 3)
        attribution.next_to(quote, DOWN, buff=0.2)
        
        self.play(Write(quote))
        self.play(Write(attribution))
        
        self.wait(10)  # Wait for narration to finish


# Fallback version without audio
class RelativityNoAudio(Scene):
    def construct(self):
        """Simple version without audio dependencies"""
        title = Text("Einstein's Relativity", font_size=48, color=BLUE)
        subtitle = Text("Visual Explanation", font_size=24, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        
        equation = Text("E = mc²", font_size=64, color=GOLD)
        equation.shift(DOWN)
        self.play(Write(equation))
        self.wait(3)


if __name__ == "__main__":
    print("🎬 Einstein's Relativity with Real Audio Integration")
    print("="*55)
    print("\n🎵 This version creates videos WITH embedded audio!")
    print("\n📋 Requirements:")
    print("   pip install edge-tts")
    print("\n🎯 Commands:")
    print("   python -m manim -pql relativity_audio_fixed.py RelativityWithRealAudio")
    print("   python -m manim -pql relativity_audio_fixed.py RelativityNoAudio")
    print("\n✨ Features:")
    print("   • Pre-generates all audio files")
    print("   • Embeds audio directly in video")
    print("   • Professional narration")
    print("   • Synchronized timing")
    print("\n🎬 Ready to create your narrated video!")
