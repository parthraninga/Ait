@echo off
echo 🎬 Creating Einstein's Relativity Video with Audio
echo ================================================

echo.
echo 📦 Installing required packages...
pip install edge-tts

echo.
echo 🎵 Generating video with embedded audio...
python -m manim -pql relativity_audio_fixed.py RelativityWithRealAudio

echo.
echo ✅ Done! Your video with audio is ready!
echo 📁 Check the media\videos folder for your final video file.
echo.
pause
