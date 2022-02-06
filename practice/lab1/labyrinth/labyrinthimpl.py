import math
from typing import Iterator, List, Tuple, Optional
from .cell import Cell


class LabyrinthImplementation:
    def __init__(self, field: List[List[Cell]]):
        self.field: List[List[Cell]] = field
        self.start, self.finish = self.find_start_and_end_cells()

    def __iter__(self) -> Iterator[Cell]:
        for row in self.field:
            for cell in row:
                yield cell

    def __str__(self) -> str:
        labyrinth = '\n'
        for row in self.field:
            for cell in row:
                if cell.distance is None:
                    labyrinth += f' {cell.get_cell_type()} '
                else:
                    labyrinth += f' {str(cell.distance)} '
            labyrinth += '\n'
        return labyrinth

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

    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        if 0 <= x < len(self.field) and 0 <= y < len(self.field[x]):
            return self.field[x][y]

    def find_cell_neighbours(self, cell: Cell) -> List[Cell]:
        coordinates_list = [(cell.x, cell.y - 1), (cell.x + 1, cell.y), (cell.x, cell.y + 1), (cell.x - 1, cell.y)]
        cells: List[Cell] = []
        for coordinate in coordinates_list:
            cell: Cell = self.get_cell(coordinate[0], coordinate[1])
            if not cell.is_border():
                cells.append(cell)
        return cells

    def calculate_distance(self) -> None:
        def _get_checked_cells_list(new_cells: List[Cell]) -> List[Cell]:
            checked_cells: List[Cell] = []
            for new_cell in new_cells:
                if new_cell not in checked_cells and new_cell.checked is False:
                    checked_cells.append(new_cell)
            return checked_cells

        distance: int = 0
        checked_cells: List[Cell] = [self.start]
        while len(checked_cells) != 0:

            new_cells: List[Cell] = []
            for cell in checked_cells:
                cell.distance = distance
                cell.checked = True
                neighbours_cells = self.find_cell_neighbours(cell)
                new_cells.extend(neighbours_cells)
            checked_cells = _get_checked_cells_list(new_cells)
            distance += 1

            if self.finish.distance is not None:
                break

    def find_route(self):
        def _find_cell_with_min_distance(cells: List[Cell]) -> Cell:
            min_distance_cell: Optional[Cell] = None
            min_distance = math.inf
            for cell in cells:
                if isinstance(cell.distance, int):
                    if cell.distance < min_distance:
                        min_distance = cell.distance
                        min_distance_cell = cell
            return min_distance_cell

        if self.finish.distance is None:
            raise ValueError('Еhe route to the finish line was not found')
        current_cell: Cell = self.finish
        while current_cell != self.start:
            neighbours_cell = self.find_cell_neighbours(current_cell)
            if current_cell is not self.finish:
                current_cell.cell_type = ROUTE
            current_cell = _find_cell_with_min_distance(neighbours_cell)