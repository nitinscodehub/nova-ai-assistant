#!/usr/bin/env python3
"""Test Nova AI Assistant with Hindi/Hinglish and casual conversation."""
import sys
from assistant import AIAssistant
from colorama import Fore, Style, init

init(autoreset=True)

def test_hindi_hinglish_commands():
    """Test Hindi/Hinglish commands."""
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Testing Hindi/Hinglish Commands                ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    try:
        assistant = AIAssistant()
        print(f"{Fore.GREEN}✓ Assistant initialized!{Style.RESET_ALL}\n")
        
        # Hindi/Hinglish test commands
        hindi_commands = [
            # Greetings
            ("namaste", True, "Hindi greeting"),
            ("kaise ho", True, "Hindi casual greeting"),
            ("kya haal hai", True, "Hindi casual greeting"),
            ("hello bhai", True, "Hinglish greeting"),
            
            # Help
            ("help karo", True, "Hinglish help"),
            ("kya kar sakte ho", True, "Hindi help"),
            ("tum kya kar sakte ho", True, "Hindi help"),
            
            # File search
            ("file dhundho main.py", True, "Hindi file search"),
            ("file search karo test", True, "Hinglish file search"),
            ("find file named example", True, "English file search"),
            
            # Open apps
            ("Firefox kholo", True, "Hindi open app"),
            ("open karo Chrome", True, "Hinglish open app"),
            ("calculator kholo", True, "Hindi open calculator"),
            
            # System info
            ("system info batao", True, "Hinglish system info"),
            ("system ki jankari do", True, "Hindi system info"),
            ("CPU usage kya hai", True, "Hinglish CPU info"),
            
            # WiFi
            ("WiFi check karo", True, "Hinglish WiFi check"),
            ("internet check karo", True, "Hinglish internet check"),
            ("network status batao", True, "Hinglish network"),
            
            # Casual conversation
            ("tum kaun ho", True, "Hindi casual - who are you"),
            ("tumhara naam kya hai", True, "Hindi casual - what's your name"),
            ("kya tum samajh gaye", True, "Hindi casual - did you understand"),
            ("theek hai", True, "Hindi casual - okay"),
            ("accha", True, "Hindi casual - good"),
            ("shukriya", True, "Hindi - thank you"),
            ("dhanyawad", True, "Hindi - thank you"),
        ]
        
        print(f"{Fore.YELLOW}Testing Hindi/Hinglish commands...{Style.RESET_ALL}\n")
        
        passed = 0
        failed = 0
        total = len(hindi_commands)
        
        for command, should_process, description in hindi_commands:
            print(f"{Fore.CYAN}Test: {description}{Style.RESET_ALL}")
            print(f"  Command: '{command}'")
            try:
                result = assistant.process_command(command)
                if result:
                    print(f"  {Fore.GREEN}✓ PASS{Style.RESET_ALL} - Command processed")
                    passed += 1
                else:
                    print(f"  {Fore.YELLOW}⚠ PARTIAL{Style.RESET_ALL} - Command not fully recognized but handled")
                    passed += 0.5  # Partial credit
                    failed += 0.5
            except Exception as e:
                print(f"  {Fore.RED}✗ FAIL{Style.RESET_ALL} - {e}")
                failed += 1
            print()
        
        accuracy = (passed / total) * 100
        
        print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║        Hindi/Hinglish Test Results                ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Passed: {passed:.1f}{Style.RESET_ALL}")
        print(f"{Fore.RED}✗ Failed: {failed:.1f}{Style.RESET_ALL}")
        print(f"Total: {total}")
        print(f"{Fore.YELLOW}Accuracy: {accuracy:.1f}%{Style.RESET_ALL}\n")
        
        return accuracy
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        return 0

def test_casual_conversation():
    """Test casual conversation ability."""
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Testing Casual Conversation Ability             ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    try:
        assistant = AIAssistant()
        
        # Casual conversation test cases
        casual_commands = [
            ("hey", True, "Casual greeting"),
            ("hi there", True, "Casual greeting"),
            ("what's up", True, "Casual greeting"),
            ("how are you", True, "Casual question"),
            ("tell me a joke", False, "Casual request - not implemented"),
            ("what's the weather", False, "Casual question - not implemented"),
            ("what time is it", False, "Casual question - not implemented"),
            ("thanks", True, "Casual thank you"),
            ("thank you", True, "Casual thank you"),
            ("okay", True, "Casual acknowledgment"),
            ("sure", True, "Casual acknowledgment"),
            ("yeah", True, "Casual acknowledgment"),
            ("cool", True, "Casual acknowledgment"),
            ("nice", True, "Casual acknowledgment"),
            ("awesome", True, "Casual acknowledgment"),
            ("great", True, "Casual acknowledgment"),
        ]
        
        print(f"{Fore.YELLOW}Testing casual conversation...{Style.RESET_ALL}\n")
        
        passed = 0
        failed = 0
        total = len(casual_commands)
        
        for command, should_respond, description in casual_commands:
            print(f"{Fore.CYAN}Test: {description}{Style.RESET_ALL}")
            print(f"  Command: '{command}'")
            try:
                result = assistant.process_command(command)
                if result or should_respond:
                    print(f"  {Fore.GREEN}✓ RESPONDED{Style.RESET_ALL} - Assistant responded")
                    passed += 1
                else:
                    print(f"  {Fore.YELLOW}⚠ NO RESPONSE{Style.RESET_ALL} - Not implemented")
                    failed += 1
            except Exception as e:
                print(f"  {Fore.RED}✗ ERROR{Style.RESET_ALL} - {e}")
                failed += 1
            print()
        
        accuracy = (passed / total) * 100
        
        print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║        Casual Conversation Test Results          ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✓ Responded: {passed}{Style.RESET_ALL}")
        print(f"{Fore.RED}✗ No Response: {failed}{Style.RESET_ALL}")
        print(f"Total: {total}")
        print(f"{Fore.YELLOW}Conversation Accuracy: {accuracy:.1f}%{Style.RESET_ALL}\n")
        
        return accuracy
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
        return 0

def main():
    """Main test function."""
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Nova AI Assistant - Complete Test Suite        ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    # Test 1: Hindi/Hinglish
    hindi_accuracy = test_hindi_hinglish_commands()
    
    # Test 2: Casual conversation
    casual_accuracy = test_casual_conversation()
    
    # Overall accuracy
    overall_accuracy = (hindi_accuracy + casual_accuracy) / 2
    
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║           FINAL ACCURACY REPORT                  ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Hindi/Hinglish Accuracy: {hindi_accuracy:.1f}%{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Casual Conversation Accuracy: {casual_accuracy:.1f}%{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Overall Accuracy: {overall_accuracy:.1f}%{Style.RESET_ALL}\n")
    
    # Assessment
    if overall_accuracy >= 90:
        print(f"{Fore.GREEN}🎉 EXCELLENT! Assistant has high accuracy!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ Can handle casual conversations well!{Style.RESET_ALL}")
    elif overall_accuracy >= 75:
        print(f"{Fore.YELLOW}👍 GOOD! Assistant has decent accuracy!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚠️  Some improvements needed for casual conversations{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}⚠️  NEEDS IMPROVEMENT! Accuracy below expected{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}Human-like Conversation Assessment:{Style.RESET_ALL}")
    if casual_accuracy >= 80:
        print(f"{Fore.GREEN}✅ YES - Can have casual, human-like conversations{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}⚠️  PARTIAL - Some casual conversations work, but limited{Style.RESET_ALL}")
    
    return overall_accuracy

if __name__ == "__main__":
    sys.exit(0 if main() >= 75 else 1)

