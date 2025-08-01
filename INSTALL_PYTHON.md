# 🐍 Python Installation Guide

Python is not currently installed on your system. Here's how to install it:

## Windows Installation (Recommended)

### Method 1: Official Python Installer (Easiest)
1. **Download Python**:
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Click "Download Python 3.11.x" (latest version)

2. **Install Python**:
   - Run the downloaded installer
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
   - Click "Install Now"

3. **Verify Installation**:
   - Open Command Prompt (cmd) or PowerShell
   - Type: `python --version`
   - Should show: `Python 3.11.x`

### Method 2: Microsoft Store (Alternative)
1. Open Microsoft Store
2. Search for "Python 3.11"
3. Install the official Python app

### Method 3: Package Manager (Advanced)
If you have Chocolatey or Winget:
```bash
# Using Chocolatey
choco install python

# Using Winget
winget install Python.Python.3.11
```

## After Python Installation

### 1. Verify Installation
Open PowerShell and run:
```bash
python --version
pip --version
```

### 2. Install Required Packages
```bash
# Install basic packages for simple demo
pip install matplotlib numpy

# Install Manim for advanced videos (optional)
pip install manim
```

### 3. Run the Relativity Explainer
```bash
# Navigate to project folder
cd "g:\My Drive\Ait"

# Run quick start
python quick_start.py

# Or run simple demo directly
python simple_relativity_demo.py
```

## What Each Component Does

### 🎬 Simple Demo (Works Immediately)
- **File**: `simple_relativity_demo.py`
- **Requirements**: matplotlib, numpy
- **Features**: Basic animations, interactive calculator
- **Best for**: Quick learning and testing

### 🎥 Professional Videos (Advanced)
- **Files**: `relativity_explainer.py`, `relativity_explainer_enhanced.py`
- **Requirements**: Manim library
- **Features**: High-quality animations, mathematical formulas
- **Best for**: Creating educational videos

## Quick Commands Reference

```bash
# Check if Python is installed
python --version

# Install basic packages
pip install matplotlib numpy

# Install Manim (for professional videos)
pip install manim

# Run interactive menu
python quick_start.py

# Run simple demo directly
python simple_relativity_demo.py

# Create professional video (requires Manim)
manim -pql relativity_explainer.py RelativityExplainer
```

## Troubleshooting

### "Python not found" Error
- Make sure Python is added to PATH during installation
- Restart your terminal/PowerShell after installation
- Try `py` instead of `python`

### Package Installation Issues
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Then install packages
pip install matplotlib numpy
```

### Manim Installation Issues
```bash
# Install dependencies first
pip install --upgrade pip setuptools wheel

# Install Manim
pip install manim

# If still issues, try:
pip install manim[GUI]
```

## Next Steps After Installation

1. **Install Python** (if not done already)
2. **Run**: `python quick_start.py`
3. **Choose option 7** to install basic packages
4. **Choose option 1** to run simple demo
5. **Optional**: Choose option 8 to install Manim for advanced videos

## Alternative: Online Python

If you can't install Python locally, you can run the code online:
- **Google Colab**: colab.research.google.com
- **Replit**: replit.com
- **CodePen**: codepen.io (for JavaScript versions)

Just copy the code from `simple_relativity_demo.py` into any online Python environment!

---

**Happy coding and exploring relativity! 🚀✨**
