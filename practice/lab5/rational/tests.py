import pytest

from rational import Rational
from exceptions import *


def test_init_rational():
    rational1 = Rational()
    rational2 = Rational(6)
    rational3 = Rational(2, 4)
    rational4 = Rational(0, 5)

    assert rational1.numerator == 0 and rational1.denominator == 1
    assert rational2.numerator == 6 and rational2.denominator == 1
    assert rational3.numerator == 2 and rational3.denominator == 4
    assert rational4.numerator == 0 and rational4.denominator == 5
    with pytest.raises(ZeroDenominatorError):
        rational5 = Rational(1, 0)


def test_normalize_rationals():
    rational1 = Rational(1, 4)
    rational2 = Rational(8, 32)
    rational3 = Rational(1000, 4000)

    rational4 = Rational(-3, 7)
    rational5 = Rational(-9, 21)
    rational6 = Rational(-33, 77)

    assert rational1 == rational2 == rational3
    assert rational4 == rational5 == rational6


def test_unary_plus_not_change_rational():
    rational1 = Rational()
    rational2 = Rational(3, 5)
    rational3 = Rational(5, 25)
    rational4 = Rational(-1, 3)
    rational5 = Rational(-8, 64)

    assert + rational1 == rational1
    assert + rational2 == rational2
    assert + rational3 == rational3
    assert + rational4 == rational4
    assert + rational5 == rational5
