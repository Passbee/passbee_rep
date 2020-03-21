a = input('Input num a: ')
b = input('Input num b: ')


def calculate(num_1, num_2):
    try:
        print((int(num_1) ** 2) / int(num_2))
    except ZeroDivisionError:
        print('Can not divide ZERO')
    except ValueError:
        if num_1.isdigit() == True and num_2.isalpha() == True:
            print('b is not a digit')
        if num_1.isdigit() == False and num_2.isdigit() == True:
            print('a is not a digit')
        if num_1.isdigit() == False and num_2.isdigit() == False:
            print('A and B are not digits')


calculate(a, b)
