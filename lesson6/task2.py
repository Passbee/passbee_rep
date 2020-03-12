'''
Task 2

Input data:
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.
'''
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "jeans": 20,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

res = 0
for key, value in stock.items():
    res += prices[key] * value