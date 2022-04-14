from gear import Gear


class NeutralGear(Gear):
    def __init__(self, min_speed=None, max_speed=None):
        super().__init__(min_speed, max_speed)
