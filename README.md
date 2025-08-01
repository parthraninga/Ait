# Einstein's Theory of Relativity Explainer Video

An educational Python project that creates animated explainer videos about Einstein's Theory of Relativity using the Manim (Mathematical Animation Engine) library.

## 🎯 Project Overview

This project creates comprehensive animated videos explaining:
- **Special Relativity**: Time dilation, length contraction, and relativistic effects
- **General Relativity**: Spacetime curvature and gravitational effects  
- **E=mc²**: Mass-energy equivalence
- **Real-world Applications**: GPS, particle accelerators, nuclear energy
- **Historical Context**: Einstein's revolutionary discoveries

## 🚀 Features

### Basic Version (`relativity_explainer.py`)
- Core concepts of relativity
- Mathematical formulas with animations
- Time dilation and length contraction demonstrations
- Spacetime curvature visualization

### Enhanced Version (`relativity_explainer_enhanced.py`)
- Comprehensive narration and explanations
- Historical context and timeline
- Twin paradox demonstration
- Real-world applications (GPS, particle accelerators, etc.)
- Modern implications and future technologies

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- Windows/macOS/Linux
- At least 4GB RAM (8GB recommended for high-quality rendering)
- Graphics card with OpenGL support (recommended)

### Python Dependencies
```
manim>=0.18.0
numpy>=1.21.0
matplotlib>=3.5.0
scipy>=1.7.0
pillow>=8.3.0
opencv-python>=4.5.0
pydub>=0.25.0 (optional, for audio)
```

## 🛠️ Installation

### Method 1: Automatic Setup
1. Clone or download this project
2. Run the setup script:
   ```bash
   python setup.py
   ```

### Method 2: Manual Installation
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Manim:
   ```bash
   pip install manim
   ```

### Additional Dependencies (Platform-specific)

#### Windows
- Install Microsoft Visual C++ Build Tools
- Install FFmpeg: `choco install ffmpeg` (with Chocolatey)

#### macOS
- Install with Homebrew: `brew install ffmpeg`

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

## 🎬 Usage

### Quick Start
```bash
# Render basic version (low quality, fast)
manim -pql relativity_explainer.py RelativityExplainer

# Render enhanced version (low quality, fast)
manim -pql relativity_explainer_enhanced.py EnhancedRelativityExplainer
```

### Quality Options
```bash
# Low quality (480p) - fastest rendering
manim -pql relativity_explainer.py RelativityExplainer

# Medium quality (720p)
manim -pqm relativity_explainer.py RelativityExplainer

# High quality (1080p) - recommended for final output
manim -pqh relativity_explainer.py RelativityExplainer

# 4K quality (2160p) - best quality, slowest rendering
manim -pqk relativity_explainer.py RelativityExplainer
```

### Command Options
- `-p` = Preview video after rendering
- `-q` = Quality settings (l=low, m=medium, h=high, k=4K)
- `--fps` = Set frame rate (default: 30)
- `--format` = Output format (mp4, mov, avi, etc.)

### Render Specific Scenes
```bash
# Render only the calculator scene
manim -pql relativity_explainer.py RelativityCalculator

# Render multiple scenes
manim -pql relativity_explainer.py RelativityExplainer RelativityCalculator
```

## 📁 Project Structure
```
relativity_explainer/
├── relativity_explainer.py          # Basic version
├── relativity_explainer_enhanced.py # Enhanced version with narration
├── requirements.txt                  # Python dependencies
├── setup.py                         # Automated setup script
├── README.md                        # This file
├── media/                           # Generated video files (created after rendering)
│   ├── videos/
│   ├── images/
│   └── texts/
└── output_videos/                   # Custom output directory
```

## 🎨 Customization

### Modifying Content
1. **Add new scenes**: Create new methods in the class
2. **Change animations**: Modify the `construct()` method
3. **Adjust timing**: Change `self.wait()` durations
4. **Modify colors**: Use Manim color constants (RED, BLUE, etc.)

### Example: Adding a New Scene
```python
def custom_scene(self):
    """Your custom explanation"""
    title = Text("My Custom Topic", font_size=36, color=BLUE)
    self.play(Write(title))
    # Add your animations here
```

### Changing Video Settings
```python
# In your scene class
def construct(self):
    self.camera.background_color = "#001122"  # Dark blue background
    # Your scene content
```

## 🎵 Adding Audio/Narration

### Method 1: External Audio
1. Record narration separately
2. Use video editing software to combine with rendered video

### Method 2: Programmatic Audio (Advanced)
```python
# Add to your scene
self.add_sound("path/to/audio.wav")
```

## 🐛 Troubleshooting

### Common Issues

#### "Module not found" errors
```bash
pip install manim
# or
pip install --upgrade manim
```

#### FFmpeg not found
- **Windows**: Install FFmpeg and add to PATH
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

#### Slow rendering
- Use lower quality settings (`-ql`)
- Reduce video complexity
- Close other applications
- Use SSD storage

#### Memory issues
- Render shorter scenes separately
- Reduce video quality
- Increase system virtual memory

### Performance Tips
1. **Start with low quality** for testing
2. **Use background rendering** for long videos
3. **Cache common objects** to speed up rendering
4. **Split long videos** into shorter segments

## 📚 Learning Resources

### Manim Documentation
- [Official Manim Documentation](https://docs.manim.community/)
- [Manim Tutorial](https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/)

### Relativity Resources
- [Einstein's Original Papers](https://www.gutenberg.org/ebooks/30155)
- [Stanford Encyclopedia of Philosophy: Special Relativity](https://plato.stanford.edu/entries/spacetime-supertasks/)
- [NASA: Einstein's Relativity](https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-the-theory-of-relativity-k4.html)

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Add new scenes or improve existing ones
3. Submit a pull request

### Ideas for Contributions
- Add more real-world examples
- Improve visual effects
- Add interactive elements
- Create shorter topic-specific videos
- Add audio narration
- Translate to other languages

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning and teaching.

## 🙏 Acknowledgments

- **Albert Einstein** - For revolutionizing our understanding of space and time
- **Grant Sanderson (3Blue1Brown)** - For creating Manim
- **Manim Community** - For maintaining and improving the library

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review Manim documentation
3. Search for solutions in Manim community forums

---

**Happy animating! 🎬✨**

*"Imagination is more important than knowledge." - Albert Einstein*
