class ComplexException(Exception):
    ...


class InvalidOperandType(ComplexException):
    def __init__(self, operand):
        print(f'Invalid operand type. [float, Complex] expected but {type(operand)} were given')
