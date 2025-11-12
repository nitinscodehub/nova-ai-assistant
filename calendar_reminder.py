"""Calendar and reminder management using SQLite."""
import sqlite3
import json
import threading
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from error_handler import ErrorHandler
from colorama import Fore, Style, init

init(autoreset=True)

# Lazy import schedule - will be imported after ensuring it's installed
schedule = None

class CalendarReminder:
    """Manages calendar events and reminders."""
    
    def __init__(self, db_path: str = "reminders.db", tts_callback=None):
        self.db_path = db_path
        self.tts_callback = tts_callback
        self._setup_database()
        self._start_scheduler()
    
    def _setup_database(self):
        """Setup SQLite database for reminders."""
        global schedule
        try:
            ErrorHandler.ensure_package("schedule")
            import schedule as schedule_module
            schedule = schedule_module
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    datetime TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    notified INTEGER DEFAULT 0
                )
            """)
            conn.commit()
            conn.close()
            print("✓ Calendar database ready")
        except Exception as e:
            print(f"Database setup error: {e}")
    
    def add_reminder(self, title: str, reminder_datetime: datetime, description: str = "") -> bool:
        """Add a reminder."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reminders (title, description, datetime, created_at, notified)
                VALUES (?, ?, ?, ?, ?)
            """, (title, description, reminder_datetime.isoformat(), datetime.now().isoformat(), 0))
            conn.commit()
            conn.close()
            print(f"{Fore.GREEN}✓ Reminder added: {title} at {reminder_datetime}{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}Failed to add reminder: {e}{Style.RESET_ALL}")
            return False
    
    def parse_reminder_time(self, text: str) -> Optional[datetime]:
        """Parse natural language time into datetime."""
        text_lower = text.lower()
        now = datetime.now()
        
        # Parse "tomorrow at 10 AM"
        if "tomorrow" in text_lower:
            target_date = now + timedelta(days=1)
            # Extract time
            if "am" in text_lower or "pm" in text_lower:
                time_part = text_lower.split("at")[1].strip() if "at" in text_lower else ""
                try:
                    hour = int(time_part.split(":")[0].split()[0])
                    minute = int(time_part.split(":")[1].split()[0]) if ":" in time_part else 0
                    if "pm" in time_part and hour != 12:
                        hour += 12
                    elif "am" in time_part and hour == 12:
                        hour = 0
                    return target_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
                except:
                    return target_date.replace(hour=10, minute=0, second=0, microsecond=0)
            return target_date.replace(hour=10, minute=0, second=0, microsecond=0)
        
        # Parse "in 1 hour"
        if "in" in text_lower and "hour" in text_lower:
            try:
                hours = int(text_lower.split("in")[1].split("hour")[0].strip())
                return now + timedelta(hours=hours)
            except:
                pass
        
        # Parse "at 3 PM"
        if "at" in text_lower:
            try:
                time_part = text_lower.split("at")[1].strip()
                hour = int(time_part.split(":")[0].split()[0])
                minute = int(time_part.split(":")[1].split()[0]) if ":" in time_part else 0
                if "pm" in time_part and hour != 12:
                    hour += 12
                elif "am" in time_part and hour == 12:
                    hour = 0
                target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                if target < now:
                    target += timedelta(days=1)
                return target
            except:
                pass
        
        return None
    
    def get_upcoming_reminders(self, limit: int = 10) -> List[Dict]:
        """Get upcoming reminders."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, title, description, datetime, notified
                FROM reminders
                WHERE datetime >= ?
                ORDER BY datetime ASC
                LIMIT ?
            """, (datetime.now().isoformat(), limit))
            results = cursor.fetchall()
            conn.close()
            
            reminders = []
            for row in results:
                reminders.append({
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "datetime": datetime.fromisoformat(row[3]),
                    "notified": row[4]
                })
            return reminders
        except Exception as e:
            print(f"Error getting reminders: {e}")
            return []
    
    def check_reminders(self):
        """Check for due reminders."""
        try:
            now = datetime.now()
            reminders = self.get_upcoming_reminders(limit=20)
            
            for reminder in reminders:
                reminder_time = reminder["datetime"]
                if reminder_time <= now and reminder["notified"] == 0:
                    # Notify user
                    message = f"Reminder: {reminder['title']}"
                    if reminder["description"]:
                        message += f" - {reminder['description']}"
                    
                    print(f"{Fore.YELLOW}🔔 {message}{Style.RESET_ALL}")
                    
                    if self.tts_callback:
                        self.tts_callback(message)
                    
                    # Mark as notified
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute("UPDATE reminders SET notified = 1 WHERE id = ?", (reminder["id"],))
                    conn.commit()
                    conn.close()
        except Exception as e:
            print(f"Error checking reminders: {e}")
    
    def _start_scheduler(self):
        """Start the reminder scheduler in a separate thread."""
        global schedule
        import time
        
        if schedule is None:
            try:
                ErrorHandler.ensure_package("schedule")
                import schedule as schedule_module
                schedule = schedule_module
            except Exception as e:
                print(f"Warning: Could not load schedule module: {e}")
                return
        
        def run_scheduler():
            if schedule is not None:
                schedule.every(1).minutes.do(self.check_reminders)
                while True:
                    schedule.run_pending()
                    time.sleep(60)
        
        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()
        print("✓ Reminder scheduler started")

