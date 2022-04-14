class Gear:
    _code: int
    _min_speed: int
    _max_speed: int

    def __init__(self, code: int,  min_speed: int, max_speed: int):
        self._code = code
        self._min_speed = min_speed
        self._max_speed = max_speed

    @property
    def code(self):
        return self._code
