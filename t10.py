class Book:
    def __init__(self, name, page_count, price) -> None:
        self.name = name
        self.page_count = page_count
        self.price = price

def next(book):
    book.page_count += 10
    if book.page_count >= 100:
        book.page_count /= 2

book_list = []

for i in range(5):
    name = input(f"{i+1}-kitob nomini kiriting: ")
    page_count = int(input(f"{i+1}-kitibning saxifasini kiriting: "))
    price = int(input(f"{i+1}-kitobning narxini kiriting: "))
    
    book = Book(name, page_count, price)
    book_list.append(book)

for book in book_list:
    next(book)
    print(f"""
Kitob nomi: {book.name},
Saxifasi: {book.page_count},
Narxi: {book.price}""")
