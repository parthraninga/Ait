"""
Subtitle Generator for Einstein's Relativity Video
Creates SRT subtitle files that can be used with any video player
"""

import asyncio
import edge_tts
from pathlib import Path
import re

class SubtitleGenerator:
    def __init__(self):
        self.audio_dir = Path("audio")
        self.subtitle_dir = Path("subtitles")
        self.subtitle_dir.mkdir(exist_ok=True)
        
    def generate_srt_subtitles(self):
        """Generate SRT subtitle file"""
        
        # Subtitle content with timings (approximate)
        subtitles = [
            {
                "start": "00:00:00,000",
                "end": "00:00:08,000", 
                "text": "Welcome to Einstein's Theory of Relativity.\nToday we'll explore revolutionary ideas that changed\nour understanding of space, time, and the universe."
            },
            {
                "start": "00:00:10,000",
                "end": "00:00:18,000",
                "text": "Einstein's Special Theory of Relativity is built\non two fundamental postulates about physics\nand the speed of light."
            },
            {
                "start": "00:00:20,000",
                "end": "00:00:35,000",
                "text": "One mind-bending consequence is time dilation.\nWhen objects move at high speeds,\ntime actually runs slower for the moving object."
            },
            {
                "start": "00:00:37,000",
                "end": "00:00:45,000",
                "text": "The mathematical relationship is given by\nthe time dilation formula, where gamma\nis the Lorentz factor."
            },
            {
                "start": "00:00:47,000",
                "end": "00:00:58,000",
                "text": "Another fascinating effect is length contraction.\nObjects moving at high speeds appear shorter\nin the direction of motion."
            },
            {
                "start": "00:01:00,000",
                "end": "00:01:15,000",
                "text": "Einstein's most famous equation, E = mc²,\nreveals that mass and energy are equivalent.\nEven tiny mass contains enormous energy."
            },
            {
                "start": "00:01:17,000",
                "end": "00:01:30,000",
                "text": "General Relativity reveals that gravity\nis not a force, but the curvature of spacetime.\nMassive objects warp the fabric of spacetime."
            },
            {
                "start": "00:01:32,000",
                "end": "00:01:45,000",
                "text": "Einstein's theories revolutionized physics\nand continue to impact our daily lives,\nfrom GPS satellites to nuclear energy."
            },
            {
                "start": "00:01:47,000",
                "end": "00:01:55,000",
                "text": "The universe is far stranger and more beautiful\nthan we ever imagined.\n\"Imagination is more important than knowledge.\""
            }
        ]
        
        # Generate SRT file
        srt_content = ""
        for i, subtitle in enumerate(subtitles, 1):
            srt_content += f"{i}\n"
            srt_content += f"{subtitle['start']} --> {subtitle['end']}\n"
            srt_content += f"{subtitle['text']}\n\n"
        
        # Save SRT file
        srt_path = self.subtitle_dir / "relativity_subtitles.srt"
        with open(srt_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        
        print(f"✅ Created subtitle file: {srt_path}")
        return srt_path

    def generate_vtt_subtitles(self):
        """Generate WebVTT subtitle file for web players"""
        
        vtt_content = "WEBVTT\n\n"
        
        subtitles = [
            ("00:00.000", "00:08.000", "Welcome to Einstein's Theory of Relativity."),
            ("00:08.000", "00:16.000", "Today we'll explore revolutionary ideas that changed our understanding."),
            ("00:20.000", "00:35.000", "One mind-bending consequence is time dilation."),
            ("00:35.000", "00:45.000", "The mathematical relationship uses the Lorentz factor."),
            ("00:47.000", "00:58.000", "Length contraction makes objects appear shorter when moving."),
            ("01:00.000", "01:15.000", "E = mc² reveals mass and energy are equivalent."),
            ("01:17.000", "01:30.000", "Gravity is the curvature of spacetime itself."),
            ("01:32.000", "01:45.000", "These theories continue to impact our daily lives."),
            ("01:47.000", "01:55.000", "\"Imagination is more important than knowledge.\"")
        ]
        
        for start, end, text in subtitles:
            vtt_content += f"{start} --> {end}\n{text}\n\n"
        
        # Save VTT file
        vtt_path = self.subtitle_dir / "relativity_subtitles.vtt"
        with open(vtt_path, 'w', encoding='utf-8') as f:
            f.write(vtt_content)
        
        print(f"✅ Created WebVTT file: {vtt_path}")
        return vtt_path

    def generate_subtitle_overlay_script(self):
        """Generate a script to overlay subtitles on existing video"""
        
        script = '''
# FFmpeg command to add subtitles to video
# Replace 'input_video.mp4' with your video filename

# Add SRT subtitles (burned into video):
ffmpeg -i input_video.mp4 -vf "subtitles=subtitles/relativity_subtitles.srt:force_style='FontSize=20,PrimaryColour=&Hffffff,OutlineColour=&H000000,Outline=2'" output_with_subtitles.mp4

# Add SRT subtitles (separate subtitle track):
ffmpeg -i input_video.mp4 -i subtitles/relativity_subtitles.srt -c copy -c:s mov_text output_with_subtitle_track.mp4

# For web players, use WebVTT:
# Just load the .vtt file alongside your video in HTML5 video player

# Example HTML:
<video controls>
    <source src="relativity_video.mp4" type="video/mp4">
    <track src="relativity_subtitles.vtt" kind="subtitles" srclang="en" label="English">
</video>
        '''
        
        script_path = self.subtitle_dir / "add_subtitles_guide.txt"
        with open(script_path, 'w') as f:
            f.write(script)
        
        print(f"✅ Created subtitle guide: {script_path}")

    def create_multi_language_subtitles(self):
        """Create subtitles in multiple languages"""
        
        languages = {
            "es": "es-ES-ElviraNeural",  # Spanish
            "fr": "fr-FR-DeniseNeural",  # French
            "de": "de-DE-KatjaNeural",   # German
        }
        
        base_text = "Welcome to Einstein's Theory of Relativity. Today we explore the revolutionary ideas that changed our understanding of the universe."
        
        # This would require translation - for demo, showing structure
        translations = {
            "es": "Bienvenido a la Teoría de la Relatividad de Einstein. Hoy exploramos las ideas revolucionarias que cambiaron nuestra comprensión del universo.",
            "fr": "Bienvenue dans la Théorie de la Relativité d'Einstein. Aujourd'hui, nous explorons les idées révolutionnaires qui ont changé notre compréhension de l'univers.",
            "de": "Willkommen zu Einsteins Relativitätstheorie. Heute erforschen wir die revolutionären Ideen, die unser Verständnis des Universums veränderten."
        }
        
        for lang_code, translation in translations.items():
            srt_content = f"""1
00:00:00,000 --> 00:00:08,000
{translation}

"""
            
            lang_path = self.subtitle_dir / f"relativity_subtitles_{lang_code}.srt"
            with open(lang_path, 'w', encoding='utf-8') as f:
                f.write(srt_content)
            
            print(f"✅ Created {lang_code} subtitles: {lang_path}")

def main():
    """Generate all subtitle files"""
    
    print("📝 Einstein's Relativity Subtitle Generator")
    print("="*45)
    
    generator = SubtitleGenerator()
    
    print("\n🎯 Generating subtitle files...")
    
    # Generate different formats
    generator.generate_srt_subtitles()
    generator.generate_vtt_subtitles()
    generator.generate_subtitle_overlay_script()
    generator.create_multi_language_subtitles()
    
    print("\n✅ All subtitle files generated!")
    print(f"\n📁 Check the '{generator.subtitle_dir}' folder for:")
    print("   • relativity_subtitles.srt (for video players)")
    print("   • relativity_subtitles.vtt (for web players)")
    print("   • add_subtitles_guide.txt (integration instructions)")
    print("   • Multi-language subtitle files")
    
    print("\n🎬 Usage:")
    print("   1. Use SRT files with VLC, MPV, or other video players")
    print("   2. Use VTT files for web video players")
    print("   3. Follow the guide to burn subtitles into video")
    print("   4. Load subtitle tracks separately for user selection")

if __name__ == "__main__":
    main()
