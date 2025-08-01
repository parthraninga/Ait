"""
Setup and Installation Guide for Relativity Explainer Video

This script helps you set up the environment and provides instructions
for creating the Einstein's Theory of Relativity explainer video.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def check_manim_installation():
    """Check if Manim is properly installed"""
    try:
        import manim
        print(f"✅ Manim version {manim.__version__} is installed")
        return True
    except ImportError:
        print("❌ Manim is not installed")
        return False

def create_output_directory():
    """Create output directory for videos"""
    output_dir = "output_videos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Created output directory: {output_dir}")
    else:
        print(f"✅ Output directory already exists: {output_dir}")

def display_instructions():
    """Display instructions for using the script"""
    print("\n" + "="*60)
    print("EINSTEIN'S RELATIVITY EXPLAINER VIDEO")
    print("="*60)
    print("\nHow to create your video:")
    print("\n1. Basic video (low quality, fast render):")
    print("   manim -pql relativity_explainer.py RelativityExplainer")
    
    print("\n2. High quality video:")
    print("   manim -pqh relativity_explainer.py RelativityExplainer")
    
    print("\n3. 4K quality video:")
    print("   manim -pqk relativity_explainer.py RelativityExplainer")
    
    print("\n4. Calculator scene:")
    print("   manim -pql relativity_explainer.py RelativityCalculator")
    
    print("\n5. Render without preview:")
    print("   manim -ql relativity_explainer.py RelativityExplainer")
    
    print("\nQuality flags:")
    print("  -pql = preview, low quality (480p)")
    print("  -pqm = preview, medium quality (720p)")
    print("  -pqh = preview, high quality (1080p)")
    print("  -pqk = preview, 4K quality (2160p)")
    
    print("\nOutput files will be saved in the 'media' folder")
    print("\nFor more options, run: manim --help")
    print("="*60)

def main():
    """Main setup function"""
    print("Setting up Einstein's Theory of Relativity Explainer...")
    
    # Install requirements
    if not install_requirements():
        print("Setup failed. Please install requirements manually.")
        return
    
    # Check Manim installation
    if not check_manim_installation():
        print("Please install Manim manually: pip install manim")
        return
    
    # Create output directory
    create_output_directory()
    
    # Display instructions
    display_instructions()
    
    print("\n✅ Setup complete! You can now create your relativity explainer video.")

if __name__ == "__main__":
    main()
