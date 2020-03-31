class Author:
    books = []

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f'{self.name} - was born in {self.country} on {self.birthday}'

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
    books = []
    authors = []

    def __init__(self, name, *books, **authors):
        self.name = name

    def __repr__(self):
        return f'Library - {self.name}'

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    lib = Library('O\'Donalds')
    print(lib.__str__())
    a1 = Author('Greg Litter', 'USA', '01.03.96')
    print(a1.__str__())