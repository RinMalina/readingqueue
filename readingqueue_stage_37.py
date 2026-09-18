# === Stage 37: Add recommendations for the next useful action ===
# Project: ReadingQueue
def get_next_action(user):
    """Suggest the next useful action based on user state."""
    if not user.books:
        return "Add your first book to the to-read queue."
    unread = [b for b in user.books if not b.progress]
    if unread:
        return f"Pick one of your {len(unread)} unread books and start reading."
    if not any(b.progress >= 1.0 for b in user.books):
        return "Finish your current book before adding new ones."
    if not any(b.progress >= 0.5 for b in user.books):
        return "Continue reading your in-progress books."
    if user.streak < 3:
        return "Read at least 30 minutes today to build your streak."
    if user.last_rating is None:
        return "Rate a book you finished to help improve recommendations."
    if user.last_rating < 3.0:
        return "Try a different genre or author to find something you enjoy."
    return "You're on a great track! Keep reading and rating books."
