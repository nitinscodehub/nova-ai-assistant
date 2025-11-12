#!/usr/bin/env python3
"""Test script for Nova AI Assistant."""
import sys
from assistant import AIAssistant
from colorama import Fore, Style, init

init(autoreset=True)

def test_assistant():
    """Test the assistant with sample commands."""
    print(f"{Fore.CYAN}Testing Nova AI Assistant...{Style.RESET_ALL}\n")
    
    try:
        # Initialize assistant
        assistant = AIAssistant()
        print(f"\n{Fore.GREEN}✓ Assistant initialized successfully!{Style.RESET_ALL}\n")
        
        # Test commands
        test_commands = [
            "hello",
            "help",
            "find file named test",
            "open Firefox",
            "create folder named TestFolder",
            "system info",
            "check WiFi",
            "search the web for Python",
        ]
        
        print(f"{Fore.YELLOW}Testing voice commands...{Style.RESET_ALL}\n")
        
        for command in test_commands:
            print(f"{Fore.CYAN}Testing: '{command}'{Style.RESET_ALL}")
            try:
                result = assistant.process_command(command)
                if result:
                    print(f"{Fore.GREEN}✓ Command processed: {command}{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.YELLOW}⚠ Command not recognized: {command}{Style.RESET_ALL}\n")
            except Exception as e:
                print(f"{Fore.RED}✗ Error processing command '{command}': {e}{Style.RESET_ALL}\n")
        
        print(f"{Fore.GREEN}✓ Testing complete!{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Note: This is a test run. For voice commands, run: python3 main.py{Style.RESET_ALL}\n")
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error initializing assistant: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_assistant()

