#polymor

class Book:
    def __init__(self,pages):
        self.pages=pages
        
b_one = Book(100)
b_two = Book(200)

b_three = b_one + b_two
