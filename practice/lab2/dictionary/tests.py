import os.path

import pytest
import os
from dictionary import *

DATA_DIR = os.path.abspath('data')


def test_parse_dict_string():
    string = 'слово : translate'
    excepted = ('слово', 'translate')
    res = parse_dict_string(string)
    assert res == excepted


def test_check_translate_exists():
    data = ['кот: cat', 'собака: dog', 'мышь: mouse']
    assert find_translate('мышь', data) == True
    assert find_translate('волк', data) == False


def test_create_temp_file():
    file_path = os.path.join(DATA_DIR, 'test.txt')
    temp_file_path = ''
    try:
        file = open(file_path, 'w', encoding='UTF-8')
        file.write('Test string')
        file.close()
        temp_file_path = create_temp_file(file_path)

        file = open(temp_file_path, 'r', encoding='UTF-8')
        st = file.readline()
        file.close()

        assert 'Test string' == st
    finally:
        os.remove(file_path)
        os.remove(temp_file_path)
