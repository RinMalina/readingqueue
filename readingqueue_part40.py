# === Stage 40: Add plain text report export ===
# Project: ReadingQueue
def export_plain_text(self):
    lines = [f"=== ReadingQueue Report ({self.now:%Y-%m-%d}) ==="]
    for book in self.queue:
        lines.append(f"\n--- {book['title']} ---")
        lines.append(f"Author: {book['author']}")
        lines.append(f"Status: {book['status']}")
        lines.append(f"Progress: {book.get('progress', 'N/A')}")
        if 'rating' in book:
            lines.append(f"Rating: {book['rating']}/5")
        lines.append(f"Added: {book['added']}")
    lines.append(f"\nTotal: {len(self.queue)} books")
    return "\n".join(lines)
