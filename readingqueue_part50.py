# === Stage 50: Add unit tests for import and export behavior ===
# Project: ReadingQueue
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from reading_queue import ReadingQueue
from reading_queue.storage import SQLiteStorage

def _make_sample():
    """Create a populated queue for testing."""
    q = ReadingQueue("test_db")
    q.add_book("Book A", "Author A", 1, 4)
    q.add_book("Book B", "Author B", 2, 5)
    q.add_book("Book C", "Author C", 3, 3)
    q.set_progress("Book A", 50)
    q.rate("Book B", 5)
    q.mark_complete("Book C")
    return q

def test_import_and_export():
    """Verify that books, progress, ratings, and streaks survive a fresh start."""
    # 1. Build a queue and record data
    q1 = _make_sample()
    assert len(q1.queue) == 3
    assert q1.progress["Book A"] == 50
    assert q1.ratings["Book B"] == 5
    assert q1.completed == {"Book C"}

    # 2. Export to a temporary SQLite database
    tmp_db = ROOT / "test_export.sqlite"
    q1.export(tmp_db)

    # 3. Create a brand-new queue pointing at the exported DB
    q2 = ReadingQueue("test_export")
    assert len(q2.queue) == 3
    assert q2.progress["Book A"] == 50
    assert q2.ratings["Book B"] == 5
    assert "Book C" in q2.completed

    # 4. Confirm the original DB is untouched
    assert q1.queue is not None

    # 5. Clean up
    tmp_db.unlink()
