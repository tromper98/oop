from typing import List
from Gear import *


class Gearbox:
    _gears: List[Gear]

    def __init__(self):
        self._gears = self._get_gears()

    def _get_gears(self) -> List[Gear]:
        gears: List[Gear] = []
        gears.append(ReverseGear(0, 20))
        gears.append(NeutralGear())
        gears.append(FirstGear(0, 30))

        return gears