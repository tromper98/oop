from typing import Dict, Callable, Optional, List
from calculator import Calculator
from expression import Expression
from exceptions import *


class CommandLineParser:
    _command: str
    _expr: Expression

    def __init__(self, command: str, expr: Optional[Expression]) -> None:
        self._command = command
        self._expr = expr

    @property
    def command(self) -> str:
        return self._command

    @property
    def expr(self) -> Expression:
        return self._expr

    @staticmethod
    def parse_command_line(user_input: str):
        user_input: str = user_input.lstrip().rstrip()
        space_pos: int = user_input.find(' ')

        if space_pos == -1:
            return CommandLineParser(user_input, None)

        command: str = user_input[:space_pos]
        row_expr: str = user_input[space_pos + 1:]
        expr = Expression.parse_expr(row_expr)

        return CommandLineParser(command, expr)


class CalculatorController:
    _calculator: Calculator
    _actions: Dict[str, Callable]
    _output: Callable

    def __init__(self, calculator: Calculator, output: Callable = print):
        self._calculator = calculator
        self._actions = self._get_actions()
        self._output = output

    def execute_command(self, user_input: str) -> bool:
        parser = CommandLineParser.parse_command_line(user_input)

        if self._has_action(parser.command):
            return self._actions[parser.command](parser.expr)

        self._output('Invalid command')
        return True

    def _create_var(self, expr: Expression) -> bool:
        if expr.right_operands or expr.operation:
            self._output('Command "var" has only one parameter: variable_name')
            return True
        try:
            self._calculator.create_variable(expr.left_operand)
        except CalculatorException as e:
            print(e)
        return True

    def _set_var_value(self, expr: Expression) -> bool:
        if len(expr.right_operands) != 1:
            self._output(f'Too much operands for command "let" ')
            return True

        try:
            self._calculator.set_variable_value(expr.left_operand, expr.right_operands[0])
        except CalculatorException as e:
            print(e)
        return True

    def _create_fn(self, expr: Expression) -> bool:
        if not expr.right_operands:
            self._output('Can\'t create function without operands')
            return True

        try:
            self._calculator.create_function(expr.left_operand, expr.right_operands, expr.operation)
        except CalculatorException as e:
            print(e)
        return True

    def _print_by_identifier(self, expr: Expression) -> bool:
        if not expr.left_operand:
            self._output('Operand name was not passed')
        if expr.right_operands:
            self._output('Invalid params were given')
            return True
        try:
            value: Optional[float] = self._calculator.get_operand_by_name(expr.left_operand)
            self._output(f'{expr.left_operand}: {value}')
        except CalculatorException as e:
            print(e)
        return True

    def _print_vars(self, expr: Expression) -> bool:
        if expr:
            self._output('Method "printvars" doesn\'t contains any params')
            return True

        variables: List[(str, Optional[float])] = self._calculator.get_all_variables()
        for var, value in variables:
            self._output(f'{var}: {value}')

        return True

    def _print_funcs(self, expr: Expression) -> bool:
        if expr:
            self._output('Method "printfns" doesn\'t contains any params')
            return True

        funcs: List[(str, Optional[float])] = self._calculator.get_all_functions()
        for func_name, value in funcs:
            self._output(f'{func_name}: {value}')

        return True

    def _exit(self, expr: Expression) -> bool:
        if expr:
            self._output('Method "exit" doesn\'t contains any params')
            return True

        return False

    def _get_actions(self) -> Dict[str, Callable]:
        actions: Dict[str, Callable] = {
            'var': self._create_var,
            'let': self._set_var_value,
            'fn': self._create_fn,
            'print': self._print_by_identifier,
            'printvars': self._print_vars,
            'printfns': self._print_funcs,
            'exit': self._exit
        }
        return actions

    def _has_action(self, searchable_action: str) -> bool:
        return searchable_action in [action for action in self._actions.keys()]


def main():
    calc = Calculator()
    controller = CalculatorController(calc)
    while True:
        cmd: str = input('\nEnter a command: ')
        if not controller.execute_command(cmd):
            break


if __name__ == '__main__':
    main()
