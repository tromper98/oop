from __future__ import annotations

from math import gcd
from typing import Union, Tuple, Optional

from exceptions import *


class Rational:
    _numerator: int
    _denominator: int
#Лучше знак не хранить

    def __init__(self, numerator: int = 0, denominator: int = 1):
        if not isinstance(numerator, int):
            raise InvalidNumeratorType(numerator)
        if not isinstance(denominator, int):
            raise InvalidDenominatorType(denominator)

        if denominator == 0:
            raise ZeroDenominatorError

        if denominator < 0:
            numerator *= -1

        self._numerator = numerator
        self._denominator = abs(denominator)
        self._normalize_rational()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def to_float(self):
        return self.numerator / self.denominator

#Возможно код станет проще, если сразу нормализовывать при создании
    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.numerator == other * self.denominator

        if isinstance(other, Rational):
            return self.numerator == other.numerator

        raise InvalidOperandType(other)

    def __ne__(self, other) -> bool:
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
        return Rational._div(other, self)

#Попробовать реализовать _add как модифицирующую операцию
    # def __iadd__(self, other):
    #     return self._add(other, create_new=False)
    #
    # def __isub__(self, other):
    #     return Rational._sub(self, other, create_new=False)
    #
    # def __imul__(self, other):
    #     return Rational._mul(self, other, create_new=False)
    #
    # def __itruediv__(self, other):
    #     if other == 0:
    #         raise ZeroDivisionError
    #
    #     return Rational._div(self, other, create_new=False)

    def __lt__(self, other: Union[int, Rational]) -> bool:
        if isinstance(other, int):
            return self.numerator < other * self.denominator

        if isinstance(other, Rational):
            return self.numerator < other.numerator  # упростить

        raise InvalidOperandType(other)

    def __gt__(self, other: Union[int, Rational]) -> bool:
        if isinstance(other, int):
            return self.numerator > other * self.denominator

        if isinstance(other, Rational):
            return self.numerator > other.numerator

        raise InvalidOperandType(other)

    def __le__(self, other) -> bool:
        return True if self.__lt__(other) or self.__eq__(other) else False

    def __ge__(self, other) -> bool:
        return True if self.__gt__(other) or self.__eq__(other) else False

#написать тест
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def _normalize_rational(self):
        gcd_result = gcd(self.numerator, self.denominator)
        self._numerator = self._numerator // gcd_result
        self._denominator = self._denominator // gcd_result

    def to_compound_fraction(self) -> Tuple[int, Rational]:
        integer_part: int = abs(self.numerator) // self.denominator
        new_numerator = abs(self.numerator) % self.denominator
        if self.numerator < 0:
            integer_part *= -1
            new_numerator *= -1

        fractional_part: Rational = Rational(new_numerator, self.denominator)
        return integer_part, fractional_part

    def _add(self, second: Union[Rational, int]) -> Optional[Rational]:
        if isinstance(second, int):
            new_numerator: int = self.numerator + (second * self.denominator)
            return Rational(new_numerator, self.denominator)

        if isinstance(second, Rational):
            new_denominator = self.denominator * second.denominator
            new_numerator = (self.numerator * second.denominator) + (second.numerator * self.denominator)
            new_rational = Rational(new_numerator, new_denominator)

            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _sub(first: Union[Rational, int], second: Union[Rational, int]) -> Rational:
        if not isinstance(first, (Rational, int)):
            raise InvalidOperandType(first)

        if isinstance(second, int):
            new_numerator: int = first.numerator - (second * first.denominator)
            new_rational = Rational(new_numerator, first.denominator)
            return new_rational

        if isinstance(second, Rational):
            new_denominator = first.denominator * second.denominator
            new_numerator = (first.numerator * second.denominator) - (second.numerator * first.denominator)
            new_rational = Rational(new_numerator, new_denominator)
            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _mul(first: Union[Rational, int], second: Union[Rational, int]) -> Rational:
        if isinstance(second, int):
            new_numerator: int = first.numerator * second
            new_rational = Rational(new_numerator, first.denominator)
            return new_rational

        if isinstance(second, Rational):
            new_numerator: int = first.numerator * second.numerator
            new_denominator: int = first.denominator * second.denominator
            new_rational = Rational(new_numerator, new_denominator)
            return new_rational

        raise InvalidOperandType(second)

    @staticmethod
    def _div(first: Union[Rational, int], second: Union[Rational, int]) -> Rational:
        if isinstance(second, int):
            if second == 0:
                return Rational()

            new_denominator: int = first.denominator * second
            new_rational = Rational(first.numerator, new_denominator)
            return new_rational

        if isinstance(second, Rational):
            new_numerator: int = first.numerator * second.denominator
            new_denominator: int = first.denominator * second.numerator
            new_rational = Rational(new_numerator, new_denominator)
            return new_rational

        raise InvalidOperandType(second)
