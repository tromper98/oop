from typing import Dict, List, Optional, Union
from function import Function


class Calculator:
    _variables: Dict[str, Optional[float]]
    _functions: List[Function]

    def __init__(self):
        self._variables = {}
        self._functions = []

    def create_variable(self, variable: str, value: Optional[Union[float, str]] = None) -> None:
        if isinstance(value, (float, int)):
            self.__try_create_variable_from_number(variable, value)
            return

        if isinstance(value, str):
            self.__try_create_variable_from_other_variable(variable, value)
            return

        self.__try_create_variable_with_none_value(variable)

    def update_variable(self, variable: str, new_value: float) -> bool:
        if not self._has_variable(variable):
            print(f'Can\'t update variable "{variable}" because variable was not declared')
            return False

        self._variables[variable] = new_value
        return True

    def print_variable(self, variable: str) -> None:
        if not self._has_variable(variable):
            print(f'Variable {variable} does not exist')

        value: Optional[float] = self._get_variable_value(variable)
        print(value)

    def print_all_variables(self) -> None:
        for variable in self._variables:
            value = self._get_variable_value(variable)
            print(value)

    def _calculate_variable(self, new_var_name: str,  variables: List[str], operations: List[str]) -> bool:
        new_value: Optional[float] = self._get_variable_value(variables[0])

        for i, operation in enumerate(operations):
            second_value = self._get_variable_value(variables[i + 1])
            if not new_value or not second_value:
                return False

            result = self.__perform_operation(operation, new_value, second_value)

            if not result:
                return False

            new_value = result

        self.create_variable(new_var_name, new_value)
        return True

    @staticmethod
    def __perform_operation(operation: str, first_value: float, second_value: float) -> Optional[float]:
        if operation == '+':
            return first_value + second_value

        if operation == '-':
            return first_value - second_value

        if operation == '*':
            return first_value * second_value

        if second_value == 0:
            print('Error. Division by zero')
            return None

        return first_value / second_value

    def _get_variable_value(self, variable: str) -> Optional[float]:
        if not self._has_variable(variable):
            print(f'"{variable}" the variable was not declared')
            return None

        return self._variables[variable]

    def _has_variable(self, variable: str) -> bool:
        return variable in self._variables.keys()

    def __try_create_variable_from_number(self, variable: str, value: float) -> bool:
        if not self._has_variable(variable):
            self._variables[variable] = value
            return True

        print(f'Can\'t add variable "{variable}" because variable with same name has already been declared')
        return False

    def __try_create_variable_from_other_variable(self, new_variable: str, other_variable: str) -> bool:
        if self._has_variable(other_variable):
            value = self._get_variable_value(other_variable)
            self._variables[new_variable] = value
            return True

        print(f'Can\'t add variable "{new_variable}" because {other_variable} was not declared')
        return False

    def __try_create_variable_with_none_value(self, variable) -> bool:
        if not self._has_variable(variable):
            self._variables[variable] = None
            return True

        print(f'Can\' create variable "{variable}" because variable with same name has already been declared')
