import pytest
from book_dao import BookDAO  
from book import Book  

@pytest.fixture
def book_dao():
    book_dao = BookDAO(":memory:")  
    book_dao.create_table()  
    for i in range(1, 4):
        book = Book(f"title{i}", f"description{i}", f"author{i}")  
        book_dao.insert_book(book)  
    return book_dao  

def test_get_all_books(dao):  
    books = book_dao.get_all_books()  
    assert len(books) == 3  

def test_insert_book(book_dao):  
    book = Book("title4", "description4", "author4") 
    book_id = book_dao.insert_book(book)  
    assert book_id == 4  
    books = book_dao.get_all_books() 
    assert len(books) == 4  

def test_find_by_title(book_dao): 
       book = book_dao.find_by_title("title1") 
       assert book != None
       assert book.description == "description1"
    
def test_update_book(book_dao):  
    book = book_dao.find_by_title("title1")  
    book.description = "new description"
    book_dao.update_book(book)  
    updated_book = book_dao.find_by_title("title1")  
    assert updated_book.description == "new description"
    
def test_delete_book(book_dao): 
       book = book_dao.find_by_title("title1")  
       assert book != None  
       book_dao.delete_book(book)  
       deleted_book = book_dao.find_by_title("title1")  
       assert deleted_book == None  

       