my_name = 'ilya pasichnyk'
unknown_name = str(input('|Input your name to access locked data|\n:'))
if my_name == unknown_name.lower():
    print('|Access Granted!|\n|Have a good day)|')
else:
    print('|Access Denied|')