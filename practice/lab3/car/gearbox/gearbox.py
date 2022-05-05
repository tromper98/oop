from typing import List
from .gear import *
from exceptions import InvalidGear, InvalidGearSpeed


class Gearbox:
    _gears: List[Gear]
    _current_gear: Gear
    _min_gear_code: int
    _max_gear_code: int

    def __init__(self):
        self._gears = Gearbox._get_gears() #вызов статического метода через имя класса
        self._current_gear = self._get_gear_by_code(NEUTRAL_GEAR_CODE)
        self._min_gear_code = self._get_min_gear_code()
        self._max_gear_code = self._get_max_gear_code()

    @staticmethod
    def _get_gears() -> List[Gear]:
        gears: List[Gear] = [Gear(REVERSE_GEAR_CODE, -20, 0),
                             Gear(NEUTRAL_GEAR_CODE, None, None),
                             Gear(1, 0, 30),
                             Gear(2, 20, 50),
                             Gear(3, 30, 60),
                             Gear(4, 40, 90),
                             Gear(5, 50, 150)]
        return gears

    def _get_min_gear_code(self):
        return min(self._gears, key=lambda x: x.code).code

    def _get_max_gear_code(self):
        return max(self._gears, key=lambda x: x.code).code

    def _get_gear_by_code(self, code: int) -> Gear:
        return next(filter(lambda x: x.code == code, self._gears))

    @property
    def gear(self) -> Gear:
        return self._current_gear

    @property #is_on_neutral_gear
    def is_on_neutral_gear(self) -> bool:
        return self._current_gear.code == NEUTRAL_GEAR_CODE

    @property
    def is_on_reverse_gear(self) -> bool:
        return self._current_gear.code == REVERSE_GEAR_CODE

#Есть риск неправильного использования, так как ожидается модуль скорости
    def change_gear(self, speed: float, new_gear_code: int) -> None:
        if not self._min_gear_code <= new_gear_code <= self._max_gear_code:
            raise InvalidGear(new_gear_code)

        new_gear: Gear = self._get_gear_by_code(new_gear_code)

        if new_gear.code == NEUTRAL_GEAR_CODE:
            self._current_gear = new_gear
            return

        if new_gear_code == REVERSE_GEAR_CODE and speed == 0:
            self._current_gear = new_gear
            return

        if not new_gear.min_speed <= speed <= new_gear.max_speed:
            raise InvalidGearSpeed(new_gear, speed)

        self._current_gear = new_gear
