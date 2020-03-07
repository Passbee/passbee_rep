from random import randint


l = []

i = 0

while len(l) != 10:
    l.append(randint(1, 100))

maxEl = l[0]

while i < len(l):
    if l[i] > maxEl:
        maxEl = l[i]
    i += 1

print(l, '\n', maxEl)