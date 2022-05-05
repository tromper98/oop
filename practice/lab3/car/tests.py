import pytest
from car import Car, Gearbox, REVERSE_DIRECTION, FORWARD_DIRECTION
from exceptions import *


def test_change_gear_from_neutral_to_one():
    gearbox = Gearbox()
    gearbox.change_gear(0, 1)
    assert gearbox.gear.code == 1


def test_change_gear_from_neutral_to_reverse():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    assert gearbox.gear.code == -1


def test_change_gear_from_reverse_to_one_when_stop():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    gearbox.change_gear(0, 1)
    assert gearbox.gear.code == 1


def test_fail_change_gear_from_reverse_to_one_moving_backwards():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    with pytest.raises(InvalidGearSpeed):
        gearbox.change_gear(-10, 1)


def test_change_gear_from_reverse_to_neutral_none_zero_speed():
    gearbox = Gearbox()
    gearbox.change_gear(0, -1)
    gearbox.change_gear(-10, 0)
    assert gearbox.gear.code == 0


def test_consistent_change_gears():
    gearbox = Gearbox()
    gearbox.change_gear(0, 1)
    gearbox.change_gear(30, 3)
    gearbox.change_gear(70, 4)
    gearbox.change_gear(90, 5)
    assert gearbox.gear.code == 5


def test_fail_engine_off_while_moving():
    car = Car()
    car.engine_on()
    car.set_gear(1)
    car.set_speed(20)
    with pytest.raises(EngineOffError):
        car.engine_off()


def test_change_direction_when_start_moving():
    car1 = Car()
    car1.engine_on()
    car1.set_gear(1)
    car1.set_speed(20)
    car1_direction = car1.direction

    car2 = Car()
    car2.engine_on()
    car2.set_gear(-1)
    car2.set_speed(10)
    car2_direction = car2.direction
    assert car1_direction == 'Forward'
    assert car2_direction == 'Reverse'


def test_change_direction_to_stop():
    car = Car()
    car.engine_on()
    car.set_gear(1)
    car.set_speed(30)
    car.set_gear(2)
    car.set_speed(50)
    car.set_speed(20)
    car.set_gear(1)
    car.set_speed(0)
    assert car.direction == 'Stop'


def test_fail_increase_speed_on_neutral():
    car = Car()
    car.engine_on()
    car.set_gear(1)
    car.set_speed(25)
    car.set_gear(2)
    car.set_speed(40)
    car.set_gear(0)
    with pytest.raises(IncreaseSpeedOnNeutralGearError):
        car.set_speed(50)


def test_cannot_engine_off_while_moving():
    car = Car()
    car.engine_on()
    car.set_gear(1)
    car.set_speed(10)
    with pytest.raises(EngineOffError):
        car.engine_off()


def test_cannot_engine_off_on_none_neutral_gear():
    car = Car()
    car.engine_on()
    car.set_gear(1)
    with pytest.raises(EngineOffError):
        car.engine_off()


def test_no_change_direction_when_change_gear_to_neutral():
    car1 = Car()
    car1.engine_on()
    car1.set_gear(1)
    car1.set_speed(10)
    car1.set_gear(0)

    car2 = Car()
    car2.engine_on()
    car2.set_gear(-1)
    car2.set_speed(10)
    car1.set_gear(0)

    assert car1.direction == FORWARD_DIRECTION
    assert car2.direction == REVERSE_DIRECTION


def test_fail_change_gear_when_engine_off():
    car = Car()
    with pytest.raises(GearSwitchingEngineOffError):
        car.set_gear(1)