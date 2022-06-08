import pytest

from rational import Rational
from exceptions import *


def test_init_rational():
    rational1 = Rational()
    rational2 = Rational(6)
    rational3 = Rational(2, 4)
    rational4 = Rational(0, 5)
    rational5 = Rational(-1, 5)
    rational6 = Rational(5, -6)

    assert rational1.numerator == 0 and rational1.denominator == 1
    assert rational2.numerator == 6 and rational2.denominator == 1
    assert rational3.numerator == 2 and rational3.denominator == 4
    assert rational4.numerator == 0 and rational4.denominator == 5
    assert rational5.numerator == -1 and rational5.denominator == 5
    assert rational6.numerator == -5 and rational6.denominator == 6
    with pytest.raises(ZeroDenominatorError):
        Rational(1, 0)


def test_normalize_rationals():
    rational1 = Rational(1, 4)
    rational2 = Rational(8, 32)
    rational3 = Rational(1000, 4000)

    rational4 = Rational(-3, 7)
    rational5 = Rational(-9, 21)
    rational6 = Rational(-33, 77)

    assert rational1 == rational2 == rational3
    assert rational4 == rational5 == rational6


def test_unary_plus_return_equal_rational():
    rational1 = Rational()
    rational2 = Rational(3, 5)
    rational3 = Rational(5, 25)
    rational4 = Rational(-1, 3)
    rational5 = Rational(-8, 64)

    assert +rational1 == rational1
    assert +rational2 == rational2
    assert +rational3 == rational3
    assert +rational4 == rational4
    assert +rational5 == rational5


def test_unary_minus_return_opposite_rational():
    rational1 = Rational()
    rational2 = Rational(1, 5)
    rational3 = Rational(-1, 8)
    rational4 = Rational(0, 5)

    expected_rational1 = Rational()
    expected_rational2 = Rational(-1, 5)
    expected_rational3 = Rational(1, 8)
    expected_rational4 = Rational(0, 5)

    assert -rational1 == expected_rational1
    assert -rational2 == expected_rational2
    assert -rational3 == expected_rational3
    assert -rational4 == expected_rational4


def test_rational_to_float():
    rational1 = Rational()
    rational2 = Rational(1, 3)
    rational3 = Rational(-1, 8)
    rational4 = Rational(0, 9)

    assert rational1.to_float == 0.0
    assert rational2.to_float == 1 / 3
    assert rational3.to_float == -1 / 8
    assert rational4.to_float == 0 / 9


def test_add_to_rational():
    rational1 = Rational(1, 5)
    rational2 = Rational(-1, 8)
    rational3 = Rational(10, 9)
    rational4 = Rational(-8, 4)

    expected_rational1 = Rational(11, 5)
    expected_rational2 = Rational(47, 8)
    expected_rational3 = Rational(-8, 9)

    assert rational1 + 2 == expected_rational1
    assert 6 + rational2 == expected_rational2
    assert rational3 + rational4 == expected_rational3


def test_fail_add_with_incorrect_operand():
    rational = Rational(1, 5)

    with pytest.raises(InvalidOperandType):
        rational + 'some string'
        rational + 10.05
        rational + [10]
        'some str' + rational
        9.5 + rational
        (566, 24) + rational


def test_sub_rational():
    rational1 = Rational(11, 5)
    rational2 = Rational(11, 8)
    rational3 = Rational(8, 9)
    rational4 = Rational(-3, 4)
    rational5 = Rational(4, 16)
    rational6 = Rational(-1, 9)
    rational7 = Rational(-2, 19)

    expected_rational1 = Rational(1, 5)
    expected_rational2 = Rational(-3, 8)
    expected_rational3 = Rational(-1, 9)
    expected_rational4 = Rational(-1, 1)
    expected_rational5 = Rational(-1, 171)

    assert rational1 - 2 == expected_rational1
    assert 1 - rational2 == expected_rational2
    assert rational3 - 1 == expected_rational3
    assert rational4 - rational5 == expected_rational4
    assert rational6 - rational7 == expected_rational5


def test_fail_sub_with_incorrect_operand():
    rational = Rational(1, 5)

    with pytest.raises(InvalidOperandType):
        rational - 'some string'
        rational - 10.05
        rational - [10]
        'some str' - rational
        9.5 - rational
        (566, 24) - rational


def test_iadd_and_isub_rational():
    rational1 = Rational(4, 5)
    rational2 = Rational(3, 8)
    rational3 = Rational(1, 2)
    rational4 = Rational(17, 50)

    rational1 += Rational(1, 5)
    rational2 += 10
    rational3 -= 1
    rational4 -= Rational(1, 5)

    expected_rational1 = Rational(1, 1)
    expected_rational2 = Rational(83, 8)
    expected_rational3 = Rational(-1, 2)
    expected_rational4 = Rational(7, 50)

    assert rational1 == expected_rational1
    assert rational2 == expected_rational2
    assert rational3 == expected_rational3
    assert rational4 == expected_rational4


def test_mul_rational():
    rational1 = Rational(8, 19)
    rational2 = Rational(3, 7)
    rational3 = Rational()
    rational4 = Rational(-1, 2)
    rational5 = Rational(7, 13)
    rational6 = Rational(4, 6)

    expected_rational1 = Rational(24, 19)
    expected_rational2 = Rational(6, 7)
    expected_rational3 = Rational(0, 1)
    expected_rational4 = Rational(-9, 2)
    expected_rational5 = Rational(14, 39)

    assert rational1 * 3 == expected_rational1
    assert 2 * rational2 == expected_rational2
    assert rational3 * 99 == expected_rational3
    assert rational4 * 9 == expected_rational4
    assert rational5 * rational6 == expected_rational5


def test_div_rational():
    rational1 = Rational(4, 9)
    rational2 = Rational(-1, 2)
    rational3 = Rational(3, 10)
    rational4 = Rational(-6, 15)
    rational5 = Rational(7, 10)
    rational6 = Rational(10, 7)

    expected_rational1 = Rational(4, 72)
    expected_rational2 = Rational(-1, 4)
    expected_rational3 = Rational(2, 25)
    expected_rational4 = Rational(49, 100)
    expected_rational5 = Rational(0, 1)

    assert rational1 / 8 == expected_rational1
    assert 2 / rational2 == expected_rational2
    assert rational4 / -5 == expected_rational3
    assert rational5 / rational6 == expected_rational4
    assert 0 / rational3 == expected_rational5
    with pytest.raises(ZeroDivisionError):
        rational3 / 0


def test_imul_isub_rational():
    rational1 = Rational(4, 5)
    rational2 = Rational(3, 8)
    rational3 = Rational(10, 8)
    rational4 = Rational(6, 2)

    rational1 *= 2
    rational2 *= Rational(-6, 9)
    rational3 /= 7
    rational4 /= Rational(3, 2)

    expected_rational1 = Rational(8, 5)
    expected_rational2 = Rational(-1, 4)
    expected_rational3 = Rational(5, 28)
    expected_rational4 = Rational(2, 1)

    assert rational1 == expected_rational1
    assert rational2 == expected_rational2
    assert rational3 == expected_rational3
    assert rational4 == expected_rational4


def test_not_equal_rational():
    rational1 = Rational(1, 2)
    rational2 = Rational(3, 8)
    rational3 = Rational(3, 6)
    rational4 = Rational(9, 24)
    rational5 = Rational()
    rational6 = Rational(0, 1000)

    assert rational1 != rational2
    assert not rational1 != rational3
    assert not rational2 != rational4
    assert not rational5 != rational6
    assert rational3 != rational5


def test_lt_operator_rational():
    rational1 = Rational(6, 11)
    rational2 = Rational(-3, 5)
    rational3 = Rational(5, 10)
    rational4 = Rational(1, 2)
    rational5 = Rational(-2, 7)
    rational6 = Rational(-8, 19)

    assert rational1 < 1
    assert rational2 < rational1
    assert not rational3 < rational4
    assert not 3 < rational4
    assert rational6 < rational5


def test_gt_operator_rational():
    rational1 = Rational(1, 2)
    rational2 = Rational(4, 8)
    rational3 = Rational(18, 30)
    rational4 = Rational(5, 9)
    rational5 = Rational(-3, 7)
    rational6 = Rational(-2, 21)

    assert not rational1 > rational2
    assert rational3 > -1
    assert not rational4 > 10
    assert rational6 > rational5
