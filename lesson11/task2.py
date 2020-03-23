class Mathematician:
    pass


def square_nums(num_list):
    old_num_list = []
    old_num_list += num_list
    for item in range(len(num_list)):
        num_list[item] **= 2
    print(f'{old_num_list} -> {num_list}')


def remove_positives(num_list):
    r = num_list[:]
    for item in num_list:
        if item > 0:
            r.remove(item)
    print(f'{num_list} -> {r}')


def filter_leaps(year_list):
    r = year_list[:]
    for item in year_list:
        if item % 2 == 1:
            r.remove(item)
    print(f'{year_list} -> {r}')


if __name__ == '__main__':
    m = Mathematician()
    square_nums([1, 2, 3, 4])
    remove_positives([-1, -2, 15, 34, 6, 5])
    filter_leaps([2003, 2001, 2020, 2002, 1992, 1987, 1966])
