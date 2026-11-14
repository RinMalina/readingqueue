# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ReadingQueue
CLEAR_CONFIRM = False


def clear_state():
    global CLEAR_CONFIRM
    if not CLEAR_CONFIRM:
        print("A confirmation flag is required to clear state. Set CLEAR_CONFIRM = True first.")
        return
    CLEAR_CONFIRM = False
    books = []
    progress = {}
    ratings = {}
    streak = {"current": 0, "best": 0, "start": None, "last": None}
    with open("reading_queue.json", "w") as f:
        json.dump({"books": books, "progress": progress, "ratings": ratings, "streak": streak}, f)
    print("State cleared successfully.")
