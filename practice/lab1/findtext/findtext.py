import os
import argparse
import sys

from dataclasses import dataclass
from typing import List, Optional, Iterator


@dataclass()
class ProgramArguments:
    def __init__(self, file_path: str, text_to_find: str) -> None:
        self.file_path = file_path
        self.text_to_find = text_to_find


def parse_command_line() -> ProgramArguments:
    parser = argparse.ArgumentParser()

    parser.add_argument('file_path', help='The path to the file in which to search for the string')
    parser.add_argument('searchable_string', help='The string to be found in the file')

    args = parser.parse_args()
    return ProgramArguments(args.file_path, args.searchable_string)


def check_file_exists(file_path: str) -> None:
    file_path = os.path.abspath(file_path)
    if os.path.isfile(file_path):
        return
    raise FileNotFoundError(f'File {file_path} doesn\'t exist')


def file_iterator(file_path: str) -> Iterator[str]:
    with open(file_path, 'r', encoding='UTF-8') as f:
        yield f.readline()

#Выделить в отдельную функцию работу с файлом и чтение данных
#Лучше сделать через Iterator
def find_text_in_file(file_path: str, searchable_string: str) -> Optional[List[int]]:
    file_path = os.path.abspath(file_path)
    rows_number: List[int] = []
    with open(file_path, "r", encoding='UTF-8') as f:
        for (i, row) in enumerate(f):
            if searchable_string in row:
                rows_number.append(i + 1)

    return rows_number


def print_array(row_numbers: List[int]) -> None:
    for number in row_numbers:
        print(number)


def find_rows_in_text_file() -> None:
    args: ProgramArguments = parse_command_line()
    check_file_exists(args.file_path)
    result: Optional[List[int]] = find_text_in_file(args.file_path, args.text_to_find)
    if len(result) > 0:
        print_array(result)
    else:
        print('Text not found')
        sys.exit(1)


if __name__ == '__main__':
    find_rows_in_text_file()
