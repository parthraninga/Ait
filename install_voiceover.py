"""
Install Voiceover Packages for Relativity Video
Run this script to install text-to-speech capabilities
"""

import subprocess
import sys

def install_voiceover_packages():
    """Install all packages needed for voiceover"""
    packages = [
        "edge-tts",        # Microsoft Edge TTS (best quality)
        "pygame",          # Audio playback
        "pydub",          # Audio processing
        "asyncio"         # Async support (usually built-in)
    ]
    
    print("🎙️ Installing Voiceover Packages for Einstein's Relativity Video")
    print("=" * 60)
    
    for package in packages:
        try:
            print(f"📦 Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, "--upgrade"
            ])
            print(f"✅ {package} installed successfully!")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
        except Exception as e:
            print(f"❌ Error installing {package}: {e}")
        print()
    
    print("🎉 Voiceover setup complete!")
    print("\n🎯 Next steps:")
    print("1. Run: python generate_narration.py")
    print("2. This will create professional audio files in the 'audio' folder")
    print("3. Use these audio files with your Manim videos")

if __name__ == "__main__":
    install_voiceover_packages()
    input("\nPress Enter to continue...")
