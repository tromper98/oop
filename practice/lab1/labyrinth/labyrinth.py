import os
import math
import sys
from argparse import ArgumentParser
from typing import List, Tuple, Optional

BORDER = '#'
PASSABLE = ' '
START = 'A'
FINISH = 'B'
ROUTE = '.'

CELL_CODES = {
    BORDER: -2,
    PASSABLE: -1,
    START: 0,
    FINISH: -3,
    ROUTE: -4
}


class ProgramArguments:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def parse_command_line():
    parser = ArgumentParser()
    parser.add_argument('input_file_path', help='Path to the labyrinth file')
    parser.add_argument('output_file_path', help='Path to the file where the found route will be saved')
    args = parser.parse_args()
    return ProgramArguments(args.input_file_path, args.output_file_path)


def encode_labyrinth_cell(cell: str) -> int:
    return CELL_CODES.get(cell)


def decode_labyrinth_cell(number: int) -> str:
    for key, code in CELL_CODES.items():
        if code == number:
            return key
    return ' '


# Можно возвращать класс
def find_start_and_finish_cell(labyrinth: List[List[int]]) -> Optional[Tuple[Cell, Cell]]:
    start_cell: Optional[Cell] = None
    finish_cell: Optional[Cell] = None
    for i, row in enumerate(labyrinth):
        for j, cell_number in enumerate(row):
            if decode_labyrinth_cell(cell_number) == START:
                if isinstance(start_cell, tuple):
                    print('More than one start point find in labyrinth')
                    return
                start_cell = Cell(i, j)

            if decode_labyrinth_cell(cell_number) == FINISH:
                if isinstance(finish_cell, tuple):
                    print('More than one finish point find in labyrinth')
                    return
                finish_cell = Cell(i, j)

    if not start_cell:
        print('Start point not found in labyrinth')
        return
    if not finish_cell:
        print('Finish point not found in labyrinth')
        return

    return start_cell, finish_cell


def find_cell_neighbours(labyrinth: List[List[int]], cell: Cell) -> List[Cell]:
    def _labyrinth_cell_exists(cell: Cell) -> bool:
        return 0 <= cell.x <= len(labyrinth) - 1 and 0 <= cell.y <= len(labyrinth[cell.x]) - 1

    def _filter_passable_cells(cell: Cell) -> Cell:
        if _labyrinth_cell_exists(cell):
            cell_code: int = labyrinth[cell.x][cell.y]
            if cell_code != CELL_CODES.get(BORDER):
                return cell

    x, y = cell.x, cell.y
    all_neighbours: List[Cell] = [Cell(x, y - 1), Cell(x + 1, y), Cell(x, y + 1), Cell(x - 1, y)]  # Можно назвать all_neighbours
    neighbours_cells: List[Cell] = list(filter(_filter_passable_cells, all_neighbours))
    return neighbours_cells


# Кортеж может служчить источником ошибок. Легко перепутать строки со столбцами
def start_wave(labyrinth: List[List[int]], start_cell: Cell, finish_cell: Cell) -> List[List[int]]:

    def _find_unchecked_cell_neighbours(cell: Cell) -> List[Cell]:
        def _filter_unchecked_cells(cell: Cell):
            cell_number = labyrinth[cell.x][cell.y]
            if cell_number == CELL_CODES.get(PASSABLE) or cell_number == CELL_CODES.get(FINISH):
                return cell

        all_neighbours: List[Cell] = find_cell_neighbours(labyrinth, cell)
        unchecked_neighbours_cells = list(filter(_filter_unchecked_cells, all_neighbours))
        return unchecked_neighbours_cells

    distance: int = 0
    current_wave: List[Cell] = [start_cell]
    next_wave: List[Cell] = []

    while len(current_wave) != 0:
        for i in range(len(current_wave)):
            selected_cell: Cell = current_wave[i]
            labyrinth[selected_cell.x][selected_cell.y] = distance

            neighbours_cells = _find_unchecked_cell_neighbours(selected_cell)
            next_wave.extend(neighbours_cells)

        current_wave = next_wave.copy()
        next_wave.clear()
        distance += 1

        if labyrinth[finish_cell.x][finish_cell.y] > 0:
            break
    return labyrinth


def find_route(labyrinth: List[List[int]], start_cell: Cell, finish_cell: Cell) -> List[List[int]]:
    def _find_cell_with_min_distance(cells: List[Cell]) -> Cell:
        for cell in cells:
            cell_distance = labyrinth[cell.x][cell.y]
            if cell_distance == distance - 1:
                return cell

    def _route_to_cell_exists(cell: Cell) -> bool:
        return True if labyrinth[cell.x][cell.y] > 0 else False

    if not _route_to_cell_exists(finish_cell):
        return labyrinth

    current_cell: Cell = finish_cell
    while current_cell != start_cell:
        neighbours_cells: List[Cell] = find_cell_neighbours(labyrinth, current_cell)
        x, y = current_cell.x, current_cell.y
        distance = labyrinth[x][y]

        if current_cell == finish_cell:
            labyrinth[x][y] = CELL_CODES.get(FINISH)
        else:
            labyrinth[x][y] = CELL_CODES.get(ROUTE)

        current_cell = _find_cell_with_min_distance(neighbours_cells)
    return labyrinth


def find_route_in_labyrinth(labyrinth: List[List[int]]) -> Optional[List[List[int]]]:
    cells: Optional[tuple] = find_start_and_finish_cell(labyrinth)
    if isinstance(cells, tuple):
        start_cell, finish_cell = cells
    else:
        return
    labyrinth: List[List[int]] = start_wave(labyrinth, start_cell, finish_cell)
    return find_route(labyrinth, start_cell, finish_cell)


def get_labyrinth_from_file(file_path: str):
    labyrinth: List[List[int]] = []
    with open(os.path.abspath(file_path), 'r', encoding='utf-8') as file:
        for row in file:
            field_row: List[int] = []
            for cell in row:
                field_row.append(encode_labyrinth_cell(cell))
            labyrinth.append(field_row)
    return labyrinth


def save_labyrinth_to_file(labyrinth: List[List[int]], output_file_path: str):
    with open(os.path.abspath(output_file_path), 'w', encoding='utf-8') as file:
        for row in labyrinth:
            for number in row:
                file.write(decode_labyrinth_cell(number))
            file.write('\n')


def find_way_in_labyrinth() -> None:
    args: ProgramArguments = parse_command_line()

    if not os.path.isfile(args.input_file):
        print(f'File {args.input_file} doesn\'t not exists')
        sys.exit(1)

    labyrinth: List[List[int]] = get_labyrinth_from_file(args.input_file)
    labyrinth = find_route_in_labyrinth(labyrinth)

    if not labyrinth:
        sys.exit(1)

    save_labyrinth_to_file(labyrinth, args.output_file)
    sys.exit(0)


if __name__ == "__main__":
    find_way_in_labyrinth()
