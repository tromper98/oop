import os
import argparse
import sys

from dataclasses import dataclass
from typing import List, Optional


#Лучше назвать по другому ProgramArguments, Args
@dataclass()
class ProgramArguments:
    def __init__(self, file_path: str, text_to_find: str) -> None:
        self.file_path = file_path
        self.text_to_find = text_to_find


#лучше назвать parse_command_line
def parse_command_line() -> ProgramArguments:
    parser = argparse.ArgumentParser()

    parser.add_argument('file_path', help='The path to the file in which to search for the string')
    parser.add_argument('searchable_string', help='The string to be found in the file')

    args = parser.parse_args()
    return ProgramArguments(args.file_path, args.searchable_string)


#Лучше чтобы функция принимала отдельные аргументы
def find_text_in_file(file_path: str, searchable_string: str) -> Optional[List[int]]:
    file_path = os.path.abspath(file_path)
    rows_number: List[int] = []
    try:
        with open(file_path, "r", encoding='UTF-8') as f:
            for (i, row) in enumerate(f):
                if searchable_string in row:
                    rows_number.append(i + 1)
    except FileNotFoundError:
        print(f'File {file_path} doesn\'t exist')
        return None #в функции не должно быть sys.exit()

    if not rows_number:
        print('Text not found')
        return None

    return rows_number


def print_array(row_numbers: List[int]) -> None:
    for number in row_numbers:
        print(number)
    #не должно быть sys.exit()


def find_rows_in_text_file() -> None:
    args: ProgramArguments = parse_command_line()
    result: Optional[List[int]] = find_text_in_file(args.file_path, args.text_to_find)
    if isinstance(result, list):
        print_array(result)
    else:
        sys.exit(1)


if __name__ == '__main__':
    find_rows_in_text_file()
