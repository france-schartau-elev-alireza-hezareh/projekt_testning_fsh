from src.book_dao import BookDAO
from src.book import Book
import pytest
 
 
class TestBookDao:
    def setup_method(self):
        self.book_dao = BookDAO() #skapar en instans av BookDAO
        self.book_dao.create_table() #skapar en tabell
        for i in range (1,4): #skapar 3 böcker
            book = Book(f"title{i}", f"description{i}", f"author{i}") #skapar en bok
            self.book_dao.insert_book(book) #lägger till boken i tabellen
    
    def teardown_method(self):
        self.book_dao.clear_table() #tömmer tabellen
        self.book_dao.close() #stänger anslutningen till databasen
   
    
    
    #För betyg G skriv dessa tester:
    
    # 1: Hämta alla böcker
    
    def test_get_all_books(self): #testar get_all_books
        books = self.book_dao.get_all_books() #hämtar alla böcker
        assert len(books) == 3 #kollar att det finns 3 böcker i listan  
        for i in range(1,4): #loopar igenom böckerna kollar att böckerna har rätt värden
            assert books[i-1].title == f"title{i}"
            assert books[i-1].description == f"description{i}"
            assert books[i-1].author == f"author{i}"
            assert books[i-1].id == i #kollar att böckerna har rätt id
    
        
    # 2: Lägg till en ny bok
    
    def test_add_new_book(self): #testar insert_book
        book = Book("title", "description", "author") #skapar en bok
        book_id = self.book_dao.insert_book(book) #lägger till boken i tabellen
        assert book_id == 4 #kollar att boken har fått id 4
        books = self.book_dao.get_all_books() #hämtar alla böcker
        assert len(books) == 4 #kollar att det finns 4 böcker i listan
    
    
    # 3: Hämta en bok via titel och verifiera att dess beskrivning (description) stämmer med förväntat värde.
    def test_get_book_by_title(self): #testar get_book_by_title
        book = self.book_dao.get_book_by_title("title1") #hämtar boken med titel "title1"
        assert book.description == "description1" #kollar att beskrivningen stämmer
    
    # 4: Hämta en bok via titel och uppdatera bokens beskrivning, hämta den igen via titel och verifiera att ändringen har slagit igenom.
    def test_update_book_by_title(self): #testar update_book_by_title
        self.book_dao.update_book_by_title("title1", "new description") #uppdaterar boken med titel "title1"
        book = self.book_dao.get_book_by_title("title1") #hämtar boken med titel "title1"
        assert book.description == "new description" #kollar att beskrivningen har ändrats
    
    
    # 5: Hämta en bok via titel och radera boken, försök sedan hämta den och verifiera att den är == None
    def test_delete_book_by_title(self): #testar delete_book_by_title
        self.book_dao.delete_book_by_title("title1") #raderar boken med titel "title1"
        book = self.book_dao.get_book_by_title("title1") #hämtar boken med titel "title1"
        assert book == None #kollar att boken inte finns
    