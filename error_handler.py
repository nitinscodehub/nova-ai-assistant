"""Auto-install missing packages and handle errors."""
import subprocess
import sys
import importlib
from typing import Optional

class ErrorHandler:
    """Handles errors and auto-installs missing packages."""
    
    @staticmethod
    def install_package(package_name: str) -> bool:
        """Install a package using pip."""
        try:
            print(f"Installing {package_name}...")
            # Check if we're in a virtual environment
            in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
            
            if in_venv:
                # In venv, use regular pip install
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--quiet"])
                    print(f"✓ {package_name} installed successfully!")
                    return True
                except subprocess.CalledProcessError as e:
                    print(f"⚠ Could not install {package_name} in venv.")
                    print(f"   Please run: pip install {package_name}")
                    return False
            else:
                # Not in venv, try --user first (for externally-managed environments)
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package_name, "--quiet"])
                    print(f"✓ {package_name} installed successfully!")
                    return True
                except subprocess.CalledProcessError:
                    # Fallback: try with break-system-packages flag
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", package_name, "--quiet"])
                        print(f"✓ {package_name} installed successfully!")
                        return True
                    except subprocess.CalledProcessError:
                        print(f"⚠ Could not install {package_name} automatically.")
                        print(f"   Please run: pip install --user {package_name}")
                        print(f"   Or use virtual environment: python3 -m venv venv && source venv/bin/activate")
                        return False
        except Exception as e:
            print(f"✗ Failed to install {package_name}: {e}")
            return False
    
    @staticmethod
    def ensure_package(package_name: str, import_name: Optional[str] = None) -> bool:
        """Ensure a package is installed, install if missing."""
        if import_name is None:
            import_name = package_name
        
        try:
            importlib.import_module(import_name)
            return True
        except ImportError:
            print(f"Package {package_name} not found. Installing...")
            return ErrorHandler.install_package(package_name)
    
    @staticmethod
    def retry_operation(operation, max_retries: int = 3, delay: float = 1.0):
        """Retry an operation with exponential backoff."""
        import time
        for attempt in range(max_retries):
            try:
                return operation()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"Retry {attempt + 1}/{max_retries}: {e}")
                time.sleep(delay * (2 ** attempt))
        return None

