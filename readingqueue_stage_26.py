# === Stage 26: Add weekly summary calculations ===
# Project: ReadingQueue
def weekly_summary(self, week_start):
    """Calculate reading summary for a given week."""
    week_end = week_start + timedelta(days=7)
    total_read = 0
    books_read = 0
    pages_read = 0
    for book in self.books.values():
        if book['last_read'] and week_start <= book['last_read'] < week_end:
            if book['status'] in ['reading', 'read']:
                total_read += book['pages_read']
                books_read += 1
                pages_read += book['pages_read']
    return {
        'week_start': week_start,
        'week_end': week_end,
        'books_read': books_read,
        'pages_read': pages_read,
        'total_read': total_read
    }
