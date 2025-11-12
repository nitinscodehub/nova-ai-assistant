@echo off
REM Nova AI Assistant Setup Script for Windows
REM This script installs all required dependencies

echo ╔══════════════════════════════════════════════════╗
echo ║   Nova AI Assistant - Setup Script (Windows)    ║
echo ╚══════════════════════════════════════════════════╝
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

echo Python found!
python --version

echo.
echo Installing Python packages...

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
python -m pip install -r requirements.txt

REM Install Windows-specific packages for screenshots
python -m pip install pillow pyautogui

echo.
echo Creating Python virtual environment...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

echo.
echo Installing packages in virtual environment...

REM Upgrade pip in venv
python -m pip install --upgrade pip

REM Install requirements in venv
python -m pip install -r requirements.txt

REM Install Windows-specific packages
python -m pip install pillow pyautogui

echo.
echo Setting up Vosk model...
echo Vosk model will be downloaded automatically on first run

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║           Setup Complete! 🎉                     ║
echo ╚══════════════════════════════════════════════════╝
echo.
echo To start the assistant:
echo   1. Activate virtual environment: venv\Scripts\activate.bat
echo   2. Run: python main.py
echo.
echo Or use the start script: start_windows.bat
echo.

pause

