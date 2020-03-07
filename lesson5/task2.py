from random import randint

l1 = []
l2 = []

i = 0

while len(l1) != 10 and len(l2) != 10:
    l1.append(randint(1, 10))
    l2.append(randint(1, 10))

l3 = list(set(l1 + l2))

print(l3)
