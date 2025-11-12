"""File search functionality."""
import os
from pathlib import Path
from typing import List, Optional
from colorama import Fore, Style, init

init(autoreset=True)

class FileSearch:
    """Handles file search operations."""
    
    def __init__(self):
        import platform
        system = platform.system().lower()
        
        if system == "windows":
            # Windows search paths
            self.search_paths = [
                str(Path.home()),
                "C:\\Users",
                "C:\\Program Files",
                "C:\\Program Files (x86)"
            ]
        elif system == "darwin":  # macOS
            self.search_paths = [
                str(Path.home()),
                "/Users",
                "/Applications",
                "/usr"
            ]
        else:  # Linux
            self.search_paths = [
                str(Path.home()),
                "/home",
                "/usr",
                "/opt"
            ]
    
    def search_file(self, filename: str, search_path: Optional[str] = None) -> List[str]:
        """Search for a file by name."""
        results = []
        paths_to_search = [search_path] if search_path else self.search_paths
        
        print(f"{Fore.CYAN}Searching for '{filename}'...{Style.RESET_ALL}")
        
        for search_path in paths_to_search:
            if not os.path.exists(search_path):
                continue
            
            try:
                for root, dirs, files in os.walk(search_path):
                    # Skip hidden directories
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    
                    # Search in files
                    for file in files:
                        if filename.lower() in file.lower():
                            full_path = os.path.join(root, file)
                            results.append(full_path)
                            if len(results) >= 10:  # Limit results
                                return results
            except PermissionError:
                pass
            except Exception as e:
                print(f"Search error: {e}")
        
        return results
    
    def search_in_current_directory(self, filename: str) -> List[str]:
        """Search in current working directory."""
        results = []
        try:
            current_dir = os.getcwd()
            for root, dirs, files in os.walk(current_dir):
                for file in files:
                    if filename.lower() in file.lower():
                        full_path = os.path.join(root, file)
                        results.append(full_path)
        except Exception as e:
            print(f"Search error: {e}")
        return results
    
    def format_results(self, results: List[str]) -> str:
        """Format search results for display."""
        if not results:
            return "No files found."
        
        formatted = f"Found {len(results)} file(s):\n"
        for i, path in enumerate(results, 1):
            formatted += f"{Fore.GREEN}{i}. {path}{Style.RESET_ALL}\n"
        return formatted

