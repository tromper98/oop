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
    assert rational3.numerator == 1 and rational3.denominator == 2
    assert rational4.numerator == 0 and rational4.denominator == 1
    assert rational5.numerator == -1 and rational5.denominator == 5
    assert rational6.numerator == -5 and rational6.denominator == 6
    with pytest.raises(ZeroDenominatorError):
        Rational(1, 0)

    with pytest.raises(InvalidNumeratorType):
        Rational(1.0, 5)

    with pytest.raises(InvalidDenominatorType):
        Rational(1, ['str'])


def test_normalize_rationals():
    assert Rational(1, 4) == Rational(8, 32) == Rational(1000, 4000)
    assert Rational(-3, 7) ==  Rational(-9, 21) == Rational(-33, 77)


def test_unary_plus_return_equal_rational():
    assert +Rational() == Rational()
    assert +Rational(3, 5) == Rational(3, 5)
    assert +Rational(5, 25) == Rational(5, 25)
    assert +Rational(-1, 3) == Rational(-1, 3)
    assert +Rational(-8, 64) == Rational(-8, 64)


def test_unary_minus_return_opposite_rational():
    assert -Rational() == Rational()
    assert -Rational(1, 5) == Rational(-1, 5)
    assert -Rational(-1, 8) == Rational(1, 8)
    assert -Rational(0, 5) == Rational(0, 5)


def test_rational_to_float():
    assert Rational().to_float == 0.0
    assert Rational(1, 3).to_float == 1 / 3
    assert Rational(-1, 8).to_float == -1 / 8
    assert  Rational(0, 9).to_float == 0 / 9


def test_add_to_rational():
    assert Rational(1, 5) + 2 == Rational(11, 5)
    assert 6 + Rational(-1, 8) == Rational(47, 8)
    assert Rational(10, 9) + Rational(-8, 4) == Rational(-8, 9)


def test_fail_add_with_incorrect_operand():
    rational = Rational(1, 5)

# этот тест работает не так, как ожидается
    with pytest.raises(InvalidOperandType):
        rational + 'some string'
    with pytest.raises(InvalidOperandType):
        rational + 10.05
    with pytest.raises(InvalidOperandType):
        rational + [10]
    with pytest.raises(InvalidOperandType):
        'some str' + rational
    with pytest.raises(InvalidOperandType):
        9.5 + rational
    with pytest.raises(InvalidOperandType):
        (566, 24) + rational


def test_sub_rational():
#Здесь и в других местах тесты будут читаться легче без локальных переменных
    assert Rational(11, 5) - 2 == Rational(1, 5)
    assert 1 - Rational(11, 8) == Rational(-3, 8)
    assert Rational(8, 9) - 1 == Rational(-1, 9)
    assert Rational(-3, 4) - Rational(4, 16) == Rational(-1, 1)
    assert Rational(-1, 9) - Rational(-2, 19) == Rational(-1, 171)


def test_fail_sub_with_incorrect_operand():
    rational = Rational(1, 5)

    with pytest.raises(InvalidOperandType):
        rational - 'some string'
    with pytest.raises(InvalidOperandType):
        rational - 10.05
    with pytest.raises(InvalidOperandType):
        rational - [10]
    # with pytest.raises(InvalidOperandType):
    #     'some str' - rational
    with pytest.raises(InvalidOperandType):
        9.5 - rational
    with pytest.raises(InvalidOperandType):
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

    assert rational1 == Rational(1, 1)
    assert rational2 == Rational(83, 8)
    assert rational3 == Rational(-1, 2)
    assert rational4 == Rational(7, 50)


def test_multiply_rational():
    assert Rational(8, 19) * 3 == Rational(24, 19)
    assert 2 * Rational(3, 7) == Rational(6, 7)
    assert Rational() * 99 == Rational(0, 1)
    assert Rational(-1, 2) * 9 == Rational(-9, 2)
    assert Rational(7, 13) * Rational(4, 6) == Rational(14, 39)


def test_divide_rational():
    assert Rational(4, 9) / 8 == Rational(4, 72)
    assert 2 / Rational(-1, 2) == Rational(-1, 4)
    assert Rational(-6, 15) / -5 == Rational(2, 25)
    assert Rational(7, 10) / Rational(10, 7) == Rational(49, 100)
    assert 0 / Rational(3, 10) == Rational(0, 1)
    with pytest.raises(ZeroDivisionError):
        Rational(3, 10) / 0


def test_imul_isub_rational():
    rational1 = Rational(4, 5)
    rational2 = Rational(3, 8)
    rational3 = Rational(10, 8)
    rational4 = Rational(6, 2)

    rational1 *= 2
    rational2 *= Rational(-6, 9)
    rational3 /= 7
    rational4 /= Rational(3, 2)

    assert rational1 == Rational(8, 5)
    assert rational2 == Rational(-1, 4)
    assert rational3 == Rational(5, 28)
    assert rational4 == Rational(2, 1)


def test_not_equal_rational():
    assert Rational(1, 2) != Rational(3, 8)
    assert not Rational(1, 2) != Rational(3, 6)
    assert not Rational(3, 8) != Rational(9, 24)
    assert not Rational() != Rational(0, 1000)
    assert Rational(3, 6) != Rational()
    assert Rational(1, 10) != 10
    assert 1 != Rational(1, 10)


def test_less_operator_rational():
    assert Rational(6, 11) < 1
    assert Rational(-3, 5) < Rational(6, 11)
    assert not Rational(5, 10) < Rational(1, 2)
    assert not 3 < Rational(1, 2)
    assert Rational(-8, 19) < Rational(-2, 7)


def test_grater_operator_rational():
    assert Rational(-2, -2) >= Rational(1, 1)
    assert not Rational(1, 2) > Rational(4, 8)
    assert Rational(18, 30) > -1
    assert not Rational(5, 9) > 10
    assert Rational(-2, 21) > Rational(-3, 7)


def test_less_or_equal_operator_rational():
    assert Rational(-1, -1) <= Rational(3, 3)
    assert not Rational(4, 9) <= Rational(-1, 2)
    assert Rational(-1, 2) <= Rational(3, 8)
    assert not Rational(3, 8) <= Rational(-6, 15)
    assert Rational(-6, 15) <= Rational(7, 10)
    assert Rational(7, 10) <= Rational(21, 30)


def test_grater_or_equal_operator_rational():
    assert Rational(4, 9) >= Rational(-1, 2)
    assert not Rational(-1, 2) >= Rational(3, 8)
    assert Rational(3, 8) >= Rational(-6, 15)
    assert not Rational(-6, 15) >= Rational(7, 10)
    assert Rational(7, 10) >= Rational(21, 30)
    assert 1 >= Rational(21, 30)


def test_to_compound_fraction_rational():
    rational1 = Rational(3, 9)
    rational2 = Rational(0, 6)
    rational3 = Rational(10, 3)
    rational4 = Rational(-9, 4)

    expected1 = (0, Rational(3, 9))
    expected2 = (0, Rational(0, 6))
    expected3 = (3, Rational(1, 3))
    expected4 = (-2, Rational(-1, 4))

    assert rational1.to_compound_fraction() == expected1
    assert rational2.to_compound_fraction() == expected2
    assert rational3.to_compound_fraction() == expected3
    assert rational4.to_compound_fraction() == expected4


def test_rational_to_str():
    assert Rational().__str__() == '0/1'
    assert Rational(3, 4).__str__() == '3/4'
    assert Rational(6, 18).__str__() == '1/3'
    assert Rational(-1, 5).__str__() == '-1/5'
    assert Rational(-1, -9).__str__() == '1/9'
