import numpy as np
import pandas as pd

class BookLover:
    
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre, num_books = 0):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
   
    def add_book(self, book_name, rating):
        new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [rating]})
        if (book_name not in self.book_list.book_name.values):
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
    
    def has_read(self, book_name):
        return book_name  in self.book_list.book_name.values
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating.values > 3]
    

if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Catcher in the Rye", 4)
    test_object.add_book("Great Gatsby", 5)
    test_object.add_book("1984", 2)
    test_object.add_book("F 451", 4)    
    