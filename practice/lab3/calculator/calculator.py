from typing import Dict, List
from function import Function


class Calculator:
    _variables: Dict[str, float]
    _functions: List[Function]

    def __init__(self):
        self._variables = {}
        self._functions = []

    def add_variable(self, variable: str, value: float) -> None:
        if not self._has_variable(variable):
            self._variables[variable] = value
            return

        print(f'Can\'t add variable "{variable}" because same variable because it has already been declared')

    def update_variable(self, variable: str, new_value: float) -> None:
        if not self._has_variable(variable):
            print(f'Can\'t update variable "{variable}" because variable was not declared')
            return

        self._variables[variable] = new_value

    def _has_variable(self, variable: str) -> bool:
        return variable in self._variables.keys()
