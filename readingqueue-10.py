# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ReadingQueue
def search_books(self, query: str) -> list[dict]:
    """Case-insensitive search across title, author, notes, and tags."""
    query = query.strip().lower()
    if not query:
        return list(self.books.values())
    results = []
    for book in self.books.values():
        searchable = (
            book.get("title", "") + " "
            + book.get("author", "") + " "
            + book.get("notes", "") + " "
            + " ".join(book.get("tags", []))
        ).lower()
        if query in searchable:
            results.append(book)
    return results
