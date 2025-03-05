#Sauda del:

from book_dao import BookDAO
from book import Book
import pytest
 
class TestBookDao:
   def setup_method(self):
       self.book_dao = BookDAO(":memory:")
       self.book_dao.create_table()
       for i in range(1, 4): 
           book = Book(f"title{i}", f"description{i}", f"author{i}")
           self.book_dao.insert_book(book)

     
   def teardown_method(self):   
       self.book_dao.clear_table()
       self.book_dao.close()
       
#Habbenurs del:        
   def test_get_all_books(self):
       books = self.book_dao.get_all_books()
       assert len(books) == 3  
 
   def test_insert_book(self):
       book = Book("title4", "description4", "author4") 
       book_id = self.book_dao.insert_book(book) 
       assert book_id == 4 
       books = self.book_dao.get_all_books() 
       assert len(books) == 4  
 
   def test_find_by_title(self):
       book = self.book_dao.find_by_title("title1") 
       assert book != None
       assert book.description == "description1"
 
   def test_update_book(self): 
       book = self.book_dao.find_by_title("title1") 
       book.description = "new description"
       self.book_dao.update_book(book) 
       updated_book = self.book_dao.find_by_title("title1") 
       assert updated_book.description == "new description" 
       
   def test_delete_book(self):
       book = self.book_dao.find_by_title("title1")
       assert book != None
       self.book_dao.delete_book(book)
       deleted_book = self.book_dao.find_by_title("title1")
       assert deleted_book == None 