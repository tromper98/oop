from typing import Dict, List, Optional
from function import Function


class Calculator:
    _variables: Dict[str, float]
    _functions: List[Function]

    def __init__(self):
        self._variables = {}
        self._functions = []

    def _add_variable(self, variable: str, value: float) -> bool:
        if not self._has_variable(variable):
            self._variables[variable] = value
            return True

        print(f'Can\'t add variable "{variable}" because same variable because it has already been declared')
        return False

    def update_variable(self, variable: str, new_value: float) -> bool:
        if not self._has_variable(variable):
            print(f'Can\'t update variable "{variable}" because variable was not declared')
            return False

        self._variables[variable] = new_value
        return True

    def _calculate_variable(self, new_var_name: str,  variables: List[str], operations: List[str]) -> bool:
        new_value: float = 0
        for i, operation in enumerate(operations):
            result = self.__perform_operation(operation, variables[i], variables[i+1])
            if not result:
                return False

            new_value += result

        self._add_variable(new_var_name, new_value)
        return True

    def __perform_operation(self, operation: str, first_var: str, second_var: str) -> Optional[float]:
        first_value: float = self.get_variable_value(first_var)
        second_value: float = self.get_variable_value(second_var)

        if not first_value or not second_value:
            return None

        if operation == '+':
            return first_value + second_value

        if operation == '-':
            return first_value - second_value

        if operation == '*':
            return first_value * second_value

        return first_value / second_value

    def get_variable_value(self, variable: str) -> Optional[float]:
        if not self._has_variable(variable):
            print(f'"{variable}" the variable was not declared')
            return None

        return self._variables[variable]

    def _has_variable(self, variable: str) -> bool:
        return variable in self._variables.keys()
