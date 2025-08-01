"""
Quick Start Script for Einstein's Relativity Explainer

This script helps you quickly get started with creating relativity explainer videos.
It will check your system, install dependencies, and provide easy commands to run.
"""

import subprocess
import sys
import os
import importlib

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def check_package(package_name):
    """Check if a package is installed"""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def install_basic_packages():
    """Install basic packages for simple demo"""
    packages = ["matplotlib", "numpy"]
    missing_packages = [pkg for pkg in packages if not check_package(pkg)]
    
    if missing_packages:
        print(f"Installing basic packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print("✅ Basic packages installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install basic packages")
            return False
    else:
        print("✅ All basic packages are already installed")
        return True

def install_voiceover_packages():
    """Install packages for text-to-speech narration"""
    packages = ["edge-tts", "pygame", "pydub"]
    print("Installing voiceover packages...")
    
    missing_packages = [pkg for pkg in packages if not check_package(pkg.replace('-', '_'))]
    
    if missing_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)
            print("✅ Voiceover packages installed successfully!")
            print("🎙️ You can now generate professional narration!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install voiceover packages")
            return False
    else:
        print("✅ All voiceover packages are already installed")
        return True

def generate_subtitles():
    """Generate subtitle files"""
    try:
        print("📝 Generating subtitle files...")
        subprocess.run([sys.executable, "generate_subtitles.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to generate subtitles")
    except FileNotFoundError:
        print("❌ generate_subtitles.py not found")

def create_video_with_subtitles():
    """Create video with audio and subtitles"""
    if not check_package("edge_tts"):
        print("❌ edge-tts not installed. Please install voiceover packages first (option B)")
        return
    
    try:
        print("🎬 Creating video with audio and subtitles...")
        subprocess.run([
            sys.executable, "-m", "manim", 
            "-pql", "relativity_subtitles.py", "RelativityWithSubtitles"
        ], check=True)
        print("✅ Video with subtitles created successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to create video with subtitles")
    except FileNotFoundError:
        print("❌ relativity_subtitles.py not found")

def generate_narration():
    """Generate audio narration files"""
    if not check_package("edge_tts"):
        print("❌ edge-tts not installed. Please install voiceover packages first (option A)")
        return
    
    try:
        print("🎙️ Generating professional narration...")
        subprocess.run([sys.executable, "generate_narration.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to generate narration")
    except FileNotFoundError:
        print("❌ generate_narration.py not found")

def install_manim():
    """Install Manim for advanced video creation"""
    if check_package("manim"):
        print("✅ Manim is already installed")
        return True
    
    print("Installing Manim (this may take a few minutes)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "manim"])
        print("✅ Manim installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Manim")
        print("   You can still use the simple demo version")
        return False

def run_simple_demo():
    """Run the simple matplotlib demo"""
    try:
        print("Starting simple relativity demonstration...")
        subprocess.run([sys.executable, "simple_relativity_demo.py"], check=False)
    except FileNotFoundError:
        print("❌ simple_relativity_demo.py not found")

def run_manim_demo(scene_name="RelativityExplainer", quality="low"):
    """Run Manim demonstration"""
    quality_flags = {
        "low": "-pql",
        "medium": "-pqm", 
        "high": "-pqh",
        "4k": "-pqk"
    }
    
    flag = quality_flags.get(quality, "-pql")
    
    try:
        print(f"Rendering {scene_name} with {quality} quality...")
        subprocess.run([
            "manim", flag, "relativity_explainer.py", scene_name
        ], check=False)
    except FileNotFoundError:
        print("❌ Manim not found. Please install Manim first.")

def show_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("EINSTEIN'S THEORY OF RELATIVITY EXPLAINER")
    print("="*60)
    print("Choose an option:")
    print()
    print("BASIC DEMOS (No Manim required):")
    print("1. 🎬 Run simple matplotlib demo")
    print("2. 🧮 Interactive relativity calculator")
    print()
    print("ADVANCED VIDEOS (Requires Manim):")
    print("3. 🎥 Render basic explainer video (low quality)")
    print("4. 🎥 Render basic explainer video (high quality)")
    print("5. 🎬 Render enhanced explainer video (low quality)")
    print("6. 🎬 Render enhanced explainer video (high quality)")
    print()
    print("VOICEOVER & NARRATION:")
    print("A. 🎙️ Generate professional narration audio")
    print("B. 🔊 Install text-to-speech packages")
    print("C. 📝 Generate subtitle files (SRT/VTT)")
    print("D. 🎬 Create video with audio + subtitles")
    print()
    print("SETUP:")
    print("7. 📦 Install basic packages (matplotlib, numpy)")
    print("8. 📦 Install Manim for advanced videos")
    print("9. 🔧 Check system requirements")
    print()
    print("0. ❌ Exit")
    print("="*60)

def check_system():
    """Check system requirements and installed packages"""
    print("\n" + "="*50)
    print("SYSTEM CHECK")
    print("="*50)
    
    # Python version
    check_python_version()
    
    # Check packages
    packages = {
        "matplotlib": "For simple demonstrations",
        "numpy": "For mathematical calculations", 
        "manim": "For advanced video creation",
        "ffmpeg": "For video encoding (part of manim)"
    }
    
    print("\nPackage Status:")
    for package, description in packages.items():
        if check_package(package):
            print(f"✅ {package}: Installed - {description}")
        else:
            print(f"❌ {package}: Not installed - {description}")
    
    # Check if FFmpeg is available (for Manim)
    try:
        subprocess.run(["ffmpeg", "-version"], 
                      capture_output=True, check=True)
        print("✅ FFmpeg: Available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg: Not available (needed for Manim)")
        print("   Install: https://ffmpeg.org/download.html")

def main():
    """Main program loop"""
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (0-9, A, B, C, D): ").strip().upper()
        
        if choice == "0":
            print("Thank you for exploring Einstein's Theory of Relativity!")
            break
            
        elif choice == "1":
            if check_package("matplotlib") and check_package("numpy"):
                run_simple_demo()
            else:
                print("❌ Missing packages. Please install basic packages first (option 7)")
                
        elif choice == "2":
            if check_package("numpy"):
                # Run just the calculator part
                try:
                    exec(open("simple_relativity_demo.py").read())
                except FileNotFoundError:
                    print("❌ simple_relativity_demo.py not found")
            else:
                print("❌ NumPy required. Please install basic packages first (option 7)")
                
        elif choice == "3":
            run_manim_demo("RelativityExplainer", "low")
            
        elif choice == "4":
            run_manim_demo("RelativityExplainer", "high")
            
        elif choice == "5":
            run_manim_demo("EnhancedRelativityExplainer", "low")
            
        elif choice == "6":
            run_manim_demo("EnhancedRelativityExplainer", "high")
            
        elif choice == "7":
            install_basic_packages()
            
        elif choice == "8":
            install_manim()
            
        elif choice == "9":
            check_system()
            
        elif choice == "A":
            generate_narration()
            
        elif choice == "B":
            install_voiceover_packages()
            
        elif choice == "C":
            generate_subtitles()
            
        elif choice == "D":
            create_video_with_subtitles()
            
        else:
            print("❌ Invalid choice. Please enter 0-9, A, B, C, or D.")
        
        if choice != "0":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("Einstein's Theory of Relativity - Quick Start")
    print("=" * 50)
    main()
