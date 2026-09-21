# === Stage 45: Add restore from backup with validation ===
# Project: ReadingQueue
import json, os

BACKUP_FILE = "reading_queue_backup.json"

def load_backup():
    if not os.path.exists(BACKUP_FILE):
        return None
    try:
        with open(BACKUP_FILE, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return None
    if not isinstance(data, dict):
        return None
    valid_keys = {"queue", "progress", "ratings", "streaks", "last_read"}
    if not all(k in data for k in valid_keys):
        return None
    return data
