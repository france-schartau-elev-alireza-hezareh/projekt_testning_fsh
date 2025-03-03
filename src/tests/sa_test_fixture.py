#saudas version 

import pytest
from book_dao import BookDAO  
from book import Book  
 
@pytest.fixture # Skapar en fixture
def book_dao(): # Skapar en funktion som returnerar book_daos instans
    book_dao = BookDAO(":memory:") # Skapar en instans av BookDAO
    book_dao.create_table() # Skapar en tabell
    for i in range(1, 4): # Skapar 3 böcker
        book = Book(f"title{i}", f"description{i}", f"author{i}") # Skapar en bok
        book_dao.insert_book(book)  # Lägger till boken i databasen
    return book_dao  # Returnerar book_dao
     
def test_get_all_books(book_dao): # Testar att hämta alla böcker
    books = book_dao.get_all_books() # Hämtar alla böcker
    assert len(books) == 3 # Kollar att det finns 3 böcker
    
def test_insert_book(book_dao): # Testar att lägga till en bok
    book = Book("title4", "description4", "author4") # Skapar en bok
    book_id = book_dao.insert_book(book) # Lägger till boken i databasen
    assert book_id == 4  # Kollar att bokens id är 4
    books = book_dao.get_all_books() # Hämtar alla böcker
    assert len(books) == 4 # Kollar att det finns 4 böcker
 
def test_find_by_title(book_dao): # Testar att hitta en bok med titel
       book = book_dao.find_by_title("title1") # Hittar boken med titel title1
       assert book != None # Kollar att boken inte är None
       assert book.description == "description1" # Kollar att bokens beskrivning är description1
   
def test_update_book(book_dao): # Testar att uppdatera en bok 
    book = book_dao.find_by_title("title1") # Hittar boken med titel title1
    book.description = "new description" # Uppdaterar bokens beskrivning
    book_dao.update_book(book) # Uppdaterar boken i databasen
    updated_book = book_dao.find_by_title("title1") # Hittar boken med titel title1
    assert updated_book.description == "new description" # Kollar att bokens beskrivning är new description
   
def test_delete_book(book_dao): # Testar att ta bort en bok
       book = book_dao.find_by_title("title1")  # Hittar boken med titel title1
       assert book != None  # Kollar att boken inte är None
       book_dao.delete_book(book)  # Tar bort boken från databasen
       deleted_book = book_dao.find_by_title("title1")  # Hittar boken med titel title1
       assert deleted_book == None # Kollar att boken är None