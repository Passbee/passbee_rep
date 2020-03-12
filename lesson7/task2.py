"""
Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


country = input('Name your desire country: ')
capital = input('Name capital of this country: ')
country_folder = {country: capital for i in range(1, 2)}
print(country_folder)
