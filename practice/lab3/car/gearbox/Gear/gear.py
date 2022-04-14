class Gear:
    _min_speed: int
    _max_speed: int

    def __init__(self, min_speed: int, max_speed: int):
        self._min_speed = min_speed
        self._max_speed = max_speed
