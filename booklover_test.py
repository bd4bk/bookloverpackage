import unittest

from booklover import BookLover

class BookLoverSuiteTest(unittest.TestCase):
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Catcher in the Rye", 4)
    test_object.add_book("Great Gatsby", 5)
    test_object.add_book("1984", 2)
    test_object.add_book("F 451", 4)    

    def test_1_add_book(self):
        self.test_object.add_book("To Kill a Mockingbird",3)
        self.assertTrue("To Kill a Mockingbird" in self.test_object.book_list.book_name.unique())

    def test_2_add_book(self):
        self.test_object.add_book("1984",2)
        count=0
        for x in self.test_object.book_list.book_name.values:
            if (x == "1984") :
                count+=1
        self.assertTrue(count == 1)
        
    def test_3_has_read(self):
        self.assertTrue(self.test_object.has_read("Great Gatsby"))

    def test_4_has_read(self):
        self.assertFalse(self.test_object.has_read("Freakonomics"))
        
    def test_5_num_books_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 5)
        test_object.add_book("Catcher in the Rye", 4)
        test_object.add_book("Great Gatsby", 2)
        self.assertTrue(test_object.num_books_read()==3)
    
    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 5)
        test_object.add_book("Catcher in the Rye", 4)
        test_object.add_book("Great Gatsby", 2)
        bool_test=True
        for x in test_object.fav_books().book_rating:
            if x <= 3:
                bool_test = False
        self.assertTrue(bool_test)
    
if __name__ == '__main__':
    unittest.main(verbosity=3)
    
