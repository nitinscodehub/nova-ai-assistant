"""Main AI Assistant module that coordinates all features."""
import re
from typing import Optional
from config import Config
from speech_recognition_module import SpeechRecognitionModule
from tts_module import TTSModule
from file_search import FileSearch
from task_automation import TaskAutomation
from web_search import WebSearch
from calendar_reminder import CalendarReminder
from error_handler import ErrorHandler
from colorama import Fore, Style, init

init(autoreset=True)

class AIAssistant:
    """Main AI Assistant class."""
    
    def __init__(self):
        print(f"{Fore.CYAN}Initializing Nova AI Assistant...{Style.RESET_ALL}")
        
        # Initialize configuration
        self.config = Config()
        
        # Initialize modules
        self.speech_recognition = SpeechRecognitionModule(self.config)
        self.tts = TTSModule(self.config)
        self.file_search = FileSearch()
        self.task_automation = TaskAutomation()
        self.web_search = WebSearch(self.config)
        self.calendar = CalendarReminder(tts_callback=self.tts.speak)
        
        # Conversation state (for continuity)
        self.conversation_history = []  # Last 3 turns
        self.last_command = None
        self.last_response = None
        self.retry_count = 0
        self.max_retries = 3
        
        # Startup sound
        if self.config.get("startup_sound", True):
            self._play_startup_sound()
        
        print(f"{Fore.GREEN}✓ Nova AI Assistant ready!{Style.RESET_ALL}")
        self._speak_naturally("Hello! I'm Nova, your AI assistant. How can I help you today?")
    
    def _play_startup_sound(self):
        """Play startup sound."""
        try:
            import sys
            # Simple beep
            sys.stdout.write('\a')
            sys.stdout.flush()
        except:
            pass
    
    def _speak_naturally(self, text: str, print_text: bool = True):
        """Speak with natural pauses and emphasis."""
        if print_text:
            print(f"🤖 Nova: {text}")
        
        # Add natural pauses in speech
        if self.tts.engine:
            try:
                # Break into clauses for natural pauses
                import re
                clauses = re.split(r'[.!?]', text)
                for i, clause in enumerate(clauses):
                    clause = clause.strip()
                    if clause:
                        self.tts.engine.say(clause)
                        # Add micro-pause between clauses (except last)
                        if i < len(clauses) - 1:
                            self.tts.engine.say("...")
                self.tts.engine.runAndWait()
            except Exception as e:
                # Fallback to simple speak
                self.tts.speak(text, print_text=False)
        else:
            print(f"TTS not available. Would say: {text}")
    
    def _add_to_history(self, command: str, response: str):
        """Add to conversation history (keep last 3 turns)."""
        self.conversation_history.append({"command": command, "response": response})
        if len(self.conversation_history) > 3:
            self.conversation_history.pop(0)
    
    def _get_contextual_response(self, base_response: str, follow_up: bool = True):
        """Create multi-part, human-like response with follow-ups."""
        import random
        
        # Main response
        response = base_response
        
        # Add natural connectors and follow-ups - more varied and human-like
        if follow_up:
            follow_ups = [
                " Aur agar kuch aur chahiye to batao, main yahan hi hoon.",
                " Phir bhi koi sawaal ho to pooch sakte ho, koi baat nahi.",
                " Yaad rahe, main yahan hi hoon help ke liye, bas bulao.",
                " Kuch aur bhi chahiye? Bas bol do.",
                " Aur batao? Main ready hoon.",
                " Agar kuch aur help chahiye ho to batao.",
                " Koi aur kaam hai? Main yahan hi hoon.",
            ]
            response += random.choice(follow_ups)
        
        return response
    
    def _handle_error_with_retry(self, operation, error_msg: str, max_retries: int = 3):
        """Handle errors with automatic retry and self-heal."""
        for attempt in range(max_retries):
            try:
                result = operation()
                if result:
                    self.retry_count = 0
                    return result
            except Exception as e:
                if attempt < max_retries - 1:
                    import time
                    time.sleep(0.5)  # Brief pause before retry
                    continue
                else:
                    # After max retries, provide helpful message
                    self._speak_naturally(
                        f"Oops, thoda glitch hua — {error_msg}. "
                        f"3 baar try kiya, abhi fix nahi kar paaya. "
                        f"Kya aap manually check kar sakte ho? Ya phir thoda baad try karein."
                    )
                    return None
        return None
    
    def process_command(self, command: str) -> bool:
        """Process a voice command with human-like behavior."""
        if not command:
            return False
        
        command_lower = command.lower().strip()
        print(f"\n{Fore.YELLOW}Command: {command}{Style.RESET_ALL}")
        
        # Check for continuity/resume
        if self.last_command and "continue" in command_lower or "resume" in command_lower:
            if self.last_response:
                self._speak_naturally(f"Wapas — jahan chhoda tha: {self.last_response}. Continue karte hain.")
                return True
        
        # Update history
        self.last_command = command
        self.last_response = None  # Will be set after processing
        
        # File search (English + Hindi/Hinglish)
        file_search_phrases = [
            "find file", "search file", "file named", "file dhundho",
            "file search karo", "file khojo", "file find karo"
        ]
        if any(phrase in command_lower for phrase in file_search_phrases):
            self._handle_file_search(command)
            return True
        
        # Task automation - Open application (English + Hindi/Hinglish)
        open_phrases = [
            "open", "kholo", "open karo", "start karo", "launch karo"
        ]
        if any(phrase in command_lower for phrase in open_phrases):
            self._handle_open_application(command)
            return True
        
        # Task automation - Create folder
        if "create folder" in command_lower or "make folder" in command_lower:
            self._handle_create_folder(command)
            return True
        
        # Web search
        if "search the web" in command_lower or "search for" in command_lower or "google" in command_lower:
            self._handle_web_search(command)
            return True
        
        # Reminder
        if "remind me" in command_lower or "reminder" in command_lower:
            self._handle_reminder(command)
            return True
        
        # System info (English + Hindi/Hinglish)
        system_info_phrases = [
            "system info", "system information", "system ki jankari",
            "system info batao", "system status", "system ka haal"
        ]
        if any(phrase in command_lower for phrase in system_info_phrases):
            self._handle_system_info()
            return True
        
        # WiFi check (English + Hindi/Hinglish)
        wifi_phrases = [
            "wifi", "wi-fi", "network", "internet", "wifi check karo",
            "internet check karo", "network status", "network batao"
        ]
        if any(phrase in command_lower for phrase in wifi_phrases):
            self._handle_wifi_check()
            return True
        
        # Screenshot
        if "screenshot" in command_lower or "take screenshot" in command_lower:
            self._handle_screenshot()
            return True
        
        # Change mode
        if "switch to offline" in command_lower or "go offline" in command_lower:
            self._handle_mode_switch("offline")
            return True
        
        if "switch to online" in command_lower or "go online" in command_lower:
            self._handle_mode_switch("online")
            return True
        
        # Greeting (English + Hindi/Hinglish) - Multi-part response
        greeting_words = [
            "hello", "hi", "hey", "good morning", "good afternoon",
            "namaste", "namaskar", "kaise ho", "kya haal hai", 
            "hello bhai", "hi bhai", "hey bhai"
        ]
        if any(word in command_lower for word in greeting_words):
            import random
            responses = [
                "Hey! Kaise ho bhai? Main Nova hoon, tumhara AI assistant. Main file search kar sakta hoon, apps open kar sakta hoon, web search bhi kar sakta hoon, aur bhi bahut kuch. Batao kya chahiye?",
                "Namaste! Kaise ho? Main Nova hoon. Dekho, main tumhari madad kar sakta hoon — files dhundh sakta hoon, apps khol sakta hoon, system info bhi de sakta hoon. Kya karna hai?",
                "Hi! Main Nova. Tumhara personal AI assistant. Dekho, main bahut kuch kar sakta hoon — files search, apps open, system info, web search, sab kuch. Kya help chahiye?",
                "Hello! Main Nova hoon. Accha, tumhari kaise madad kar sakta hoon? Main files dhundh sakta hoon, apps khol sakta hoon, ya koi aur kaam bhi ho sakta hai. Batao kya karna hai?"
            ]
            response = random.choice(responses)
            self._speak_naturally(self._get_contextual_response(response))
            self._add_to_history(command, response)
            return True
        
        # Help (English + Hindi/Hinglish)
        help_phrases = [
            "help", "what can you do", "kya kar sakte ho", 
            "tum kya kar sakte ho", "help karo", "madad chahiye"
        ]
        if any(phrase in command_lower for phrase in help_phrases):
            self._handle_help()
            return True
        
        # Casual conversation responses - More human-like, natural
        casual_responses = {
            "thanks": "Arre koi baat nahi bhai! Kuch aur chahiye to bas bol do, main yahan hi hoon.",
            "thank you": "Welcome yaar! Main yahan hi hoon agar kuch aur help chahiye ho to.",
            "shukriya": "Koi baat nahi dost! Aur kuch chahiye? Bas batao.",
            "dhanyawad": "Welcome! Main yahan hi hoon agar kuch aur chahiye ho to batao.",
            "okay": "Accha theek hai! Samajh gaya. Kuch aur?",
            "ok": "Theek hai bhai! Continue karte hain, batao kya karna hai.",
            "sure": "Perfect! Main ready hoon, batao kya karna hai.",
            "yeah": "Awesome! Phir batao kya karna hai, main ready hoon.",
            "cool": "Thanks yaar! Glad I could help. Aur kuch chahiye?",
            "nice": "Glad you liked it bhai! Aur kuch chahiye to batao.",
            "awesome": "Thanks! Happy to help. Kuch aur?",
            "great": "Great! Main yahan hi hoon agar kuch aur chahiye to bas bol do.",
            "tum kaun ho": "Arre main Nova hoon bhai, tumhara AI assistant! Main files search kar sakta hoon, apps open kar sakta hoon, aur bhi bahut kuch. Kya help chahiye?",
            "tumhara naam kya hai": "Mera naam Nova hai! Main tumhara personal AI assistant hoon. Kaise help kar sakta hoon?",
            "kya tum samajh gaye": "Haan bhai, bilkul samajh gaya! Main ready hoon. Batao kya karna hai?",
            "theek hai": "Theek hai! Phir batao kya karna hai, main ready hoon.",
            "accha": "Accha! Samajh gaya. Continue karte hain?",
            "haan": "Accha! Phir batao kya karna hai.",
            "nahi": "Theek hai, koi baat nahi. Agar kuch aur chahiye ho to batao.",
        }
        
        for phrase, response in casual_responses.items():
            if phrase in command_lower:
                self._speak_naturally(self._get_contextual_response(response, follow_up=False))
                self._add_to_history(command, response)
                return True
        
        # Unknown command - Infer intention or ask clarification only if 2+ interpretations
        # Try to infer from context
        if self.conversation_history:
            last_context = self.conversation_history[-1]
            # If last command was about files, maybe this is related
            if "file" in last_context.get("command", "").lower():
                inferred_response = "File search ke baare mein baat kar rahe ho? File ka naam batao, main dhundh dunga."
                self._speak_naturally(self._get_contextual_response(inferred_response))
                self._add_to_history(command, inferred_response)
                return True
        
        # Only ask clarification if truly unclear - more human-like
        unknown_responses = [
            "Hmm, thoda unclear laga bhai. Shayad yeh karna chahte ho — file search, app open, ya kuch aur? 'help' bolkar sab commands dekh sakte ho.",
            "Arre samajh nahi aaya exactly. Kya yeh file search hai, ya app open karna hai? 'help' bolkar options dekh sakte ho.",
            "Thoda unclear tha yaar. Dekho, main file search kar sakta hoon, apps open kar sakta hoon, system info bhi de sakta hoon, aur bhi bahut kuch. 'help' bolkar sab dekh sakte ho."
        ]
        import random
        self._speak_naturally(random.choice(unknown_responses))
        self._add_to_history(command, "unknown")
        return False
    
    def _handle_file_search(self, command: str):
        """Handle file search command with auto-retry and helpful follow-ups."""
        command_lower = command.lower()
        
        # Extract filename from command (English + Hindi/Hinglish)
        patterns = [
            r"file named (.+)",
            r"find file (.+)",
            r"search file (.+)",
            r"file (.+)",
            r"file dhundho (.+)",
            r"file search karo (.+)",
            r"file khojo (.+)",
            r"file find karo (.+)",
            r"dhundho (.+)",
        ]
        
        filename = None
        for pattern in patterns:
            match = re.search(pattern, command_lower)
            if match:
                filename = match.group(1).strip()
                # Remove Hindi words that might be in the filename
                filename = filename.replace("ko", "").replace("se", "").strip()
                break
        
        if not filename:
            # Infer likely intention - check if there's any word that could be a filename
            words = command_lower.split()
            for word in words:
                if '.' in word or len(word) > 3:
                    filename = word
                    break
            
            if not filename:
                self._speak_naturally("Konsi file dhundhni hai? File ka naam batao, main search kar dunga.")
                return
        
        # Auto-retry file search with error handling
        def search_operation():
            return self.file_search.search_file(filename)
        
        results = self._handle_error_with_retry(
            search_operation,
            "file search mein issue aaya",
            max_retries=3
        )
        
        if results:
            message = f"Arre haan, mil gaya bhai! {len(results)} file(s) mili. Yahan results hain, dekh lo."
            self._speak_naturally(self._get_contextual_response(message))
            print(self.file_search.format_results(results))
            self.last_response = message
            self._add_to_history(command, message)
        else:
            # Try alternate search paths automatically
            alt_results = self.file_search.search_in_current_directory(filename)
            if alt_results:
                message = f"Main directory mein mili! {len(alt_results)} file(s) yahan mili."
                self._speak_naturally(self._get_contextual_response(message))
                print(self.file_search.format_results(alt_results))
            else:
                message = (
                    f"File nahi mili — main alternate locations bhi check kar chuka hoon. "
                    f"Shayad file different location mein hai, ya naam thoda alag ho sakta hai. "
                    f"Kya aap exact path ya folder ka naam de sakte ho?"
                )
                self._speak_naturally(self._get_contextual_response(message))
            self.last_response = message
            self._add_to_history(command, message)
    
    def _handle_open_application(self, command: str):
        """Handle open application command with natural response."""
        command_lower = command.lower()
        # Extract app name
        app_name = command_lower.replace("open", "").replace("kholo", "").replace("open karo", "").replace("start karo", "").strip()
        if self.task_automation.open_application(app_name):
            response = f"Opening {app_name} for you! Thoda wait karo, app open ho rahi hai."
            self._speak_naturally(self._get_contextual_response(response))
            self.last_response = response
            self._add_to_history(command, response)
        else:
            response = (
                f"Sorry, {app_name} open nahi kar paaya. "
                f"Shayad app installed nahi hai, ya koi issue hai. "
                f"Kya aap manually check kar sakte ho?"
            )
            self._speak_naturally(self._get_contextual_response(response))
            self.last_response = response
            self._add_to_history(command, response)
    
    def _handle_create_folder(self, command: str):
        """Handle create folder command."""
        # Extract folder name
        patterns = [
            r"folder named (.+)",
            r"folder (.+)",
            r"named (.+)"
        ]
        
        folder_name = None
        for pattern in patterns:
            match = re.search(pattern, command.lower())
            if match:
                folder_name = match.group(1).strip()
                break
        
        if not folder_name:
            folder_name = command.lower().replace("create folder", "").replace("make folder", "").strip()
        
        if folder_name:
            if self.task_automation.create_folder(folder_name):
                self.tts.speak(f"Created folder {folder_name} successfully!")
            else:
                self.tts.speak(f"Sorry, I couldn't create the folder {folder_name}.")
        else:
            self.tts.speak("What should I name the folder?")
    
    def _handle_web_search(self, command: str):
        """Handle web search command."""
        # Extract query
        patterns = [
            r"search the web for (.+)",
            r"search for (.+)",
            r"google (.+)"
        ]
        
        query = None
        for pattern in patterns:
            match = re.search(pattern, command.lower())
            if match:
                query = match.group(1).strip()
                break
        
        if not query:
            query = command.lower().replace("search the web", "").replace("search for", "").replace("google", "").strip()
        
        if query:
            results = self.web_search.search(query)
            summary = self.web_search.get_summary(query)
            self.tts.speak(summary)
            print(self.web_search.format_results(results))
        else:
            self.tts.speak("What should I search for?")
    
    def _handle_reminder(self, command: str):
        """Handle reminder command."""
        # Extract reminder details
        reminder_text = command.lower().replace("remind me", "").strip()
        
        # Parse time
        reminder_time = self.calendar.parse_reminder_time(reminder_text)
        
        if reminder_time:
            # Extract title
            title = reminder_text.split("to")[-1].strip() if "to" in reminder_text else "Reminder"
            self.calendar.add_reminder(title, reminder_time)
            self.tts.speak(f"Got it! I'll remind you about {title} at {reminder_time.strftime('%I:%M %p')}.")
        else:
            self.tts.speak("I couldn't understand the time. Try saying something like 'remind me tomorrow at 10 AM to attend meeting'.")
    
    def _handle_system_info(self):
        """Handle system info command with natural multi-part response."""
        def get_info():
            return self.task_automation.get_system_info()
        
        info = self._handle_error_with_retry(
            get_info,
            "system info fetch karne mein",
            max_retries=2
        )
        
        if info and "error" not in info:
            message = (
                f"Dekho, system status: CPU {info['cpu_percent']:.1f} percent use ho raha hai, "
                f"Memory {info['memory_percent']:.1f} percent, aur Disk {info['disk_percent']:.1f} percent. "
                f"Overall system theek lag raha hai bhai."
            )
            self._speak_naturally(self._get_contextual_response(message))
            print(f"{Fore.GREEN}System Info:{Style.RESET_ALL}")
            print(f"  CPU: {info['cpu_percent']}%")
            print(f"  Memory: {info['memory_percent']}%")
            print(f"  Disk: {info['disk_percent']}%")
            print(f"  Platform: {info['platform']}")
            self.last_response = message
            self._add_to_history(self.last_command, message)
        else:
            self._speak_naturally(
                "Sorry, system info fetch nahi kar paaya. Thoda baad try karein, ya manually check kar sakte ho."
            )
    
    def _handle_wifi_check(self):
        """Handle WiFi check command."""
        wifi_info = self.task_automation.check_wifi()
        status = wifi_info.get("status", "unknown")
        if status == "connected":
            self.tts.speak("WiFi is connected!")
        elif status == "disconnected":
            self.tts.speak("WiFi is disconnected.")
        else:
            self.tts.speak("I couldn't check the WiFi status.")
    
    def _handle_screenshot(self):
        """Handle screenshot command."""
        if self.task_automation.take_screenshot():
            self.tts.speak("Screenshot taken successfully!")
        else:
            self.tts.speak("Sorry, I couldn't take a screenshot. Make sure you have a screenshot tool installed.")
    
    def _handle_mode_switch(self, mode: str):
        """Handle mode switch."""
        self.config.set("mode", mode)
        self.tts.speak(f"Switched to {mode} mode.")
        print(f"{Fore.GREEN}Mode switched to: {mode}{Style.RESET_ALL}")
    
    def _handle_help(self):
        """Handle help command with natural multi-part response."""
        help_text = """
        I can help you with:
        - File search: "Find file named example.txt"
        - Open applications: "Open Firefox"
        - Create folders: "Create folder named Projects"
        - Web search: "Search the web for Python tutorials"
        - Reminders: "Remind me tomorrow at 10 AM to attend meeting"
        - System info: "Show system information"
        - WiFi check: "Check WiFi"
        - Screenshot: "Take screenshot"
        - Switch modes: "Switch to online mode" or "Switch to offline mode"
        """
        response = "Here's what I can do for you! Main files search kar sakta hoon, apps open kar sakta hoon, folders bana sakta hoon, aur bhi bahut kuch. Details niche hain."
        self._speak_naturally(self._get_contextual_response(response))
        print(help_text)
        self.last_response = response
        self._add_to_history(self.last_command, response)
    
    def run(self, mode: str = "continuous"):
        """Run the assistant with both voice and text input."""
        import threading
        
        if mode == "continuous":
            print(f"{Fore.CYAN}🔄 Continuous mode active!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}You can:{Style.RESET_ALL}")
            print(f"  - Say 'Hey Nova' followed by your command (voice)")
            print(f"  - Type your command and press Enter (text)")
            print(f"  - Type 'exit' or 'quit' to stop\n")
            
            # Start voice listening in background thread
            def voice_listen():
                try:
                    self.speech_recognition.continuous_listen(
                        callback=self.process_command,
                        wake_word=self.config.get("wake_word", "nova")
                    )
                except Exception as e:
                    print(f"{Fore.RED}Voice listening error: {e}{Style.RESET_ALL}")
            
            voice_thread = threading.Thread(target=voice_listen, daemon=True)
            voice_thread.start()
            
            # Text input in main thread
            try:
                while True:
                    try:
                        user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
                        if not user_input:
                            continue
                        
                        # Check for exit commands
                        if user_input.lower() in ["exit", "quit", "stop", "bye"]:
                            print(f"{Fore.CYAN}Shutting down...{Style.RESET_ALL}")
                            self.shutdown()
                            break
                        
                        # Process text command
                        self.process_command(user_input)
                    except EOFError:
                        break
                    except KeyboardInterrupt:
                        print(f"\n{Fore.CYAN}Shutting down...{Style.RESET_ALL}")
                        self.shutdown()
                        break
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        else:
            # Single command mode
            while True:
                try:
                    text = self.speech_recognition.listen()
                    if text:
                        self.process_command(text)
                except KeyboardInterrupt:
                    break
    
    def shutdown(self):
        """Shutdown the assistant gracefully."""
        self.tts.speak("Goodbye! Have a great day!")
        print(f"{Fore.CYAN}Nova AI Assistant shutting down...{Style.RESET_ALL}")

