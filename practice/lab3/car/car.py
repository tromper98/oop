from gearbox import Gearbox


class Car:
    _speed: float
    _gearbox: Gearbox
    _engine: bool

    def __init__(self):
        self._speed = 0
        self._gearbox = Gearbox()
        self._engine = False

    def engine_on(self):
        if self.engine:
            return True

    def engine_off(self):
        if not self.engine:
            return True

        if self.engine and self.gear == NeutralGear and self.speed == 0:
            self.engine = False
            return True

        return False
