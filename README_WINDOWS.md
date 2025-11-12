# Nova AI Assistant - Windows Support ✅

## 🪟 Windows पर काम करता है! (Works on Windows!)

Nova AI Assistant अब **Windows, Linux, और macOS** सभी platforms पर काम करता है!

## 🚀 Quick Start (Windows)

### Step 1: Python Install करें
1. Python 3.10+ download करें: https://www.python.org/downloads/
2. Install करते समय **"Add Python to PATH"** check करें
3. Install complete करें

### Step 2: Project Setup
```cmd
# Project folder में जाएं
cd "path\to\nova project"

# Setup script run करें
setup_windows.bat
```

### Step 3: Start Assistant
```cmd
# Start script use करें
start_windows.bat

# या manually
venv\Scripts\activate.bat
python main.py
```

## ✅ Windows पर Working Features

- ✅ **Voice Recognition** - Offline (Vosk) और Online (Google Speech API)
- ✅ **Text-to-Speech** - Windows SAPI (built-in voices)
- ✅ **File Search** - Windows paths में search करता है
- ✅ **Task Automation** - Windows apps open करता है (Chrome, Calculator, Notepad, etc.)
- ✅ **Web Search** - DuckDuckGo (online mode)
- ✅ **Calendar & Reminders** - SQLite database
- ✅ **System Information** - CPU, Memory, Disk usage
- ✅ **WiFi Check** - Windows netsh command use करता है
- ✅ **Screenshots** - Pillow/pyautogui use करता है

## 🎤 Windows Voice Commands

- **"nova open Chrome"** - Chrome browser open करता है
- **"nova open Calculator"** - Calculator open करता है
- **"nova open Notepad"** - Notepad open करता है
- **"nova open File Manager"** - File Explorer open करता है
- **"nova find file named example.txt"** - File search करता है
- **"nova search the web for Python"** - Web search करता है
- **"nova take screenshot"** - Screenshot लेता है
- **"nova check WiFi"** - WiFi status check करता है

## 🔧 Windows-Specific Features

### Applications:
- **Chrome/Edge**: Browser open करता है
- **Calculator**: Windows Calculator
- **Notepad**: Text editor
- **File Manager**: Windows Explorer
- **VS Code**: Code editor
- **Spotify/Discord**: अगर installed हो तो

### Screenshots:
- Windows पर screenshots लेने के लिए `Pillow` या `pyautogui` install होना चाहिए
- Setup script automatically install कर देगा

### WiFi Check:
- Windows पर `netsh wlan show interfaces` command use होता है
- Automatically detect करता है

## 📝 Configuration (Windows)

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

## 🐛 Troubleshooting (Windows)

### Problem 1: Microphone not working
**Solution:**
- Windows Settings > Privacy > Microphone में microphone access enable करें
- Microphone को test करें

### Problem 2: PyAudio installation failed
**Solution:**
- Windows पर PyAudio optional है
- Online mode use करें (Google Speech API)
- Ya Windows Speech Recognition use करें

### Problem 3: Screenshot not working
**Solution:**
```cmd
pip install pillow pyautogui
```

### Problem 4: Permission errors
**Solution:**
- Command Prompt को "Run as Administrator" में open करें
- Ya user permissions check करें

## 📋 Requirements (Windows)

- Python 3.10+
- Microphone (voice commands के लिए)
- Internet connection (first time setup और online mode के लिए)
- Windows 10/11 (recommended)

## 🎯 Installation (Windows)

### Option 1: Automated Setup
```cmd
setup_windows.bat
```

### Option 2: Manual Setup
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

## ✅ Cross-Platform Support

Nova AI Assistant अब **3 platforms** पर काम करता है:

1. **Windows** ✅ - Full support
2. **Linux** ✅ - Full support (Kali Linux tested)
3. **macOS** ✅ - Full support

## 🚀 Features Comparison

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| Voice Recognition | ✅ | ✅ | ✅ |
| Text-to-Speech | ✅ (SAPI) | ✅ (espeak) | ✅ (say) |
| File Search | ✅ | ✅ | ✅ |
| Task Automation | ✅ | ✅ | ✅ |
| Web Search | ✅ | ✅ | ✅ |
| Calendar | ✅ | ✅ | ✅ |
| Screenshots | ✅ (Pillow) | ✅ (gnome-screenshot) | ✅ (screencapture) |
| WiFi Check | ✅ (netsh) | ✅ (iwconfig) | ✅ (networksetup) |

## 📞 Support

अगर कोई problem आए तो:
1. `WINDOWS_SETUP.md` file check करें
2. `instructions.txt` file check करें
3. Error messages carefully read करें
4. Windows Settings में microphone permissions check करें

## 🎉 Enjoy!

**Nova AI Assistant अब Windows पर भी काम करता है!** 🚀

---

**Windows Support: ✅ Ready!**

