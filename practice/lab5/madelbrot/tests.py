import pytest
import math

from exceptions import *
from complex import Complex


def test_create_complex():
    complex1 = Complex()
    complex2 = Complex(1)
    complex3 = Complex(3, -4)
    complex4 = Complex(-9, 4)
    complex5 = Complex(-10, -6)
    assert complex1.re == 0 and complex2.im == 0
    assert complex2.re == 1 and complex2.im == 0
    assert complex3.re == 3 and complex3.im == -4
    assert complex4.re == -9 and complex4.im == 4
    assert complex5.re == -10 and complex5.im == -6


def test_fail_create_complex():
    with pytest.raises(InvalidVariableType):
        Complex([1])
    with pytest.raises(InvalidVariableType):
        Complex('str')


def test_equal_complex():
    assert Complex() == Complex()
    assert Complex(1, 4) == Complex(1, 4)
    assert Complex(1.9, -9.0000005) == Complex(1.900000, -9.0000005)
    assert Complex(-1, -10) == Complex(-1, -10)
    assert not Complex(5, 4) == Complex(9, 10)
    assert Complex(4, 0) == 4
    assert not Complex(3.99) == 4


def test_not_equal_complex():
    assert Complex(3, 5) != Complex(1, 5)
    assert Complex(2, 9) != Complex(-2, -9)
    assert not Complex(-2, 10) != Complex(-2, 10)
    assert Complex(2) != 3
    assert not Complex() != 0


def test_add_complex():
    assert Complex(1, 1) + Complex() == Complex(1, 1)
    assert Complex(3, 4) + Complex(2, 10) == Complex(5, 14)
    assert Complex(3.5, -2.8) + Complex(1.25, 5.8) == Complex(4.75, 3)
    assert Complex(-17, -5) + Complex(-3.25, -17.73) == Complex(-20.25, -22.73)
    assert Complex(4, 9) + 17 == Complex(21, 9)
    assert -8 + Complex(33, -5) == Complex(25, -5)


def test_sub_complex():
    assert Complex(8, 10) - Complex(3, 2) == Complex(5, 8)
    assert Complex(3, 2) - Complex(8, 10) == Complex(-5, -8)
    assert Complex(1, 8) - Complex() == Complex(1, 8)
    assert Complex() - Complex(1, 8) == Complex(-1, -8)
    assert Complex(16, 9) - 9 == Complex(7, 9)
    assert 5 - Complex(12.002, 6.45) == Complex(-7.002, -6.45)


def test_mul_complex():
    assert Complex(3, 5) * Complex(2, 8) == Complex(-34, 34)
    assert Complex(-2.5, 18.35) * Complex(19, 29.5) == Complex(-588.825, 274.9)
    assert Complex(-2, -5) * Complex(-4, -6) == Complex(-22, 32)
    assert Complex(9, 3) * 3.5 == Complex(31.5, 10.5)
    assert 9.5 * Complex(2, 4) == Complex(19, 38)


def test_div_complex():
    assert Complex(1, 0) / Complex(3, 4) == Complex(0.12, -0.16)
    assert Complex(7, -3) / Complex(-3, -10) == Complex(0.082568807, 0.72477064)
    assert Complex(-2, -1) / Complex(-15, -7) == Complex(0.135036496, 0.0036496350)
    assert Complex(8, -3) / 4 == Complex(2, -0.75)
    assert 9 / Complex(3, 1) == Complex(2.7, -0.9)


def test_pos_operator_complex():
    assert +Complex(1) == Complex(1)
    assert +Complex(-1, -10) == Complex(-1, -10)
    assert +Complex(9, 25) == Complex(9, 25)


def test_neg_operator_complex():
    assert -Complex(1, 5) == Complex(-1, -5)
    assert -Complex(9, -5) == Complex(-9, 5)
    assert -Complex(-10, 4) == Complex(10, -4)
    assert -Complex(-9, -15) == Complex(9, 15)


def test_complex_to_str():
    assert Complex().__str__() == '0 + 0i'
    assert Complex(3, 8).__str__() == '3 + 8i'
    assert Complex(5, -2).__str__() == '5 - 2i'
    assert Complex(-6, -10).__str__() == '-6 - 10i'


def test_magnitude_complex():
    assert Complex(1,1).magnitude == math.sqrt(2)
    assert Complex(4, 9).magnitude == math.sqrt(97)
    assert Complex(-5, 9).magnitude == math.sqrt(106)
    assert Complex(-4, -7).magnitude == math.sqrt(65)
