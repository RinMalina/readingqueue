# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ReadingQueue
def dispatch(text):
    """Simple command dispatcher for text commands."""
    text = text.strip().lower()
    if text in ("quit", "exit", "q"):
        return "quit"
    if text in ("clear", "cls", "reset"):
        return "clear"
    if text.startswith("help"):
        help_text = text[4:].strip()
        if help_text:
            return help_text
        return "help"
    if text in ("show", "ls", "list"):
        return "show"
    if text in ("stats", "summary", "report"):
        return "stats"
    if text in ("clear screen", "reset display"):
        return "clear"
    return text
