from random import randint

while True:
    ran_num = randint(1, 5)
    guess_num = int(input('Lets play guessing game!\nInput your number: '))
    if ran_num == guess_num:
        print('Wow! You guessed my number! Congrats!')
        break
    else:
        print('Uh, that\'s bad(((\nYou failed please try again)')
