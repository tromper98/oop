from __future__ import annotations

from math import gcd
from operator import xor
from typing import Union, Tuple

from exceptions import *


class Rational:
    _numerator: int
    _denominator: int
    _sign: int

    def __init__(self, numerator: int = 0, denominator: int = 1):
        if not isinstance(numerator, int):
            raise InvalidNumeratorType(numerator)
        if not isinstance(denominator, int):
            raise InvalidDenominatorType(denominator)

        if denominator == 0:
            raise ZeroDenominatorError

        if xor(numerator < 0, denominator < 0):
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
        if isinstance(other, int):
            return True if self.numerator == other * self.denominator else False

        if isinstance(other, Rational):
            self_gcd = gcd(self.numerator, self.denominator)
            other_gcd = gcd(other.numerator, other.denominator)

            if self.numerator / self_gcd != other.numerator / other_gcd:
                return False

            if self.denominator / self_gcd != other.denominator / other_gcd:
                return False

            return True

        raise InvalidOperandType(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __pos__(self):
        return Rational(self.numerator, self.denominator)

    def __neg__(self):
        return Rational(self.numerator * -1, self.denominator)

    def __add__(self, other: Union[Rational, int]) -> Rational:
        return Rational._add(self, other)

    def __radd__(self, other: Union[Rational, int]) -> Rational:
        return Rational._add(self, other)

    def __sub__(self, other: Union[Rational, int]) -> Rational:
        return Rational._sub(self, other)

    def __rsub__(self, other: Union[Rational, int]) -> Rational:
        return Rational._sub(other, self)

    def __mul__(self, other: Union[Rational, int]) -> Rational:
        return Rational._mul(self, other)

    def __rmul__(self, other: Union[Rational, int]) -> Rational:
        return Rational._mul(self, other)

    def __truediv__(self, other: Union[Rational, int]) -> Rational:
        if other == 0:
            raise ZeroDivisionError

        return Rational._div(self, other)

    def __rtruediv__(self, other: Union[Rational, int]) -> Rational:
        return Rational._div(self, other)

    def __iadd__(self, other):
        return Rational._add(self, other, create_new=False)

    def __isub__(self, other):
        return Rational._sub(self, other, create_new=False)

    def __imul__(self, other):
        return Rational._mul(self, other, create_new=False)

    def __itruediv__(self, other):
        if other == 0:
            raise ZeroDivisionError

        return Rational._div(self, other, create_new=False)

    def __lt__(self, other: Union[int, Rational]) -> bool:
        if isinstance(other, int):
            return True if self.numerator < other * self.denominator else False

        if isinstance(other, Rational):
            new_numerator1 = self.numerator * other.denominator
            new_numerator2 = other.numerator * self.denominator
            return True if new_numerator1 < new_numerator2 else False

        raise InvalidOperandType(other)

    def __gt__(self, other: Union[int, Rational]) -> bool:
        if isinstance(other, int):
            return True if self.numerator > other * self.denominator else False

        if isinstance(other, Rational):
            new_numerator1 = self.numerator * other.denominator
            new_numerator2 = other.numerator * self.denominator
            return True if new_numerator1 > new_numerator2 else False

        raise InvalidOperandType(other)

    def __le__(self, other) -> bool:
        return True if self.__lt__(other) or self.__eq__(other) else False

    def __ge__(self, other) -> bool:
        return True if self.__gt__(other) or self.__eq__(other) else False

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def _normalize_rational(self):
        gcd_result = gcd(self.numerator, self.denominator)
        self._numerator = self._numerator // gcd_result
        self._denominator = self._denominator // gcd_result

    def to_compound_fraction(self) -> Tuple[int, Rational]:
        integer_part: int = self._numerator // self.denominator * self._sign
        fractional_part: Rational = Rational(self._numerator % self.denominator * self._sign, self.denominator)
        return integer_part, fractional_part

    @staticmethod
    def _add(first: Rational, second: Union[Rational, int], create_new: bool = True) -> Rational:
        if isinstance(second, int):
            new_numerator: int = first.numerator + (second * first.denominator)

            if not create_new:
                first._numerator = new_numerator
                first._normalize_rational()
                return first

            return Rational(new_numerator, first.denominator)

        if isinstance(second, Rational):
            new_denominator = first.denominator * second.denominator
            new_numerator = (first.numerator * second.denominator) + (second.numerator * first.denominator)

            if not create_new:
                first._numerator = new_numerator
                first._denominator = new_denominator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _sub(first: Union[Rational, int], second: Union[Rational, int], create_new: bool = True) -> Rational:
        if isinstance(second, int):
            new_numerator: int = first.numerator - (second * first.denominator)

            if not create_new:
                first._numerator = new_numerator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, first.denominator)
            new_rational._normalize_rational()
            return new_rational

        if isinstance(second, Rational):
            new_denominator = first.denominator * second.denominator
            new_numerator = (first.numerator * second.denominator) - (second.numerator * first.denominator)

            if not create_new:
                first._numerator = new_numerator
                first._denominator = new_denominator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _mul(first: Union[Rational, int], second: Union[Rational, int], create_new: bool = True) -> Rational:
        if isinstance(second, int):
            new_numerator: int = first.numerator * second

            if not create_new:
                first._numerator = new_numerator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, first.denominator)
            new_rational._normalize_rational()
            return new_rational

        if isinstance(second, Rational):
            new_numerator: int = first.numerator * second.numerator
            new_denominator: int = first.denominator * second.denominator

            if not create_new:
                first._numerator = new_numerator
                first._denominator = new_denominator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _div(first: Union[Rational, int], second: Union[Rational, int], create_new: bool = True) -> Rational:
        if isinstance(second, int):
            if second == 0:
                return Rational()

            new_denominator: int = first.denominator * second

            if not create_new:
                first._denominator = new_denominator
                first._normalize_rational()
                return first

            new_rational = Rational(first.numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

        if isinstance(second, Rational):
            new_numerator: int = first.numerator * second.denominator
            new_denominator: int = first.denominator * second.numerator

            if not create_new:
                first._numerator = new_numerator
                first._denominator = new_denominator
                first._normalize_rational()
                return first

            new_rational = Rational(new_numerator, new_denominator)
            new_rational._normalize_rational()
            return new_rational

        raise InvalidOperandType(second)
