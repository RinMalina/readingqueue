# === Stage 66: Add export of a short status dashboard ===
# Project: ReadingQueue
def export_status_dashboard(queue, books_by_id, streaks):
    total = len(queue)
    reading = [b for b in queue if b.get('status') == 'reading']
    finished = [b for b in queue if b.get('status') == 'finished']
    to_read = [b for b in queue if b.get('status') == 'to_read']
    completed = len(finished)
    in_progress = len(reading)
    rated = [b for b in queue if 'rating' in b]
    avg_rating = sum(b['rating'] for b in rated) / len(rated) if rated else 0
    active_streak = streaks.get('current', 0)
    longest_streak = streaks.get('longest', 0)
    total_pages = sum(b.get('pages', 0) for b in reading)
    lines = []
    lines.append("ReadingQueue Status Dashboard")
    lines.append("=" * 25)
    lines.append(f"Total books:        {total}")
    lines.append(f"To read:           {len(to_read)}")
    lines.append(f"Currently reading: {in_progress}")
    lines.append(f"Finished:          {completed}")
    lines.append(f"Pages this month:  {total_pages}")
    lines.append(f"Average rating:    {avg_rating:.1f}/5")
    lines.append(f"Current streak:    {active_streak} days")
    lines.append(f"Longest streak:    {longest_streak} days")
    return "\n".join(lines)
