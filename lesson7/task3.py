"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter.

For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""
while True:
    num_list = []
    while len(num_list) != 2:
        numbers = int(input('Input your number: '))
        num_list.append(numbers)
    operation = input('Choose one operation out of these: + - *\nYour choice: ')
    if operation != '+' and operation != '-' and operation != '*':
        print('please use only available symbols')
        break

    def make_operation(arithmetic_operation, *args):
        for item in args[1:]:
            a = args[0]
            b = args[1]
            if arithmetic_operation == '+':
                return a + b
            if arithmetic_operation == '-':
                return a - b
            if arithmetic_operation == '*':
                return a * b

    print(make_operation(operation, *num_list))

    break
