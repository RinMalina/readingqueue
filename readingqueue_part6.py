# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ReadingQueue
def delete_book(self, book_id, confirm=False):
    """Delete a book from the queue. Returns True if deleted."""
    try:
        book = self.books[book_id]
    except KeyError:
        print(f"Book {book_id} not found.")
        return False
    if not confirm:
        print(f"⚠️  Deleting '{book.title}'? [y/N]")
        if input().strip().lower() != 'y':
            print("Cancelled.")
            return False
    del self.books[book_id]
    if book_id in self.read_books:
        del self.read_books[book_id]
    print(f"✅ '{book.title}' deleted.")
    return True
