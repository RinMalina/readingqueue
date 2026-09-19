# === Stage 38: Add data integrity checks for broken references ===
# Project: ReadingQueue
def check_integrity(db):
    """Validate that every book reference is still valid."""
    errors = []
    for book in db.books.values():
        if book['id'] not in db.books:
            errors.append(f"Book {book['id']} is missing from the registry.")
        if book['source'] and book['source'].get('id') not in db.books:
            errors.append(f"Book {book['id']} references a broken source.")
        if book['current'] and book['current'].get('id') not in db.books:
            errors.append(f"Book {book['id']} references a broken current.")
    return errors
