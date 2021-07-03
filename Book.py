class Book:
    def __init__(self, name, author, pub_year, pages):
        self.__name = name
        self.__author = author
        self.__pub_year = pub_year
        self.__pages = pages
    def info(self):
        print('Name of the book: ' + self.__name)
        print('Author of the book: ' + self.__author)
        print('The book is published in ' + str(self.__pub_year))
        print('The book has ' + str(self.__pages) + ' pages\n')

if __name__ == "__main__":
    book_0 = Book('book0', 'auth0', 2021, 350)
    book_1 = Book('book1', 'auth1', 2015, 270)
    book_0.info()
    book_1.info()