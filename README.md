# 🌌 Nova AI Assistant – Kali Linux Edition  
**Developed by [Nitin Dhurve](https://github.com/nitinscodehub)**  

> 🧠 An advanced Windows-like AI Assistant built for **Kali Linux** — featuring voice recognition, text-to-speech, automation, and both offline & online modes.  

---

## 🪄 Key Features

- 🎤 **Human-like Voice Chat** — Speak naturally, get smart responses  
- ⚙️ **Task Automation** — Open apps, check Wi-Fi, take screenshots, etc.  
- 🗂️ **File Search** — Find any file via voice or text command  
- 🌐 **Online Web Search** — Uses DuckDuckGo for privacy  
- 🗓️ **Smart Reminders & Calendar** — Stores data in SQLite  
- 🧩 **Dual Mode** — Works **offline** (Vosk) or **online** (Google API)  
- 🛠️ **Auto-Fix** — Installs missing Python libs automatically  
- 🎨 **Customizable Settings** — Edit everything in `settings.json`

---

## ⚙️ Installation Guide

### 🐧 For Linux (Kali Recommended)
```bash
chmod +x setup.sh
./setup.sh

Manual Setup

sudo apt update
sudo apt install -y python3 python3-pip portaudio19-dev python3-pyaudio
sudo apt install -y espeak espeak-data libespeak1 libespeak-dev ffmpeg libasound2-dev
pip3 install -r requirements.txt

🪟 For Windows
setup_windows.bat


Or manual:

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

🚀 Run the Assistant
🔹 On Linux/macOS
./start.sh
# or
python3 main.py

🔹 On Windows
start_windows.bat
# or
venv\Scripts\activate
python main.py

🗣️ Voice Commands Examples
Command	Action
“Find file named notes.txt”	Search for files
“Open Firefox”	Launch an app
“Create folder named Projects”	Make a directory
“Search the web for Python tutorials”	Use online mode
“Remind me tomorrow 10 AM to study”	Add a reminder
“Take screenshot”	Capture screen instantly
“Switch to online mode”	Change recognition engine
⚙️ Configuration (settings.json)

Example:

{
  "mode": "offline",
  "voice_type": "female",
  "voice_speed": 160,
  "wake_word": "nova"
}

📂 Folder Structure
nova project/
├── main.py
├── assistant.py
├── config.py
├── speech_recognition_module.py
├── tts_module.py
├── file_search.py
├── task_automation.py
├── web_search.py
├── calendar_reminder.py
├── error_handler.py
├── setup.sh
├── start.sh
├── requirements.txt
└── settings.json

💡 Modes Overview
📴 Offline Mode

Uses Vosk + pyttsx3

No Internet needed

Works for file, tasks, reminders

🌐 Online Mode

Uses Google Speech API

More accurate

Allows web search

🔧 Troubleshooting

🎙️ Mic not working:

sudo apt install portaudio19-dev python3-pyaudio
arecord -d 5 test.wav


🗣️ TTS issue:

sudo apt install espeak espeak-data
espeak "test"


Speech accuracy low?
➡️ Use online mode
➡️ Speak clearly, reduce noise

🧑‍💻 Author

👤 Nitin Dhurve
🔗 GitHub: @nitinscodehub

📦 Project Repo: Nova AI Assistant

📝 License

Open Source — for educational & personal use.

⭐ Show Some Love

If you like this project, please star the repo 🌟 — it motivates further innovation!


---

Chaahe to mai ye `README.md` file **automatically bana ke** teri repo (`nova-ai-assistant`) me push karwa du (commit message: `Added official README by Nitin Dhurve ✨`).  
Bas bol — **"ready to push"** 🚀
