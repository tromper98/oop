from typing import List, Tuple, Iterator

BORDER = '#'
PASSABLE = ' '
START = 'S'
FINISH = 'F'
ROOT = '_'


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

    def is_root(self) -> bool:
        return True if self._cell_type == ROOT else False

    def get_coordinates(self) -> Tuple[int, int]:
        return self._x, self._y

    def set_distance(self, distance) -> None:
        self.distance = distance

    def get_cell(self) -> str:
        if self.is_border():
            return BORDER

        if self.is_start():
            return START

        if self.is_finish():
            return FINISH

        if self.is_passable():
            return PASSABLE

        return ROOT


class Labyrinth:
    def __init__(self, field: List[List[Cell]]):
        self.field: List[List[Cell]] = field
        self.start, self.finish = self.find_start_and_end_cells()

    def __iter__(self) -> Iterator[Cell]:
        for row in self.field:
            for cell in row:
                yield cell

    def find_start_and_end_cells(self) -> Tuple[Cell, Cell]:
        start_cell = None
        finish_cell = None
        for cell in self:
            if cell.is_start():
                start_cell = cell
            if cell.is_finish():
                finish_cell = cell
        if not start_cell:
            raise AttributeError('Start point not found in labyrinth')
        if not finish_cell:
            raise AttributeError('Finish point not found in labyrinth')
        return start_cell, finish_cell

    def to_file(self, output_file_path: str):
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for row in self.field:
                for cell in row:
                    file.write(cell.get_cell())
                file.write('\n')

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

