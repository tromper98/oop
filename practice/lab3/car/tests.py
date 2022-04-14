import pytest
from gearbox import Gearbox


def test_change_gear_from_neutral_to_one():
    gearbox = Gearbox()
    res = gearbox.change_gear(0, 1)
    assert res is True


def test_change_gear_from_neutral_to_reverse():
    gearbox = Gearbox()
    res = gearbox.change_gear(0, -1)
    assert res is True


def test_change_gear_from_reverse_to_one():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    res = gearbox.change_gear(0, 1)
    assert res is True


def test_change_gear_from_reverse_to_one_none_zero_speed():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    res = gearbox.change_gear(-10, 1)
    assert res is False


def test_change_gear_from_reverse_to_neutral_none_zero_speed():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    res = gearbox.change_gear(-10, 0)
    assert res is True


def test_change_gear_from_reverse_to_five_none_zero_speed():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    res = gearbox.change_gear(-10, 5)
    assert res is False


def test_change_gears():
    gearbox = Gearbox()
    gearbox.change_gear(0, 1)
    gearbox.change_gear(30, 3)
    gearbox.change_gear(70, 4)
    gearbox.change_gear(90, 5)
    assert gearbox.gear.code == 5

