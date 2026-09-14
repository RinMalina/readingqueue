# === Stage 27: Add monthly summary calculations ===
# Project: ReadingQueue
def monthly_summary(records, year, month):
    """Compute a compact monthly summary from reading records.

    Returns a dict with keys:
        - 'books_read': count of books finished in that month
        - 'total_pages': total pages read
        - 'average_rating': mean rating (rounded to 2 decimals)
        - 'streak_days': longest consecutive day streak
        - 'books_by_genre': dict of genre -> count
    """
    month_key = f"{year}-{month:02d}"
    month_records = [r for r in records if r.get("date", "")[:7] == month_key]
    books_read = sum(1 for r in month_records if r.get("status") == "finished")
    total_pages = sum(r.get("pages_read", 0) for r in month_records)
    ratings = [r.get("rating", 0) for r in month_records if r.get("rating")]
    average_rating = round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    dates = sorted(set(r.get("date", "") for r in month_records if r.get("date")))
    streak_days = 0
    max_streak = 0
    if dates:
        streak_days = 1
        max_streak = 1
        for i in range(1, len(dates)):
            delta = (datetime.date.fromisoformat(dates[i]) - datetime.date.fromisoformat(dates[i - 1])).days
            if delta == 1:
                streak_days += 1
                max_streak = max(max_streak, streak_days)
            else:
                streak_days = 1
    genre_counts = {}
    for r in month_records:
        genre = r.get("genre", "Unknown")
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return {
        "books_read": books_read,
        "total_pages": total_pages,
        "average_rating": average_rating,
        "streak_days": max_streak,
        "books_by_genre": genre_counts,
    }
