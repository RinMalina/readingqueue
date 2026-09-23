# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ReadingQueue
import pytest
from reading_queue.models import Book


def test_book_creation():
    book = Book(title="1984", author="George Orwell", year=1949)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.year == 1949


def test_book_validation():
    with pytest.raises(ValueError):
        Book(title="", author="", year=0)
    with pytest.raises(ValueError):
        Book(title="Good Book", author="", year=2023)
    with pytest.raises(ValueError):
        Book(title="", author="Author", year=2023)
    with pytest.raises(ValueError):
        Book(title="Good Book", author="Author", year=-1)
