# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ReadingQueue
class FavoriteRecord:
    def __init__(self, book_id, rating, date, reason):
        self.book_id = book_id
        self.rating = rating
        self.date = date
        self.reason = reason

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "rating": self.rating,
            "date": self.date,
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            book_id=data["book_id"],
            rating=data["rating"],
            date=data["date"],
            reason=data.get("reason", ""),
        )

class FavoriteManager:
    def __init__(self):
        self._favorites = []

    def add_favorite(self, book_id, rating, date, reason=""):
        record = FavoriteRecord(book_id, rating, date, reason)
        self._favorites.append(record)
        return record

    def get_favorites(self):
        return self._favorites

    def get_top_favorites(self, limit=5):
        return sorted(self._favorites, key=lambda x: x.rating, reverse=True)[:limit]

    def get_favorite_by_book(self, book_id):
        for fav in self._favorites:
            if fav.book_id == book_id:
                return fav
        return None
