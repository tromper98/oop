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

    @property
    def is_neutral_gear(self) -> bool:
        return isinstance(self._current_gear, NeutralGear)

    @property
    def is_reverse_gear(self) -> bool:
        return isinstance(self._current_gear, ReverseGear)

    def change_gear(self, speed: float, new_gear_code: int) -> bool:
        if not self._min_gear_code <= new_gear_code <= self._max_gear_code:
            print(f'Invalid gear. There is no {new_gear_code} gear')
            return False

        new_gear: Gear = self._get_gear_by_code(new_gear_code)

        can_change: bool = False

        if isinstance(new_gear, NeutralGear):
            can_change = True

        elif self.is_neutral_gear:
            can_change = self.__try_change_from_neutral(speed, new_gear)

        elif self.is_reverse_gear:
            can_change = self.__try_change_from_reverse(speed)

        elif isinstance(new_gear, ReverseGear):
            can_change = self.__try_change_to_reverse(speed, new_gear)

        elif new_gear.min_speed <= speed <= new_gear.max_speed:
            can_change = True

        if can_change:
            self._current_gear = new_gear
            print(f'Gear changed successfully to gear {self._current_gear.code}')
            return True

        if not new_gear.min_speed <= speed <= new_gear.max_speed:
            print(f'Invalid speed for gear {new_gear.code} . Speed must by in [{new_gear.min_speed}, {new_gear.max_speed}]')
            return False

        print(f"Can't change gear from {self._current_gear.code} to {new_gear.code}")
        return False

    def __try_change_from_reverse(self, speed: float) -> bool:
        return True if speed == 0 else False

    def __try_change_from_neutral(self, speed: float, new_gear: Gear) -> bool:
        return True if new_gear.min_speed <= speed <= new_gear.max_speed else False

    def __try_change_to_reverse(self, speed: float, new_gear: Gear):
        return True if speed == 0 and new_gear.code == 1 else False
