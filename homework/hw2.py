#   TASK 1
from datetime import date

name = input("Hi, what's your name?\n")
today = date.today()
print('Nice to meet you!')
print(f"Good day {name}! {today} is a perfect day to learn some python.")
print('-' * 100)
#   TASK 2
name1 = 'Ilya Pasichnyk'
namefrst = name1[:5]
namelast = name1[5:]
print('So you are %s %s, that\'s great' % (namefrst, namelast))
#   TASK 3
print('Hi, my name is Calc!)\nThings that I can do: + - / * ** % //')
a = 2
b = 5

print(a + b, '\t', a - b, '\t', a / b, '\t', a * b, '\t', a ** b, '\t', a % b, '\t', a // b)
