"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
"""

s = 'hello world, my name is passbee.  world, is great'
for junk_char in "%$@*.,!&?:;":
    s = s.replace(junk_char, '')
tokens = s.split()
# clean data
d = dict()
for word in tokens:
    word = word.strip()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)
