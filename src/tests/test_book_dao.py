from book_dao import BookDAO
from book import Book
import pytest
 
class TestBookDao:
   def setup_method(self):
       self.book_dao = BookDAO(":memory:")  # Skapar en instans av BookDAO
       self.book_dao.create_table()  # Skapar en tabell
       for i in range(1, 4):  # Skapar 3 böcker
           book = Book(f"title{i}", f"description{i}", f"author{i}")  # Skapar en bok
           self.book_dao.insert_book(book)  # Lägger till boken i tabellen

     
   def teardown_method(self):   
       self.book_dao.clear_table()  # rensar tabellen
       self.book_dao.close()  # Stänger anslutningen till databasen

        
   def test_get_all_books(self):  # Testar get_all_books
       books = self.book_dao.get_all_books()  # gör en lista Hämtar alla böcker
       assert len(books) == 3  
 
   def test_insert_book(self):  # Testar insert_book
       book = Book("title4", "description4", "author4")  # Skapar en bok
       book_id = self.book_dao.insert_book(book)  # Lägger till boken i Databasen
       assert book_id == 4  # Kollar att boken har fått ID 4
       books = self.book_dao.get_all_books()  # Hämtar alla böcker
       assert len(books) == 4  # Kollar att det finns 4 böcker i listan
 
   def test_find_by_title(self):  # Testar find_by_title
       book = self.book_dao.find_by_title("title1")  # Hämtar boken med titel "title1"
       assert book != None
       assert book.description == "description1"  # Kollar att beskrivningen stämmer
 
   def test_update_book(self):  # Testar update_book
       book = self.book_dao.find_by_title("title1")  # Hämtar boken med titel "title1"
       book.description = "new description"
       self.book_dao.update_book(book)  # Uppdaterar boken
       updated_book = self.book_dao.find_by_title("title1")  # Hämtar boken igen
       assert updated_book.description == "new description"  # Kollar att ändringen har sparats
       
   def test_delete_book(self):  # Testar delete_book
       book = self.book_dao.find_by_title("title1")  # Hämtar boken med titel "title1"
       assert book != None  # Kontrollera att boken faktiskt finns
       self.book_dao.delete_book(book)  # Tar bort boken
       deleted_book = self.book_dao.find_by_title("title1")  # Försöker hämta boken igen
       assert deleted_book == None  # Kollar att boken är borttagen

@pytest.fixture # Skapar en fixture
def book_dao(): # Skapar en funktion som returnerar book_dao
    book_dao = BookDAO(":memory:") # Använder en temporär databas i minnet
    for i in range(1, 4): # Skapar tre böcker
        book = Book(f"title{i}", f"description{i}", f"author{i}")  # Skapar en bok
        book_dao.insert_book(book) # Lägger till boken i databasen
    yield book_dao # Returnerar book_dao
    book_dao.clear_table()  # Rensar databasen
    book_dao.close() # Stänger anslutningen till databasen