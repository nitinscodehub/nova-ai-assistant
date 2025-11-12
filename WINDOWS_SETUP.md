# Nova AI Assistant - Windows Setup Guide

## 🪟 Windows पर कैसे Install करें (How to Install on Windows)

### Requirements (जरूरी चीजें):

1. **Python 3.10+** - [Download here](https://www.python.org/downloads/)
2. **Microphone** - Voice commands के लिए
3. **Internet Connection** - First time setup के लिए

### Installation Steps (Installation Steps):

#### Step 1: Python Install करें
1. Python 3.10+ download करें: https://www.python.org/downloads/
2. Install करते समय **"Add Python to PATH"** checkbox को check करें
3. "Install Now" पर click करें

#### Step 2: Project Setup
1. Project folder को extract करें
2. `setup_windows.bat` file को double-click करें
3. Ya manually command prompt में:

```cmd
cd "path\to\nova project"
setup_windows.bat
```

#### Step 3: Manual Installation (अगर script काम नहीं करे)
```cmd
# Virtual environment create करें
python -m venv venv

# Virtual environment activate करें
venv\Scripts\activate.bat

# Dependencies install करें
pip install -r requirements.txt

# Windows-specific packages
pip install pillow pyautogui
```

#### Step 4: Start Assistant
```cmd
# Option 1: Start script use करें
start_windows.bat

# Option 2: Manually
venv\Scripts\activate.bat
python main.py
```

## 🎤 Voice Commands (Windows पर)

Windows पर भी सभी voice commands काम करेंगे:

- **File Search**: "nova find file named example.txt"
- **Open Apps**: "nova open Chrome"
- **Create Folders**: "nova create folder named Projects"
- **Web Search**: "nova search the web for Python tutorials"
- **Reminders**: "nova remind me tomorrow at 10 AM to attend meeting"
- **System Info**: "nova show system information"
- **WiFi Check**: "nova check WiFi"
- **Screenshot**: "nova take screenshot"
- **Help**: "nova help"

## 🪟 Windows-Specific Features

### Applications (Apps):
- **Chrome**: "nova open Chrome"
- **Edge**: "nova open Edge"
- **Calculator**: "nova open Calculator"
- **Notepad**: "nova open Notepad"
- **File Manager**: "nova open File Manager"
- **VS Code**: "nova open VS Code"

### Screenshots:
- Windows पर screenshots लेने के लिए `Pillow` ya `pyautogui` install होना चाहिए
- Automatically install हो जाएगा setup script के दौरान

### WiFi Check:
- Windows पर WiFi status check करने के लिए `netsh` command use होता है
- Automatically detect हो जाएगा

## ⚙️ Configuration (Settings)

`settings.json` file में settings customize करें:

```json
{
    "mode": "offline",
    "language": "en",
    "voice_type": "female",
    "voice_speed": 150,
    "wake_word": "nova"
}
```

## 🐛 Troubleshooting (समस्या का समाधान)

### Problem 1: Python not found
**Solution:**
- Python को PATH में add करें
- Ya Python installer में "Add Python to PATH" option check करें

### Problem 2: Microphone not working
**Solution:**
- Windows Settings > Privacy > Microphone में microphone access enable करें
- Microphone को test करें: Settings > System > Sound > Test microphone

### Problem 3: Speech recognition not accurate
**Solution:**
- Online mode use करें (better accuracy के लिए)
- `settings.json` में `"mode": "online"` set करें
- Internet connection check करें

### Problem 4: Screenshot not working
**Solution:**
```cmd
pip install pillow pyautogui
```

### Problem 5: Permission errors
**Solution:**
- Command Prompt को "Run as Administrator" में open करें
- Ya user permissions check करें

## 📝 Notes (नोट्स)

1. **Virtual Environment**: Virtual environment use करना recommended है
2. **Microphone**: Windows Settings में microphone permissions enable करें
3. **Offline Mode**: Offline mode में भी काम करेगा (Vosk model use करके)
4. **Online Mode**: Better accuracy के लिए online mode use करें
5. **TTS**: Windows पर pyttsx3 SAPI use करता है (built-in Windows voices)

## ✅ Windows पर Working Features

- ✓ Voice recognition (offline/online)
- ✓ Text-to-speech (Windows SAPI)
- ✓ File search
- ✓ Task automation (open apps, create folders)
- ✓ Web search (online mode)
- ✓ Calendar & Reminders
- ✓ System information
- ✓ WiFi status check
- ✓ Screenshots (with Pillow/pyautogui)

## 🚀 Quick Start (Windows)

1. **Download Python 3.10+**: https://www.python.org/downloads/
2. **Run setup_windows.bat**: Double-click करें
3. **Start assistant**: `start_windows.bat` या `python main.py`
4. **Say "nova"**: Followed by your command

## 📞 Support

अगर कोई problem आए तो:
1. `instructions.txt` file check करें
2. Error messages carefully read करें
3. Internet connection verify करें
4. Python version check करें: `python --version`

---

**Enjoy using Nova AI Assistant on Windows! 🚀**

