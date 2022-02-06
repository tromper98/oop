

from labirint import *


labyrinth = Labyrinth.from_file('./data/labyrinth-1.txt')
print(labyrinth)
labyrinth.calculate_distance()
print('_' * 5, 'calculate distance complete', '_' * 5)
print(labyrinth)
labyrinth.find_route()
print('_' * 5, 'draw route complete', '_' * 5)
print(labyrinth)