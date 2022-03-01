import os
import sys
import math
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


def find_start_and_finish_cell(labyrinth: List[List[int]]) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
    start_cell: Optional[Tuple[int, int]] = None
    finish_cell: Optional[Tuple[int, int]] = None
    for i, row in enumerate(labyrinth):
        for j, cell_number in enumerate(row):
            if decode_labyrinth_cell(cell_number) == START:
                if isinstance(start_cell, tuple):
                    print('More than one start point find in labyrinth')
                    return
                start_cell = (i, j)

            if decode_labyrinth_cell(cell_number) == FINISH:
                if isinstance(finish_cell, tuple):
                    print('More than one finish point find in labyrinth')
                    return
                finish_cell = (i, j)

    if not start_cell:
        print('Start point not found in labyrinth')
        return
    if not finish_cell:
        print('Finish point not found in labyrinth')
        return

    return start_cell, finish_cell


def labyrinth_coordinates_exists(labyrinth: List[List[int]], x: int, y: int) -> bool:
    return 0 <= x <= len(labyrinth) - 1 and 0 <= y <= len(labyrinth[x]) - 1


def find_cell_neighbours(labyrinth: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    coordinates_list: List[Tuple[int, int]] = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    cells: List[Tuple[int, int]] = []
    for coordinate in coordinates_list:
        x, y = coordinate
        if labyrinth_coordinates_exists(labyrinth, x, y):
            cell_number: int = labyrinth[x][y]
            if cell_number != CELL_CODES.get(BORDER):
                cells.append((coordinate[0], coordinate[1]))
    return cells


# Дать другое имя функции
def start_wave(labyrinth: List[List[int]],
               start_cell: Tuple[int, int],
               finish_cell: Tuple[int, int]) -> List[List[int]]:


#Меньше параметров. Labyrinth в области видимости вложенной функции
    def _find_unchecked_cell_neighbours(x: int, y: int) -> List[Tuple[int, int]]:
        neighbours_cells: List[Tuple[int, int]] = find_cell_neighbours(labyrinth, x, y)
        cells: List[Tuple[int, int]] = []
        for neighbour_cell in neighbours_cells:
            x, y = neighbour_cell
            cell_number = labyrinth[x][y]
            if cell_number == CELL_CODES.get(PASSABLE) or cell_number == CELL_CODES.get(FINISH):
                cells.append((x, y))
        return cells
    distance: int = 0
    current_wave: List[Tuple[int, int]] = [start_cell]
    next_wave: List[Tuple[int, int]] = []

    while len(current_wave) != 0:
        for i in range(len(current_wave)):
            selected_cell: Tuple[int, int] = current_wave[i]
            x, y = selected_cell
            labyrinth[x][y] = distance

            neighbours_cells = _find_unchecked_cell_neighbours(x, y)
            next_wave.extend(neighbours_cells)

        current_wave = next_wave.copy()
        next_wave.clear()
        distance += 1

        if labyrinth[finish_cell[0]][finish_cell[1]] > 0:
            break
    return labyrinth


def find_route(labyrinth: List[List[int]],
               start_cell: Tuple[int, int],
               finish_cell: Tuple[int, int]) -> List[List[int]]:

    # Меньше параметров. Labyrinth в области видимости вложенной функции
    def _find_cell_with_min_distance(cells: List[Tuple[int, int]]) -> Tuple[int, int]:

        # Можно с каждым шагом просто искать distance - 1
        min_distance_cell: Optional[Tuple[int, int]] = None
        min_distance = math.inf
        for cell in cells:
            x, y = cell
            cell_number = labyrinth[x][y]
            if cell_number >= 0:
                if cell_number < min_distance:
                    min_distance = cell_number
                    min_distance_cell = cell
        return min_distance_cell

    def _route_to_cell_exists(cell: Tuple[int, int]) -> bool:
        x, y = cell
        return True if labyrinth[x][y] > 0 else False

    if not _route_to_cell_exists(finish_cell):
        return labyrinth

    current_cell: Tuple[int, int] = finish_cell
    while current_cell != start_cell:
        neighbours_cell: List[Tuple[int, int]] = find_cell_neighbours(labyrinth, current_cell[0], current_cell[1])
        x, y = current_cell

        if current_cell == finish_cell:
            labyrinth[x][y] = CELL_CODES.get(FINISH)
        else:
            labyrinth[x][y] = CELL_CODES.get(ROUTE)

        current_cell = _find_cell_with_min_distance(neighbours_cell)
    return labyrinth


def find_route_in_labyrinth(labyrinth: List[List[int]]) -> Optional[List[List[int]]]:
    start_cell, finish_cell = find_start_and_finish_cell(labyrinth)
    if not start_cell or not finish_cell:
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
        print(f'File {args.input_file} doesn\t not exists')
        return

    labyrinth: List[List[int]] = get_labyrinth_from_file(args.input_file)
    labyrinth = find_route_in_labyrinth(labyrinth)

    if labyrinth:
        save_labyrinth_to_file(labyrinth, args.output_file)


if __name__ == "__main__":
    find_way_in_labyrinth()
