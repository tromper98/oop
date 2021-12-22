from typing import List, Tuple

BORDER = '#'
PASSABLE = ' '
START = 'S'
FINISH = 'F'


class Cell:
    def __init__(self, x: int, y: int, cell_type: str):
        self._x: int = x
        self._y: int = y
        self._cell_type: str = cell_type
        self.distance: int = 0

    def is_border(self) -> bool:
        return True if self._cell_type == BORDER else False

    def is_start(self) -> bool:
        return True if self._cell_type == START else False

    def is_finish(self) -> bool:
        return True if self._cell_type == FINISH else False

    def is_passable(self) -> bool:
        return True if self._cell_type == PASSABLE else False

    def get_coords(self) -> Tuple[int, int]:
        return self._x, self._y

    def set_distance(self, distance) -> None:
        self.distance = distance


class Labyrinth:
    def __init__(self, field: List[List[Cell]]):
        self.field = field


    @staticmethod
    def from_file(filename: str):
        field: List[List[Cell]] = []
        with open(filename, 'r', encoding='utf-8') as file:
            for i, row in enumerate(file):
                field_row: List[Cell] = []
                for j, symbol in enumerate(row):
                    cell = Cell(i, j, symbol)
                    field_row.append(cell)
                field.append(field_row)
        return Labyrinth(field)
