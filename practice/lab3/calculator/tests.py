import pytest
from typing import Dict
from unittest import TestCase
from calculator import Calculator, Function


def test_add_new_variables():
    calc = Calculator()
    calc._add_variable('x1', 10.35)
    calc._add_variable('x2', 30.50)

    expected = {
        'x1': 10.35,
        'x2': 30.50
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_add_new_variable_with_none_value():
    calc = Calculator()
    calc._add_variable('x1', None)

    res = calc.get_variable_value('x1')
    assert res is None


def test_update_variable_value():
    calc = Calculator()
    calc._add_variable('x1', 10.35)
    calc.update_variable('x1', 50)
    expected = {'x1': 50}

    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_add_existing_variable():
    calc = Calculator()
    calc._add_variable('x1', 10)
    result = calc._add_variable('x1', 20)
    assert result is False


def test_fail_update_update_not_exist_variable():
    calc = Calculator()
    calc._add_variable('x1', 20)
    result = calc.update_variable('x2', 40)
    assert result is False


def test_get_variable_value():
    calc = Calculator()
    calc._add_variable('x1', 100.50)

    expected = 100.50
    result = calc.get_variable_value('x1')
    assert result == expected


def test_fail_get_not_declared_variable_value():
    calc = Calculator()
    calc._add_variable('x1', 100.50)
    calc._add_variable('x2', 50.25)
    result = calc.get_variable_value('y1')
    assert result is None


def test_calculate_new_variable():
    calc = Calculator()
    calc._add_variable('x1', 10)
    calc._add_variable('x2', 30)
    calc._add_variable('x3', 5)
    calc._add_variable('x4', 29)
    operations = ['+', '-', '*']
    variables = ['x1', 'x2', 'x3', 'x4']
    calc._calculate_variable('res', variables, operations)
    result = calc.get_variable_value('res')
    expected = 1015
    assert result == expected


def test_fail_calculate_variable_not_declared():
    calc = Calculator()
    calc._add_variable('x1', 45.09)
    calc._add_variable('x2', 25.10)
    calc._add_variable('x3', 30)
    operations = ['+', '-', '*']
    variables = ['x1', 'x2', 'x3', 'z2']

    result = calc._calculate_variable('res', variables, operations)
    assert result is False


def test_fail_calculate_variable_divided_by_zero():
    calc = Calculator()
    calc._add_variable('x1', 45.09)
    calc._add_variable('x2', 0)
    operations = ['/']
    variable = ['x1', 'x2']
    result = calc._calculate_variable('res', variable, operations)
    assert result is False
