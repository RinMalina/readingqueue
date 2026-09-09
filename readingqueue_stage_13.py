# === Stage 13: Add file save support using a configurable path ===
# Project: ReadingQueue
import json
import os

def save_to_file(data, path="reading_queue.json"):
    """Save reading queue data to a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path

def load_from_file(path="reading_queue.json"):
    """Load reading queue data from a JSON file."""
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)
