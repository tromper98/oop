class RationalException(Exception):
    ...


class ZeroDenominatorError(RationalException):
    def __init__(self):
        print('Denominator of rational can\'t be 0')


class InvalidOperandType(RationalException):
    def __init__(self, operand):
        print(f'Invalid operator type. Except [Rational, int], but {type(operand)} were given')


class InvalidNumeratorType(RationalException):
    def __init__(self, value):
        print(f'Invalid numerator type. Except int, but {type(value)} were given')


class InvalidDenominatorType(RationalException):
    def __init__(self, value):
        print(f'Invalid denominator type. Except int, but {type(value)} were given')