# === Stage 14: Add file load support with fallback demo data ===
# Project: ReadingQueue
def load_books(path=None):
    """Load books from a JSON file; fall back to demo data if file missing."""
    if path is None:
        path = os.path.join(DATA_DIR, "books.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            books = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        books = DEMO_BOOKS
    if not books:
        books = DEMO_BOOKS
    return books
