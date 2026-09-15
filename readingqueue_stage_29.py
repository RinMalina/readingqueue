# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ReadingQueue
def get_upcoming_reminders(books, days_ahead=7):
    """Return books whose estimated finish date falls within the next `days_ahead` days."""
    upcoming = []
    today = datetime.date.today()
    for book in books:
        if book.progress is None:
            continue
        estimated_end = today + timedelta(days=book.progress)
        if today <= estimated_end <= today + timedelta(days=days_ahead):
            upcoming.append(book)
    return upcoming


def get_overdue_books(books, grace_days=30):
    """Return books that are past their estimated finish date by more than `grace_days`."""
    overdue = []
    today = datetime.date.today()
    for book in books:
        if book.progress is None:
            continue
        estimated_end = today + timedelta(days=book.progress)
        if estimated_end < today - timedelta(days=grace_days):
            overdue.append(book)
    return overdue


def get_streak_reminder(books):
    """Return books whose reading streak is about to break (last read > 3 days ago)."""
    today = datetime.date.today()
    at_risk = []
    for book in books:
        if book.last_read is None:
            continue
        if today - book.last_read > timedelta(days=3):
            at_risk.append(book)
    return at_risk
