class RGB:
    _r: int
    _g: int
    _b: int

    def __init__(self, r: int, g: int, b: int):
        if not RGB._is_valid_numbers(r, g, b):
            raise ValueError('Invalid color number')
        self._r = r
        self._g = g
        self._b = b

    @staticmethod
    def _is_valid_numbers(r: int, g: int, b: int) -> bool:
        if not 0 <= r <= 255:
            return False
        if not 0 <= g <= 255:
            return False
        if not 0 <= b <= 255:
            return False

        return True

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b
