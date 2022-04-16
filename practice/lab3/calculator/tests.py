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
