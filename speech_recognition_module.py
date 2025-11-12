"""Speech recognition module supporting offline (Vosk) and online (Google) modes."""
import os
import json
from typing import Optional, Callable
from error_handler import ErrorHandler

class SpeechRecognitionModule:
    """Handles speech recognition in offline and online modes."""
    
    def __init__(self, config):
        self.config = config
        self.mode = config.get("mode", "offline")
        self.vosk_model = None
        self.recognizer = None
        self.microphone = None
        self._setup()
    
    def _setup(self):
        """Setup speech recognition based on mode."""
        if self.mode == "offline":
            self._setup_offline()
        else:
            try:
                self._setup_online()
            except Exception as e:
                print(f"⚠ Online setup failed: {e}, falling back to offline mode")
                self.mode = "offline"
                self._setup_offline()
    
    def _setup_offline(self):
        """Setup Vosk for offline speech recognition."""
        try:
            ErrorHandler.ensure_package("vosk")
            import vosk
            
            # Download model if not exists
            model_path = "vosk-model-small-en-us-0.15"
            if not os.path.exists(model_path):
                print("Downloading Vosk model... This may take a while.")
                import urllib.request
                import zipfile
                model_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
                zip_path = "vosk-model.zip"
                urllib.request.urlretrieve(model_url, zip_path)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(".")
                os.remove(zip_path)
            
            if os.path.exists(model_path):
                self.vosk_model = vosk.Model(model_path)
                print("✓ Offline speech recognition ready (Vosk)")
            else:
                print("⚠ Vosk model not found, falling back to online mode")
                self.mode = "online"
                self._setup_online()
        except Exception as e:
            print(f"⚠ Offline setup failed: {e}, falling back to online mode")
            self.mode = "online"
            self._setup_online()
    
    def _setup_online(self):
        """Setup Google Speech Recognition for online mode."""
        import platform  # Import at function start, before try block
        try:
            ErrorHandler.ensure_package("SpeechRecognition")
            import speech_recognition as sr
            
            self.recognizer = sr.Recognizer()
            
            # Windows पर microphone setup अलग हो सकता है
            try:
                self.microphone = sr.Microphone()
                # Adjust for ambient noise
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
            except Exception as mic_error:
                # Windows पर microphone access issue हो सकता है
                if platform.system().lower() == "windows":
                    print(f"⚠ Microphone setup warning: {mic_error}")
                    print("⚠ Make sure microphone is enabled in Windows Settings > Privacy > Microphone")
                self.microphone = sr.Microphone()  # Try to initialize anyway
            
            print("✓ Online speech recognition ready (Google)")
        except Exception as e:
            print(f"✗ Speech recognition setup failed: {e}")
            if platform.system().lower() == "windows":
                print("💡 Tip: Make sure microphone permissions are enabled in Windows Settings")
    
    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """Listen for speech and return transcribed text."""
        if self.mode == "offline" and self.vosk_model:
            return self._listen_offline(timeout, phrase_time_limit)
        else:
            return self._listen_online(timeout, phrase_time_limit)
    
    def _listen_offline(self, timeout: int, phrase_time_limit: int) -> Optional[str]:
        """Listen using Vosk (offline)."""
        try:
            import vosk
            import pyaudio
            
            rec = vosk.KaldiRecognizer(self.vosk_model, 16000)
            rec.SetWords(True)
            
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
            stream.start_stream()
            
            print("🎤 Listening... (offline mode)")
            frames = []
            silent_frames = 0
            max_silent_frames = 20
            
            for _ in range(0, int(16000 / 8000 * phrase_time_limit)):
                data = stream.read(8000, exception_on_overflow=False)
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    if result.get("text"):
                        stream.stop_stream()
                        stream.close()
                        p.terminate()
                        return result["text"]
                else:
                    partial = json.loads(rec.PartialResult())
                    if partial.get("partial"):
                        print(f"Partial: {partial['partial']}")
            
            # Final result
            result = json.loads(rec.FinalResult())
            stream.stop_stream()
            stream.close()
            p.terminate()
            
            return result.get("text") if result.get("text") else None
        except Exception as e:
            print(f"Offline listening error: {e}")
            return None
    
    def _listen_online(self, timeout: int, phrase_time_limit: int) -> Optional[str]:
        """Listen using Google Speech Recognition (online)."""
        try:
            import speech_recognition as sr
            
            if not self.recognizer or not self.microphone:
                self._setup_online()
            
            try:
                with self.microphone as source:
                    print("🎤 Listening... (online mode)")
                    audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                try:
                    text = self.recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    # Could not understand audio - this is normal
                    return None
                except sr.RequestError as e:
                    print(f"Speech recognition error: {e}")
                    return None
            except sr.WaitTimeoutError:
                # Timeout is normal in continuous listening
                return None
        except Exception as e:
            # Only print non-timeout errors
            if "timeout" not in str(e).lower():
                print(f"Online listening error: {e}")
            return None
    
    def continuous_listen(self, callback: Callable[[str], None], wake_word: Optional[str] = None):
        """Continuously listen for commands."""
        wake_word = wake_word or self.config.get("wake_word", "nova")
        print(f"🔄 Continuous listening mode active. Say '{wake_word}' followed by your command.")
        
        while True:
            try:
                text = self.listen(timeout=2, phrase_time_limit=8)
                if text:
                    text_lower = text.lower().strip()
                    wake_lower = wake_word.lower()
                    
                    # Check if wake word is at the start
                    if text_lower.startswith(wake_lower):
                        # Remove wake word from command
                        command = text_lower[len(wake_lower):].strip()
                        if command:
                            callback(command)
                    elif wake_lower in text_lower:
                        # Wake word found anywhere, extract command after it
                        parts = text_lower.split(wake_lower, 1)
                        if len(parts) > 1:
                            command = parts[1].strip()
                            if command:
                                callback(command)
                    elif wake_word == "" or wake_word is None:
                        # If no wake word specified, process all commands
                        callback(text)
            except KeyboardInterrupt:
                break
            except Exception as e:
                error_msg = str(e).lower()
                # Ignore timeout errors - they're normal in continuous listening
                if "timeout" not in error_msg and "wait" not in error_msg:
                    # Only print non-timeout errors
                    if "timeout" not in error_msg:
                        print(f"Error in continuous listen: {e}")
                # Continue listening even on error
                continue

