import pytest
from typing import Dict
from unittest import TestCase
from calculator import Calculator, Function


def test_create_new_variables():
    calc = Calculator()
    calc.create_variable('x1', 10.35)
    calc.create_variable('x2', 30.50)

    expected = {
        'x1': 10.35,
        'x2': 30.50
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_create_new_variable_from_other_variable():
    calc = Calculator()
    calc.create_variable('x1', 10)
    calc.create_variable('x2', 'x1')

    expected = {
        'x1': 10,
        'x2': 10
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_create_new_variable_from_non_declared_variable():
    calc = Calculator()
    calc.create_variable('x1', 10)
    calc.create_variable('x2', 'x3')

    expected = {
        'x1': 10
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_create_new_variable_with_none_value():
    calc = Calculator()
    calc.create_variable('x1', None)

    res = calc._get_variable_value('x1')
    assert res is None


def test_update_variable_value():
    calc = Calculator()
    calc.create_variable('x1', 10.35)
    calc.update_variable('x1', 50)
    expected = {'x1': 50}

    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_create_existing_variable():
    calc = Calculator()
    calc.create_variable('x1', 10)
    calc.create_variable('x1', 20)

    expected = {
        'x1': 10
    }

    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_update_update_not_exist_variable():
    calc = Calculator()
    calc.create_variable('x1', 20)
    result = calc.update_variable('x2', 40)
    assert result is False


def test_get_variable_value():
    calc = Calculator()
    calc.create_variable('x1', 100.50)

    expected = 100.50
    result = calc._get_variable_value('x1')
    assert result == expected


def test_fail_get_not_declared_variable_value():
    calc = Calculator()
    calc.create_variable('x1', 100.50)
    calc.create_variable('x2', 50.25)
    result = calc._get_variable_value('y1')
    assert result is None


def test_calculate_new_variable():
    calc = Calculator()
    calc.create_variable('x1', 10)
    calc.create_variable('x2', 30)
    calc.create_variable('x3', 5)
    calc.create_variable('x4', 29)
    operations = ['+', '-', '*']
    variables = ['x1', 'x2', 'x3', 'x4']
    calc.create_function('res', variables, operations)
    result = calc.get_function_result('res')
    expected = 1015
    assert result == expected


def test_fail_calculate_variable_not_declared():
    calc = Calculator()
    calc.create_variable('x1', 45.09)
    calc.create_variable('x2', 25.10)
    calc.create_variable('x3', 30)
    operations = ['+', '-', '*']
    variables = ['x1', 'x2', 'x3', 'z2']
    calc.create_function('res', variables, operations)
    result = calc.get_function_result('res')
    assert result is None


def test_fail_calculate_variable_divided_by_zero():
    calc = Calculator()
    calc.create_variable('x1', 45.09)
    calc.create_variable('x2', 0)
    operations = ['/']
    variable = ['x1', 'x2']
    calc.create_function('res', variable, operations)
    result = calc.get_function_result('res')
    assert result is None
