# === Stage 55: Add a setting to disable colorized output ===
# Project: ReadingQueue
DISABLE_COLOR = os.environ.get("READING_QUEUE_COLOR", "auto").lower() != "on"
