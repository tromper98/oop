from typing import Dict, List, Optional, Union, Tuple
from function import Function

from exceptions import *


class Calculator:
    _variables: Dict[str, Optional[float]]
    _functions: Dict[str, Function]

    def __init__(self):
        self._variables = {}
        self._functions = {}

    def create_variable(self, variable: str) -> None:
        if not self._has_variable(variable):
            self._variables[variable] = None
            return

        raise VariableAlreadyExistError(variable)

    def set_variable_value(self, variable: str, source: Union[float, str]) -> None:
        if not self._has_variable(variable):
            raise VariableNotFoundError(variable)

        if Calculator._is_number(source):
            self._set_variable_value_from_number(variable, float(source))
            return

        self._set_variable_value_from_another_value(variable, source)
        return

    def create_function(self, func_name: str, operands: List[str], operation: Optional[str]) -> None:
        if self._has_function(func_name):
            raise FunctionAlreadyExistError(func_name)

        function = Function(operands, operation)
        self._functions[func_name] = function

    def get_operand_by_name(self, name: str) -> Optional[float]:
        if self._has_variable(name):
            return self._variables[name]

        if self._has_function(name):
            return self.get_function_result(name)

        return None

    def get_function_result(self, func_name: str) -> Optional[float]:
        if not self._has_function(func_name):
            raise FunctionNotFoundError(func_name)

        function = self._functions[func_name]
        result: Optional[float] = self._calculate_function_result(function)
        return result

    def get_all_variables(self) -> List[Tuple[str, Optional[float]]]:
        return [(variable, value) for variable, value in self._variables.items()]

    def get_all_functions(self) -> List[Tuple[str, Optional[float]]]:
        return [(func_name, self.get_function_result(func_name)) for func_name in self._functions.keys()]

    def _calculate_function_result(self, function: Function) -> Optional[float]:
        values: List[float] = []
        for operand in function.operands:
            value = self._get_operand_result(operand)
            values.append(value)

        if None in values:
            return None

        if not function.operation:
            return values[0]

        return Calculator._perform_operation(function.operation, values[0], values[1])

    @staticmethod
    def _perform_operation(operation: str, first_value: float, second_value: float) -> Optional[float]:
        if operation == '+':
            return first_value + second_value

        if operation == '-':
            return first_value - second_value

        if operation == '*':
            return first_value * second_value

        if second_value == 0:
            raise ZeroDivisionError

        return first_value / second_value

    def get_variable_value(self, variable: str) -> Optional[float]:
        if not self._has_variable(variable):
            raise VariableNotFoundError(variable)

        return self._variables[variable]

    def _has_variable(self, variable: str) -> bool:
        return variable in self._variables.keys()

    def _has_function(self, func_name: str) -> bool:
        return func_name in self._functions.keys()

    def _set_variable_value_from_number(self, variable: str, number: float) -> None:
        if not self._has_variable(variable):
            raise VariableNotFoundError(variable)

        self._variables[variable] = number

    def _set_variable_value_from_another_value(self, target_variable: str, source_variable: str) -> None:
        if not self._has_variable(target_variable):
            raise VariableNotFoundError(target_variable)

        if not self._has_variable(source_variable):
            raise VariableNotFoundError(source_variable)

        value: float = self.get_variable_value(source_variable)
        self._variables[target_variable] = value

    def _get_operand_result(self, operand: Union[float, str]) -> Optional[float]:
        if Calculator._is_number(operand):
            return float(operand)

        if self._has_variable(operand):
            return self._variables[operand]

        if self._has_function(operand):
            function: Function = self._functions[operand]
            return self._calculate_function_result(function)

        raise OperandNotFoundError(operand)


    @staticmethod
    def _is_number(number: Union[str, float]) -> bool:
        if isinstance(number, (float, int)):
            return True
        try:
            float(number)
            return True
        except:
            return False
