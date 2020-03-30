class Mathematician:

    def square_nums(self, num_list):
        old_num_list = []
        old_num_list += num_list
        for item in range(len(num_list)):
            num_list[item] **= 2
        return f'{old_num_list} -> {num_list}'

    def remove_positives(self, num_list):
        r = num_list[:]
        for item in num_list:
            if item > 0:
                r.remove(item)
        return f'{num_list} -> {r}'

    def filter_leaps(self, year_list):
        r = year_list[:]
        for item in year_list:
            if item % 2 == 1:
                r.remove(item)
        return f'{year_list} -> {r}'


if __name__ == '__main__':
    m = Mathematician()
    print(m.square_nums([1, 2, 3, 4]))
    print(m.remove_positives([-1, -2, 15, 34, 6, 5]))
    print(m.filter_leaps([2003, 2001, 2020, 2002, 1992, 1987, 1966]))
