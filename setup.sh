#!/bin/bash

# Nova AI Assistant - Setup Script for Kali Linux/Debian

echo "=========================================="
echo "Nova AI Assistant - Setup"
echo "=========================================="

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "Python 3 not found! Please install Python 3.10+"; exit 1; }

# Install system dependencies
echo ""
echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    portaudio19-dev \
    espeak \
    ffmpeg \
    python3-tk

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Download Vosk model (optional)
echo ""
echo "Vosk model setup (optional)..."
echo "To use offline speech recognition, download a Vosk model:"
echo "  wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
echo "  unzip vosk-model-small-en-us-0.15.zip"

# Create necessary directories
echo ""
echo "Creating directories..."
mkdir -p logs assets

# Make scripts executable
echo ""
echo "Making scripts executable..."
chmod +x main.py
chmod +x setup.sh

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "To run Nova AI Assistant:"
echo "  source venv/bin/activate"
echo "  python3 main.py"
echo ""
echo "Or use the start script:"
echo "  ./start.sh"
echo ""
