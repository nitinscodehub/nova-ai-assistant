# Nova AI Assistant - ChatGPT-like GUI Version

## 🎯 **ChatGPT-like Voice Assistant with Animated Robot Avatar**

Complete desktop AI Assistant with beautiful GUI, animated robot avatar, voice + text input, code generation, and ChatGPT-like responses!

## 🚀 **Quick Start**

### Linux:
```bash
./start_gui.sh
# or
python3 gui_main.py
```

### Windows:
```cmd
start_gui_windows.bat
# or
python gui_main.py
```

## ✨ **Features**

### 1. **Animated Robot Avatar** 🤖
- Real-time animation based on state (idle, listening, speaking, thinking)
- GIF animation support (if robot*.gif available)
- Emoji fallback animation
- Visual feedback for all actions

### 2. **ChatGPT-like Chat Interface** 💬
- Beautiful message bubbles with timestamps
- User messages (blue, right-aligned)
- Assistant messages (dark, left-aligned)
- Typing animation for responses
- Auto-scroll to latest message
- Full conversation history

### 3. **Voice + Text Hybrid** 🎤
- **Text Input**: Type messages and press Enter
- **Voice Input**: Click "🎙️ Listen" button
- **Wake Word**: Say "Hey Nova" to activate
- Both methods work simultaneously

### 4. **Code Generation & Execution** 💻
- **Natural Language**: "Generate a Python program for calculator"
- **Auto-Generation**: Code generated automatically
- **Formatted Display**: Code shown in syntax-highlighted blocks
- **Run Code**: Click "▶️ Run Code" button
- **Safe Execution**: Code runs in sandbox with timeout
- **Output Display**: Results shown in chat

### 5. **OpenAI Integration** 🧠
- ChatGPT-like responses using OpenAI API
- Conversation context awareness
- Natural language understanding
- Code generation using GPT
- Fallback to rule-based when offline

### 6. **Beautiful UI Design** 🎨
- Gradient neon background (blue-purple theme)
- Glowing buttons with hover effects
- Modern chat bubble design
- Professional, clean layout
- Responsive and intuitive

### 7. **Error Handling & Logging** 📝
- Automatic error logging to `logs/assistant.log`
- Self-repair mechanism
- Graceful error messages
- Auto-retry for failed operations

## 📋 **Requirements**

- Python 3.10+
- Tkinter (usually included)
- All packages from `requirements.txt`
- OpenAI API key (optional, for ChatGPT responses)

## ⚙️ **Configuration**

### Settings Window:
1. Click "⚙️ Settings" button
2. Enter OpenAI API key (optional)
3. Select mode (Offline/Online)
4. Click "💾 Save Settings"

### OpenAI API Key:
- Get from: https://platform.openai.com/api-keys
- Optional - works without it (uses fallback responses)
- Enables ChatGPT-like natural responses

## 🎤 **Usage Examples**

### Text Input:
```
Type: "Hello Nova"
Type: "Generate a Python program for calculator"
Type: "Find file named main.py"
Type: "System info"
```

### Voice Input:
```
1. Click "🎙️ Listen" button
2. Say: "Hey Nova, find file named test.txt"
3. Say: "Hey Nova, generate code for hello world"
4. Say: "Hey Nova, open Firefox"
```

### Code Generation:
```
User: "Generate a Python program for calculator"
Nova: [Shows code block with "Run Code" button]
User: [Clicks "Run Code"]
Nova: [Shows execution output]
```

## 🎨 **UI Components**

### Left Panel:
- **Robot Avatar**: Animated robot (🤖/👂/🗣️/💭)
- **Status Label**: Current status
- **🎙️ Listen Button**: Toggle voice listening
- **🧹 Clear Chat**: Clear conversation
- **⚙️ Settings**: Open settings

### Right Panel:
- **Chat Area**: Scrollable message bubbles
- **Input Field**: Type messages here
- **Send Button**: Send message

## 🔧 **Technical Details**

### Code Execution:
- Runs in temporary sandbox directory
- 10-second timeout limit
- Safe subprocess execution
- Output captured and displayed

### Voice Recognition:
- Offline: Vosk (local)
- Online: Google Speech API
- Continuous listening mode
- Wake word activation

### Text-to-Speech:
- Offline: pyttsx3
- Natural pauses between clauses
- Background speech (non-blocking)

## 📁 **Files**

- `gui_assistant.py` - Main GUI application
- `gui_main.py` - Entry point
- `openai_integration.py` - OpenAI API integration
- `logger.py` - Logging module
- `start_gui.sh` - Linux start script
- `start_gui_windows.bat` - Windows start script

## 🐛 **Troubleshooting**

### GUI doesn't start:
```bash
# Check Tkinter
python3 -c "import tkinter; print('Tkinter OK')"

# Install if missing (Linux)
sudo apt-get install python3-tk
```

### OpenAI errors:
- Check API key in settings
- Verify internet connection
- Falls back to rule-based responses automatically

### Voice not working:
- Check microphone permissions
- Test microphone: `arecord -d 5 test.wav`
- Check audio system

## ✅ **Status: READY TO USE!**

---

**GUI Version: ✅ COMPLETE** 🚀

**Enjoy your ChatGPT-like Voice Assistant!** 🎉

