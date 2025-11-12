#!/usr/bin/env python3
"""
Nova AI Assistant - Main Entry Point
Human-like AI assistant with voice and text interaction.
Run with: python3 main.py
"""
import sys
import os
import logging
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Setup logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "assistant.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("NovaAssistant")

def main():
    """Main entry point for Nova AI Assistant."""
    try:
        logger.info("=" * 60)
        logger.info("Nova AI Assistant - Starting...")
        logger.info("=" * 60)
        
        # Import assistant
        try:
            from assistant import AIAssistant
        except ImportError as e:
            logger.error(f"Failed to import assistant: {e}")
            logger.info("Attempting to install missing dependencies...")
            import subprocess
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=False)
            from assistant import AIAssistant
        
        # Create and run assistant
        assistant = AIAssistant()
        logger.info("Nova AI Assistant initialized successfully!")
        
        # Startup greeting
        print("\n" + "=" * 60)
        print("🤖 Nova AI Assistant - Online 💫")
        print("=" * 60)
        print("\nYou can:")
        print("  - Say 'Hey Nova' followed by your command (voice)")
        print("  - Type your command and press Enter (text)")
        print("  - Type 'exit' or 'quit' to stop\n")
        
        # Startup greeting (non-blocking)
        try:
            assistant.tts.speak("Hey! Nova online. Kaise help kar sakta hoon?")
        except:
            pass
        
        # Run in continuous mode (voice + text)
        assistant.run(mode="continuous")
        
    except KeyboardInterrupt:
        logger.info("\nShutting down...")
        print("\n\nShutting down systems, see ya! 👋")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        print(f"\n❌ Error: {e}")
        print("Check logs/assistant.log for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
