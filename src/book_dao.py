import sqlite3
from book import Book
from typing import List


class BookDAO:
    def __init__(self, db_file):
        """Initialisera anslutningen till databasen och skapa tabellen om den inte finns."""
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row  # Gör att vi kan hämta kolumnnamn som index
        self.create_table()

    def create_table(self):
        """Skapar 'books'-tabellen om den inte redan existerar."""
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            author TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def clear_table(self):
        """Tömmer 'books'-tabellen på alla rader."""
        query = "DELETE FROM books;"
        self.conn.execute(query)
        self.conn.commit()

    def insert_book(self, book: Book):
        """Infogar en bok i databasen och returnerar det nya bok-id:t."""
        query = """
        INSERT INTO books (title, description, author)
        VALUES (?, ?, ?);
        """
        cur = self.conn.execute(query, (book.title, book.description, book.author))
        self.conn.commit()
        return cur.lastrowid

    def get_all_books(self):
        """Returnerar en lista med alla böcker i databasen."""
        query = "SELECT * FROM books;"
        cur = self.conn.execute(query)
        rows = cur.fetchall()
        return [Book(id=row["id"], title=row["title"], description=row["description"], author=row["author"]) for row in rows]

    def close(self) -> None:
        """Stänger databasanslutningen."""
        self.conn.close()

# Exempel på hur klassen kan användas. Detta script kan testas med pytest.
if __name__ == "__main__":
    # Använd en in-memory-databas för enkel testning
    dao = BookDAO(":memory:")

    # Infoga en exempelbok
    new_book = Book(id=None, title="Exempeltitel", description="En kort beskrivning", author="Författare A")
    book_id = dao.insert_book(new_book)
    print("Infogad bok med ID:", book_id)

    # Hämta och skriv ut alla böcker
    books = dao.get_all_books()
    for book in books:
        print(book)

    # Töm tabellen
    dao.clear_table()
    print("Böcker efter tömning:", dao.get_all_books())

    dao.close()
