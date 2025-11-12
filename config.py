"""Configuration manager for the AI Assistant."""
import json
import os
from typing import Dict, Any

class Config:
    """Manages configuration settings."""
    
    def __init__(self, config_file: str = "settings.json"):
        self.config_file = config_file
        self.settings = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
                return self._default_config()
        else:
            return self._default_config()
    
    def save_config(self) -> bool:
        """Save configuration to JSON file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self.settings[key] = value
        self.save_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "mode": "offline",
            "language": "en",
            "voice_type": "female",
            "voice_speed": 150,
            "wake_word": "nova",
            "openai_api_key": "",
            "google_api_key": "",
            "auto_install": True,
            "startup_sound": True,
            "log_level": "INFO",
            "reminder_check_interval": 60,
            "offline_stt": "vosk",
            "offline_tts": "pyttsx3"
        }

