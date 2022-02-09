from typing import List
import pytest
import subprocess
from findtext import *

DATA = os.path.abspath('data')


def test_file_not_exists():
    params = ['python', 'findtext.py', 'notfile.txt', 'а']
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert res.returncode == 1


def test_run_program_with_two_arguments():
    params: List[str] = ['python', 'findtext.py', 'Terkin.txt']
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert res.returncode == 2


def test_run_file_with_four_arguments():
    params: List[str] = ['python', 'findtext.py', 'Terkin.txt', 'Теркин', 'four']
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert res.returncode == 2


def test_success_find_strings_in_file():
    params: List[str] = ['python', 'findtext.py', 'data/Terkin.txt', 'Теркин']
    expected: List[int] = [62, 68, 114, 116, 123, 150, 160, 208, 209,
                           210, 211, 226, 237, 257, 276, 334, 343
                           ]

    res = subprocess.run(params, stdout=subprocess.PIPE)
    stdout: bytes = res.stdout
    result_list: List[int] = [int(x.decode("utf8")) for x in stdout.split(b"\r\n") if len(x)]
    assert all([a == b for a, b in zip(result_list, expected)])


def test_text_found_in_file():
    params: List[str] = ['python', 'findtext.py', 'data/Ko vsemy.txt', 'Меня нет']
    expected: str = 'Text not found'
    res = subprocess.run(params, stdout=subprocess.PIPE)
    stdout: str = ' '.join(res.stdout.decode('utf-8').split())
    assert stdout == expected
