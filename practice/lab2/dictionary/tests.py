import pytest

from dictionary import *


def test_parse_dict_string():
    string = 'слово : translate'
    excepted = ('слово', 'translate')
    res = parse_dict_string(string)
    assert res == excepted


def test_check_translate_exists():
    data = ['кот: cat', 'собака: dog', 'мышь: mouse']
    assert get_translate('мышь', data) == True
    assert get_translate('волк', data) == False


