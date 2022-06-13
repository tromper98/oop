from __future__ import annotations
from typing import Union
import math

from exceptions import *

FLOAT_EPSILON = 0.00000001


class Complex:
    _real: float
    _image: float

    def __init__(self, real: float = 0, image: float = 0):
        if not isinstance(real, (int, float)):
            raise InvalidVariableType(real)

        if not isinstance(real, (int, float)):
            raise InvalidVariableType(real)

        self._real = real
        self._image = image

    @property
    def re(self) -> float:
        return self._real

    @property
    def im(self) -> float:
        return self._image

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def __add__(self, other) -> Complex:
        if isinstance(other, (int, float)):
            other = Complex(other)

        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)

        raise InvalidOperandType(other)

    def __radd__(self, other) -> Complex:
        return self.__add__(other)

    def __sub__(self, other) -> Complex:
        return Complex._sub(self, other)

    def __rsub__(self, other) -> Complex:
        return Complex._sub(other, self)

    def __mul__(self, other) -> Complex:
        if isinstance(other, (int, float)):
            other = Complex(other)

        if isinstance(other, Complex):
            new_re: float = self.re * other.re - self.im * other.im
            new_im: float = self.re * other.im + self.im * other.re
            return Complex(new_re, new_im)

        raise InvalidOperandType(other)

    def __rmul__(self, other) -> Complex:
        return self.__mul__(other)

    def __truediv__(self, other) -> Complex:
        return Complex._div(self, other)

    def __rtruediv__(self, other) -> Complex:
        return Complex._div(other, self)

    def __pos__(self) -> Complex:
        return Complex(self.re, self.im)

    def __neg__(self) -> Complex:
        return Complex(-self.re, -self.im)

    def __eq__(self, other: Union[float, int, Complex]) -> bool:
        if isinstance(other, (float, int)):
            other = Complex(other)
        if (abs(self.re - other.re) < FLOAT_EPSILON) and (abs(self.im - other.im) < FLOAT_EPSILON):
            return True

        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @staticmethod
    def _sub(first: Union[float, int, Complex], second: Union[float, int, Complex]) -> Complex:
        if isinstance(first, (int, float)):
            first = Complex(first)

        if isinstance(second, (int, float)):
            second = Complex(second)

        if isinstance(second, Complex):
            return Complex(first.re - second.re, first.im - second.im)

        raise InvalidOperandType(second)

    @staticmethod
    def _div(first: Union[float, int, Complex], second: Union[float, int, Complex]) -> Complex:
        if isinstance(first, (int, float)):
            first = Complex(first)

        if isinstance(second, (int, float)):
            second = Complex(second)

        if isinstance(second, Complex):
            new_re: float = (first.re * second.re + first.im * second.im) / (second.re ** 2 + second.im ** 2)
            new_im: float = (first.im * second.re - first.re * second.im) / (second.re ** 2 + second.im ** 2)
            return Complex(new_re, new_im)

        raise InvalidOperandType(second)
