from typing import List, Tuple

BORDER = '#'
START = 'S'
FINISH = 'F'


class Cell:
    def __init__(self, x: int, y: int, border_type: str):
        self._x: int = x
        self._y: int = y
        self._border_type: str = border_type
        self.distance: int = 0

    def is_border(self) -> bool:
        return True if self._border_type == 'border' else False

    def is_start(self) -> bool:
        return True if self._border_type == 'start' else False

    def is_finish(self) -> bool:
        return True if self._border_type == 'finish' else False

    def is_passable(self) -> bool:
        return True if self._border_type == 'passable' else False

    def get_coords(self) -> Tuple[int, int]:
        return self._x, self._y

    def set_distance(self, distance) -> None:
        self.distance = distance


class Labyrinth:
    def __init__(self, map: List[List[Cell]]):
        self.map = map

