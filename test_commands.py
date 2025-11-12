#!/usr/bin/env python3
"""Test script to verify assistant responds to commands."""
import sys
from assistant import AIAssistant
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    """Test assistant with sample commands."""
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Testing Nova AI Assistant Response            ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    try:
        # Initialize assistant (without TTS to avoid audio during testing)
        print(f"{Fore.YELLOW}Initializing assistant...{Style.RESET_ALL}")
        assistant = AIAssistant()
        
        # Disable TTS for testing (optional - comment out if you want to hear responses)
        # assistant.tts.speak = lambda text, print_text=True: print(f"🤖 Nova: {text}") if print_text else None
        
        print(f"{Fore.GREEN}✓ Assistant initialized!{Style.RESET_ALL}\n")
        
        # Test commands
        test_cases = [
            ("hello", True, "Greeting"),
            ("hi nova", True, "Greeting with wake word"),
            ("help", True, "Help command"),
            ("what can you do", True, "Help command variant"),
            ("find file named main.py", True, "File search"),
            ("open Firefox", True, "Open application"),
            ("create folder named TestProjects", True, "Create folder"),
            ("system info", True, "System information"),
            ("system information", True, "System information variant"),
            ("check WiFi", True, "WiFi check"),
            ("check wifi", True, "WiFi check variant"),
            ("search the web for Python tutorials", True, "Web search"),
            ("remind me tomorrow at 10 AM to attend meeting", True, "Reminder"),
            ("take screenshot", True, "Screenshot"),
            ("switch to online mode", True, "Mode switch"),
            ("unknown command xyz", False, "Unknown command"),
        ]
        
        print(f"{Fore.YELLOW}Testing commands...{Style.RESET_ALL}\n")
        
        passed = 0
        failed = 0
        
        for command, should_process, description in test_cases:
            print(f"{Fore.CYAN}Test: {description}{Style.RESET_ALL}")
            print(f"  Command: '{command}'")
            try:
                result = assistant.process_command(command)
                if result == should_process:
                    print(f"  {Fore.GREEN}✓ PASS{Style.RESET_ALL} - Command processed correctly")
                    passed += 1
                else:
                    print(f"  {Fore.RED}✗ FAIL{Style.RESET_ALL} - Expected {should_process}, got {result}")
                    failed += 1
            except Exception as e:
                print(f"  {Fore.RED}✗ ERROR{Style.RESET_ALL} - {e}")
                failed += 1
            print()
        
        # Summary
        print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║              Test Results Summary                ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Passed: {passed}{Style.RESET_ALL}")
        print(f"{Fore.RED}✗ Failed: {failed}{Style.RESET_ALL}")
        print(f"Total: {passed + failed}")
        print(f"Success Rate: {(passed / (passed + failed) * 100):.1f}%")
        
        if failed == 0:
            print(f"\n{Fore.GREEN}🎉 All tests passed! Assistant is working correctly!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}⚠ Some tests failed. Check the output above.{Style.RESET_ALL}")
        
        return 0 if failed == 0 else 1
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

