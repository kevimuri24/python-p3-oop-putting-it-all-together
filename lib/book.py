#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title  # This will call the setter for title
        self.page_count = page_count  # This will call the setter for page_count
        
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title="And Then There Were None"):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError ("Title must be a string")
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count='not an integer'):
        if isinstance(page_count, int) and page_count > 0:  # Ensure it's a positive integer
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
book = Book("Factflullness", 600)
print(book.title)  
print(book.page_count)
print(book.turn_page())