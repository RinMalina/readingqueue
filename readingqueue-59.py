# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ReadingQueue
def bulk_delete(confirmation):
    if not confirmation:
        print("No book deleted. Confirmation required.")
        return
    remaining = []
    for book in books:
        if book.get("id") not in bulk_deleted_ids:
            remaining.append(book)
    books[:] = remaining
    bulk_deleted_ids.clear()
    print(f"Deleted {len(books) - len(remaining)} book(s).")
