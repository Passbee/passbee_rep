class Square:
    def square_nums(self):
        copy = self.num_list[:]
        for index in range(len(self.num_list)):
            copy[index] **= 2
        return f'{self.num_list} -> {copy}'


class Filter:
    def filter_leaps(self):
        copy = self.num_list[:]
        for year in self.num_list:
            if year not in range(0, 2021, 4):
                copy.remove(year)
        return f'{self.num_list} -> {copy}'


class RemovePositives:
    def remove_positives(self):
        copy = self.num_list[:]
        for item in self.num_list:
            if item > 0:
                copy.remove(item)
        return f'{self.num_list} -> {copy}'


class Mathematician(Square, Filter, RemovePositives):
    def __init__(self, num_list):
        self.num_list = num_list


if __name__ == '__main__':
    m = Mathematician([1, 2, 3, 4, 5])
    print(m.square_nums())
    m = Mathematician([1884, 1990, 1998, 2000, 2004, 2005, 2006, 2008, 2010, 2015, 2020])
    print(m.filter_leaps())
    m = Mathematician([-1, -2, 15, 34, 6, 5])
    print(m.remove_positives())
