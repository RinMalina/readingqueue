# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ReadingQueue
import unittest
from reading_queue import ReadingQueue

class TestSearchAndFilter(unittest.TestCase):

    def setUp(self):
        self.queue = ReadingQueue()
        self.queue.add_book("1984", "Orwell", "fiction")
        self.queue.add_book("Dune", "Butler", "scifi")
        self.queue.add_book("Sapiens", "Harari", "nonfiction")
        self.queue.add_book("The Road", "Lynch", "fiction")

    def test_search_by_title(self):
        result = self.queue.search("1984")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "1984")

    def test_search_by_author(self):
        result = self.queue.search("Orwell")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].author, "Orwell")

    def test_search_by_genre(self):
        result = self.queue.search("fiction")
        self.assertEqual(len(result), 2)

    def test_search_no_match(self):
        result = self.queue.search("Nonexistent")
        self.assertEqual(len(result), 0)

    def test_filter_by_genre(self):
        result = self.queue.filter("scifi")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Dune")

    def test_filter_by_status(self):
        result = self.queue.filter("reading")
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()
