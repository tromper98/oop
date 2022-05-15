import pytest
from unittest import TestCase
from calculator import Calculator
from expression import Expression
from calculatorcontroller import CommandLineParser
from exceptions import *


def is_equal_expression(target_expr: Expression, destination_expr: Expression) -> bool:
    if target_expr is None and destination_expr is None:
        return True

    if target_expr.left_operand != destination_expr.left_operand:
        return False

    if target_expr.right_operands != destination_expr.right_operands:
        return False

    if target_expr.operation != destination_expr.operation:
        return False

    return True


def is_equal_command_line_parser(target_parser: CommandLineParser, destination_parser: CommandLineParser) -> bool:
    if target_parser.command != destination_parser.command:
        return False

    if not is_equal_expression(target_parser.expr, destination_parser.expr):
        return False

    return True


def test_create_new_variables():
    calc = Calculator()
    calc.create_variable('x1')
    calc.create_variable('x2')

    expected = {
        'x1': None,
        'x2': None
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_create_new_variable_from_other_variable():
    calc = Calculator()
    calc.create_variable('x1')
    calc.create_variable('x2')
    calc.set_variable_value('x1', 10)
    calc.set_variable_value('x2', 'x1')

    expected = {
        'x1': 10,
        'x2': 10
    }
    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_create_new_variable_from_non_declared_variable():
    calc = Calculator()
    calc.create_variable('x1')
    calc.create_variable('x2')
    with pytest.raises(VariableNotFoundError):
        calc.set_variable_value('x2', 'no_var')


def test_update_variable_value():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 10)
    calc.set_variable_value('x1', 50)
    expected = {'x1': 50}

    tester = TestCase()
    tester.assertDictEqual(calc._variables, expected)


def test_fail_create_existing_variable():
    calc = Calculator()
    calc.create_variable('x1')
    with pytest.raises(VariableAlreadyExistError):
        calc.create_variable('x1')


def test_fail_update_update_not_exist_variable():
    calc = Calculator()
    calc.create_variable('x1')
    with pytest.raises(VariableNotFoundError):
        calc.set_variable_value('x2', 40)


def test_get_variable_value():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 100.50)
    expected = 100.50
    result = calc.get_variable_value('x1')
    assert result == expected


def test_fail_get_not_declared_variable_value():
    calc = Calculator()
    calc.create_variable('x1')
    calc.create_variable('x2')
    with pytest.raises(VariableNotFoundError):
        calc.get_variable_value('y1')


def test_calculate_function():
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


def test_fail_create_function_with_variable_not_declared():
    calc = Calculator()
    calc.create_variable('x1', 45.09)
    calc.create_variable('x2', 25.10)
    calc.create_variable('x3', 30)
    operations = ['+', '-', '*']
    variables = ['x1', 'x2', 'x3', 'z2']
    calc.create_function('res', variables, operations)
    result = calc.get_function_result('res')
    assert result is None


def test_fail_calculate_function_with_variable_divided_by_zero():
    calc = Calculator()
    calc.create_variable('x1', 45.09)
    calc.create_variable('x2', 0)
    operations = ['/']
    variable = ['x1', 'x2']
    calc.create_function('res', variable, operations)
    result = calc.get_function_result('res')
    assert result is None


def test_create_function_with_already_exist_name():
    calc = Calculator()
    calc.create_variable('x1', 10)
    calc.create_variable('x2', 5)
    calc.create_variable('x3', 150)
    calc.create_function('res', ['x1', 'x2'], ['+'])
    calc.create_function('res', ['x1', 'x3'], ['*'])
    result = calc.get_function_result('res')
    expected = 15
    assert result == expected


def test_parse_expr_only_one_operand():
    expr = 'x1'
    parsed_expr = Expression.parse_expr(expr)
    expected = Expression('x1', None, None)
    assert is_equal_expression(parsed_expr, expected)


def test_parse_expr_with_two_operands():
    expr = 'x1=x2'
    parsed_expr = Expression.parse_expr(expr)
    expected = Expression('x1', ['x2'], None)
    assert is_equal_expression(parsed_expr, expected)


def test_parse_expr_with_operation():
    expr = 'x1=x2+5'
    parsed_expr = Expression.parse_expr(expr)
    expected = Expression('x1', ['x2', '5'], '+')
    assert is_equal_expression(parsed_expr, expected)


def test_parse_command_line_one_operand_exist():
    cmd = 'let x1'
    parser = CommandLineParser.parse_command_line(cmd)
    expected = CommandLineParser('let', Expression('x1', None, None))
    assert is_equal_command_line_parser(parser, expected)


def test_parse_command_line_with_expr():
    cmd = 'fn x1=y+135'
    parser = CommandLineParser.parse_command_line(cmd)
    expected = CommandLineParser('fn', Expression('x1', ['y', '135'], '+'))
    assert is_equal_command_line_parser(parser, expected)


def test_parse_command_line_only_command():
    cmd = 'printvars'
    parser = CommandLineParser.parse_command_line(cmd)
    expected = CommandLineParser('printvars', None)
    assert is_equal_command_line_parser(parser, expected)
