from typing import Dict, Callable, List

from calculator import Calculator


class CommandLineParser:
    _action: str
    _params: List[str]

    def __init__(self, action: str, params: List[str]) -> None:
        self._action = action
        self._params = params

    @property
    def action(self) -> str:
        return self._action

    @property
    def params(self) -> List[str]:
        return self._params

    @staticmethod
    def parse_params(params: List[str]):
        return CommandLineParser(params[0], params[1:])


class CalculatorController:
    _calculator: Calculator
    _actions: Dict[str, Callable]

    def __init__(self, calculator: Calculator):
        self._calculator = calculator
        self._actions = self._get_actions()

    def execute_command(self, user_input: str) -> bool:
        user_input: str = user_input.lstrip().rstrip()
        params: List[str] = user_input.split(' ')
        parser = CommandLineParser.parse_params(params)
        if self._has_action(parser.action):
            return self._actions[parser.action](parser.params)

        print('Invalid command')

    def _create_var(self, params: List[str]) -> None:
        if len(params) != 1:
            print(' "var" has only one parameter: variable name')
            return

        self._calculator.create_variable(params[0])
        ...

    def _set_var_value(self, value) -> None:
        ...

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
