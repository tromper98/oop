from .gear import Gear


class ReverseGear(Gear):
    def __init__(self, min_speed: int, max_speed: int):
        code = -1
        super().__init__(code, min_speed, max_speed)
