from typing import Optional


class Gear:
    _code: int
    _min_speed: float
    _max_speed: float

    def __init__(self, code: int,  min_speed: Optional[float], max_speed: Optional[float]):
        self._code = code
        self._min_speed = min_speed
        self._max_speed = max_speed

    @property
    def code(self):
        return self._code

    @property
    def min_speed(self):
        return self._min_speed

    @property
    def max_speed(self):
        return self._max_speed
