import pytest

from vector import *


def test_multiply_numbers_mod_3_zero():
    source = [2, 3, 51, 12, 53, 20, 54, 10]
    expected = [2, 58.8, 999.6, 235.2, 53, 20, 1058.4, 10]
    result = multiply_numbers_mod_3_zero_to_even_avg(source)
    assert expected == result


def test_multiply_empty_list():
    source = []
    expected = []
    result = multiply_numbers_mod_3_zero_to_even_avg(source)
    assert expected == result


def test_multiply_not_even_number():
    source = [1, 3, 5, 7, 9, 11, 13, 15]
    expected = []
    result = multiply_numbers_mod_3_zero_to_even_avg(source)
    assert expected == result
