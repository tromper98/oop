class ComplexException(Exception):
    ...


class InvalidVariableType(ComplexException):
    def __init__(self, variable):
        print(f'Invalid variable type. Float expected but {type(variable)} were given')


class InvalidOperandType(ComplexException):
    def __init__(self, operand):
        print(f'Invalid operand type. [float, Complex] expected but {type(operand)} were given')
