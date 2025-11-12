"""Task automation for OS-level operations."""
import os
import subprocess
import platform
import sys
from typing import Optional
from colorama import Fore, Style, init

init(autoreset=True)

class TaskAutomation:
    """Handles OS-level task automation."""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == "windows"
        self.is_linux = self.system == "linux"
        self.is_mac = self.system == "darwin"
    
    def open_application(self, app_name: str) -> bool:
        """Open an application by name."""
        try:
            app_name_lower = app_name.lower()
            
            # Map common app names to commands based on OS
            if self.is_windows:
                app_commands = {
                    "firefox": "firefox",
                    "chrome": "chrome",
                    "browser": "chrome",
                    "edge": "msedge",
                    "terminal": "cmd",
                    "file manager": "explorer",
                    "calculator": "calc",
                    "text editor": "notepad",
                    "vs code": "code",
                    "code": "code",
                    "spotify": "spotify",
                    "discord": "discord",
                    "notepad": "notepad",
                    "paint": "mspaint"
                }
            elif self.is_linux:
                app_commands = {
                    "firefox": "firefox",
                    "chrome": "google-chrome",
                    "browser": "firefox",
                    "terminal": "gnome-terminal",
                    "file manager": "nautilus",
                    "calculator": "gnome-calculator",
                    "text editor": "gedit",
                    "vs code": "code",
                    "code": "code",
                    "spotify": "spotify",
                    "discord": "discord"
                }
            else:  # macOS
                app_commands = {
                    "firefox": "firefox",
                    "chrome": "google-chrome",
                    "browser": "firefox",
                    "terminal": "Terminal",
                    "file manager": "Finder",
                    "calculator": "Calculator",
                    "text editor": "TextEdit",
                    "vs code": "code",
                    "code": "code"
                }
            
            command = app_commands.get(app_name_lower, app_name)
            print(f"{Fore.CYAN}Opening {app_name}...{Style.RESET_ALL}")
            
            if self.is_windows:
                # Windows: use start command or direct executable
                try:
                    subprocess.Popen([command], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except:
                    # Try with start command
                    subprocess.Popen(f"start {command}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.Popen([command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except Exception as e:
            print(f"{Fore.RED}Failed to open {app_name}: {e}{Style.RESET_ALL}")
            return False
    
    def create_folder(self, folder_name: str, path: Optional[str] = None) -> bool:
        """Create a folder."""
        try:
            if path:
                folder_path = os.path.join(path, folder_name)
            else:
                folder_path = os.path.join(os.getcwd(), folder_name)
            
            os.makedirs(folder_path, exist_ok=True)
            print(f"{Fore.GREEN}✓ Created folder: {folder_path}{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}Failed to create folder: {e}{Style.RESET_ALL}")
            return False
    
    def check_wifi(self) -> dict:
        """Check WiFi status."""
        try:
            if self.is_windows:
                # Windows: use netsh command
                result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
                if result.returncode == 0:
                    status = "connected" if "State" in result.stdout and "connected" in result.stdout.lower() else "disconnected"
                    return {
                        "status": status,
                        "details": result.stdout
                    }
                else:
                    return {"status": "unknown", "error": "netsh command failed"}
            elif self.is_linux:
                # Linux: use iwconfig
                result = subprocess.run(['iwconfig'], capture_output=True, text=True)
                wifi_info = {
                    "status": "connected" if "ESSID" in result.stdout else "disconnected",
                    "details": result.stdout
                }
                return wifi_info
            else:
                # macOS: use networksetup
                result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], capture_output=True, text=True)
                status = "connected" if result.returncode == 0 else "disconnected"
                return {"status": status, "details": result.stdout}
        except Exception as e:
            return {"status": "unknown", "error": str(e)}
    
    def take_screenshot(self, filename: Optional[str] = None) -> bool:
        """Take a screenshot."""
        try:
            if not filename:
                from datetime import datetime
                filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            
            if self.is_windows:
                # Windows: try PIL/Pillow first, then pyautogui
                try:
                    from PIL import ImageGrab
                    screenshot = ImageGrab.grab()
                    screenshot.save(filename)
                    print(f"{Fore.GREEN}✓ Screenshot saved: {filename}{Style.RESET_ALL}")
                    return True
                except ImportError:
                    try:
                        import pyautogui
                        screenshot = pyautogui.screenshot()
                        screenshot.save(filename)
                        print(f"{Fore.GREEN}✓ Screenshot saved: {filename}{Style.RESET_ALL}")
                        return True
                    except ImportError:
                        # Fallback to Windows Snipping Tool or PowerShell
                        try:
                            subprocess.run(['powershell', '-Command', f'Add-Type -AssemblyName System.Windows.Forms,System.Drawing; $bounds = [System.Windows.Forms.SystemInformation]::VirtualScreen; $bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height; $graphics = [System.Drawing.Graphics]::FromImage($bmp); $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size); $bmp.Save(\"{filename}\"); $graphics.Dispose(); $bmp.Dispose()'], check=True, capture_output=True)
                            print(f"{Fore.GREEN}✓ Screenshot saved: {filename}{Style.RESET_ALL}")
                            return True
                        except:
                            pass
                print(f"{Fore.RED}No screenshot tool available. Install Pillow or pyautogui: pip install pillow pyautogui{Style.RESET_ALL}")
                return False
            elif self.is_linux:
                # Linux: try different screenshot tools
                commands = [
                    ["gnome-screenshot", "-f", filename],
                    ["scrot", filename],
                    ["import", "-window", "root", filename],
                    ["screencapture", filename]  # Some Linux distros
                ]
                
                for cmd in commands:
                    try:
                        subprocess.run(cmd, check=True, capture_output=True)
                        print(f"{Fore.GREEN}✓ Screenshot saved: {filename}{Style.RESET_ALL}")
                        return True
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue
                
                print(f"{Fore.RED}No screenshot tool available{Style.RESET_ALL}")
                return False
            else:
                # macOS: use screencapture
                try:
                    subprocess.run(['screencapture', filename], check=True, capture_output=True)
                    print(f"{Fore.GREEN}✓ Screenshot saved: {filename}{Style.RESET_ALL}")
                    return True
                except:
                    print(f"{Fore.RED}Failed to take screenshot{Style.RESET_ALL}")
                    return False
        except Exception as e:
            print(f"{Fore.RED}Failed to take screenshot: {e}{Style.RESET_ALL}")
            return False
    
    def get_system_info(self) -> dict:
        """Get system information."""
        try:
            import psutil
            # Get disk usage - use appropriate root for OS
            if self.is_windows:
                disk_path = 'C:\\'
            elif self.is_linux:
                disk_path = '/'
            else:  # macOS
                disk_path = '/'
            
            info = {
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage(disk_path).percent,
                "platform": platform.platform()
            }
            return info
        except Exception as e:
            return {"error": str(e)}
    
    def execute_command(self, command: str) -> Optional[str]:
        """Execute a system command."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Error: {e}"

