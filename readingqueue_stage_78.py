# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ReadingQueue
def _split_by_progress(book):
    if book['progress'] >= 100:
        return 'completed'
    if book['progress'] > 0:
        return 'reading'
    return 'to-read'

def _update_streak(date_str, books):
    today = date_str
    streak = 0
    for book in books:
        if book['status'] == 'completed':
            if book.get('completed_date') == today:
                streak += 1
    return streak

def _add_day_to_streak(date_str, books):
    today = date_str
    for book in books:
        if book['status'] == 'completed' and book.get('completed_date') == today:
            book['completed_date'] = _next_day(today)

def _next_day(date_str):
    d, m, y = map(int, date_str.split('-'))
    d += 1
    if d > 31:
        return date_str
    return f"{d:02d}-{m:02d}-{y}"

def _compute_stats(books):
    total = len(books)
    completed = sum(1 for b in books if b['status'] == 'completed')
    average_rating = _average_rating(books)
    streak = _update_streak(_today(), books)
    return {
        'total': total,
        'completed': completed,
        'average_rating': average_rating,
        'streak': streak,
    }

def _average_rating(books):
    rated = [b['rating'] for b in books if b.get('rating')]
    if not rated:
        return 0
    return sum(rated) / len(rated)

def _today():
    import datetime
    return datetime.date.today().strftime('%Y-%m-%d')

def refresh_reading_stats(books):
    _add_day_to_streak(_today(), books)
    return _compute_stats(books)
