class CalculatorException(Exception):
    pass


class VariableAlreadyExistError(CalculatorException):
    def __init__(self, var_name: str):
        super().__init__(f'Variable with same name "{var_name}" already exist')


class VariableNotFoundError(CalculatorException):
    def __init__(self, var_name: str):
        super().__init__(f'Variable with name "{var_name}" doesn\'t  exist')


class FunctionAlreadyExistError(CalculatorException):
    def __init__(self, func_name: str):
        super().__init__(f'Function with name "{func_name}" already_exist')


class FunctionNotFoundError(CalculatorException):
    def __init__(self, func_name: str):
        super().__init__(f'Function with name "{func_name}" doesn\'t  exist')


class OperandNotFoundError(CalculatorException):
    def __init__(self, operand: str):
        super().__init__(f"Operand '{operand}' doesn\'t  exist")
