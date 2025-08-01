"""
Einstein's Relativity Video with Audio and Professional Subtitles
This version includes synchronized narration and on-screen subtitles
"""

from manim import *
import numpy as np
import asyncio
import edge_tts
import os
from pathlib import Path

class RelativityWithSubtitles(Scene):
    def __init__(self):
        super().__init__()
        self.audio_dir = Path("audio")
        self.audio_dir.mkdir(exist_ok=True)
        
    def construct(self):
        """Main scene with audio and subtitles"""
        
        # Pre-generate all audio files
        print("🎵 Generating audio and subtitles...")
        asyncio.run(self.generate_all_audio())
        
        # Title scene
        self.title_scene_with_subtitles()
        
        # Time dilation scene
        self.time_dilation_with_subtitles()
        
        # E=mc² scene
        self.energy_mass_with_subtitles()
        
        # Conclusion scene
        self.conclusion_with_subtitles()

    async def generate_all_audio(self):
        """Pre-generate all audio files"""
        
        audio_scripts = {
            "title": "Welcome to Einstein's Theory of Relativity. Today we'll explore the revolutionary ideas that changed our understanding of space, time, and the universe forever.",
            
            "time_dilation": "One of the most mind-bending effects of relativity is time dilation. When objects move at very high speeds, time actually runs slower for the moving object compared to a stationary observer.",
            
            "energy_mass": "Einstein's most famous equation, E equals M C squared, reveals that mass and energy are equivalent. Even a tiny amount of mass contains enormous energy.",
            
            "conclusion": "Einstein's theories revolutionized physics and continue to impact our daily lives, from GPS satellites to nuclear energy. The universe is far stranger than we ever imagined."
        }
        
        voice = "en-US-AriaNeural"
        
        for filename, text in audio_scripts.items():
            audio_path = self.audio_dir / f"{filename}.wav"
            if not audio_path.exists():
                print(f"🎙️ Generating {filename}.wav...")
                communicate = edge_tts.Communicate(text, voice)
                await communicate.save(str(audio_path))

    def add_narration_with_subtitles(self, filename, subtitle_text):
        """Add audio and display subtitles"""
        audio_path = self.audio_dir / f"{filename}.wav"
        
        if audio_path.exists():
            print(f"🔊 Adding audio: {filename}.wav")
            self.add_sound(str(audio_path))
        
        # Show subtitles
        self.display_subtitle_sequence(subtitle_text)

    def display_subtitle_sequence(self, text):
        """Display subtitles in chunks"""
        # Split text into readable chunks
        sentences = text.replace('. ', '.|').split('|')
        
        for sentence in sentences:
            if sentence.strip():
                self.show_subtitle(sentence.strip())

    def show_subtitle(self, text):
        """Show a single subtitle with professional styling"""
        # Create subtitle text
        subtitle = Text(
            text,
            font_size=18,
            color=WHITE,
            weight=NORMAL,
            font="Arial"
        )
        
        # Create semi-transparent background
        padding = 0.3
        bg = Rectangle(
            width=min(subtitle.width + padding * 2, 12),
            height=subtitle.height + padding,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1,
            stroke_opacity=0.3
        )
        
        # Group subtitle with background
        subtitle_group = VGroup(bg, subtitle)
        subtitle_group.to_edge(DOWN, buff=0.8)
        
        # Animate subtitle appearance
        duration = len(text.split()) * 0.5  # Reading time
        
        self.play(FadeIn(subtitle_group), run_time=0.5)
        self.wait(max(duration - 1, 1))
        self.play(FadeOut(subtitle_group), run_time=0.5)

    def title_scene_with_subtitles(self):
        """Title scene with narration and subtitles"""
        subtitle_text = "Welcome to Einstein's Theory of Relativity. Today we'll explore the revolutionary ideas that changed our understanding of space, time, and the universe forever."
        
        # Start audio and subtitles
        self.add_narration_with_subtitles("title", subtitle_text)
        
        # Title animation
        title = Text("Einstein's Theory", font_size=56, color=BLUE, weight=BOLD)
        subtitle = Text("of Relativity", font_size=56, color=BLUE, weight=BOLD)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=2)
        
        # Famous equation
        equation = Text("E = mc²", font_size=48, color=GOLD, weight=BOLD)
        equation.shift(DOWN * 2)
        
        self.play(Write(equation), run_time=2)
        self.wait(4)  # Wait for narration to finish
        self.clear()

    def time_dilation_with_subtitles(self):
        """Time dilation scene with subtitles"""
        subtitle_text = "One of the most mind-bending effects of relativity is time dilation. When objects move at very high speeds, time actually runs slower for the moving object compared to a stationary observer."
        
        self.add_narration_with_subtitles("time_dilation", subtitle_text)
        
        title = Text("Time Dilation", font_size=40, color=RED, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create clocks
        clock1 = Circle(radius=0.8, color=BLUE, stroke_width=3).shift(LEFT * 3)
        clock2 = Circle(radius=0.8, color=RED, stroke_width=3).shift(RIGHT * 3)
        
        # Clock labels
        label1 = Text("Stationary Clock", font_size=16, color=BLUE).next_to(clock1, DOWN)
        label2 = Text("Moving at 90% Light Speed", font_size=14, color=RED).next_to(clock2, DOWN)
        
        self.play(Create(clock1), Create(clock2))
        self.play(Write(label1), Write(label2))
        
        # Clock hands
        hand1 = Line(ORIGIN, UP * 0.6, color=WHITE, stroke_width=4).move_to(clock1.get_center())
        hand2 = Line(ORIGIN, UP * 0.6, color=WHITE, stroke_width=4).move_to(clock2.get_center())
        
        self.play(Create(hand1), Create(hand2))
        
        # Animate time difference
        for i in range(5):
            self.play(
                Rotate(hand1, PI/2, about_point=clock1.get_center()),
                Rotate(hand2, PI/6, about_point=clock2.get_center()),  # Much slower
                run_time=1.2
            )
        
        # Add explanation
        explanation = Text("Moving clocks run slower!", font_size=24, color=YELLOW, weight=BOLD)
        explanation.shift(UP * 2.5)
        self.play(Write(explanation))
        
        self.wait(6)
        self.clear()

    def energy_mass_with_subtitles(self):
        """E=mc² scene with subtitles"""
        subtitle_text = "Einstein's most famous equation, E equals M C squared, reveals that mass and energy are equivalent. Even a tiny amount of mass contains enormous energy."
        
        self.add_narration_with_subtitles("energy_mass", subtitle_text)
        
        title = Text("Mass-Energy Equivalence", font_size=36, color=PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # The famous equation with glow effect
        equation = Text("E = mc²", font_size=80, color=GOLD, weight=BOLD)
        equation_glow = Text("E = mc²", font_size=82, color=YELLOW, weight=BOLD)
        equation_glow.set_opacity(0.3)
        
        equation_group = VGroup(equation_glow, equation)
        self.play(Write(equation_group), run_time=3)
        
        # Visual demonstration
        mass = Circle(radius=0.3, color=WHITE, fill_opacity=1, stroke_width=2).shift(LEFT * 4)
        mass_label = Text("1 gram", font_size=14, color=WHITE).next_to(mass, DOWN)
        
        # Conversion arrow
        arrow = Arrow(LEFT * 2, RIGHT * 1, color=RED, buff=0.3, stroke_width=6)
        conversion_text = Text("× c²", font_size=24, color=RED, weight=BOLD).next_to(arrow, UP)
        
        # Energy visualization
        energy = Circle(radius=2.5, color=YELLOW, fill_opacity=0.3, stroke_width=3).shift(RIGHT * 3)
        energy_inner = Circle(radius=1.8, color=GOLD, fill_opacity=0.5).shift(RIGHT * 3)
        energy_label = Text("90 Trillion\nJoules!", font_size=20, color=YELLOW, weight=BOLD)
        energy_label.move_to(energy.get_center())
        
        # Animate the demonstration
        self.play(Create(mass), Write(mass_label))
        self.wait(1)
        self.play(Create(arrow), Write(conversion_text))
        self.wait(1)
        self.play(Create(energy), Create(energy_inner), Write(energy_label))
        
        # Add practical example
        example = Text("Enough to power a city for hours!", font_size=16, color=GREEN)
        example.shift(DOWN * 3)
        self.play(Write(example))
        
        self.wait(6)
        self.clear()

    def conclusion_with_subtitles(self):
        """Conclusion scene with subtitles"""
        subtitle_text = "Einstein's theories revolutionized physics and continue to impact our daily lives, from GPS satellites to nuclear energy. The universe is far stranger than we ever imagined."
        
        self.add_narration_with_subtitles("conclusion", subtitle_text)
        
        title = Text("Einstein's Legacy", font_size=40, color=GREEN, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Impact points with icons
        impacts = VGroup(
            Text("🌟 Revolutionized our view of reality", font_size=22),
            Text("📡 Enabled GPS and satellite technology", font_size=22),
            Text("⚡ Made nuclear energy possible", font_size=22),
            Text("🌌 Revealed cosmic mysteries", font_size=22),
            Text("🔬 Continues to guide modern physics", font_size=22),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        impacts.shift(LEFT * 1)
        
        for impact in impacts:
            self.play(Write(impact))
            self.wait(1.5)
        
        # Final inspirational message
        final_message = Text("The universe is far stranger and more", font_size=24, color=GOLD)
        final_message2 = Text("beautiful than we ever imagined!", font_size=24, color=GOLD, weight=BOLD)
        
        final_group = VGroup(final_message, final_message2).arrange(DOWN, buff=0.2)
        final_group.shift(DOWN * 2)
        
        self.play(Write(final_group))
        
        # Einstein's quote
        quote = Text('"Imagination is more important than knowledge"', 
                    font_size=18, color=YELLOW, slant=ITALIC)
        attribution = Text("- Albert Einstein", font_size=16, color=YELLOW)
        
        quote_group = VGroup(quote, attribution).arrange(DOWN, buff=0.2)
        quote_group.shift(DOWN * 3.5)
        
        self.play(Write(quote_group))
        self.wait(8)


# Version with advanced subtitle features
class RelativityAdvancedSubtitles(Scene):
    def construct(self):
        """Advanced subtitle demo with different styles"""
        
        # Example of different subtitle styles
        self.subtitle_style_demo()

    def subtitle_style_demo(self):
        """Demonstrate different subtitle styles"""
        
        # Style 1: Classic bottom subtitles
        subtitle1 = self.create_subtitle("Classic bottom subtitle style", style="bottom")
        self.play(FadeIn(subtitle1))
        self.wait(2)
        self.play(FadeOut(subtitle1))
        
        # Style 2: Top subtitles
        subtitle2 = self.create_subtitle("Top subtitle for special emphasis", style="top")
        self.play(FadeIn(subtitle2))
        self.wait(2)
        self.play(FadeOut(subtitle2))
        
        # Style 3: Floating subtitles
        subtitle3 = self.create_subtitle("Floating subtitle that follows content", style="floating")
        self.play(FadeIn(subtitle3))
        self.wait(2)
        self.play(FadeOut(subtitle3))

    def create_subtitle(self, text, style="bottom", color=WHITE):
        """Create styled subtitles"""
        subtitle_text = Text(text, font_size=18, color=color)
        
        # Background for readability
        bg = Rectangle(
            width=subtitle_text.width + 0.5,
            height=subtitle_text.height + 0.3,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=color,
            stroke_width=1,
            stroke_opacity=0.5
        )
        bg.move_to(subtitle_text.get_center())
        
        subtitle_group = VGroup(bg, subtitle_text)
        
        # Position based on style
        if style == "bottom":
            subtitle_group.to_edge(DOWN, buff=0.8)
        elif style == "top":
            subtitle_group.to_edge(UP, buff=0.8)
        elif style == "floating":
            subtitle_group.move_to(ORIGIN)
        
        return subtitle_group


if __name__ == "__main__":
    print("🎬 Einstein's Relativity with Audio and Subtitles")
    print("="*50)
    print("\n🎵 This version includes:")
    print("   • Professional narration")
    print("   • Synchronized subtitles")
    print("   • Multiple subtitle styles")
    print("   • Enhanced readability")
    print("\n📋 Requirements:")
    print("   pip install edge-tts")
    print("\n🎯 Commands:")
    print("   python -m manim -pql relativity_subtitles.py RelativityWithSubtitles")
    print("   python -m manim -pql relativity_subtitles.py RelativityAdvancedSubtitles")
    print("\n✨ Features:")
    print("   • Auto-generated subtitles from narration")
    print("   • Professional subtitle styling")
    print("   • Timed subtitle display")
    print("   • Multiple subtitle positions")
