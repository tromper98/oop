from typing import List, Iterator, Tuple, Optional

import os
import math
from cell import Cell


class Labyrinth:
    def __init__(self, field: List[List[Cell]]) -> None:
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
                if isinstance(start_cell, Cell):
                    raise ValueError('More than one start point find in labyrinth')
                start_cell = cell
            if cell.is_finish():
                if isinstance(finish_cell, Cell):
                    raise ValueError('More than one finish point find in labyrinth ')
                finish_cell = cell

        if not start_cell:
            raise ValueError('Start point not found in labyrinth')
        if not finish_cell:
            raise ValueError('Finish point not found in labyrinth')
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
            return

        current_cell: Cell = self.finish
        while current_cell != self.start:
            neighbours_cell = self.find_cell_neighbours(current_cell)
            if current_cell is not self.finish:
                current_cell.set_route_cell_type()
            current_cell = _find_cell_with_min_distance(neighbours_cell)

    def find_route_in_labyrinth(self):
        self.calculate_distance()
        self.find_route()

    def save_labyrinth_to_file(self, file_path: str):
        self.save_to_file(self.field, file_path)

    @staticmethod
    def save_to_file(field: List[List[Cell]], output_file_path: str):
        with open(os.path.abspath(output_file_path), 'w', encoding='utf-8') as file:
            for row in field:
                for cell in row:
                    file.write(cell.get_cell_type())
                file.write('\n')

    @staticmethod
    def from_file(file_path: str):
        field: List[List[Cell]] = []
        with open(os.path.abspath(file_path), 'r', encoding='utf-8') as file:
            for i, row in enumerate(file):
                field_row: List[Cell] = []
                for j, symbol in enumerate(row):
                    cell = Cell(i, j, symbol)
                    field_row.append(cell)
                field.append(field_row)
        return Labyrinth(field)
