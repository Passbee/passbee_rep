"""
Task 1

A simple function.

Create a simple function called favorite_movie,
 which takes a string containing the name of your favorite movie.

The function should then print “My favorite movie is named {name}”.
"""
my_string = input('Input your favorite movie: ')


def favorite_movie(movie_name):
    print(f'"My favorite movie is named {movie_name}".')


favorite_movie(my_string)
