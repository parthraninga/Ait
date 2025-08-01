"""
Simple Text-to-Speech Script for Relativity Videos
This script generates audio files for your relativity explanations
"""

import asyncio
import edge_tts
from pathlib import Path
import os

class RelativityNarrator:
    def __init__(self):
        self.audio_dir = Path("audio")
        self.audio_dir.mkdir(exist_ok=True)
        
        # Voice options (you can change these):
        # "en-US-AriaNeural" (female, clear)
        # "en-US-GuyNeural" (male, professional)
        # "en-GB-SoniaNeural" (British female)
        # "en-AU-NatashaNeural" (Australian female)
        self.voice = "en-US-AriaNeural"
        self.rate = "+0%"  # Speed: -50% to +100%
        self.volume = "+0%"  # Volume: -50% to +50%

    async def generate_audio(self, text, filename):
        """Generate audio file from text"""
        output_path = self.audio_dir / f"{filename}.mp3"
        
        print(f"🎙️ Generating: {filename}.mp3")
        print(f"📝 Text: {text[:60]}...")
        
        communicate = edge_tts.Communicate(text, self.voice, rate=self.rate, volume=self.volume)
        await communicate.save(str(output_path))
        
        print(f"✅ Saved: {output_path}")
        return output_path

    async def generate_all_narrations(self):
        """Generate all audio files for the relativity video"""
        
        narrations = {
            "title_intro": """
                Welcome to Einstein's Theory of Relativity explained. 
                Today we'll explore one of the most revolutionary theories in physics, 
                which completely changed our understanding of space, time, and the universe itself.
            """,
            
            "special_relativity_intro": """
                Einstein's Special Theory of Relativity, published in 1905, 
                is built on two fundamental postulates. 
                First, the laws of physics are the same in all inertial reference frames. 
                Second, the speed of light in a vacuum is constant for all observers, 
                regardless of their motion or the motion of the light source.
            """,
            
            "time_dilation": """
                One of the most mind-bending consequences of special relativity is time dilation. 
                When objects move at high speeds relative to an observer, time actually runs slower 
                for the moving object. Watch as these two clocks demonstrate this remarkable effect. 
                The stationary clock runs normally, while the clock moving at 80% the speed of light 
                runs significantly slower.
            """,
            
            "time_dilation_formula": """
                The mathematical relationship is given by the time dilation formula, 
                where gamma is the Lorentz factor. For an object moving at 80% the speed of light, 
                gamma equals 1.67, meaning time runs 67% slower for the moving observer.
            """,
            
            "length_contraction": """
                Another fascinating effect is length contraction. Objects moving at high speeds 
                appear shorter in the direction of motion when observed from a stationary frame. 
                Here we see a ruler that is 8 units long when at rest, but when moving at 
                80% the speed of light, it appears to contract to only 4.8 units in length.
            """,
            
            "energy_mass": """
                Perhaps Einstein's most famous equation is E equals M C squared. 
                This revolutionary formula reveals that mass and energy are equivalent - 
                even a tiny amount of mass contains an enormous amount of energy. 
                Just one gram of matter, if completely converted to energy, would release 
                90 trillion joules - enough energy to power a large city for several hours.
            """,
            
            "spacetime_curvature": """
                Einstein's General Theory of Relativity reveals that gravity is not actually a force, 
                but rather the curvature of spacetime itself. Massive objects like stars and planets 
                warp the fabric of spacetime around them, and this curvature is what we experience 
                as gravitational attraction. Planets orbit stars not because they're being pulled 
                by a mysterious force, but because they're following the straightest possible paths 
                through curved spacetime.
            """,
            
            "conclusion": """
                Einstein's theories revolutionized our understanding of the universe. 
                Time and space are relative to the observer. Nothing can travel faster than light. 
                Mass and energy are two forms of the same thing. And gravity is the curvature 
                of spacetime itself. These aren't just abstract mathematical concepts - 
                they're measurable effects that impact everything from GPS satellites to 
                particle accelerators. As Einstein himself once said, imagination is more 
                important than knowledge, for knowledge is limited, while imagination 
                embraces the entire world.
            """
        }

        print("🎬 Generating all narration audio files...")
        print("="*60)
        
        for filename, text in narrations.items():
            # Clean up the text (remove extra whitespace)
            clean_text = " ".join(text.split())
            await self.generate_audio(clean_text, filename)
            print()  # Empty line for readability
        
        print("🎉 All audio files generated successfully!")
        print(f"📁 Check the '{self.audio_dir}' folder for your audio files.")
        
        return list(narrations.keys())

    def create_audio_sync_script(self):
        """Create a script showing when to play each audio file"""
        script = """
# Audio Sync Script for Manim
# Use this to manually sync audio with your animations

def add_voiceover_to_scene(scene):
    # Title Scene (3-4 seconds)
    scene.add_sound("audio/title_intro.mp3")
    
    # Special Relativity Intro (4-5 seconds)  
    scene.add_sound("audio/special_relativity_intro.mp3")
    
    # Time Dilation Demo (5-6 seconds)
    scene.add_sound("audio/time_dilation.mp3")
    
    # Time Dilation Formula (3-4 seconds)
    scene.add_sound("audio/time_dilation_formula.mp3")
    
    # Length Contraction (4-5 seconds)
    scene.add_sound("audio/length_contraction.mp3")
    
    # Energy-Mass Equivalence (5-6 seconds)
    scene.add_sound("audio/energy_mass.mp3")
    
    # Spacetime Curvature (6-7 seconds)
    scene.add_sound("audio/spacetime_curvature.mp3")
    
    # Conclusion (7-8 seconds)
    scene.add_sound("audio/conclusion.mp3")

# To use in your Manim scene:
# 1. Copy audio files to your project folder
# 2. Use scene.add_sound(filename) at appropriate points
# 3. Adjust timing with self.wait() commands
        """
        
        with open("audio_sync_guide.py", "w") as f:
            f.write(script)
        
        print("📋 Created audio_sync_guide.py with timing instructions")

async def main():
    """Main function to generate all audio files"""
    narrator = RelativityNarrator()
    
    print("🎙️ Einstein's Relativity Narrator")
    print("=" * 40)
    print(f"Voice: {narrator.voice}")
    print(f"Speed: {narrator.rate}")
    print(f"Volume: {narrator.volume}")
    print()
    
    # Generate all audio files
    audio_files = await narrator.generate_all_narrations()
    
    # Create sync guide
    narrator.create_audio_sync_script()
    
    print("\n🎯 Next Steps:")
    print("1. Listen to the generated audio files")
    print("2. Adjust timing in your Manim script")
    print("3. Use scene.add_sound() to sync audio with animations")
    print("4. Render your video with: manim -pql your_script.py SceneName")

if __name__ == "__main__":
    print("📦 Make sure you have installed: pip install edge-tts")
    print("🎬 Generating professional narration for relativity video...\n")
    
    try:
        asyncio.run(main())
    except ImportError:
        print("❌ Error: edge-tts not installed")
        print("💡 Install with: pip install edge-tts")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have an internet connection for text-to-speech")
