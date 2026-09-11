# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ReadingQueue
class LogEntry:
    def __init__(self, action, timestamp=None):
        self.action = action
        self.timestamp = timestamp or datetime.now()

    def __repr__(self):
        return f"LogEntry({self.action}, {self.timestamp})"

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, timestamp=None):
        self.entries.append(LogEntry(action, timestamp))

    def recent(self, limit=5):
        return self.entries[-limit:]

    def __repr__(self):
        return f"ActivityLog({len(self.entries)} entries)"
