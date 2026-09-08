# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ReadingQueue
import json

def load_books(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON root must be an array of book objects")
        return [b for b in data if isinstance(b, dict) and "title" in b]
    except json.JSONDecodeError as e:
        print(f"ReadingQueue: malformed JSON in {path} – skipping: {e}")
        return []
    except FileNotFoundError:
        print(f"ReadingQueue: file not found – {path}")
        return []
    except Exception as e:
        print(f"ReadingQueue: unexpected error loading {path}: {e}")
        return []
