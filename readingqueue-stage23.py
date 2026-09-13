# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ReadingQueue
def add_tags(book, tags):
    """Add one or more tags to a book. Returns the updated book dict."""
    existing = set(book.get('tags', []))
    for t in tags:
        if t not in existing:
            existing.add(t)
    book['tags'] = sorted(existing)
    return book

def remove_tags(book, tags):
    """Remove tags from a book. Returns the updated book dict."""
    existing = set(book.get('tags', []))
    for t in tags:
        existing.discard(t)
    book['tags'] = sorted(existing)
    return book

def tag_summary(reading_log, tag):
    """Return a compact summary of all books tagged with the given tag."""
    from collections import defaultdict
    books = defaultdict(list)
    for entry in reading_log:
        if tag in entry.get('tags', []):
            books[entry['title']].append(entry)
    return {
        'tag': tag,
        'count': len(books),
        'details': {title: books[title] for title in books}
    }
