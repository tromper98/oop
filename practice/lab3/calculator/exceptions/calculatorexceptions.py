class CalculatorException(Exception):
    pass


class VariableExistError(CalculatorException):
    def __init__(self, var_name: str):
        super().__init__(f'Variable with same name "{var_name}" already exist')


class VariableNotFoundError(CalculatorException):
    def __init__(self, var_name: str):
        super().__init__(f'Variable with name "{var_name}" doesn\'t  exist')
