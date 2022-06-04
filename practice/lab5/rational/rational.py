from __future__ import annotations

from exceptions import *


class Rational:
    _numerator: int
    _denominator: int

    def __init__(self, numerator: int = 0, denominator: int = 1):
        if denominator == 0:
            raise ZeroDenominatorError

        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def to_float(self):
        return self._numerator / self._denominator

    @staticmethod
    def _find_gcd(num1: int, num2: int):
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        return num1 + num2
