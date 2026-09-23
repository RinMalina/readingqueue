# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ReadingQueue
import unittest
from reading_queue import ReadingQueue

def test_update_edge_cases():
    """Test updating non-existent and invalid entries."""
    queue = ReadingQueue()

    # Update a non-existent entry should raise or return False
    result = queue.update("book1", {"progress": 50, "rating": None})
    assert result is False

    # Update with invalid rating
    result = queue.update("book1", {"progress": 50, "rating": "abc"})
    assert result is False

    # Update with invalid progress
    result = queue.update("book1", {"progress": -1, "rating": None})
    assert result is False

    # Update with invalid progress
    result = queue.update("book1", {"progress": 200, "rating": None})
    assert result is False

    # Update with valid data should work
    queue.add("book1", {"title": "Book One", "author": "Author One"})
    result = queue.update("book1", {"progress": 50, "rating": 4})
    assert result is True

    # Verify the update
    book = queue.get("book1")
    assert book["progress"] == 50
    assert book["rating"] == 4

def test_delete_edge_cases():
    """Test deleting non-existent and invalid entries."""
    queue = ReadingQueue()

    # Delete a non-existent entry should return False
    result = queue.delete("book1")
    assert result is False

    # Delete with invalid book_id
    result = queue.delete("")
    assert result is False

    # Add a book and then delete it
    queue.add("book1", {"title": "Book One", "author": "Author One"})
    result = queue.delete("book1")
    assert result is True

    # Verify the deletion
    assert queue.get("book1") is None

    # Delete again should return False
    result = queue.delete("book1")
    assert result is False

if __name__ == "__main__":
    test_update_edge_cases()
    test_delete_edge_cases()
    print("All edge case tests passed!")
