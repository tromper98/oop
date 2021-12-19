import os
import sys

from typing import Tuple, Optional, List

DATA = os.path.abspath('data')


def get_filename_and_searchable_string(args: list) -> Optional[Tuple]:
    def _check_params_count(count_args) -> None:
        if count_args == 3:
            return

        if count_args > 3:
            raise NotImplementedError("Too much parameters was given")

        if count_args < 3:
            raise NotImplementedError("Not enough parameters was given")

    _check_params_count(len(args))
    book: str = args[1]
    searchable_string: str = args[2]
    return book, searchable_string


def find_string_in_file(filename: str, searchable_string: str) -> List:
    rows_number: List[int] = []
    with open(os.path.join(DATA, filename), "r", encoding='UTF-8') as f:
        for (i, row) in enumerate(f):
            if searchable_string in row:
                rows_number.append(i)
    return rows_number


def output_result(row_numbers: List[int]) -> None:
    if not row_numbers:
        print('1', 'Text not found', sep='\n')
        return

    print('0')
    for number in row_numbers:
        print(number)


if __name__ == '__main__':
    file, string = get_filename_and_searchable_string(sys.argv)
    result: List[int] = find_string_in_file(file, string)
    output_result(result)
