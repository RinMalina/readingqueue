# === Stage 67: Add a function that returns key project metrics ===
# Project: ReadingQueue
def get_project_metrics():
    total_books = len(to_read) + len(in_progress) + len(completed)
    finished_books = len(completed)
    completion_rate = (finished_books / total_books * 100) if total_books else 0.0
    total_stars = sum(book.rating for book in completed)
    average_rating = (total_stars / finished_books) if finished_books else 0.0
    current_streak = calculate_streak()
    long_time_books = [book for book in to_read if book.days_since_added >= 30]
    metrics = {
        "total_books": total_books,
        "finished_books": finished_books,
        "completion_rate": round(completion_rate, 1),
        "average_rating": round(average_rating, 1),
        "current_streak": current_streak,
        "overdue_books": len(long_time_books),
    }
    return metrics
