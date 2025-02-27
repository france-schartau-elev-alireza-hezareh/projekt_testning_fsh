import pytest
import os
from book_dao import BookDAO
from book import Book

class TestBookDAO:
    def setup_method(self):
        """Set up a temporary SQLite database for testing."""
        self.db_file = "test_books.db"
        self.book_dao = BookDAO(self.db_file)

    def teardown_method(self):
        """Clean up the temporary database after each test."""
        self.book_dao.close()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    # Test 1: Test creating the table and inserting a book
    def test_create_table_and_insert_book(self):
        # Insert a book
        book = Book("Test Title", "Test Description", "Test Author")
        book_id = self.book_dao.insert_book(book)

        # Verify the book was inserted correctly
        assert book_id == 1  # First book should have ID 1
        books = self.book_dao.get_all_books()
        assert len(books) == 1
        assert books[0].title == "Test Title"
        assert books[0].description == "Test Description"
        assert books[0].author == "Test Author"
        assert books[0].id == 1

    # Test 2: Test getting all books
    def test_get_all_books(self):
        # Insert multiple books
        book1 = Book("Title1", "Description1", "Author1")
        book2 = Book("Title2", "Description2", "Author2")
        self.book_dao.insert_book(book1)
        self.book_dao.insert_book(book2)

        # Get all books and verify
        books = self.book_dao.get_all_books()
        assert len(books) == 2
        assert books[0].title == "Title1"
        assert books[1].title == "Title2"

    # Test 3: Test finding a book by title
    def test_find_by_title(self):
        # Insert a book
        book = Book("Unique Title", "Unique Description", "Unique Author")
        self.book_dao.insert_book(book)

        # Find the book by title
        found_book = self.book_dao.find_by_title("Unique Title")
        assert found_book is not None
        assert found_book.title == "Unique Title"
        assert found_book.description == "Unique Description"
        assert found_book.author == "Unique Author"

        # Test finding a non-existent book
        non_existent_book = self.book_dao.find_by_title("Non Existent Title")
        assert non_existent_book is None

    # Test 4: Test updating a book
    def test_update_book(self):
        # Insert a book
        book = Book("Old Title", "Old Description", "Old Author")
        book_id = self.book_dao.insert_book(book)

        # Update the book
        updated_book = Book("New Title", "New Description", "New Author", id=book_id)
        update_success = self.book_dao.update_book(updated_book)
        assert update_success is True

        # Verify the update
        found_book = self.book_dao.find_by_title("New Title")
        assert found_book is not None
        assert found_book.title == "New Title"
        assert found_book.description == "New Description"
        assert found_book.author == "New Author"

    # Test 5: Test deleting a book
    def test_delete_book(self):
        # Insert a book
        book = Book("Delete Me", "Description", "Author")
        book_id = self.book_dao.insert_book(book)

        # Delete the book
        delete_success = self.book_dao.delete_book(Book("", "", "", id=book_id))
        assert delete_success is True

        # Verify the book is deleted
        found_book = self.book_dao.find_by_title("Delete Me")
        assert found_book is None

    # Test 6: Test clearing the table
    def test_clear_table(self):
        # Insert some books
        book1 = Book("Title1", "Description1", "Author1")
        book2 = Book("Title2", "Description2", "Author2")
        self.book_dao.insert_book(book1)
        self.book_dao.insert_book(book2)

        # Clear the table
        self.book_dao.clear_table()

        # Verify the table is empty
        books = self.book_dao.get_all_books()
        assert len(books) == 0