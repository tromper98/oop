from typing import Dict, List, Optional, Union, Tuple, Set

from function import Function
from exceptions import *

POSSIBLE_SYMBOLS = '1234567890abcdefghijklmnopqrstuvwxyz_'


class Calculator:
    _variables: Dict[str, Optional[float]]
    _functions: Dict[str, Function]
    _calculation_memory: Dict[str, Optional[float]]

    def __init__(self):
        self._variables = {}
        self._functions = {}
        self._calculation_memory = {}

    def create_variable(self, variable: str) -> None:
        if not Calculator._is_valid_identifier_name(variable):
            raise InvalidIdentifierName(variable)

        if not self._contains_identifier(variable):
            self._variables[variable] = None
            return

        raise IdentifierAlreadyExists(variable)

    def set_variable_value(self, variable: str, value: Union[float, str]) -> None:
        if not Calculator._is_valid_identifier_name(variable):
            raise InvalidIdentifierName(variable)

        # Если операция выполнилась неуспешно, то состояние калькулятора не должно измениться
        if Calculator._is_number(value):
            self._variables[variable] = float(value)
            return

        self._set_variable_value_from_another_value(variable, value)
        return

    def create_function(self, func_name: str, operands: List[str], operation: Optional[str]) -> None:
        if not Calculator._is_valid_identifier_name(func_name):
            raise InvalidIdentifierName(func_name)

        for operand in operands:
            if not self._contains_identifier(operand):
                raise OperandNotFoundError(operand)

        if self._contains_identifier(func_name):
            raise IdentifierAlreadyExists(func_name)

        function = Function(operands, operation)
        self._functions[func_name] = function

    def get_operand_by_name(self, name: str) -> Optional[float]:
        if self._has_variable(name):
            return self._variables[name]

        if self._has_function(name):
            return self.get_function_result(name)

        raise OperandNotFoundError(name)

    def get_function_result(self, func_name: str) -> Optional[float]:
        if not self._has_function(func_name):
            raise FunctionNotFoundError(func_name)

        self._calculation_memory = {}
        functions_stack = self._create_functions_stack(func_name)
        for i in range(len(functions_stack)):
            current_function = functions_stack.pop()
            self._calculate_function_result(current_function)

        return self._calculation_memory[func_name]

    def get_all_variables(self) -> List[Tuple[str, Optional[float]]]:
        variables = [(variable, value) for variable, value in self._variables.items()]
        variables.sort(key=lambda tup: tup[0])
        return variables

    def get_all_functions(self) -> List[Tuple[str, Optional[float]]]:
        functions = [(func_name, self.get_function_result(func_name)) for func_name in self._functions.keys()]
        functions.sort(key=lambda tup: tup[0])
        return functions

    def _calculate_function_result(self, func_name: str) -> Optional[float]:
        result: float = self._calculation_memory.get(func_name)
        if result:
            return result

        function = self._functions[func_name]
        values: List[float] = []
        for operand in function.operands:
            value = self._get_operand_result(operand)
            values.append(value)

        if None in values:
            self._calculation_memory[func_name] = None
            return None

        if not function.operation:
            result = values[0]
            self._calculation_memory[func_name] = result
            return result

        result = Calculator._perform_operation(function.operation, values[0], values[1])
        result = self._calculation_memory[func_name] = result
        return result

    @staticmethod
    def _perform_operation(operation: str, first_value: float, second_value: float) -> Optional[float]:
        if operation == '+':
            return first_value + second_value

        elif operation == '-':
            return first_value - second_value

        elif operation == '*':
            return first_value * second_value

#Проверять операцию в калькуляторе
        elif second_value == 0:
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

    def _set_variable_value_from_another_value(self, target_variable: str, source_variable: str) -> None:
        if not self._has_variable(source_variable):
            raise VariableNotFoundError(source_variable)

        value: float = self.get_variable_value(source_variable)
        self._variables[target_variable] = value

    def _get_operand_result(self, operand: Union[float, str]) -> Optional[float]:
        if self._has_variable(operand):
            return self._variables[operand]
        if not self._calculation_memory.get(operand):
            return self._calculate_function_result(operand)

        return self._calculation_memory[operand]

    def _contains_identifier(self, identifier_name: str) -> bool:
        if self._has_variable(identifier_name):
            return True

        if self._has_function(identifier_name):
            return True

        return False

    def _create_functions_stack(self, function_name: str) -> List[str]:
        functions_stack: List[str] = [function_name]
        current_functions: List[str] = [function_name]
        new_functions: List[str] = []

        while len(current_functions) != 0:
            for f_name in current_functions:
                child_functions = self._get_child_functions(f_name)
                Calculator._add_difference_to_list(new_functions, child_functions)

            functions_stack.extend(new_functions)
            current_functions = new_functions.copy()
            new_functions.clear()

        return functions_stack

    def _get_child_functions(self, function_name: str) -> List[str]:
        function: Function = self._functions[function_name]
        child_functions: List[str] = []

        for operand in function.operands:
            if self._has_function(operand):
                child_functions.append(operand)
        return child_functions

    @staticmethod
    def _is_number(number: Union[str, float]) -> bool:
        if isinstance(number, (float, int)):
            return True
        try:
            float(number)
            return True
        except:
            return False

    @staticmethod
    def _is_valid_identifier_name(string: str) -> bool:
        if string[0].isdigit():
            return False

        for symbol in string:
            if symbol not in POSSIBLE_SYMBOLS:
                return False
        return True

    @staticmethod
    def _add_difference_to_list(stack: List[str], new_values: List[str]) -> List[str]:
        stack.extend(set(new_values).difference(set(stack)))
        return stack
