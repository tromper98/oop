class RationalException(Exception):
    ...


class ZeroDenominatorError(RationalException):
    def __init__(self):
        print('Denominator of rational can\t be 0')
