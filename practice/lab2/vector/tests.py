import pytest

from vector import *


def test_multiply_numbers_mod_3_zero():
    source = [2, 3, 51, 12, 53, 20, 54, 10]
    expected = [2, 58.8, 999.6, 235.2, 53, 20, 1058.4, 10]
    process_list(source)
    assert expected == [round(n, 3) for n in source]


def test_multiply_empty_list():
    source = []
    expected = []
    process_list(source)
    assert expected == source


def test_multiply_not_even_number():
    source = [1, 3, 5, 7, 9, 11, 13, 15]
    expected = [1, 3, 5, 7, 9, 11, 13, 15]
    process_list(source)
    assert expected == source
