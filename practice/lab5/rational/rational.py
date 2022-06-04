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

    def __add__(self, other):
        if isinstance(other, int):
            new_numerator: int = self.numerator + (other * self.denominator)
            return Rational(new_numerator, self.denominator)

        if isinstance(other, Rational):
            new_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)

            new_rational = Rational(new_numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

    def __radd__(self, other):
        return self.__add__(other)

    def _normalize_rational(self):
        gcd_result = gcd(self.numerator, self.denominator)
        self._numerator = self._numerator // gcd_result
        self._denominator = self._denominator // gcd_result


