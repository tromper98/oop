class RationalException(Exception):
    ...


class ZeroDenominatorError(RationalException):
    def __init__(self):
        print('Denominator of rational can\t be 0')


class InvalidOperandType(RationalException):
    def __init__(self, operand):
        print(f'Invalid operator type. Except [Rational, int], but {type(operand)} were given')
