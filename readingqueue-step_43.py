# === Stage 43: Add CSV import for the primary record type ===
# Project: ReadingQueue
import csv

def import_book_queue(filename: str) -> list[dict]:
    """Read a CSV file of books and return a list of book dicts."""
    books = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            book = {
                'title': row.get('title', '').strip(),
                'author': row.get('author', '').strip(),
                'status': row.get('status', 'to-read'),
                'rating': row.get('rating', ''),
                'started_date': row.get('started_date', ''),
                'finished_date': row.get('finished_date', ''),
                'pages_read': row.get('pages_read', '0'),
            }
            if book['pages_read'].strip():
                book['pages_read'] = int(book['pages_read'])
            books.append(book)
    return books
