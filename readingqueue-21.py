# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ReadingQueue
def archive_old_records(db_path):
    """Move completed records older than 180 days to an archive file."""
    import sqlite3, shutil
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cutoff = (sqlite3.date_function('datetime', 'now') +
              '180 days').replace('180 days', '')
    cursor.execute(
        "SELECT id FROM books WHERE status = 'completed' "
        "AND last_readed < ?", (cutoff,))
    old_ids = cursor.fetchall()
    if not old_ids:
        conn.commit()
        return
    for row in old_ids:
        cursor.execute("UPDATE books SET status = 'archived' WHERE id = ?", (row[0],))
    shutil.move(db_path, db_path.replace('.db', '.db.archive'))
    conn.commit()
    conn.close()
