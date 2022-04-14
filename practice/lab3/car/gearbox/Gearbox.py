from typing import List
from Gear import *


class Gearbox:
    _gears: List[Gear]
    _current_gear: Gear

    def __init__(self):
        self._gears = self._get_gears()
        self._current_gear = NeutralGear()

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

    @property
    def gear(self) -> Gear:
        return self._current_gear
