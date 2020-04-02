class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name} - was born in {self.country} on {self.birthday}\nHe is author of those books - {self.books}'

    def __str__(self):
        return self.__repr__()


class Book:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        pass

    def __str__(self):
        return self.__repr__()


class Library:

    def __init__(self, name, books, authors):
        self.name = name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f'Library name - {self.name}\nBooks in availability : {self.books}\nAuthors - {self.authors}'

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    a1 = Author('Greg Litter', 'USA', '01.03.96', ['book1', 'book2', 'book3'])
    print(a1.__str__())

    lib = Library('O\'Donald', ['book1', 'book2', 'book3'], ['author1', 'author2', 'author3'])
    print(lib.__str__())
