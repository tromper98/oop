from typing import Dict, Callable, Optional
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

    def __init__(self, calculator: Calculator):
        self._calculator = calculator
        self._actions = self._get_actions()

    def execute_command(self, user_input: str) -> bool:
        parser = CommandLineParser.parse_command_line(user_input)

        if self._has_action(parser.command):
            return self._actions[parser.command](parser.expr)

        print('Invalid command')

    def _create_var(self, expr: Expression) -> None:
        if expr.right_operands or expr.operation:
            print('Command "var" has only one parameter: variable name')
            return

        self._calculator.create_variable(expr.left_operand)
        ...

    def _set_var_value(self, expr: Expression) -> None:
        if len(expr.right_operands) != 1:
            print(f'Too much operands for command "let" ')
            return

        self._calculator.set_variable_value(expr.left_operand, expr.right_operands[0])

    def _create_fn(self,) -> None:
        ...

    def _print_by_identifier(self, name: str) -> None:
        ...

    def _print_vars(self) -> None:
        ...

    def _print_funcs(self) -> None:
        ...

    def _exit(self) -> None:
        ...

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
