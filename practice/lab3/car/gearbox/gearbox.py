from typing import List
from .gear import *


class Gearbox:
    _gears: List[Gear]
    _current_gear: Gear
    _min_gear_code: int
    _max_gear_code: int

    def __init__(self):
        self._gears = self._get_gears()
        self._current_gear = NeutralGear()
        self._min_gear_code = self._get_min_gear_code()
        self._max_gear_code = self._get_max_gear_code()

    @staticmethod
    def _get_gears() -> List[Gear]:
        gears: List[Gear] = [ReverseGear(0, 20),
                             NeutralGear(),
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

    def change_gear(self, speed: float, new_gear_code: int) -> bool:
        if not self._min_gear_code <= new_gear_code <= self._max_gear_code:
            print(f'Invalid gear. There is no {new_gear_code} gear')
            return False

        new_gear: Gear = self._get_gear_by_code(new_gear_code)

        if isinstance(new_gear, NeutralGear):
            self._current_gear = new_gear
            print(f'Gear changed successfully. New gear - {self._current_gear.code}')
            return True

        if isinstance(new_gear, ReverseGear):
            if speed == 0:
                self._current_gear = new_gear
                print(f'Gear changed successfully. New gear - {self._current_gear.code}')
                return True

            print(f"Can't change gear from {self._current_gear} to {new_gear}")
            return False

        if isinstance(self._current_gear, ReverseGear) and new_gear.code == 1:
            if speed == 0:
                self._current_gear = new_gear
                print(f'Gear changed successfully. New gear - {self._current_gear.code}')
                return True

            print(f"Can't change gear from {self._current_gear} to {new_gear}")
            return False

        if isinstance(self._current_gear, NeutralGear) and new_gear.code == 1:
            if speed == 0:
                self._current_gear = new_gear
                print(f'Gear changed successfully. New gear - {self._current_gear.code}')
                return True

            print(f"Can't change gear from {self._current_gear} to {new_gear}")
            return False

        if not new_gear.min_speed <= speed <= new_gear.max_speed:
            print(f'Invalid speed for new gear. Speed must by in [{new_gear.min_speed}, {new_gear.max_speed}]')
            return False

        self._current_gear = new_gear
        print(f'Gear changed successfully. New gear - {self._current_gear.code}')
        return True

