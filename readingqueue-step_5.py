# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ReadingQueue
def update_book(self, book_id, updates):
    """Update an existing book record. Returns the new record or None if not found."""
    if book_id not in self.books:
        return None
    record = dict(self.books[book_id])
    record.update(updates)
    self.books[book_id] = record
    return record

def update_reading(self, reading_id, updates):
    """Update an existing reading record. Returns the new record or None if not found."""
    if reading_id not in self.readings:
        return None
    record = dict(self.readings[reading_id])
    record.update(updates)
    self.readings[reading_id] = record
    return record

def remove_book(self, book_id):
    """Remove a book and all its associated readings. Returns the removed book or None."""
    if book_id not in self.books:
        return None
    removed = dict(self.books[book_id])
    page = self.books[book_id].get("page", 0)
    self.readings = {rid: r for rid, r in self.readings.items() if r.get("book_id") != book_id}
    self.books.pop(book_id)
    return removed
