# === Stage 36: Add templates for quickly creating common records ===
# Project: ReadingQueue
def create_record():
    """Create a new book record with default values."""
    return {
        'title': '',
        'author': '',
        'genre': '',
        'pages': 0,
        'pages_read': 0,
        'rating': None,
        'notes': '',
        'added_date': None,
        'last_read_date': None,
        'status': 'planned',
    }

def create_review():
    """Create a new review entry."""
    return {
        'book_id': None,
        'rating': None,
        'review_text': '',
        'review_date': None,
    }

def create_reading_log():
    """Create a new reading log entry."""
    return {
        'book_id': None,
        'pages_read': 0,
        'reading_date': None,
        'reading_duration': 0,
    }
