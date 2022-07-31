# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 09:30:47 2022

@author: Ziyah
"""
class Bookshelf:
    def _init_(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishing_year = publishing_year
        
    def add_book(self):
        print("Book Name : " + self.book_name)
        print("Book Author : " + self.book_author)
        print("Book Price : " + str(self.book_price))
        print("Book Publishing Year : " + str(self.book_publishing_year))
        print("Book added to Bookshelf")
        
book1 = Bookshelf("Harry Potter and the Soccerers Stone","J.K.Rowling",1928,1997)
book1.add_book()

book2 = Bookshelf("Harry Potter and the Chamber of Secrets","J.K.Rowling",9000,1998)
book2.add_book()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
