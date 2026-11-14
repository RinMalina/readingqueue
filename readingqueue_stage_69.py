# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ReadingQueue
def reset_demo_data():
    """Overwrite the in-memory store with a fresh set of demo records."""
    with DATA_FILE, json.load(f) as data:
        data["books"] = [
            {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien",
             "status": "reading", "pages_total": 310, "pages_current": 120,
             "rating": None, "shelved": None, "start_date": "2025-01-01",
             "finish_date": None},
            {"id": 2, "title": "1984", "author": "George Orwell",
             "status": "finished", "pages_total": 328, "pages_current": 328,
             "rating": 5, "shelved": "2025-01-15", "start_date": "2024-12-01",
             "finish_date": "2025-01-15"},
            {"id": 3, "title": "Dune", "author": "Frank Herbert",
             "status": "to_read", "pages_total": 412, "pages_current": 0,
             "rating": None, "shelved": None, "start_date": None,
             "finish_date": None},
        ]
        data["streak"] = {"days": 7, "last_date": "2025-01-21", "start_date": "2025-01-15"}
        json.dump(data, f, indent=2)
    print("Demo data reset.")
