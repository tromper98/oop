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

    def create_function(self, func_name: str, variables: List[str], operations: List[str]) -> None:
        if not self._has_function(func_name):
            function = Function(func_name, variables, operations)
            self._functions.append(function)
            return

        print(f'Can\t create function {func_name} because function with same name already exists')

    def get_function_result(self, func_name: str) -> Optional[float]:
        if not self._has_function(func_name):
            print(f'Function {func_name} doesn\'t exist')
            return

        function = self._get_function_by_name(func_name)
        result: Optional[float] = self._calculate_function_result(function)
        return result

    def print_variable(self, variable: str) -> None:
        if not self._has_variable(variable):
            print(f'Variable {variable} does not exist')

        value: Optional[float] = self._get_variable_value(variable)
        print(value)

    def print_all_variables(self) -> None:
        for variable in self._variables:
            value = self._get_variable_value(variable)
            print(value)

    def _calculate_function_result(self, function: Function) -> Optional[float]:
        result: Optional[float] = self._get_variable_value(function.variables[0])
        if not result:
            return None

        for i, operation in enumerate(function.operations):
            second_value = self._get_variable_value(function.variables[i + 1])
            if not second_value:
                return None

            operation_result = self.__perform_operation(operation, result, second_value)

            if not operation_result:
                return None

            result = operation_result

        return result

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

    def _get_function_by_name(self, func_name) -> Function:
        for function in self._functions:
            if function.name == func_name:
                return function

    def _has_variable(self, variable: str) -> bool:
        return variable in self._variables.keys()

    def _has_function(self, func_name: str) -> bool:
        return func_name in [function.name for function in self._functions]

    def __try_create_variable_from_number(self, variable: str, value: float) -> None:
        if not self._has_variable(variable):
            self._variables[variable] = value
            return

        print(f'Can\'t add variable "{variable}" because variable with same name has already exist')

    def __try_create_variable_from_other_variable(self, new_variable: str, other_variable: str) -> None:
        if self._has_variable(other_variable):
            value = self._get_variable_value(other_variable)
            self._variables[new_variable] = value
            return

        print(f'Can\'t add variable "{new_variable}" because {other_variable} was not declared')

    def __try_create_variable_with_none_value(self, variable) -> None:
        if not self._has_variable(variable):
            self._variables[variable] = None
            return

        print(f'Can\' create variable "{variable}" because variable with same name has already exist')
