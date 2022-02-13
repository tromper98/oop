from argparse import ArgumentParser
from typing import List

import os
from impl import LabyrinthImplementation
from impl.cell import Cell


class ProgramArgument:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file


class Labyrinth(LabyrinthImplementation):
    def __init__(self, labyrinth: List[List[Cell]]) -> None:
        super().__init__(labyrinth)

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


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('input_file_path', help='Path to the labyrinth file')
    parser.add_argument('output_file_path', help='Path to the file where the found route will be saved')
    args = parser.parse_args()
    return ProgramArgument(args.input_file_path, args.output_file_path)


def find_way_in_labyrinth() -> None:
    args: ProgramArgument = parse_arguments()
    labyrinth = Labyrinth.from_file(args.input_file)
    labyrinth.find_route_in_labyrinth()
    labyrinth.save_labyrinth_to_file(args.output_file)


if __name__ == "__main__":
    find_way_in_labyrinth()
