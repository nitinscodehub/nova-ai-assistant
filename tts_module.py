"""Text-to-Speech module supporting offline (pyttsx3) and online modes."""
from typing import Optional
from error_handler import ErrorHandler

class TTSModule:
    """Handles text-to-speech in offline and online modes."""
    
    def __init__(self, config):
        self.config = config
        self.mode = config.get("mode", "offline")
        self.engine = None
        self.voice_speed = config.get("voice_speed", 150)
        self.voice_type = config.get("voice_type", "female")
        self._setup()
    
    def _setup(self):
        """Setup TTS based on mode."""
        if self.mode == "offline":
            self._setup_offline()
        else:
            self._setup_offline()  # Use offline TTS by default for reliability
    
    def _setup_offline(self):
        """Setup pyttsx3 for offline TTS."""
        try:
            ErrorHandler.ensure_package("pyttsx3")
            import pyttsx3
            
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', self.voice_speed)
            
            # Set voice type
            voices = self.engine.getProperty('voices')
            if voices:
                voice_found = False
                if self.voice_type == "female":
                    for voice in voices:
                        if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                            self.engine.setProperty('voice', voice.id)
                            voice_found = True
                            break
                elif self.voice_type == "male":
                    for voice in voices:
                        if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                            self.engine.setProperty('voice', voice.id)
                            voice_found = True
                            break
                
                # If no specific voice found, use default
                if not voice_found and len(voices) > 0:
                    self.engine.setProperty('voice', voices[0].id)
            
            print("✓ Offline TTS ready (pyttsx3)")
        except Exception as e:
            print(f"✗ TTS setup failed: {e}")
    
    def speak(self, text: str, print_text: bool = True) -> None:
        """Speak the given text."""
        if print_text:
            print(f"🤖 Nova: {text}")
        
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS error: {e}")
        else:
            print(f"TTS not available. Would say: {text}")
    
    def set_speed(self, speed: int) -> None:
        """Set speech speed."""
        self.voice_speed = speed
        if self.engine:
            self.engine.setProperty('rate', speed)
        self.config.set("voice_speed", speed)
    
    def set_voice(self, voice_type: str) -> None:
        """Set voice type (male/female)."""
        self.voice_type = voice_type
        self.config.set("voice_type", voice_type)
        self._setup_offline()

