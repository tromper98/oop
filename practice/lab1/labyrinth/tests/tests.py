
from practice.lab1.labyrinth.src.labyrinth import Labyrinth


labyrinth = Labyrinth('./data/labyrinth-1.txt')
print(labyrinth)
labyrinth.calculate_distance()
print('_' * 5, 'calculate distance complete', '_' * 5)
print(labyrinth)
labyrinth.find_route()
print('_' * 5, 'draw route complete', '_' * 5)
print(labyrinth)