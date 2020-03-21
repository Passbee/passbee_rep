x = [1, 2, 3]


def oops(num_list, n):
    for i in num_list:
        try:
            print(num_list[n] + 2)
            break
        except IndexError:
            print('oops')
            break


def main():
    try:
        oops(x, 3)
    except KeyError:
        print('oops')


main()
