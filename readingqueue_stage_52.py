# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ReadingQueue
def _get_current_year():
    """Return the current calendar year as an integer."""
    return datetime.datetime.now().year

def _format_date(date_obj):
    """Convert a date object to a human-readable string in 'YYYY-MM-DD' format."""
    if isinstance(date_obj, datetime.datetime):
        date_obj = date_obj.date()
    return date_obj.strftime("%Y-%m-%d")

def _is_within_streak_days(start_date, end_date, max_gap_days=5):
    """Check if two dates are within a reasonable gap for a reading streak."""
    delta = (end_date - start_date).days
    return 0 <= delta <= max_gap_days

def _calculate_weekly_progress(total_pages, weekly_target):
    """Return progress percentage for a reading week, capping at 100%."""
    if weekly_target <= 0:
        return 0.0
    progress = min((total_pages / weekly_target) * 100, 100.0)
    return round(progress, 1)

def _get_days_since_last_read(last_read_date, today=None):
    """Calculate the number of days since the last reading session."""
    if today is None:
        today = datetime.date.today()
    if last_read_date is None:
        return None
    return (today - last_read_date).days

def _validate_book_title(title):
    """Ensure the book title is non-empty and under 200 characters."""
    if not title or len(title.strip()) == 0:
        raise ValueError("Book title must not be empty")
    if len(title) > 200:
        raise ValueError("Book title exceeds maximum length of 200 characters")
    return title.strip()
