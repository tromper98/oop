from gear import Gear


class ReverseGear(Gear):

    def __init__(self, min_speed: int, max_speed: int):
        super().__init__(min_speed, max_speed)