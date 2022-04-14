import pytest
from gearbox import Gearbox


def test_change_gear_from_neutral_to_one():
    gearbox = Gearbox()
    res = gearbox.change_gear(0, 1)
    assert res == 1
