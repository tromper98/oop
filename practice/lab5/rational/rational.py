from __future__ import annotations

from math import gcd
from exceptions import *


class Rational:
    _numerator: int
    _denominator: int
    _sign: int

    def __init__(self, numerator: int = 0, denominator: int = 1):
        if denominator == 0:
            raise ZeroDenominatorError

        if numerator < 0 or denominator < 0:
            self._sign = -1
        else:
            self._sign = 1

        self._numerator = abs(numerator)
        self._denominator = abs(denominator)

    @property
    def numerator(self):
        return self._numerator * self._sign

    @property
    def denominator(self):
        return self._denominator

    @property
    def to_float(self):
        return self.numerator / self.denominator

    def __eq__(self, other) -> bool:
        if isinstance(other, Rational):
            self_gcd = gcd(self.numerator, self.denominator)
            other_gcd = gcd(other.numerator, other.denominator)

            if self.numerator / self_gcd != other.numerator / other_gcd:
                return False

            if self.denominator / self_gcd != other.denominator / other_gcd:
                return False

            return True

    def __pos__(self):
        return Rational(self.numerator, self.denominator)

    def __neg__(self):
        return Rational(self.numerator * -1, self.denominator)

