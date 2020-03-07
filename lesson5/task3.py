l = []
i = 0
l_divisible7 = []
while len(l) != 100:
    l.append(i + 1)
    if not l[i] % 7 and l[i] % 5:
        l_divisible7.append(l[i])
    i += 1
print(l_divisible7)
