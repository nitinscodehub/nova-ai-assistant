Nova AI Assistant – Kali Linux Edition

Developed by Nitin Dhurve

🧠 A complete Windows-like Basic AI Assistant built specially for Kali Linux, featuring offline + online modes, voice recognition, text-to-speech, task automation, and more.

🚀 Features

🎤 Human-like Voice Conversation – Realistic speech recognition & TTS

📁 File Search – Search files in directories with voice commands

⚙️ Task Automation – Open apps, check WiFi, take screenshots, etc.

🌐 Web Search – Online browsing via DuckDuckGo

📅 Calendar & Reminders – Smart reminder system with SQLite

🔌 Offline + Online Modes – Switch anytime

🛠️ Self-Error Resolution – Auto-install missing dependencies

⚙️ Fully Configurable – Modify settings in settings.json

🧩 Requirements

Kali Linux, Debian, Windows 10/11, or macOS

Python 3.10+

Microphone

Internet (for online mode)

⚙️ Installation
🔸 Linux (Kali)
chmod +x setup.sh
./setup.sh
# Manual setup
sudo apt-get update
sudo apt-get install -y python3 python3-pip portaudio19-dev python3-pyaudio
sudo apt-get install -y espeak espeak-data libespeak1 libespeak-dev ffmpeg libasound2-dev
pip3 install -r requirements.txt

🔹 Windows
setup_windows.bat
# Manual install
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pip install pillow pyautogui

🔸 macOS
brew install python3 portaudio
pip3 install -r requirements.txt

▶️ Usage
Start Assistant

Windows:

start_windows.bat
# or
venv\Scripts\activate.bat
python main.py


Linux/macOS:

./start.sh
# or
python3 main.py

🗣️ Example Commands
Command	Action
“Find file named notes.txt”	Search file
“Open Firefox”	Launch app
“Create folder named Projects”	Make directory
“Search the web for Python tutorials”	Web search
“Remind me tomorrow 10 AM to attend meeting”	Add reminder
“Show system information”	Display system info
“Take screenshot”	Capture screen
“Switch to online mode”	Change speech mode
⚙️ Configuration

Edit settings.json to customize:

{
  "mode": "offline",
  "voice_type": "female",
  "voice_speed": 160,
  "wake_word": "nova"
}

📂 Project Structure
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
├── settings.json
├── setup.sh
├── start.sh
├── requirements.txt
└── instructions.txt

🎛️ Modes
🔸 Offline Mode

Uses Vosk + pyttsx3

No internet needed

Works for: File search, reminders, system tasks

🔹 Online Mode

Uses Google Speech API

Requires internet

Best accuracy & response

🧠 Self-Fix & Error Handling

Nova checks for missing libraries or mic errors and auto-fixes them.
If something breaks → restart with:

python3 main.py --repair

🐛 Troubleshooting

Microphone not working:

sudo apt-get install portaudio19-dev python3-pyaudio
arecord -d 5 test.wav


TTS not working:

sudo apt-get install espeak espeak-data
espeak "test"


Speech not accurate:

Use online mode

Reduce noise

Speak clearly

📝 License

Open Source — Free for educational and personal use.

🤝 Author & Credits

👨‍💻 Developed by Nitin Dhurve

💬 Project Repo: Nova AI Assistant – Kali Edition

❤️ Support

For detailed setup or help, check instructions.txt in the repo.
