from random import choice
string = input('Hi!\nInput your string, and i\'ll choose one letter from it)\n')
random_letter = choice(string)
print(f'So i chose letter - |{random_letter}|')
