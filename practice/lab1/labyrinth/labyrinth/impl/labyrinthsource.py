import os.path as path
from typing import List

from .cell import Cell


class LabyrinthSource:
    @staticmethod
    def save_to_file(field: List[List[Cell]], output_file_path: str):
        with open(path.abspath(output_file_path), 'w', encoding='utf-8') as file:
            for row in field:
                for cell in row:
                    file.write(cell.get_cell_type())
                file.write('\n')

    @staticmethod
    def from_file(file_path: str):
        field: List[List[Cell]] = []
        with open(path.abspath(file_path), 'r', encoding='utf-8') as file:
            for i, row in enumerate(file):
                field_row: List[Cell] = []
                for j, symbol in enumerate(row):
                    cell = Cell(i, j, symbol)
                    field_row.append(cell)
                field.append(field_row)
        return field