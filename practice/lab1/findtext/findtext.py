import os
import sys
import argparse

from dataclasses import dataclass
from typing import List


@dataclass()
class TextFile:
    def __init__(self, file_path: str, searchable_string: str) -> None:
        self.file_path = file_path
        self.searchable_string = searchable_string


def get_filename_and_searchable_string() -> TextFile:
    parser = argparse.ArgumentParser()

    parser.add_argument('file_path', help='The path to the file in which to search for the string')
    parser.add_argument('searchable_string', help='The string to be found in the file')

    args = parser.parse_args()
    return TextFile(args.file_path, args.searchable_string)


def find_string_in_file(file: TextFile) -> List[int]:
    file_path = os.path.abspath(file.file_path)
    rows_number: List[int] = []
    try:
        with open(file_path, "r", encoding='UTF-8') as f:
            for (i, row) in enumerate(f):
                if file.searchable_string in row:
                    rows_number.append(i)
    except FileNotFoundError:
        print(f'File {file_path} doesn\'t exist')
        sys.exit(1)

    if not rows_number:
        print('Text not found')
        sys.exit(1)

    return rows_number


def print_array(row_numbers: List[int]) -> None:
    for number in row_numbers:
        print(number)
    sys.exit(0)


def find_rows_in_text_file() -> None:
    file = get_filename_and_searchable_string()
    result: List[int] = find_string_in_file(file)
    print_array(result)


if __name__ == '__main__':
    find_rows_in_text_file()
