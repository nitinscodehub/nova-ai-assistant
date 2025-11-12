# Nova AI Assistant - Kali Linux Edition

A complete Windows-like Basic AI Assistant for Kali Linux, featuring both offline and online modes with voice recognition, text-to-speech, file search, task automation, web search, and calendar/reminder functionality.

## 🚀 Features

- **🎤 Human-like Voice Conversation**: Natural speech recognition and text-to-speech
- **📁 File Search**: Search files in local directories using voice commands
- **⚙️ Task Automation**: Open applications, create folders, check WiFi, take screenshots
- **🌐 Web Search**: Search the web using DuckDuckGo (online mode)
- **📅 Calendar & Reminders**: Manage reminders with SQLite database
- **🔌 Offline & Online Modes**: Works offline with Vosk or online with Google Speech API
- **🛠️ Self-Error Resolution**: Auto-installs missing packages
- **⚙️ Configurable**: Customize settings via settings.json

## 📋 Requirements

- **Windows 10/11**, **Linux** (Kali Linux, Debian-based), or **macOS**
- Python 3.10+
- Microphone (for voice input)
- Internet connection (for first-time setup and online mode)

## 🔧 Installation

### Windows Installation

```cmd
# Quick Install
setup_windows.bat

# Manual Install
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pip install pillow pyautogui
```

### Linux Installation

```bash
# Quick Install
chmod +x setup.sh
./setup.sh

# Manual Install
sudo apt-get update
sudo apt-get install -y python3 python3-pip portaudio19-dev python3-pyaudio
sudo apt-get install -y espeak espeak-data libespeak1 libespeak-dev
sudo apt-get install -y ffmpeg libasound2-dev
pip3 install -r requirements.txt
```

### macOS Installation

```bash
# Install dependencies
brew install python3 portaudio

# Install Python packages
pip3 install -r requirements.txt
```

## 🎯 Usage

### Start the Assistant

**Windows:**
```cmd
start_windows.bat
# Or manually
venv\Scripts\activate.bat
python main.py
```

**Linux/macOS:**
```bash
./start.sh
# Or manually
python3 main.py
```

### Voice Commands

- **File Search**: "Find file named example.txt"
- **Open Apps**: "Open Firefox"
- **Create Folders**: "Create folder named Projects"
- **Web Search**: "Search the web for Python tutorials"
- **Reminders**: "Remind me tomorrow at 10 AM to attend meeting"
- **System Info**: "Show system information"
- **WiFi Check**: "Check WiFi"
- **Screenshot**: "Take screenshot"
- **Mode Switch**: "Switch to online mode" or "Switch to offline mode"

### Configuration

Edit `settings.json` to customize:

- **Mode**: "offline" or "online"
- **Voice Type**: "male" or "female"
- **Voice Speed**: 100-200
- **Wake Word**: Default is "nova"

## 📁 Project Structure

```
nova project/
├── main.py                      # Main entry point
├── assistant.py                 # Main assistant class
├── config.py                    # Configuration manager
├── speech_recognition_module.py # Speech recognition
├── tts_module.py                # Text-to-speech
├── file_search.py               # File search functionality
├── task_automation.py           # OS-level automation
├── web_search.py                # Web search (DuckDuckGo)
├── calendar_reminder.py         # Reminders & calendar
├── error_handler.py             # Auto-install & error handling
├── settings.json                # Configuration file
├── requirements.txt             # Python dependencies
├── setup.sh                     # Setup script
├── start.sh                     # Start script
└── instructions.txt             # Detailed instructions
```

## 🎤 Modes

### Offline Mode (Default)

- Uses Vosk for speech recognition
- Uses pyttsx3 for text-to-speech
- No internet required
- Works for file search, task automation, reminders

### Online Mode

- Uses Google Speech API for better accuracy
- Web search available
- Requires internet connection
- Better speech recognition

## 🐛 Troubleshooting

### Microphone not working
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
arecord -d 5 test.wav  # Test microphone
```

### Speech recognition not accurate
- Switch to online mode for better accuracy
- Speak clearly and reduce background noise
- Check internet connection (for online mode)

### TTS not working
```bash
sudo apt-get install espeak espeak-data
espeak "test"  # Test TTS
```

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please check `instructions.txt` for detailed documentation.

---

**Enjoy using Nova AI Assistant! 🚀**

