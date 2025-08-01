@echo off
title Einstein's Relativity Explainer - Quick Start

echo ================================================
echo EINSTEIN'S THEORY OF RELATIVITY EXPLAINER
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo.
    echo Please install Python first:
    echo 1. Go to https://python.org/downloads/
    echo 2. Download and install Python 3.8 or higher  
    echo 3. Make sure to check "Add Python to PATH"
    echo 4. Restart this script after installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version

echo.
echo Checking for required packages...

REM Check if matplotlib is installed
python -c "import matplotlib" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing matplotlib and numpy...
    python -m pip install matplotlib numpy
    if %errorlevel% neq 0 (
        echo ❌ Failed to install packages
        pause
        exit /b 1
    )
    echo ✅ Basic packages installed
) else (
    echo ✅ matplotlib is available
)

echo.
echo Starting Einstein's Relativity Explainer...
echo.

REM Run the quick start script
python quick_start.py

echo.
echo Thank you for exploring relativity!
pause
