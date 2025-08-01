# 🎙️ Adding Professional Voiceover to Your Relativity Videos

## Quick Start Guide

### Step 1: Install Voiceover Packages
```bash
# Option 1: Use the quick start menu
python quick_start.py
# Then choose option "B" to install voiceover packages

# Option 2: Install manually
pip install edge-tts pygame pydub

# Option 3: Use the dedicated installer
python install_voiceover.py
```

### Step 2: Generate Audio Files
```bash
# Generate all narration audio files
python generate_narration.py
```

This creates professional MP3 files in the `audio/` folder:
- `title_intro.mp3` - Opening narration
- `special_relativity_intro.mp3` - Special relativity explanation
- `time_dilation.mp3` - Time dilation narration
- `energy_mass.mp3` - E=mc² explanation
- And more...

### Step 3: Add Audio to Your Manim Videos

#### Method 1: Manual Sync (Recommended for beginners)
```python
from manim import *

class RelativityWithVoiceover(Scene):
    def construct(self):
        # Add sound at the beginning of each section
        self.add_sound("audio/title_intro.mp3")
        
        # Your title animation here
        title = Text("Einstein's Theory of Relativity")
        self.play(Write(title))
        self.wait(4)  # Wait for audio to finish
        self.clear()
        
        # Next section
        self.add_sound("audio/special_relativity_intro.mp3")
        # Your special relativity animation...
```

#### Method 2: Use the Pre-built Voiceover Class
```python
# Use the enhanced script with built-in voiceover
manim -pql relativity_explainer_with_voiceover.py VoiceoverRelativityExplainer
```

## Voice Options

You can customize the voice in `generate_narration.py`:

```python
# Available voices:
self.voice = "en-US-AriaNeural"      # Female, clear (default)
self.voice = "en-US-GuyNeural"       # Male, professional  
self.voice = "en-GB-SoniaNeural"     # British female
self.voice = "en-AU-NatashaNeural"   # Australian female

# Adjust speed and volume:
self.rate = "+0%"     # Normal speed (-50% to +100%)
self.volume = "+0%"   # Normal volume (-50% to +50%)
```

## Audio Timing Guide

Each narration segment is timed for specific parts:

| Audio File | Duration | Use For |
|------------|----------|---------|
| `title_intro.mp3` | ~8 seconds | Opening title sequence |
| `special_relativity_intro.mp3` | ~12 seconds | Postulates explanation |
| `time_dilation.mp3` | ~15 seconds | Clock animation |
| `time_dilation_formula.mp3` | ~8 seconds | Formula explanation |
| `length_contraction.mp3` | ~12 seconds | Ruler demonstration |
| `energy_mass.mp3` | ~15 seconds | E=mc² explanation |
| `spacetime_curvature.mp3` | ~18 seconds | General relativity |
| `conclusion.mp3` | ~20 seconds | Final thoughts |

## Troubleshooting

### "edge_tts not found"
```bash
pip install edge-tts
```

### "No internet connection"
Edge TTS requires internet to generate audio. Once generated, audio files work offline.

### Audio not syncing with video
Adjust the `self.wait()` times in your Manim script to match audio duration.

### Poor audio quality
Try different voices or adjust volume/rate settings in `generate_narration.py`.

## Advanced Tips

### 1. Custom Narration Text
Edit the narration text in `generate_narration.py`:
```python
narrations = {
    "title_intro": "Your custom introduction text here...",
    # ... other sections
}
```

### 2. Multiple Languages
Change the voice to support different languages:
```python
self.voice = "es-ES-ElviraNeural"  # Spanish
self.voice = "fr-FR-DeniseNeural"  # French
self.voice = "de-DE-KatjaNeural"   # German
```

### 3. Background Music
Use audio editing software to add background music to the generated narration files.

### 4. Professional Production
For broadcast-quality results:
1. Generate high-quality Manim videos (`-pqh` or `-pqk`)
2. Use consistent audio levels
3. Add subtle background music
4. Export final video in high resolution

## File Structure After Setup
```
your_project/
├── audio/                    # Generated audio files
│   ├── title_intro.mp3
│   ├── special_relativity_intro.mp3
│   └── ...
├── generate_narration.py     # Audio generator script
├── relativity_explainer.py  # Original video script
├── relativity_explainer_with_voiceover.py  # Enhanced with voice
└── quick_start.py           # Menu system
```

## Example Complete Workflow

1. **Setup**: `python quick_start.py` → Option B (install packages)
2. **Generate Audio**: `python quick_start.py` → Option A (generate narration)
3. **Create Video**: `manim -pql relativity_explainer_with_voiceover.py VoiceoverRelativityExplainer`
4. **Result**: Professional video with synchronized narration!

---

🎬 **Ready to create your narrated relativity video?** 

Start with: `python quick_start.py` and follow the menu!
