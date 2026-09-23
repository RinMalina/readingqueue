# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ReadingQueue
from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Optional

@dataclass
class ReadingEntry:
    book_title: str
    author: str
    start_date: date
    progress_pct: int = 0
    rating: Optional[int] = None
    notes: str = ""

def demo_workflow() -> None:
    # 1. Create initial to-read queue
    queue: List[ReadingEntry] = [
        ReadingEntry("Dune", "Frank Herbert", date(2024, 1, 15), 0, None, ""),
        ReadingEntry("The Great Gatsby", "F. Scott Fitzgerald", date(2024, 1, 20), 0, None, ""),
    ]
    print("Initial to-read queue:")
    for entry in queue:
        print(f"  - {entry.book_title} by {entry.author}")

    # 2. Simulate reading progress
    queue[0].progress_pct = 45
    queue[0].notes = "Loved the world-building"
    queue[1].progress_pct = 100
    queue[1].rating = 5
    print("\nAfter reading:")
    for entry in queue:
        status = f"Rating: {entry.rating}/5" if entry.rating else "Not yet rated"
        print(f"  - {entry.book_title}: {entry.progress_pct}% complete, {status}")

    # 3. Calculate reading streak
    completed = [e for e in queue if e.progress_pct == 100]
    if completed:
        last_completed = max(e.start_date for e in completed)
        streak_days = (date.today() - last_completed).days
        print(f"\nReading streak: {streak_days} days since last completed book")
    else:
        print("\nNo completed books yet")

    # 4. Add a new book to the queue
    new_book = ReadingEntry("Project Hail Mary", "Andy Weir", date.today(), 0, None, "")
    queue.append(new_book)
    print(f"\nAdded new book: {new_book.book_title}")

    # 5. Sort queue by start date
    queue.sort(key=lambda x: x.start_date)
    print("\nQueue sorted by start date:")
    for entry in queue:
        print(f"  - {entry.book_title} (started {entry.start_date})")

    print("\nDemo workflow completed successfully!")
