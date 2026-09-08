# === Stage 11: Add JSON export for the current application state ===
# Project: ReadingQueue
def export_json(state):
    """Export the current ReadingQueue state to a JSON string."""
    return json.dumps(state, indent=2, ensure_ascii=False)
