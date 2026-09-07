# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ReadingQueue
def filter_books(self, status=None, category=None, owner=None, tag=None):
    results = self._books.copy()
    if status is not None:
        results = [b for b in results if b.status == status]
    if category is not None:
        results = [b for b in results if b.category == category]
    if owner is not None:
        results = [b for b in results if b.owner == owner]
    if tag is not None:
        results = [b for b in results if tag in b.tags]
    return results
