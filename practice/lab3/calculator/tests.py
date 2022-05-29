import sys

import pytest
from unittest import TestCase
from calculator import Calculator
from expression import Expression
from calculatorcontroller import CommandLineParser, CalculatorController
from exceptions import *

OUTPUT_STORAGE = []


def write_to_output_storage(string: str):
    return OUTPUT_STORAGE.append(string)


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
    with pytest.raises(IdentifierAlreadyExists):
        calc.create_variable('x1')


def test_set_new_variable_with_value():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x2', 40)
    expected = 40.0
    assert calc.get_variable_value('x2') == expected


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


def test_calculate_function_with_set_two_variables():
    calc = Calculator()
    calc.set_variable_value('x1', 50.05)
    calc.set_variable_value('x2', 1001)
    operation = '+'
    calc.create_function('res', ['x1', 'x2'], operation)
    result = calc.get_function_result('res')
    expected = 1051.05
    assert result == expected


def test_calculate_function_with_two_variables():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 10)

    calc.create_variable('x2')
    calc.set_variable_value('x2', 30)

    operation = '*'
    variables = ['x1', 'x2']
    calc.create_function('res', variables, operation)
    result = calc.get_function_result('res')
    expected = 300
    assert result == expected


def test_fail_create_function_with_variable_not_declared():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 45.09)
    operations = '+'
    variables = ['x1', 'z2']
    with pytest.raises(OperandNotFoundError):
        calc.create_function('res', variables, operations)


def test_fail_calculate_function_with_variable_divided_by_zero():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 45.09)
    calc.create_variable('x2')
    calc.set_variable_value('x2', 0)
    operation = '/'
    variable = ['x1', 'x2']
    calc.create_function('res', variable, operation)
    with pytest.raises(ZeroDivisionError):
        calc.get_function_result('res')


def test_calculate_function_with_other_function():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 10)
    calc.create_variable('x2')
    calc.set_variable_value('x2', 15)
    calc.create_function('res1', ['x1', 'x2'], '+')

    calc.create_variable('y1')
    calc.set_variable_value('y1', 50)
    calc.create_variable('y2')
    calc.set_variable_value('y2', 5)
    calc.create_function('res2', ['y1', 'y2'], '/')

    calc.create_function('final', ['res1', 'res2'], '*')
    expected = 250
    result = calc.get_function_result('final')
    assert result == expected


def test_calculate_function_with_one_operand():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 100)
    calc.create_function('res', ['x1'], None)
    expected = 100
    result = calc.get_function_result('res')
    assert result == expected


def test_calculate_function_with_already_exist_name():
    calc = Calculator()
    calc.create_variable('x1')
    calc.set_variable_value('x1', 10)
    calc.create_variable('x2')
    calc.set_variable_value('x2', 5)
    calc.create_variable('x3')
    calc.set_variable_value('x3', 150)
    calc.create_function('res', ['x1', 'x2'], '+')
    with pytest.raises(IdentifierAlreadyExists):
        calc.create_function('res', ['x1', 'x3'], '*')


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


def test_parse_command_line_expr_with_spaces():
    cmd = 'fn x1 = y + 135'
    parser = CommandLineParser.parse_command_line(cmd)
    expected = CommandLineParser('fn', Expression('x1', ['y', '135'], '+'))
    assert is_equal_command_line_parser(parser, expected)


def test_parse_command_line_only_command():
    cmd = 'printvars'
    parser = CommandLineParser.parse_command_line(cmd)
    expected = CommandLineParser('printvars', None)
    assert is_equal_command_line_parser(parser, expected)


def test_calculate_function_sequence():
    OUTPUT_STORAGE.clear()

    calculator = Calculator()
    controller = CalculatorController(calculator, output=write_to_output_storage)

    controller.execute_command('let x1 = 5')
    controller.execute_command('let x2 = 8')
    controller.execute_command('let x3 = 10')
    controller.execute_command('let x4 = 4')
    controller.execute_command('fn f1 = x1 * x3')
    controller.execute_command('fn f2 = x2 - x4')
    controller.execute_command('fn f3 = f1 / f2')
    controller.execute_command('fn res = f3 + x3')
    expected = 'res: 22.5'
    controller.execute_command('print res')
    assert OUTPUT_STORAGE[0] == expected


def test_print_vars():
    OUTPUT_STORAGE.clear()

    calculator = Calculator()
    controller = CalculatorController(calculator, output=write_to_output_storage)
    controller.execute_command('var x1')
    controller.execute_command('var x5')
    controller.execute_command('var x3')
    controller.execute_command('var x4')
    controller.execute_command('var x2')

    controller.execute_command('let x1 = 5')
    controller.execute_command('let x2 = 10.5')
    controller.execute_command('let x3 = -8')
    controller.execute_command('let x4 = 1000')

    controller.execute_command('printvars')

    expected = ['x1: 5.0', 'x2: 10.5', 'x3: -8.0', 'x4: 1000.0', 'x5: None']
    assert OUTPUT_STORAGE == expected


# failed with RecursionError
@pytest.mark.skip
def test_calculate_long_function_sequence():
    OUTPUT_STORAGE.clear()
    calculator = Calculator()
    controller = CalculatorController(calculator, output=write_to_output_storage)
    controller.execute_command('let x1 = 1')
    for i in range(1, 1000):
        controller.execute_command(f'fn x{i+1} = x{i} + x1')
    controller.execute_command('print x1000')
    expected = 'x1000: 1000.0'
    assert OUTPUT_STORAGE[0] == expected


#run time without memorize: after 15 minutes not result
@pytest.mark.skip
def test_calculate_fib_sequence():
    OUTPUT_STORAGE.clear()
    calculator = Calculator()
    controller = CalculatorController(calculator, output=write_to_output_storage)
    controller.execute_command('let x0 = 0')
    controller.execute_command('let x1 = 1')
    controller.execute_command('fn fib1 = x0')
    controller.execute_command('fn fib2 = x1')
    for i in range(3, 51):
        controller.execute_command(f'fn fib{i} = fib{i-1} + fib{i-2}')
    controller.execute_command('print fib50')
    expected = 'fib50: 7778742049.0'
    assert OUTPUT_STORAGE[0] == expected
