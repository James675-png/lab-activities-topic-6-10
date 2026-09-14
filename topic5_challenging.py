# topic5_challenging.py
# Purpose: Implement and test searching books by author.

import unittest


class BookRepository:
    """Handle book records and author searches."""

    def __init__(self):
        self.books = [
            (1, "Introduction to Python", "J. Smith", 1),
            (2, "Data Structures in Python", "R. Lee", 1),
            (3, "Advanced Python", "J. Smith", 0),
        ]

    def search_by_author(self, author_name):
        """Return all books written by the specified author."""
        return [
            book
            for book in self.books
            if book[2] == author_name
        ]


class TestSearchByAuthor(unittest.TestCase):

    def test_search_by_author(self):
        repo = BookRepository()

        results = repo.search_by_author("J. Smith")

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0][1], "Introduction to Python")
        self.assertEqual(results[1][1], "Advanced Python")


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)