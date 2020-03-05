from random import randint

print('It\'s quizzing time!!!')

while True:
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    summ_num = num1 + num2
    quiz_quess = int(input(f'So today\'s question is...\nGive answer for this mathematical expression: {num1} + {num2}\nYour answer: '))
    if quiz_quess == summ_num:
        print('Yep, that\'s the right one!) Congratulation!')
        break
    else:
        print(f'You were so close(\nRight answer was {summ_num}\nMaybe you\'ll get lucky another time?')