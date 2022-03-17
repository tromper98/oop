import os
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


#Лучше назвать coordinate
class Coord:
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


def find_start_and_finish_cell(labyrinth: List[List[int]]) -> Optional[Tuple[Coord, Coord]]:
    start_cell: Optional[Coord] = None
    finish_cell: Optional[Coord] = None
    for i, row in enumerate(labyrinth):
        for j, cell_code in enumerate(row):
            if decode_labyrinth_cell(cell_code) == START:
                if isinstance(start_cell, Coord):
                    print('More than one start point find in labyrinth')
                    return
                start_cell = Coord(i, j)

            if decode_labyrinth_cell(cell_code) == FINISH:
                if isinstance(finish_cell, Coord):
                    print('More than one finish point find in labyrinth')
                    return
                finish_cell = Coord(i, j)

    if not start_cell:
        print('Start point not found in labyrinth')
        return
    if not finish_cell:
        print('Finish point not found in labyrinth')
        return

    return start_cell, finish_cell


def find_cell_neighbours(labyrinth: List[List[int]], cell: Coord) -> List[Coord]:
    def _labyrinth_cell_exists(cell: Coord) -> bool:
        return 0 <= cell.x <= len(labyrinth) - 1 and 0 <= cell.y <= len(labyrinth[cell.x]) - 1

    def _filter_passable_cells(cell: Coord) -> Coord:
        if _labyrinth_cell_exists(cell):
            cell_code: int = labyrinth[cell.x][cell.y]
            if cell_code != CELL_CODES.get(BORDER):
                return cell

    x, y = cell.x, cell.y
    all_neighbours: List[Coord] = [Coord(x, y - 1), Coord(x + 1, y), Coord(x, y + 1), Coord(x - 1, y)]  # Можно назвать all_neighbours
    neighbours_cells: List[Coord] = list(filter(_filter_passable_cells, all_neighbours))
    return neighbours_cells


# Кортеж может служчить источником ошибок. Легко перепутать строки со столбцами
def start_wave(labyrinth: List[List[int]], start_cell: Coord, finish_cell: Coord) -> List[List[int]]:

    def _find_unchecked_cell_neighbours(cell: Coord) -> List[Coord]:
        def _filter_unchecked_cells(cell: Coord):
            cell_number = labyrinth[cell.x][cell.y]
            if cell_number == CELL_CODES.get(PASSABLE) or cell_number == CELL_CODES.get(FINISH):
                return cell

        all_neighbours: List[Coord] = find_cell_neighbours(labyrinth, cell)
        unchecked_neighbours_cells = list(filter(_filter_unchecked_cells, all_neighbours))
        return unchecked_neighbours_cells

    distance: int = 0
    current_wave: List[Coord] = [start_cell]
    next_wave: List[Coord] = []

    while len(current_wave) != 0:
        for i in range(len(current_wave)):
            selected_cell: Coord = current_wave[i]
            labyrinth[selected_cell.x][selected_cell.y] = distance

            neighbours_cells = _find_unchecked_cell_neighbours(selected_cell)
            next_wave.extend(neighbours_cells)

        current_wave = next_wave.copy()
        next_wave.clear()
        distance += 1

        if labyrinth[finish_cell.x][finish_cell.y] > 0:
            break
    return labyrinth


def find_route(labyrinth: List[List[int]], start_cell: Coord, finish_cell: Coord) -> List[List[int]]:
    def _find_cell_with_min_distance(cells: List[Coord]) -> Coord:
        for cell in cells:
            cell_distance = labyrinth[cell.x][cell.y]
            if cell_distance == distance - 1:
                return cell

    def _route_to_cell_exists(cell: Coord) -> bool:
        return True if labyrinth[cell.x][cell.y] > 0 else False

    if not _route_to_cell_exists(finish_cell):
        return labyrinth

    current_cell: Coord = finish_cell
    while current_cell != start_cell:
        neighbours_cells: List[Coord] = find_cell_neighbours(labyrinth, current_cell)
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


if __name__ == "__main__":
    find_way_in_labyrinth()
