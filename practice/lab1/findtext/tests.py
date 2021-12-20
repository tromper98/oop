from typing import List
import pytest

from findtext import *

DATA = os.path.abspath('data')


def test_file_not_exists():
    filename: str = 'notfile.txt'
    with pytest.raises(FileNotFoundError):
        check_file_exists(filename)


def test_run_program_with_two_arguments():
    params: List[str] = ['findtext.py', 'Terkin.txt']
    with pytest.raises(NotImplementedError):
        get_filename_and_searchable_string(params)


def test_run_file_with_four_arguments():
    params: List[str] = ['findtext.py', 'Terkin.txt', 'Теркин', 'four']
    with pytest.raises(NotImplementedError):
        get_filename_and_searchable_string(params)


def test_success_find_strings_in_file():
    params: List[str] = ['findtext.py', 'Terkin.txt', 'Теркин']
    expected: List[int] = [62, 68, 114, 116, 123, 150, 160, 208, 209,
                           210, 211, 226, 237, 257, 276, 334, 343
                           ]
    filename, search_string = get_filename_and_searchable_string(params)
    check_file_exists(filename)
    result = find_string_in_file(filename, search_string)

    assert all([a == b for a, b in zip(result, expected)])


def test_no_one_string_found_in_file():
    params: List[str] = ['findtext.py', 'Ko vsemy.txt', 'Меня нет']
    expected: List = []
    filename, search_string = get_filename_and_searchable_string(params)
    check_file_exists(filename)
    result = find_string_in_file(filename, search_string)

    assert result == expected
